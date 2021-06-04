import tp_thj as function
from PyQt5.QtWidgets import QFrame,QMainWindow,QApplication, QWidget ,QPushButton ,QLabel ,QDial,QLCDNumber,QProgressBar,QComboBox
from PyQt5.QtWidgets import QGridLayout,QVBoxLayout,QScrollArea,QStackedLayout,QScrollBar,QTableWidget,QTableWidgetItem
from PyQt5.QtGui import QPixmap,QImage,QFont,QIcon,QFontDatabase
from PyQt5.QtCore import Qt,QSize
import sys
class onevsone(QWidget):
    def __init__(self):
        super().__init__()
        self.font=QFontDatabase()
        self.font.addApplicationFont("FrederickatheGreat-Regular.ttf")
        print(self.font.families())

        self.nbs=3
        self.layout=QGridLayout()
        self.setLayout(self.layout)
        #le bouton retour
        self.retour=QPushButton()
        self.mapimage=QPixmap("back.png")
        self.mapimage.scaledToWidth(20)
        self.icon=QIcon(self.mapimage)
        self.retour.setIcon(self.icon)
        self.retour.setIconSize(QSize(80,80))
        self.retour.setFlat(True)
        self.layout.addWidget(self.retour,0,0)
        #la scroll area
        self.textres=""
        self.resultat=QLabel(self.textres)

        self.scrol=QScrollArea()
        self.scrol.setFrameShape(QFrame.NoFrame)

        self.layout.addWidget(self.scrol,0,1,5,1)
        self.paneau=QWidget()
        self.scrol.setWidget(self.paneau)
        self.scrollaout=QGridLayout()
        self.paneau.setLayout(self.scrollaout)
        self.scrol.setWidgetResizable(True)

        #le tableau
        self.table = QTableWidget()
        self.table.setRowCount(self.nbs)
        self.table.setColumnCount(self.nbs)
        for i in range(self.nbs):
            self.table.setColumnWidth(i,200)
            self.table.setRowHeight(i,100)

        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setVisible(False)
        self.table.setFrameShape(QFrame.NoFrame)

        self.table.setStyleSheet("""color:#fffff8;
                                    font-size: 16pt;
                                    border-bottom: 1px solid #fffff8;
                                    border-right: 1px solid #fffff8;    
                                    border-top: 1px solid #fffff8; 
                                    border-left: 1px solid #fffff8;
                                    font-family: Heina’s Hurry;""")
        self.table.setFixedSize(201 *self.nbs,101 * self.nbs)
        self.scrollaout.addWidget(self.table,1,1,3,1)
        self.scrollaout.addWidget(self.resultat, 0, 0,1,3)
        #aleatoire
        self.aleatoire=QPushButton("")
        aleatoire=QPixmap("aleatoire.png")
        self.aleatoire.setIcon(QIcon(aleatoire))
        self.aleatoire.setIconSize(QSize(220,100))
        self.aleatoire.setFocusPolicy(Qt.NoFocus)
        self.aleatoire.setFlat(True)
        self.layout.addWidget(self.aleatoire,0,2)
        self.aleatoire.clicked.connect(self.generation_aleatoire)
        #Strictement-Dominante
        self.SD=QPushButton("")
        self.SD.setIcon(QIcon(QPixmap("strictementd.png")))
        self.SD.setIconSize(QSize(220,100))
        self.SD.setFlat(True)
        self.layout.addWidget(self.SD,1,2)
        self.SD.clicked.connect(self.lancer_SD)
        #ES
        self.ES = QPushButton("")
        self.ES.setIcon(QIcon(QPixmap("successive.png")))
        self.ES.setIconSize(QSize(220, 100))
        self.ES.setFlat(True)
        self.layout.addWidget(self.ES, 2,2 ,4,1)


        self.show()
    def generation_aleatoire(self):
        self.textres = ""
        self.resultat.setText(self.textres)
        self.resultat.setStyleSheet("color:white;")
        self.resultat.setFont(QFont("frederickathegreat", 16))
        function.anintiri.clear()
        arbre=function.arbre(nbstrat=self.nbs,nbjoueur=2,joueur=2)
        arbre.parcour_cible()
        for i in function.anintiri:
            print(i)
            self.table.setItem(i[0][1],i[0][2],QTableWidgetItem(str(i[1])))
    def lancer_SD(self):

        sd1=function.SDtest(function.anintiri,numjoueur=1)
        sd2=function.SDtest(function.anintiri,numjoueur=2)
        print(sd1,sd2)
        if sd2!=None and sd1!=None:
            for i in range(self.nbs):
                self.textres = "-la strategie num:" + str(
                    sd1 + 1) + " du joueur un \nest une strategie strictement dominante\n"+"-la strategie num:" + str(
                    sd2 + 1) + " du joueur deux \nest une strategie strictement dominante\n"+"l'issue"+self.table.item(sd1,sd2).text()+"est l'équilibre du jeu en  stratégie dominante"
                self.resultat.setText(self.textres)
                self.resultat.setStyleSheet("color:white;")
                self.resultat.setFont(QFont(self.font.applicationFontFamilies(0)[0], 25))
                self.table.item(sd1,i).setBackground(Qt.blue)
                self.table.item(i, sd2).setBackground(Qt.red)
                self.table.item(sd1,sd2).setBackground(Qt.green)
                print("done")
        else:
            if sd2 != None:
                for i in range(self.nbs):
                    self.textres = "la strategie num:" + str(
                        sd2+1) + " du joueur deux \nest une strategie strictement dominante"
                    self.resultat.setText(self.textres)
                    self.resultat.setStyleSheet("color:white;")
                    self.resultat.setFont(QFont(self.font.applicationFontFamilies(0)[0], 25))
                    self.table.item(i, sd2).setBackground(Qt.red)
                    print("done")
            else:
                if sd1 != None:
                    self.textres = "la strategie num:"+str(sd1+1)+" du joueur un \nest une strategie strictement dominante"
                    self.resultat.setText(self.textres)
                    self.resultat.setStyleSheet("color:white;")
                    self.resultat.setFont(QFont(self.font.applicationFontFamilies(0)[0], 25))
                    for i in range(self.nbs):

                        self.table.item(sd1,i).setBackground(Qt.blue)
                        print("done")
                else:
                    self.textres="les deux joueurs ne possede \npas de strategie strictement dominante"
                    self.resultat.setText(self.textres)
                    self.resultat.setStyleSheet("color:white;")
                    self.resultat.setFont(QFont(self.font.applicationFontFamilies(0)[0],25))

class WINDOW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(600,400)
        self.centre=onevsone()
        self.setCentralWidget(self.centre)
        self.setStyleSheet("""
background-image: url(background.jpg) ;
""")
        self.showMaximized()

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex = WINDOW()
    sys.exit(app.exec_())

