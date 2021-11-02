# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form4.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Thcond Converter")
        MainWindow.resize(581, 370)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 30, 571, 301))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 5, 111, 21))
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 581, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuActions = QtWidgets.QMenu(self.menubar)
        self.menuActions.setObjectName("menuActions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionConvert_to_ThCond = QtWidgets.QAction(MainWindow)
        self.actionConvert_to_ThCond.setObjectName("actionConvert_to_ThCond")
        self.actionOpen_Thcond = QtWidgets.QAction(MainWindow)
        self.actionOpen_Thcond.setObjectName("actionOpen_Thcond")
        self.actionRewrite_Thcond = QtWidgets.QAction(MainWindow)
        self.actionRewrite_Thcond.setObjectName("actionRewrite_Thcond")
        self.actionVisualize_2 = QtWidgets.QAction(MainWindow)
        self.actionVisualize_2.setObjectName("actionVisualize_2")
        self.menuFile.addAction(self.actionOpen)
        self.menuActions.addAction(self.actionOpen_Thcond)
        self.menuActions.addAction(self.actionRewrite_Thcond)
        self.menuActions.addAction(self.actionVisualize_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuActions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Thcond Converter", "Thcond Converter"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuActions.setTitle(_translate("MainWindow", "Actions"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionConvert_to_ThCond.setText(_translate("MainWindow", "Convert to ThCond"))
        self.actionOpen_Thcond.setText(_translate("MainWindow", "Open Thcond"))
        self.actionRewrite_Thcond.setText(_translate("MainWindow", "Rewrite Thcond"))
        self.actionVisualize_2.setText(_translate("MainWindow", "Visualize"))

