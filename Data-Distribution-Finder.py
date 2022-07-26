import pandas as pd
import numpy as np
import io
from matplotlib import pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display
from PyQt5 import QtCore, QtGui, QtWidgets
from About_Us import Ui_AboutUs
from About_Application import Ui_AboutApp
def is_number(s):
    try:
        float(s) or int(s)
        return True
    except ValueError:
        return False
def find(x):
    return {
        'pareto': 1,
        'weibull_max': 2,
        'weibull_min': 3,
        't': 4,
        'beta': 5,
        'genextreme': 6,
        'cauchy': 7,
        'chi2': 8,
        'expon': 9,
        'exponpow': 10,
        'gamma': 11,
        'lognorm': 12,
        'norm': 13,
        'powerlaw': 14,
        'rayleigh': 15,
        'uniform' :16
    }[x]

class Ui_MainWindow(object):        
    def OpenWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_AboutApp()
        self.ui.setupUi(self.window)
        self.window.show()
    def openWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_AboutUs()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 591)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("post.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.Browse = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Browse.setFont(font)
        self.Browse.setObjectName("Browse")
        self.verticalLayout_5.addWidget(self.Browse)
        #########################################################
        self.Browse.clicked.connect(self.clicker)
        #########################################################
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        '''
        self.Silhouette = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Silhouette.setFont(font)
        self.Silhouette.setObjectName("Silhouette")
        self.horizontalLayout_2.addWidget(self.Silhouette)
        ########################################################
        #self.Silhouette.setEnabled(False)
        #self.Silhouette.toggled.connect(self.Metric_Choosing)
        ########################################################
        self.Distortion = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Distortion.setFont(font)
        self.Distortion.setObjectName("Distortion")
        self.horizontalLayout_2.addWidget(self.Distortion)
        ########################################################
        self.Distortion.setEnabled(False)
        self.Distortion.toggled.connect(self.Metric_Choosing)
        ########################################################
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        '''
        self.Run = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Run.setFont(font)
        self.Run.setObjectName("Run")
        self.verticalLayout_5.addWidget(self.Run)
        #########################################################
        self.Run.setEnabled(False)
        self.Run.clicked.connect(self.Preprocess_Dataset)
        #########################################################
        self.Save = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Save.setFont(font)
        self.Save.setObjectName("Save")
        self.verticalLayout_5.addWidget(self.Save)
        #########################################################
        self.Save.setEnabled(False)
        self.Save.clicked.connect(self.Save_Result)
        #########################################################
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Tab = QtWidgets.QTabWidget(self.centralwidget)
        self.Tab.setObjectName("Tab")
        self.Log = QtWidgets.QWidget()
        self.Log.setObjectName("Log")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Log)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Log1 = QtWidgets.QTextBrowser(self.Log)
        self.Log1.setObjectName("Log1")
        self.verticalLayout_4.addWidget(self.Log1)
        self.Tab.addTab(self.Log, "")
        self.Result = QtWidgets.QWidget()
        self.Result.setObjectName("Result")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Result)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Result1 = QtWidgets.QTextBrowser(self.Result)
        ##########For not disapperaing the other text and opening the web page######
        self.Result1.setOpenExternalLinks(True)
        self.Result1.setOpenLinks(True)
        self.Result1.anchorClicked.connect(QtGui.QDesktopServices.openUrl)
        ######################################
        self.Result1.setObjectName("Result1")
        self.verticalLayout_3.addWidget(self.Result1)
        self.Tab.addTab(self.Result, "")
        self.verticalLayout.addWidget(self.Tab)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.AboutUs = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.openWindow())
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AboutUs.setFont(font)
        self.AboutUs.setObjectName("AboutUs")
        self.horizontalLayout.addWidget(self.AboutUs)
        self.AboutSoftware = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.OpenWindow())
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AboutSoftware.setFont(font)
        self.AboutSoftware.setObjectName("AboutSoftware")
        self.horizontalLayout.addWidget(self.AboutSoftware)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 459, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Data Distribution Finder"))
        self.label.setText(_translate("MainWindow", "Distribution Fitter"))
        self.Browse.setText(_translate("MainWindow", "Browse"))
        #self.label_2.setText(_translate("MainWindow", "روش جستجوی تعداد دسته های بهینه"))
        #self.Silhouette.setText(_translate("MainWindow", "Silhouette"))
        #self.Distortion.setText(_translate("MainWindow", "Distortion"))
        self.Run.setText(_translate("MainWindow", "Run"))
        self.Save.setText(_translate("MainWindow", "Save"))
        self.Tab.setTabText(self.Tab.indexOf(self.Log), _translate("MainWindow", "Log"))
        self.Tab.setTabText(self.Tab.indexOf(self.Result), _translate("MainWindow", "Result"))
        self.AboutUs.setText(_translate("MainWindow", "About Us"))
        self.AboutSoftware.setText(_translate("MainWindow", "About Application"))
        
    def clicker(self):
        app.processEvents()
        self.Log1.clear()
        self.Result1.clear()
        path,_ = QtWidgets.QFileDialog.getOpenFileName(None, 'Open file', '', 'Excel (*.xls, *.xlsx *.xlsm)')
        print(path)
        if path:
            df = pd.read_excel(path)
            dataset = df.values
            title = df.keys()
            self.Log1.append("The excel file loaded successfully")
            self.Log1.append("\nThe File location is: "+ str(path))
            self.dataset = dataset
            self.title = title
            self.Run.setEnabled(True)
            #self.Distortion.setEnabled(True)
            #self.Silhouette.setEnabled(True)
            return dataset
        else:
            self.Log1.append("\nNo File selected....")
       
    def Preprocess_Dataset(self):
        dataset = self.dataset
        title = self.title
        app.processEvents()
        I = dataset.shape[0]
        J = dataset.shape[1]
        ###### X is data without label and X_bolean is made for checking whter all data is number or not!
        X = []
        X_bolean = []
        for i in range(I):
          for j in range(2, J):
            X.append(dataset[i][j])
            X_bolean.append(is_number(str(dataset[i][j])))
        ##### Creating data with label
        X1 = []
        for i in range(I):
          for j in range(1, J):
            X1.append(dataset[i][j])        
        ###### Cause is_number func didn't support nan, we used isna from pandas    
        Isnan = pd.isna(X)
        sha = np.shape(Isnan)
        Res_nan = False
        Res = True
        for i in range(len(Isnan)):
            Res_nan = Res_nan or Isnan[i]
            Res = Res and X_bolean[i]
        if (Res==True and Res_nan==False and sha[0]):
            X = np.array(X)
            X = np.reshape(X,(I,J-2))
            X1 = np.array(X1)
            X1 = np.reshape(X1,(I,J-1))
            self.Log1.append("\nThe data format is ok.")
            if J-2>1:
                self.Log1.append("\nYour data have more than 3 columns, so the data of %s column should be considerd and analyzed." %(str(title[2])))
                X = X[:,0]
            self.X = X
            self.X1 = X1
            self.Distribution_Fitter()
            
        else:
            self.Log1.append("\nThe File format is not supported. For more information, visit the 'About Application' section.")
    
    
    def Distribution_Fitter(self):
        app.processEvents()
        self.Log1.append("\nFinding the best fitted distribution on input data...")
        #X = self.X
        X = self.X
        import fitter
        f = fitter.Fitter(X, timeout=120)
        f.bins = 10
        f.distributions = fitter.get_common_distributions() + ["pareto","weibull_max","weibull_min","t","beta","genextreme"]
        f.fit()
        self.Log1.append("\nThe best-fitting distribution is found.You can see the results in corresponding tab.")
        summary = f.summary()
        best = f.get_best()
        keys = list(best)
        values = list(best.values())
        param = list(values[0].keys())
        val = list(values[0].values())
        self.Result1.append("The best-fitted distribution is : %s" %(str(keys[0])))
        for i in range(len(param)):
            self.Result1.append("\nThe value of %s is :%d" %(str(param[i]), val[i])) 
        if find(keys[0])==1:
            self.Result1.append("\nFor more information click on <a href=https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pareto.html>%s</a> " %(str(keys[0])))
        elif find(keys[0])==2:
            self.Result1.append("\nFor more information click on <a href=https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.weibull_max.html>%s</a>." %(str(keys[0])))
        elif find(keys[0])==3:
            self.Result1.append("\nFor more information click on <a href=https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.weibull_min.html>%s</a>." %(str(keys[0])))
        elif find(keys[0])==4:
            self.Result1.append("\nFor more information click on <a href=https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.t.html>%s</a>." %(str(keys[0])))
        elif find(keys[0])==5:
            self.Result1.append("\nFor more information click on <a href=https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.beta.html>%s</a>." %(str(keys[0])))
        elif find(keys[0])==6:
            self.Result1.append("\nFor more information click on <a href=https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.genextreme.html>%s</a>." %(str(keys[0])))
        elif find(keys[0])==7:
            self.Result1.append("\nFor more information click on <a href=https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.cauchy.html>%s</a>." %(str(keys[0])))
        elif find(keys[0])==8:
            self.Result1.append("\nFor more information click on <a href=https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2.html>%s</a>." %(str(keys[0])))
        elif find(keys[0])==9:
            self.Result1.append("\nFor more information click on <a href=https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.expon.html>%s</a>." %(str(keys[0])))
        elif find(keys[0])==10:
            self.Result1.append("\nFor more information click on <a href=https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.exponpow.html>%s</a>." %(str(keys[0])))
        elif find(keys[0])==11:
            self.Result1.append("\nFor more information click on <a href=https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gamma.html>%s</a>." %(str(keys[0])))
        elif find(keys[0])==12:
            self.Result1.append("\nFor more information click on <a href=https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.lognorm.html>%s</a>." %(str(keys[0])))
        elif find(keys[0])==13:
            self.Result1.append("\nFor more information click on <a href=https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html>%s</a>." %(str(keys[0])))
        elif find(keys[0])==14:
            self.Result1.append("\nFor more information click on <a href=https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.powerlaw.html>%s</a>." %(str(keys[0])))
        elif find(keys[0])==15:
            self.Result1.append("\nFor more information click on <a href=https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rayleigh.html>%s</a>." %(str(keys[0])))
        else:
            self.Result1.append("\nFor more information click on <a href=https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.uniform.html>%s</a>." %(str(keys[0])))
        self.summary = summary
        self.best = best
        self.f = f
        ###############################################
        self.Save.setEnabled(True)
         
    def Save_Result(self):
        app.processEvents()
        summary = self.summary
        best = self.best
        f = self.f
        df_label= pd.DataFrame(
            {
             "sumsquare_error": ["The best-fitted distributions based on the sum of squared errors are listed below.",
                                 "In addition to the sum of squared error, AIC and BIC criteria are also determined for each distribution.",
                                 "The principal parameters of the best-fitting distribution are displayed next to the distribution's name."]
             })
        #########################result making################################
        df_best = pd.DataFrame.from_dict(best)
        df_best = pd.DataFrame.transpose(df_best)
        concat_df = pd.concat([df_label, summary])
        concat_df = concat_df.join(df_best).fillna("-")
        #########################plot making##################################
        title = self.title
        tlt = get_display( arabic_reshaper.reshape(title[2]))
        csfont = {'fontname':'B Nazanin', 'size':20}
        plt.figure()
        plt.title(tlt,**csfont)
        f.hist()
        f.plot_pdf(names=None, Nbest=1, lw=2, method='sumsquare_error')
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        ########################################################################
        
        path2,_ = QtWidgets.QFileDialog.getSaveFileName(None, 'Save file', '', 'Excel (*.xlsx)')
        print(path2)
        if path2:
            writer = pd.ExcelWriter(path2, engine = 'xlsxwriter')
            concat_df.to_excel(writer, sheet_name='results')
            worksheet = writer.sheets['results']
            worksheet.insert_image('C2', 'figure', options={'image_data':buf}) 
            writer.save()
            buf.close()
            self.Log1.append("\nFile has been saved successfully.")
            self.Log1.append("The File location is: "+ str(path2))
        else:
            self.Log1.append("\nThe File has not been saved.")
         
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
