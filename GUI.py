import tp_thj as function
from PyQt5.QtWidgets import QApplication, QWidget ,QPushButton ,QLabel ,QDial,QLCDNumber,QProgressBar
from PyQt5.QtWidgets import QGridLayout,QScrollArea,QStackedLayout,QScrollBar,QTableWidget,QTableWidgetItem
from PyQt5.QtGui import QPixmap,QImage,QFont,QIcon
from PyQt5.QtCore import Qt,QSize
import sys

class MenuPrincipale(QWidget):
    def __init__(self):
        super().__init__()
        self.layout=QGridLayout()


        self.setLayout(self.layout)
class player1v1(QWidget):
    def __init__(self,strategie):
        super().__init__()
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.table=QTableWidget()
        self.table.setRowCount(strategie)
        self.table.setColumnCount(strategie)
        self.layout.addWidget(self.table,0,0,5,1)
        self.aleatoire=QPushButton("Remplir aleatoirment")
        self.aleatoire.clicked.connect(self.remplirAleatoire)
        self.layout.addWidget(self.aleatoire,0,1)
        self.strategie=strategie
        self.FN=function.creer_taille(2,strategie)
        self.table.adjustSize()
    def remplirAleatoire(self):
        self.FN=function.forme_normal(nb_strategie=self.strategie)
        for i in range(self.table.rowCount()):
            for j in range(self.table.columnCount()):
                self.table.setItem(i,j,QTableWidgetItem(str(self.FN[i][j])))


class Mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.layout=QStackedLayout()
        self.setLayout(self.layout)
        self.principale=player1v1(3)

        self.layout.addWidget(self.principale)
        self.setFixedSize(600, 600)
        self.show()


if __name__=='__main__':
    app=QApplication(sys.argv)
    ex = Mainwindow()
    sys.exit(app.exec_())

