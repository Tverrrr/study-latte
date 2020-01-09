import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from design import Ui_MainWindow_2
from addEditCoffeeForm import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow_2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_new_window)
        self.con = sqlite3.connect("data/coffee.db")
        self.update_result()

    def update_result(self):
        cur = self.con.cursor()
        result = cur.execute("SELECT * FROM coffee").fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def open_new_window(self):
        self.op = MainWindow_2()
        self.op.show()
        self.close()


class MainWindow_2(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("data/coffee.db")
        self.pushButton_2.clicked.connect(self.old_window)
        self.update_result()
        self.tableWidget.itemChanged.connect(self.item_changed)
        self.pushButton.clicked.connect(self.save_results)
        self.pushButton_2.clicked.connect(self.old_window)

    def update_result(self):
        cur = self.con.cursor()
        result = cur.execute("SELECT * FROM coffee").fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.modified = {}

    def item_changed(self, item):
        self.modified[self.titles[item.column()]] = item.text()

    def save_results(self):
        if self.modified:
            cur = self.con.cursor()
            que = "UPDATE coffee SET\n"
            for key in self.modified.keys():
                que += "{}='{}'\n".format(key, self.modified.get(key))
            que += "WHERE id = ?"
            cur.execute(que, (self.spinBox.text(),))
            self.con.commit()

    def old_window(self):
        self.op = MainWindow()
        self.op.show()
        self.close()

app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec_())