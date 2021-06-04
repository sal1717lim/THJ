import tp_thj as function
from PyQt5.QtWidgets import QFrame,QMainWindow,QApplication, QWidget ,QPushButton ,QLabel ,QDial,QLCDNumber,QProgressBar,QComboBox
from PyQt5.QtWidgets import QGridLayout,QHBoxLayout,QVBoxLayout,QScrollArea,QStackedLayout,QScrollBar,QTableWidget,QTableWidgetItem
from PyQt5.QtGui import QPixmap,QImage,QFont,QIcon,QFontDatabase
from PyQt5.QtCore import Qt,QSize
import sys
class onevsone(QWidget):
    def __init__(self):
        super().__init__()
        self.font=QFontDatabase()
        self.font.addApplicationFont("FrederickatheGreat-Regular.ttf")
        print(self.font.families())

        self.nbs=2
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
        self.layout.addWidget(self.retour,0,0,1,1)
        #la scroll area
        self.textres=""
        self.resultat=QLabel(self.textres)
        self.scrol=QScrollArea()
        self.scrol.setFrameShape(QFrame.NoFrame)
        self.layout.addWidget(self.scrol,0,1,7,4)
        self.paneau=QWidget()
        self.scrol.setWidget(self.paneau)
        self.scrollaout=QGridLayout()
        self.paneau.setLayout(self.scrollaout)
        self.scrol.setWidgetResizable(True)
        self.stack=QWidget()
        self.liststack=[]
        self.layoutstack=QStackedLayout()
        self.stack.setLayout(self.layoutstack)
        self.scrollaout.addWidget(self.stack,0,0)
        self.pointeur=0

        #le tableau
        self.liststack.append(QWidget())
        grid=QGridLayout()
        self.liststack[-1].setLayout(grid)
        self.table = QTableWidget()
        self.table.setRowCount(self.nbs)
        self.table.setColumnCount(self.nbs)
        for i in range(self.nbs):
            self.table.setColumnWidth(i,150)
            self.table.setRowHeight(i,80)

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
        self.table.setFixedSize(151 *self.nbs,81 * self.nbs)
        grid.addWidget(self.table,1,1,3,1)
        grid.addWidget(self.resultat, 0, 0,1,3)
        for i in self.liststack:
            self.layoutstack.addWidget(i)
        #aleatoire
        self.aleatoire=QPushButton("")
        aleatoire=QPixmap("aleatoire.png")
        self.aleatoire.setIcon(QIcon(aleatoire))
        self.aleatoire.setIconSize(QSize(220,100))
        self.aleatoire.setFocusPolicy(Qt.NoFocus)
        self.aleatoire.setFlat(True)
        self.layout.addWidget(self.aleatoire,0,7)
        self.aleatoire.clicked.connect(self.generation_aleatoire)
        #Strictement-Dominante
        self.SD=QPushButton("")
        self.SD.setIcon(QIcon(QPixmap("strictementd.png")))
        self.SD.setIconSize(QSize(220,100))
        self.SD.setFlat(True)
        self.layout.addWidget(self.SD,1,7)
        self.SD.clicked.connect(self.lancer_SD)
        #ES
        self.ES = QPushButton("")
        self.ES.setIcon(QIcon(QPixmap("successive.png")))
        self.ES.setIconSize(QSize(220, 100))
        self.ES.setFlat(True)
        self.layout.addWidget(self.ES, 2,7 )
        self.ES.clicked.connect(self.runES)
        #droite
        self.droite=QPushButton("")
        self.droite.setIcon(QIcon(QPixmap("droite.png")))
        self.droite.setIconSize(QSize(220,100))
        self.layout.addWidget(self.droite,7,3,1,2)
        self.droite.show()
        self.droite.setFlat(True)
        self.droite.setEnabled(False)
        self.droite.clicked.connect(self.goDroite)
        self.show()
        #gauche
        self.gauche = QPushButton("")
        self.gauche.setIcon(QIcon(QPixmap("gauche.png")))
        self.gauche.setIconSize(QSize(220, 100))
        self.layout.addWidget(self.gauche, 7, 1, 1, 2)
        self.gauche.show()
        self.gauche.setEnabled(False)
        self.gauche.setFlat(True)
        self.show()
        self.gauche.clicked.connect(self.goGauche)
    def goGauche(self):
        print(self.pointeur)
        if (self.pointeur > 0 ):

            self.pointeur = self.pointeur -1
            self.droite.setEnabled(True)
            self.layoutstack.setCurrentWidget(self.liststack[self.pointeur])
        else:
            self.gauche.setDisabled(True)
    def goDroite(self):
        print(self.pointeur)
        if(self.pointeur<len(function.ESList) ):

            self.pointeur=self.pointeur+1
            self.gauche.setEnabled(True)
            self.layoutstack.setCurrentWidget(self.liststack[self.pointeur])
        else:
            self.droite.setDisabled(True)
    def runES(self):
        function.ESList.clear()
        function.FN=function.anintiri.copy()
        function.ES(2,self.nbs)
        if len(function.ESList)!=0:
            self.textres = "naviguer avec les fleches"
            self.resultat.setText(self.textres)
            self.resultat.setStyleSheet("color:white;")
            self.resultat.setFont(QFont(self.font.applicationFontFamilies(0)[0], 25))
            self.droite.setEnabled(True)
            for i in function.ESList:
                x=QWidget()
                layout=QGridLayout()
                x.setLayout(layout)
                lab=QLabel()

                textres = "la strategie :"+str(i[1])+"\ndu joueur "+str(i[0])+" est une strategie faiblement dominée\napres elimination"
                lab.setText(textres)
                lab.setStyleSheet("color:white;")
                lab.setFont(QFont(self.font.applicationFontFamilies(0)[0], 50/self.nbs))
                layout.addWidget(lab,0,0,1,3)
                self.liststack.append(x)
                self.layoutstack.addWidget(x)
                table=QTableWidget()
                table.setRowCount(self.nbs)
                table.setColumnCount(self.nbs)
                table.setFrameShape(QFrame.NoFrame)
                table.setFixedSize(151 * self.nbs, 81 * self.nbs)
                for k in range(self.nbs):
                    table.setColumnWidth(k, 150)
                    table.setRowHeight(k, 80)

                table.verticalHeader().setVisible(False)
                table.horizontalHeader().setVisible(False)
                table.setStyleSheet("""color:#fffff8;
                                                    font-size: 16pt;
                                                    border-bottom: 1px solid #fffff8;
                                                    border-right: 1px solid #fffff8;    
                                                    border-top: 1px solid #fffff8; 
                                                    border-left: 1px solid #fffff8;
                                                    """)
                for j in i[2]:
                    print(j[0][1],j[0][2],j[1])

                    table.setItem(j[0][1], j[0][2], QTableWidgetItem(str(j[1])))
                    table.item(j[0][1],j[0][2]).setFont(QFont(self.font.applicationFontFamilies(0)[0], 25))

                layout.addWidget(table,1,1)
        else:
            self.textres = "elimination successive impossible"
            self.resultat.setText(self.textres)
            self.resultat.setStyleSheet("color:white;")
            self.resultat.setFont(QFont(self.font.applicationFontFamilies(0)[0], 25))







    def generation_aleatoire(self):
        self.layoutstack.setCurrentWidget(self.liststack[0])
        self.pointeur=0
        for i in range(len(self.liststack)-1,0,-1):
            self.layoutstack.removeWidget(self.liststack[i])
            self.liststack.remove(self.liststack[i])
        self.droite.setEnabled(False)
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
            self.table.item(i[0][1], i[0][2]).setFont(QFont(self.font.applicationFontFamilies(0)[0], 25))
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
                self.resultat.setFont(QFont(self.font.applicationFontFamilies(0)[0], 22))
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
                    self.resultat.setFont(QFont(self.font.applicationFontFamilies(0)[0], 22))
                    self.table.item(i, sd2).setBackground(Qt.red)
                    print("done")
            else:
                if sd1 != None:
                    self.textres = "la strategie num:"+str(sd1+1)+" du joueur un \nest une strategie strictement dominante"
                    self.resultat.setText(self.textres)
                    self.resultat.setStyleSheet("color:white;")
                    self.resultat.setFont(QFont(self.font.applicationFontFamilies(0)[0], 22))
                    for i in range(self.nbs):

                        self.table.item(sd1,i).setBackground(Qt.blue)
                        print("done")
                else:
                    self.textres="les deux joueurs ne possede \npas de strategie strictement dominante"
                    self.resultat.setText(self.textres)
                    self.resultat.setStyleSheet("color:white;")
                    self.resultat.setFont(QFont(self.font.applicationFontFamilies(0)[0],22))

