from PyQt5 import QtGui, QtWidgets, QtCore
import sys
from ui import Ui_MainWindow
from moviepy import editor
from os import error, getcwd
import cv2
import numpy as np
import pyqtgraph

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.filePathLineEdit.returnPressed.connect(lambda:self.GetVideo(self.ui.filePathLineEdit.text()))
        self.ui.browseButton.clicked.connect(self.Browse)
        self.ui.videoHorizontalSlider.valueChanged.connect(self.SliderMoved)
        self.ui.convertButton.clicked.connect(self.ConvertClicked)

    def GetVideo(self, file):
        try:
            self.video = editor.VideoFileClip(file)
            self.audio = self.video.audio
            self.UpdateUi()
        except:
            pass

    def Browse(self):
        response = QtWidgets.QFileDialog.getOpenFileName(
            parent=self,
            caption="Select a Video File",
            directory=getcwd(),
            filter="Mp4 File (*.mp4)"
        )
        self.GetVideo(response[0])

    def UpdateUi(self):

        #to separate filename with path
        filename = self.video.filename.split("/")[-1]

        duration = self.SecondToMinute(self.video.duration)

        self.ui.filePathLineEdit.setText(self.video.filename)
        self.ui.fileNameLabel.setText(filename)
        self.ui.videoLenghtLabel.setText(f"Length: {duration}")
        self.ui.videoHorizontalSlider.setMaximum(int(self.video.duration))
        self.ui.endDoubleSpinBox.setMaximum(duration)
        self.ui.endDoubleSpinBox.setValue(duration)
        self.ui.videoHorizontalSlider.setValue(1)
        self.ui.videoHorizontalSlider.setValue(0)

        self.AudioPlot()
  
    def SliderMoved(self):
        try:
            value = self.ui.videoHorizontalSlider.value()
            self.ui.timeLabel.setText(str(self.SecondToMinute(value)))
            self.ui.videoLabel.setPixmap(self.ConvertNpQt(self.video.get_frame(value)))
        except:
            pass

    def SecondToMinute(self, second):
        return round((second // 60) + int(second % 60) / 100,2)

    def MinuteToSecond(self, minute):
        return (minute//1)*60 + (minute-minute//1) * 100

    def ConvertNpQt(self, img):
        image = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        h, w, ch = image.shape
        bytesPerLine = ch * w
        QtFormat = QtGui.QImage(image.data, w, h, bytesPerLine, QtGui.QImage.Format_BGR888)
        p = QtFormat.scaled(self.ui.videoLabel.width(), self.ui.videoLabel.height(), QtCore.Qt.KeepAspectRatio)
        return QtGui.QPixmap.fromImage(p)

    def AudioPlot(self):
        array = self.audio.to_soundarray()

        np.delete(array, 1)

        array = array.flatten()

        pltwdgt = pyqtgraph.GraphicsLayoutWidget(self,show=True)
        for i in reversed(range(self.ui.gridLayout_4.count())): 
            self.ui.gridLayout_4.itemAt(i).widget().deleteLater()
        self.ui.gridLayout_4.addWidget(pltwdgt)
        pltwdgt.addPlot(y=array, pen=(0,255,0))

    def ConvertClicked(self):
        path = self.video.filename.split("/")[:-1]
        path = "/".join(path)
        response = QtWidgets.QFileDialog.getSaveFileName(
            parent=self,
            caption="Save mp3 file",
            directory=path,
            filter="Mp3 File (*.mp3)"
        )
        beginning = self.MinuteToSecond(self.ui.beginningDoubleSpinBox.value())
        end = self.MinuteToSecond(self.ui.endDoubleSpinBox.value())
        
        if response[0] != "":
            clip = self.video.subclip(beginning,end)
            clipAudio = clip.audio
            clipAudio.write_audiofile(response[0])

            box = QtWidgets.QMessageBox(self)
            box.setWindowTitle("Mp4 to Mp3")
            box.setText("Convertion completed successfully")
            box.setIcon(QtWidgets.QMessageBox.Information)
            box.exec_()


def App():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    win = Main()
    win.show()
    sys.exit(app.exec_())

App()