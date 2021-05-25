import tp_thj as function
from PyQt5.QtWidgets import QApplication, QWidget ,QPushButton ,QLabel ,QDial,QLCDNumber,QProgressBar,QComboBox
from PyQt5.QtWidgets import QGridLayout,QVBoxLayout,QScrollArea,QStackedLayout,QScrollBar,QTableWidget,QTableWidgetItem
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
        self.scroll=QScrollArea()
        self.scroll.setWidgetResizable(True)

        self.interface=QWidget()
        self.scroll.setWidget(self.interface)
        self.table=QTableWidget()
        self.table.setRowCount(strategie)
        self.table.setColumnCount(strategie)
        self.table.setFixedSize(30+100*strategie,30+30*strategie)
        self.layout.addWidget(self.scroll,0,1,8,1)
        self.interfaceL=QVBoxLayout()
        self.interfaceL.addWidget(self.table)
        self.interface.setLayout(self.interfaceL)
        self.aleatoire=QPushButton("Remplir aleatoirment")
        self.aleatoire.clicked.connect(self.remplirAleatoire)
        self.sd=QPushButton("SD")
        self.sd.clicked.connect(self.SD)
        self.es = QPushButton("ES")
        self.retour=QPushButton("retour")
        self.layout.addWidget(self.retour, 0, 0)
        self.box=QComboBox()
        for i in range(2,20):
            self.box.addItem(str(i))
        self.box.setCurrentIndex(1)
        self.box.currentTextChanged.connect(self.changestrat)
        self.layout.addWidget(self.box,0,2)
        self.es.clicked.connect(self.ES)
        self.layout.addWidget(self.aleatoire,1,2)
        self.layout.addWidget(self.sd, 2, 2)
        self.layout.addWidget(self.es, 3, 2)
        self.strategie=strategie
        self.FN=function.creer_taille(2,strategie)
        self.table.adjustSize()
        self.prisonier=QPushButton("dilemme du prisonnier")
        self.layout.addWidget(self.prisonier,4,2)
        self.prisonier.clicked.connect(self.dilemme_prisonier)
        self.tirelire = QPushButton("jeux de la tirelire")
        self.layout.addWidget(self.tirelire, 5, 2)
        self.tirelire.clicked.connect(self.jeux_tirelire)
    def changestrat(self):
        self.strategie=int(self.box.currentText())
    def jeux_tirelire(self):
        self.FN = [[(0, 0), (75, -25)], [(-25, 75), (50, 50)]]
        for i in range(0, self.interfaceL.count()):
            self.interfaceL.itemAt(i).widget().deleteLater()
        self.table = QTableWidget()
        self.table.setRowCount(2)
        self.table.setColumnCount(2)
        self.table.setFixedSize(30 + 100 * 2, 30 + 30 * 2)
        self.interfaceL.addWidget(QLabel("jeux de la tirelire"))
        self.interfaceL.addWidget(self.table)
        for i in range(self.table.rowCount()):
            for j in range(self.table.columnCount()):
                self.table.setItem(i, j, QTableWidgetItem(str(self.FN[i][j])))
        self.SD()
        self.ES()
    def dilemme_prisonier(self):
        self.FN = [[(-1, -1), (-10, 0)], [(0, -10), (-5, -5)]]
        for i in range(0, self.interfaceL.count()):
            self.interfaceL.itemAt(i).widget().deleteLater()
        self.table = QTableWidget()
        self.table.setRowCount(2)
        self.table.setColumnCount(2)
        self.table.setFixedSize(30 + 100 * 2, 30 + 30 * 2)
        self.interfaceL.addWidget(QLabel("dilemme du prisonnier"))
        self.interfaceL.addWidget(self.table)
        for i in range(self.table.rowCount()):
            for j in range(self.table.columnCount()):
                self.table.setItem(i,j,QTableWidgetItem(str(self.FN[i][j])))
        self.SD()
        self.ES()

    def remplirAleatoire(self):
        self.FN=function.forme_normal(nb_strategie=self.strategie)
        for i in range(0, self.interfaceL.count()):
            self.interfaceL.itemAt(i).widget().deleteLater()
        self.table = QTableWidget()
        self.table.setRowCount(self.strategie)
        self.table.setColumnCount(self.strategie)
        self.table.setFixedSize(30 + 100 * self.strategie, 30 + 30 * self.strategie)
        self.interfaceL.addWidget(self.table)
        for i in range(self.table.rowCount()):
            for j in range(self.table.columnCount()):
                self.table.setItem(i,j,QTableWidgetItem(str(self.FN[i][j])))
    def SD(self):
        l=self.FN.copy()
        if(len(l[0][0])!=0):
            x=function.sd(l,joueur=0,strategie=self.strategie)
            if(x!=None):
                for ligne in range(len(l[x])):
                    self.table.item(x,ligne).setBackground(Qt.red)
            y=function.sd([list(i) for i in zip(*l)],joueur=1,strategie=self.strategie)
            if(y!=None):
                for Colonne in range(len(l[y])):
                    self.table.item(Colonne,y).setBackground(Qt.blue)
            if(x!=None and y!=None):
                self.table.item(x, y).setBackground(Qt.green)
    def ES(self):
        function.stack.clear()
        l=self.FN.copy()
        function.ES(l)
        for i in function.stack:
            print(i)
            x=QLabel()
            x.setText("elimination de la strategie:"+str(i[0])+"\napres elimination:")
            self.interfaceL.addWidget(x)
            t=QTableWidget()
            t.setRowCount(len(i[1]))
            t.setColumnCount(len(i[1][0]))
            t.setFixedSize(30 + 100 * t.columnCount(), 30 + 30 * t.rowCount())
            for k in range(t.rowCount()):
                for j in range(t.columnCount()):
                    print(str(i[1][k][j]))
                    t.setItem(k, j, QTableWidgetItem(str(i[1][k][j])))

            self.interfaceL.addWidget(t)
            if (t.rowCount() == 1 and t.columnCount() == 1):
                break





class Mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.layout=QStackedLayout()
        self.setLayout(self.layout)
        self.principale=player1v1(3)

        self.layout.addWidget(self.principale)
        self.setFixedSize(800, 800)
        self.show()


if __name__=='__main__':
    app=QApplication(sys.argv)
    ex = Mainwindow()
    sys.exit(app.exec_())

