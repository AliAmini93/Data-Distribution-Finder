# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'About_Us.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AboutUs(object):
    def setupUi(self, AboutUs):
        AboutUs.setObjectName("AboutUs")
        AboutUs.resize(300, 180)
        self.horizontalLayout = QtWidgets.QHBoxLayout(AboutUs)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textBrowser_About_us = QtWidgets.QTextBrowser(AboutUs)
        self.textBrowser_About_us.setObjectName("textBrowser_About_us")
        self.horizontalLayout.addWidget(self.textBrowser_About_us)

        self.retranslateUi(AboutUs)
        QtCore.QMetaObject.connectSlotsByName(AboutUs)

    def retranslateUi(self, AboutUs):
        _translate = QtCore.QCoreApplication.translate
        AboutUs.setWindowTitle(_translate("AboutUs", "About Us"))
        self.textBrowser_About_us.setHtml(_translate("AboutUs", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\"font-family:'Times New Roman'; font-size:13pt;\">This application has been provided by Ali Amini in the statistics and data analysis group of the National Post Company of Iran.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:1pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\"font-family:'Times New Roman'; font-size:13pt; font-weight:2000;\">Contact info:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\"font-family:'Times New Roman'; font-size:13pt;\">aliamini09@yahoo.com</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\"font-family:'Times New Roman'; font-size:13pt;\">+989100014392</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AboutUs = QtWidgets.QDialog()
    ui = Ui_AboutUs()
    ui.setupUi(AboutUs)
    AboutUs.show()
    sys.exit(app.exec_())