class Principale(QWidget):
    def __init__(self):
        super().__init__()
        self.font = QFontDatabase()
        self.font.addApplicationFont("FrederickatheGreat-Regular.ttf")
        self.layout=QStackedLayout()
        self.setLayout(self.layout)
        self.principale=QWidget()
        self.layout.addWidget(self.principale)
        self.principalelayoyt=QGridLayout()
        self.principale.setLayout(self.principalelayoyt)
        titre=QLabel("   Projet THJ")
        titre.setStyleSheet("color:white;")
        titre.setFont(QFont(self.font.applicationFontFamilies(0)[0],45))
        self.principalelayoyt.addWidget(QWidget(), 1, 0, 2, 3)
        self.principalelayoyt.addWidget(titre,1,1)
        self.deuxj=QPushButton("Deux joueurs")
        self.deuxj.setFlat(True)
        self.deuxj.setStyleSheet("color:white;")
        self.deuxj.setFont(QFont(self.font.applicationFontFamilies(0)[0],40))

        self.principalelayoyt.addWidget(self.deuxj,4,1)
        self.principalelayoyt.addWidget(QWidget(),0,0,1,3)
        self.nj = QPushButton("N joueurs")
        self.nj.setFlat(True)
        self.nj.setStyleSheet("color:white;")
        self.nj.setFont(QFont(self.font.applicationFontFamilies(0)[0], 40))

        self.principalelayoyt.addWidget(self.nj, 5, 1)
        self.par=QLabel("par:-AISSI MOHAMED SALIM\n     -CHIBOUB ABDERRAOUF")
        self.par.setStyleSheet("color:white;")
        self.par.setFont(QFont(self.font.applicationFontFamilies(0)[0], 20))
        self.principalelayoyt.addWidget(QWidget(), 6, 0, 3, 3)
        self.principalelayoyt.addWidget(self.par,9,2,1,1)
        #
        self.menu2j=onevsone()
        self.layout.addWidget(self.menu2j)
        self.deuxj.clicked.connect(self.aller2j)
        self.menu2j.retour.clicked.connect(self.retourprinc)
    def aller2j(self):
        self.layout.setCurrentWidget(self.menu2j)
    def retourprinc(self):
        self.layout.setCurrentWidget(self.principale)
class WINDOW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(600,400)
        self.centre=Principale()
        self.setCentralWidget(self.centre)
        self.setStyleSheet("""
background-image: url(background3.jpg) ;
""")
        self.showMaximized()

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex = WINDOW()
    sys.exit(app.exec_())

