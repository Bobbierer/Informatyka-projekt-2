# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projekt2inf.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1040, 758)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 50, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Fstopnie = QtWidgets.QLineEdit(Dialog)
        self.Fstopnie.setGeometry(QtCore.QRect(240, 70, 61, 31))
        self.Fstopnie.setObjectName("Fstopnie")
        self.Fmin = QtWidgets.QLineEdit(Dialog)
        self.Fmin.setGeometry(QtCore.QRect(320, 70, 61, 31))
        self.Fmin.setObjectName("Fmin")
        self.Fsek = QtWidgets.QLineEdit(Dialog)
        self.Fsek.setGeometry(QtCore.QRect(400, 70, 81, 31))
        self.Fsek.setObjectName("Fsek")
        self.Lstopnie = QtWidgets.QLineEdit(Dialog)
        self.Lstopnie.setGeometry(QtCore.QRect(240, 140, 61, 31))
        self.Lstopnie.setObjectName("Lstopnie")
        self.Lmin = QtWidgets.QLineEdit(Dialog)
        self.Lmin.setGeometry(QtCore.QRect(320, 140, 61, 31))
        self.Lmin.setObjectName("Lmin")
        self.Lsek = QtWidgets.QLineEdit(Dialog)
        self.Lsek.setGeometry(QtCore.QRect(400, 140, 81, 31))
        self.Lsek.setObjectName("Lsek")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(240, 20, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 380, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(50, 480, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(50, 550, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.Xdw = QtWidgets.QLabel(Dialog)
        self.Xdw.setGeometry(QtCore.QRect(380, 450, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Xdw.setFont(font)
        self.Xdw.setObjectName("Xdw")
        self.Ydw = QtWidgets.QLabel(Dialog)
        self.Ydw.setGeometry(QtCore.QRect(590, 450, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Ydw.setFont(font)
        self.Ydw.setObjectName("Ydw")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(40, 610, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.wynikx2000 = QtWidgets.QLabel(Dialog)
        self.wynikx2000.setGeometry(QtCore.QRect(330, 490, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.wynikx2000.setFont(font)
        self.wynikx2000.setText("")
        self.wynikx2000.setObjectName("wynikx2000")
        self.wynikx92 = QtWidgets.QLabel(Dialog)
        self.wynikx92.setGeometry(QtCore.QRect(330, 550, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.wynikx92.setFont(font)
        self.wynikx92.setText("")
        self.wynikx92.setObjectName("wynikx92")
        self.wyniky2000 = QtWidgets.QLabel(Dialog)
        self.wyniky2000.setGeometry(QtCore.QRect(530, 490, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.wyniky2000.setFont(font)
        self.wyniky2000.setText("")
        self.wyniky2000.setObjectName("wyniky2000")
        self.wyniky92 = QtWidgets.QLabel(Dialog)
        self.wyniky92.setGeometry(QtCore.QRect(530, 550, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.wyniky92.setFont(font)
        self.wyniky92.setText("")
        self.wyniky92.setObjectName("wyniky92")
        self.GRS80 = QtWidgets.QPushButton(Dialog)
        self.GRS80.setGeometry(QtCore.QRect(60, 220, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.GRS80.setFont(font)
        self.GRS80.setObjectName("GRS80")
        self.WRS84 = QtWidgets.QPushButton(Dialog)
        self.WRS84.setGeometry(QtCore.QRect(60, 290, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.WRS84.setFont(font)
        self.WRS84.setObjectName("WRS84")
        self.strefa5 = QtWidgets.QRadioButton(Dialog)
        self.strefa5.setGeometry(QtCore.QRect(300, 230, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.strefa5.setFont(font)
        self.strefa5.setObjectName("strefa5")
        self.strefa6 = QtWidgets.QRadioButton(Dialog)
        self.strefa6.setGeometry(QtCore.QRect(300, 260, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.strefa6.setFont(font)
        self.strefa6.setObjectName("strefa6")
        self.strefa7 = QtWidgets.QRadioButton(Dialog)
        self.strefa7.setGeometry(QtCore.QRect(300, 290, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.strefa7.setFont(font)
        self.strefa7.setObjectName("strefa7")
        self.strefa8 = QtWidgets.QRadioButton(Dialog)
        self.strefa8.setGeometry(QtCore.QRect(300, 320, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.strefa8.setFont(font)
        self.strefa8.setObjectName("strefa8")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(220, 190, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.wynikxgk = QtWidgets.QLabel(Dialog)
        self.wynikxgk.setGeometry(QtCore.QRect(330, 610, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.wynikxgk.setFont(font)
        self.wynikxgk.setText("")
        self.wynikxgk.setObjectName("wynikxgk")
        self.wynikygk = QtWidgets.QLabel(Dialog)
        self.wynikygk.setGeometry(QtCore.QRect(530, 610, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.wynikygk.setFont(font)
        self.wynikygk.setText("")
        self.wynikygk.setObjectName("wynikygk")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Wprowadź phi:"))
        self.label_2.setText(_translate("Dialog", "Wprowadź lambde:"))
        self.label_5.setText(_translate("Dialog", "Stopnie   Minuty   Sekundy"))
        self.label_6.setText(_translate("Dialog", "Wyniki:"))
        self.label_7.setText(_translate("Dialog", "Układ 2000:"))
        self.label_8.setText(_translate("Dialog", "Układ 1992:"))
        self.Xdw.setText(_translate("Dialog", "X"))
        self.Ydw.setText(_translate("Dialog", "Y"))
        self.label_11.setText(_translate("Dialog", "Płaszczyzna Gaussa-Krugera"))
        self.GRS80.setText(_translate("Dialog", "GRS80"))
        self.WRS84.setText(_translate("Dialog", "WGS84"))
        self.strefa5.setText(_translate("Dialog", "5"))
        self.strefa6.setText(_translate("Dialog", "6"))
        self.strefa7.setText(_translate("Dialog", "7"))
        self.strefa8.setText(_translate("Dialog", "8"))
        self.label_3.setText(_translate("Dialog", "Numer strefy (PL-2000)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

