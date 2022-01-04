# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1211, 695)
        MainWindow.setStyleSheet("background-color: rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.videoWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.videoWidget.sizePolicy().hasHeightForWidth())
        self.videoWidget.setSizePolicy(sizePolicy)
        self.videoWidget.setStyleSheet("background-color: rgb(15, 15, 15);")
        self.videoWidget.setObjectName("videoWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.videoWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.videoLabel = QtWidgets.QLabel(self.videoWidget)
        self.videoLabel.setText("")
        self.videoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.videoLabel.setObjectName("videoLabel")
        self.gridLayout_3.addWidget(self.videoLabel, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.videoWidget, 0, 0, 1, 1)
        self.infowidget = QtWidgets.QWidget(self.centralwidget)
        self.infowidget.setStyleSheet("")
        self.infowidget.setObjectName("infowidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.infowidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fileNameLabel = QtWidgets.QLabel(self.infowidget)
        self.fileNameLabel.setMinimumSize(QtCore.QSize(70, 0))
        self.fileNameLabel.setMaximumSize(QtCore.QSize(400, 16777215))
        self.fileNameLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.fileNameLabel.setObjectName("fileNameLabel")
        self.horizontalLayout.addWidget(self.fileNameLabel)
        self.timeLabel = QtWidgets.QLabel(self.infowidget)
        self.timeLabel.setMinimumSize(QtCore.QSize(50, 0))
        self.timeLabel.setMaximumSize(QtCore.QSize(60, 16777215))
        self.timeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.timeLabel.setObjectName("timeLabel")
        self.horizontalLayout.addWidget(self.timeLabel)
        self.videoHorizontalSlider = QtWidgets.QSlider(self.infowidget)
        self.videoHorizontalSlider.setMaximum(1000)
        self.videoHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.videoHorizontalSlider.setObjectName("videoHorizontalSlider")
        self.horizontalLayout.addWidget(self.videoHorizontalSlider)
        self.videoLenghtLabel = QtWidgets.QLabel(self.infowidget)
        self.videoLenghtLabel.setObjectName("videoLenghtLabel")
        self.horizontalLayout.addWidget(self.videoLenghtLabel)
        self.gridLayout.addWidget(self.infowidget, 1, 0, 1, 1)
        self.audioWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.audioWidget.sizePolicy().hasHeightForWidth())
        self.audioWidget.setSizePolicy(sizePolicy)
        self.audioWidget.setStyleSheet("background-color: rgb(15, 15, 15);")
        self.audioWidget.setObjectName("audioWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.audioWidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout.addWidget(self.audioWidget, 2, 0, 1, 1)
        self.settingsWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsWidget.sizePolicy().hasHeightForWidth())
        self.settingsWidget.setSizePolicy(sizePolicy)
        self.settingsWidget.setStyleSheet("")
        self.settingsWidget.setObjectName("settingsWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.settingsWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.beginningDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.settingsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.beginningDoubleSpinBox.sizePolicy().hasHeightForWidth())
        self.beginningDoubleSpinBox.setSizePolicy(sizePolicy)
        self.beginningDoubleSpinBox.setSingleStep(0.01)
        self.beginningDoubleSpinBox.setObjectName("beginningDoubleSpinBox")
        self.gridLayout_2.addWidget(self.beginningDoubleSpinBox, 9, 1, 1, 2)
        self.endDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.settingsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.endDoubleSpinBox.sizePolicy().hasHeightForWidth())
        self.endDoubleSpinBox.setSizePolicy(sizePolicy)
        self.endDoubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.endDoubleSpinBox.setSpecialValueText("")
        self.endDoubleSpinBox.setPrefix("")
        self.endDoubleSpinBox.setSingleStep(0.01)
        self.endDoubleSpinBox.setObjectName("endDoubleSpinBox")
        self.gridLayout_2.addWidget(self.endDoubleSpinBox, 10, 1, 1, 2)
        self.beginningLabel = QtWidgets.QLabel(self.settingsWidget)
        self.beginningLabel.setObjectName("beginningLabel")
        self.gridLayout_2.addWidget(self.beginningLabel, 9, 0, 1, 1)
        self.durationLabel = QtWidgets.QLabel(self.settingsWidget)
        self.durationLabel.setObjectName("durationLabel")
        self.gridLayout_2.addWidget(self.durationLabel, 6, 0, 2, 3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 5, 0, 1, 3)
        self.filePathLineEdit = QtWidgets.QLineEdit(self.settingsWidget)
        self.filePathLineEdit.setObjectName("filePathLineEdit")
        self.gridLayout_2.addWidget(self.filePathLineEdit, 3, 0, 1, 3)
        self.browseButton = QtWidgets.QPushButton(self.settingsWidget)
        self.browseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.browseButton.setObjectName("browseButton")
        self.gridLayout_2.addWidget(self.browseButton, 4, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 3)
        self.mp4FileLbael = QtWidgets.QLabel(self.settingsWidget)
        self.mp4FileLbael.setObjectName("mp4FileLbael")
        self.gridLayout_2.addWidget(self.mp4FileLbael, 2, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 11, 0, 1, 3)
        self.convertButton = QtWidgets.QPushButton(self.settingsWidget)
        self.convertButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.convertButton.setObjectName("convertButton")
        self.gridLayout_2.addWidget(self.convertButton, 12, 0, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 13, 0, 1, 3)
        self.endLabel = QtWidgets.QLabel(self.settingsWidget)
        self.endLabel.setObjectName("endLabel")
        self.gridLayout_2.addWidget(self.endLabel, 10, 0, 1, 1)
        self.gridLayout.addWidget(self.settingsWidget, 0, 1, 3, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mp4 to Mp3 Converter"))
        self.fileNameLabel.setText(_translate("MainWindow", "File Name"))
        self.timeLabel.setText(_translate("MainWindow", "00.00"))
        self.videoLenghtLabel.setText(_translate("MainWindow", "Lenght: 0.00"))
        self.beginningLabel.setText(_translate("MainWindow", "Beginning:"))
        self.durationLabel.setText(_translate("MainWindow", "Duration"))
        self.browseButton.setText(_translate("MainWindow", "Browse"))
        self.mp4FileLbael.setText(_translate("MainWindow", "Mp4 File"))
        self.convertButton.setText(_translate("MainWindow", "Convert"))
        self.endLabel.setText(_translate("MainWindow", "End:"))