import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import uic
import sqlite3


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.pushButton.clicked.connect(self.loadTable)

    def loadTable(self):
        con = sqlite3.connect("coffee.db")
        cur = con.cursor()
        cmd = """SELECT variety_name, degree_roasting, view, 
        description_taste, price, volume_packagings_grams FROM cofe_informations"""
        resultat = cur.execute(cmd).fetchall()
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(["Имя сорта",
                                                    "Степень обжарки",
                                                    "Молотый/в зернах",
                                                    "Описание вкуса",
                                                    "Цена",
                                                    "Объем упаковки"])
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(resultat):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(elem))
        self.tableWidget.resizeColumnsToContents()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())