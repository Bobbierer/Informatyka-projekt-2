# -*- coding: utf-8 -*-
"""
Created on Sun May 29 17:54:25 2022

@author: IMikulak
"""
from __future__ import unicode_literals # obsluga polskich znakÃ³w diaktrtycznych
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from projekt2inf2 import * # import kodu pythona ze schematem GUI
from Transformacje import Transformacje
class MyForm(QDialog):# QDialog jako klasa nadrzedna
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog() # Nazwa klasy z pliku przekonwertowanego z UI
        self.ui.setupUi(self)
        self.ui.GRS80.clicked.connect(self.JakieW1)
        self.ui.WRS84.clicked.connect(self.JakieW2)
        self.ui.strefa5.clicked.connect(self.S5)
        self.ui.strefa6.clicked.connect(self.S6)
        self.ui.strefa7.clicked.connect(self.S7)
        self.ui.strefa8.clicked.connect(self.S8)
        self.setWindowIcon(QtGui.QIcon('geodeta.png'))
        self.show()
        
    def S5(self):
        self.strefa = 5
    def S6(self):
        self.strefa = 6
    def S7(self):
        self.strefa = 7
    def S8(self):
        self.strefa = 8
        

    def JakieW1(self):
        t1 = Transformacje("grs80")
        Phi = int(self.ui.Fstopnie.text()) + int(self.ui.Fmin.text()) + float(self.ui.Fsek.text())
        Lam = int(self.ui.Lstopnie.text()) + int(self.ui.Lmin.text()) + float(self.ui.Lsek.text())
        (x2000,y2000) = t1.u20002(Phi,Lam,self.strefa)
        (x92,y92) = t1.u1992(Phi,Lam)
        (xgk,ygk,nr) = t1.gauss_kruger(Phi,Lam)
        self.ui.wynikxgk.setText(str(xgk))
        self.ui.wynikygk.setText(str(ygk))
        self.ui.wynikx2000.setText(str(x2000))
        self.ui.wyniky2000.setText(str(y2000))        
        self.ui.wynikx92.setText(str(x92))
        self.ui.wyniky92.setText(str(y92))
        
        
    def JakieW2(self):
        t2 = Transformacje("wgs84")
        Phi1 = int(self.ui.Fstopnie.text()) + int(self.ui.Fmin.text()) + float(self.ui.Fsek.text())
        Lam1 = int(self.ui.Lstopnie.text()) + int(self.ui.Lmin.text()) + float(self.ui.Lsek.text())
        (x20001,y20001) = t2.u20002(Phi1,Lam1,self.strefa)
        (x921,y921) = t2.u1992(Phi1,Lam1)
        (xgk1,ygk1,nr) = t2.gauss_kruger(Phi1,Lam1)
        
        
        self.ui.wynikxgk.setText(str(xgk1))
        self.ui.wynikygk.setText(str(ygk1))
        self.ui.wynikx2000.setText(str(x20001))
        self.ui.wyniky2000.setText(str(y20001))        
        self.ui.wynikx92.setText(str(x921))
        self.ui.wyniky92.setText(str(y921))
        

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
    
    