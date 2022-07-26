 # -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'About_Application.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AboutApp(object):
    def setupUi(self, AboutApp):
        AboutApp.setObjectName("AboutApp")
        AboutApp.resize(400, 600)
        self.horizontalLayout = QtWidgets.QHBoxLayout(AboutApp)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(AboutApp)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout.addWidget(self.textBrowser)

        self.retranslateUi(AboutApp)
        QtCore.QMetaObject.connectSlotsByName(AboutApp)

    def retranslateUi(self, AboutApp):
        _translate = QtCore.QCoreApplication.translate
        AboutApp.setWindowTitle(_translate("AboutApp", "About Application"))
        self.textBrowser.setHtml(_translate("AboutApp", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"left\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\"font-family:'Times New Roman'; font-size:13pt; font-weight:2000;\">Version 1.0</span></p>"
"<p align=\"justify\" dir=\'ltl\' style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roman'; font-size:13pt;\">This application computes the distribution of one-dimensional data. The format of the input data should be as stated below.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/newPrefix/Form.JPG\" /></p>\n"
"<p align=\"justify\" dir=\'ltl\' style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\"font-family:'Times New Roman'; font-size:13pt;\">The first two columns of data contain the sample number and name, which are reserved by the application and should be produced by the user based on the data. The third column, which holds the attribute values of each sample of data, must be developed and structured by the user. If the number of uploaded data columns exceeds three or there is an issue with the data format, the program will notify you that just the third column will be processed or that the necessary data will not be analyzed. To begin, the user must utilize the browse button to upload the Excel file containing the data into the application. The progress of the work may be seen in the Log Tab at each stage. The result tab displays the final result, which contains the best-fitted distribution and the parameters associated with that distribution. In addition, if you are unfamiliar with the selected distribution, a relevant link has been included to provide further background information. Finally, each user has the option of saving the work result in an Excel file. This file offers a list of the best-chosen distributions for the input data, ordered by implementation error. The parameters of the best distribution, such as mean, standard deviation, and so on, are also listed next to the best distribution's name. In addition, the histogram of the input data and the optimal distribution applied on it can be viewed at the conclusion of this Excel file. If you have any questions regarding how the software operates, please see the About Us section.</span></p></body></html>"))
import Source_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AboutApp = QtWidgets.QDialog()
    ui = Ui_AboutApp()
    ui.setupUi(AboutApp)
    AboutApp.show()
    sys.exit(app.exec_())
