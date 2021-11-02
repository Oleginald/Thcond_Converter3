# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 09:45:07 2020

@author: 0249177
"""

from PyQt5 import QtWidgets,QtGui, QtCore
from Window import Ui_MainWindow
import sys
import Sort_funcs2 as Sf

class mywindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.actionOpen.setShortcut('Ctrl+O')
        self.ui.actionOpen.setStatusTip('Open new Iges File')
        self.ui.actionOpen.triggered.connect(self.openIges)
        
        self.ui.actionOpen_Thcond.triggered.connect(self.showThcond)
        
        self.ui.actionRewrite_Thcond.triggered.connect(self.rewriteThcond)
        
        self.ui.actionVisualize_2.triggered.connect(self.visualizeThcond)
        
    
    def openIges(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        Sf.run_main_algorithm(fname)
    
    def showThcond(self):
        fname = 'THCOND.DAT'
        with open(fname, 'r') as f:
            data = f.read()
            self.ui.textEdit.setText(data)
 #       f = open(fname, 'r')
  #      with f:
   #         data = f.read()
    #        self.ui.textEdit.setText(data)
       # f.close()
            
    def rewriteThcond(self):
        fname = 'THCOND.DAT'
        f = open(fname, 'w')
        text = self.ui.textEdit.toPlainText()
        f.write(text)
        f.close()
            
        
    def visualizeThcond(self):
        print('Visualize launching')
        Sf.run_pygame()


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())