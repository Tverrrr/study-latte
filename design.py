# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_2(object):
    def setupUi(self, MainWindow_2):
        MainWindow_2.setObjectName("MainWindow_2")
        MainWindow_2.resize(800, 688)
        self.centralwidget = QtWidgets.QWidget(MainWindow_2)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 801, 561))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 570, 801, 71))
        self.pushButton.setObjectName("pushButton")
        MainWindow_2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow_2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_2)
        self.statusbar.setObjectName("statusbar")
        MainWindow_2.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_2)

    def retranslateUi(self, MainWindow_2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_2.setWindowTitle(_translate("MainWindow_2", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow_2", "Добавить/изменить данные в базе данных"))
