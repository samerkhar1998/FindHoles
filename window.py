import cv2
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QFileDialog

from algo import algorithm


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(593, 375)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 70, 121, 51))
        self.label.setObjectName("label")
        self.browse = QtWidgets.QPushButton(self.centralwidget)
        self.browse.setGeometry(QtCore.QRect(250, 120, 75, 23))
        self.browse.setObjectName("browse")
        self.run = QtWidgets.QPushButton(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(250, 220, 75, 23))
        self.run.setObjectName("run")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 270, 151, 16))
        self.label_2.setObjectName(("label_2"))
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(150, 160, 271, 31))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 593, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.browse.clicked.connect(self.browseEvent)
        self.run.clicked.connect(self.loadEvent)
        self.img = None
        self.result = None

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "1. CHOOSE IMAGE\n"
"2. RUN"))
        self.browse.setText(_translate("MainWindow", "BROWSE"))
        self.run.setText(_translate("MainWindow", "RUN"))

    def browseEvent(self):
        fName = QFileDialog.getOpenFileName(None, 'Open file')
        self.textEdit.setText(fName[0])
        self.img = cv2.imread(fName[0])

    def loadEvent(self):
        ret = algorithm(self.img)
        ret -= 1
        self.label_2.setText(f"{ret} holes found")

