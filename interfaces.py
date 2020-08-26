# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaces.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import random
import matplotlib.pyplot as plt 
from cycler import cycler
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSizePolicy, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.collections import  EventCollection
import numpy as np
import sys
import datetime
from colorama import Fore , Style
class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        # MainWindow.setStyleSheet("background-color:rgb(255, 255, 255) ; color : yellow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 761, 600))
        self.tabWidget.setStyleSheet("color : black ")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.widget_2 = QtWidgets.QWidget(self.tab)
        self.widget_2.setGeometry(QtCore.QRect(20, 30, 701, 131))
        self.widget_2.setObjectName("widget_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 40, 211, 41))
        self.pushButton_2.setStyleSheet("color : white ; background-color : black ;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(310, 30, 371, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color : rgb(255, 255, 255) ; ")
        self.label.setText("")
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.widget = QtWidgets.QWidget(self.tab_2)
        self.widget.setGeometry(QtCore.QRect(10, 20, 711, 141))
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 101, 31))
        self.pushButton.setStyleSheet("color : white ; background-color : black ;")
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setGeometry(QtCore.QRect(200, 30, 491, 41))
        font = QtGui.QFont()
        font.setKerning(True)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("color : white ; background-color : black ;")
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_price = QtWidgets.QLabel(self.widget)
        self.label_price.setGeometry(QtCore.QRect(240, 90, 191, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_price.setFont(font)
        self.label_price.setObjectName("label_price")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tab_3.setGeometry(QtCore.QRect(10, 20, 711, 500))
        self.tab_3.setStyleSheet("color : white ; background-color : black ;")
        self.tabWidget.addTab(self.tab_3, "")

        self.l = QtWidgets.QVBoxLayout(self.tab_3)
        dc = MyDynamicMplCanvas(self.tab_3, width=5, height=4, dpi=100)
        self.l.addWidget(dc)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Check your connection "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Check the connection "))
        self.pushButton.setText(_translate("MainWindow", "Check the URL"))
        self.label_2.setText(_translate("MainWindow", "Your Product Price  :"))
        self.label_price.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tcheck the URL "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Price statistics "))

    ##############################

    #### FOR EMBED MATPLOTLIB ####
    def MyUI(self):
        canvas = Canvas(self, width=5, height=4)
        canvas.move(0, 0)
    ##############################


class Canvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=5, dpi=200):
        default_cycler = (cycler(color=['b']) +
                          cycler(linestyle=['--']))

        fig = Figure(figsize=(height, width), dpi=dpi)
        self.ax1 = plt.subplots(nrows=2)
        self.axes = fig.add_subplot(111)
        print("THE CLASS IS :::", type(self.ax1))
        FigureCanvas.__init__(self, fig)
        #  self.Plot_example(self.axes)
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)



class MyDynamicMplCanvas(Canvas):
    """A canvas that updates itself every second with a new plot."""

    def __init__(self, *args, **kwargs):
        Canvas.__init__(self, *args, **kwargs)
        self.time_list = []
        self.counter = 0
        self.price_list = []
        # Here we activate a timer to use on the timer list 
        timer = QtCore.QTimer(self)
        timer2 = QtCore.QTimer(self)
        timer2.timeout.connect(self.erase_after_nine_seconde)
        # here we connect wich function we will use with the timer  to update the figure 
        timer.timeout.connect(self.update_figure)
        timer.timeout.connect(self.refreshTime)
        timer.timeout.connect(self.change_price)
        timer.start(1000)
        # Delete from  the list time_list 
        timer2.start(9000)

    def compute_initial_figure(self):
        self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], 'r--')

    def counter1(self):
        self.counter = self.counter + 1
        print("Counter is :: ", self.counter)

    def change_price(self):
        # generate a random number between 100 and 140 
        my_num = random.randint(100, 140)
        print("We add a price on the list ",len(self.price_list))
        self.price_list.append(my_num)
  
    # we use this function to delete the content of any 
    def erase_after_nine_seconde(self):
        # to erase we have to check the len of the list
        # Rule : --> always after 9s erase 3 second of price
        removed_elem_index = 6
        while len(self.time_list) >= 9 & removed_elem_index>=0:
            print(Fore.GREEN,'We remove the elem  and now the length is : ',len(self.time_list),Style.RESET_ALL)
            print(Fore.GREEN,'We remove the elem  and now the length is : ',len(self.price_list),Style.RESET_ALL)
            self.time_list.remove(self.time_list[removed_elem_index])
            self.price_list.remove(self.price_list[removed_elem_index])
            print(Fore.YELLOW , "Index of removed elem is ",removed_elem_index,Style.RESET_ALL)
            removed_elem_index -= 1

            
    # Add time  on a time_list  List  
    def refreshTime(self):
        # Declare the new list time
        Today = datetime.datetime.now()
        print(Fore.BLUE,"Today is :::: ", Today,Style.RESET_ALL)
        newTime = Today.strftime("%H:%M:%S")
        print("The length of TIME LIST is :::::", len(self.time_list))
        if len(self.time_list) != 0:
            pass
            # Add at last of the list the new time
            self.time_list.append(newTime)
        else:
            print("i am going to append a new time ")
            self.time_list.append(newTime)

    def update_figure(self):
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        # Here will gets prices randomly 
        """
        l = [random.randint(0, 10) for i in range(4)]
        x = [datetime.datetime.now() + datetime.timedelta(hours=i) for i in range(12)]
        print(Fore.BLACK,"The X list content ::: ",x,Style.RESET_ALL)
        # to give for every element of x 
        y = [i + random.gauss(0, 1) for i, _ in enumerate(x)]
        """
       
        self.axes.cla()
        print("THERE IS THE TYPE OF 8====>---", self.axes)
        self.axes.set_title("My amazone price ")
        yevents1 = EventCollection(self.price_list, color='tab:blue', linelength=0.05, orientation='vertical')
        self.axes.add_collection(yevents1)
        self.axes.plot(self.time_list, self.price_list, '--' , color='tab:orange')
        plt.gcf().autofmt_xdate()
        self.draw()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    amazone_interfaces = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(amazone_interfaces)
    amazone_interfaces.show()
    sys.exit(app.exec_())
