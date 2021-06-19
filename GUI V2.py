import tp_thj as function
from PyQt5.QtWidgets import QFrame,QMainWindow,QApplication, QWidget ,QPushButton ,QLabel ,QDial,QLCDNumber,QProgressBar,QComboBox
from PyQt5.QtWidgets import QGridLayout,QHBoxLayout,QVBoxLayout,QScrollArea,QStackedLayout,QScrollBar,QTableWidget,QTableWidgetItem
from PyQt5.QtGui import QPixmap,QImage,QFont,QIcon,QFontDatabase,QPainter,QColor
from PyQt5.QtCore import Qt,QSize
import sys
position=[50,50]
class onevsone(QWidget):
    def __init__(self):
        super().__init__()
        self.font=QFontDatabase()
        self.font.addApplicationFont("FrederickatheGreat-Regular.ttf")
        self.nbs=4
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
        self.grid=QGridLayout()
        self.liststack[-1].setLayout(self.grid)
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
        self.grid.addWidget(self.table,1,1,3,1)
        self.grid.addWidget(self.resultat, 0, 0,1,3)
        for i in self.liststack:
            self.layoutstack.addWidget(i)
        #aleatoire
        self.aleatoire=QPushButton("génération aléatoire")
        self.aleatoire.setFont(QFont(self.font.applicationFontFamilies(0)[0], 16))
        self.aleatoire.setStyleSheet("color:white;")

        self.aleatoire.setIconSize(QSize(220,100))
        self.aleatoire.setFocusPolicy(Qt.NoFocus)
        self.aleatoire.setFlat(True)
        self.layout.addWidget(self.aleatoire,0,7)
        self.aleatoire.clicked.connect(self.generation_aleatoire)
        #Strictement-Dominante
        self.SD=QPushButton("strategie strictement \ndominante")

        self.SD.setFont(QFont(self.font.applicationFontFamilies(0)[0], 16))
        self.SD.setStyleSheet("color:white;")
        self.SD.setIconSize(QSize(220,100))
        self.SD.setFlat(True)
        self.layout.addWidget(self.SD,1,7)
        self.SD.clicked.connect(self.lancer_SD)
        #ES
        self.ES = QPushButton("élimination successive")
        self.ES.setFont(QFont(self.font.applicationFontFamilies(0)[0], 16))
        self.ES.setStyleSheet("color:white;")
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
        #Nash
        self.nash=QPushButton("équilibre de nash\n en strategie pure")
        self.nash.setIconSize(QSize(220,100))
        self.layout.addWidget(self.nash,3,7)
        self.nash.show()
        self.nash.setFlat(True)
        self.nash.setFont(QFont(self.font.applicationFontFamilies(0)[0], 16))
        self.nash.setStyleSheet("color:white;")
        self.nash.clicked.connect(self.runNash)
        #pareto
        self.pareto = QPushButton("Optimum de pareto")
        self.pareto.setIconSize(QSize(220, 100))
        self.layout.addWidget(self.pareto, 4, 7)
        self.pareto.show()
        self.pareto.setFlat(True)
        self.pareto.setFont(QFont(self.font.applicationFontFamilies(0)[0], 16))
        self.pareto.setStyleSheet("color:white;")
        self.pareto.clicked.connect(self.runPareto)
        # securite
        self.securite = QPushButton("niveau de securite")
        self.securite.setIconSize(QSize(220, 100))
        self.layout.addWidget(self.securite, 5, 7)
        self.securite.show()
        self.securite.setFlat(True)
        self.securite.setFont(QFont(self.font.applicationFontFamilies(0)[0], 16))
        self.securite.setStyleSheet("color:white;")
        self.securite.clicked.connect(self.runSecurite)
        #dilemme du prisonier
        self.prisonier = QPushButton("Le dilemme du prisonnier")
        self.prisonier.setIconSize(QSize(220, 100))
        self.layout.addWidget(self.prisonier, 6, 7)
        self.prisonier.show()
        self.prisonier.setFlat(True)
        self.prisonier.setFont(QFont(self.font.applicationFontFamilies(0)[0], 16))
        self.prisonier.setStyleSheet("color:white;")
        self.prisonier.clicked.connect(self.runprisonier)
        #jeux de la tirelire
        self.tirelire= QPushButton("jeu de la tirelire")
        self.tirelire.setIconSize(QSize(220, 100))
        self.layout.addWidget(self.tirelire, 7, 7)
        self.tirelire.show()
        self.tirelire.setFlat(True)
        self.tirelire.setFont(QFont(self.font.applicationFontFamilies(0)[0], 16))
        self.tirelire.setStyleSheet("color:white;")
        self.tirelire.clicked.connect(self.runtirelire)
        #box
        self.box = QComboBox()
        for i in range(2, 20):
            self.box.addItem(str(i))
        self.box.setCurrentIndex(1)
        self.box.currentTextChanged.connect(self.changestrat)
        self.box.setWindowOpacity(0.5)
        self.box.setStyleSheet("color:blue;")
        self.box.setFont(QFont(self.font.applicationFontFamilies(0)[0], 25))
        self.layout.addWidget(self.box, 2,0)
        #text nombre de strat
        self.strat=QLabel("nombre de strategie")
        self.strat.setFont(QFont(self.font.applicationFontFamilies(0)[0], 20))
        self.strat.setStyleSheet("color:white;")
        self.layout.addWidget(self.strat, 1, 0)
    def runtirelire(self):
        self.textres = """Le jeu suivant est proposé à deux étudiants choisis au hasard : chacun à la possibilité de
mettre 0 ou 100 dinars dans une tirelire. Après que chaque étudiant ait pris sa décision
sans connaitre la décision de l’autre, le contenu de la tirelire sera multipliée par 1.5 et
partagé à parts égales entre les deux étudiants."""
        self.resultat.setText(self.textres)
        self.resultat.setStyleSheet("color:white;")
        self.resultat.setFont(QFont(self.font.applicationFontFamilies(0)[0], 20))
        self.table.setRowCount(2)
        self.table.setColumnCount(2)
        for i in range(2):
            self.table.setColumnWidth(i, 150)
            self.table.setRowHeight(i, 80)
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
        self.table.setFixedSize(151 * 2, 81 * 2)
        self.grid.addWidget(self.table, 1, 1, 3, 1)
        self.grid.addWidget(self.resultat, 0, 0, 1, 3)
        function.anintiri = [
            [{2: 0, 1: 0}, (0, 0)],
            [{2: 0, 1: 1}, (75, -25)],
            [{2: 1, 1: 0}, (-25, 75)],
            [{2: 1, 1: 1}, (50, 50)]
        ]
        self.nbs = 2
        for i in function.anintiri:
            print(i)
            self.table.setItem(i[0][1], i[0][2], QTableWidgetItem(str(i[1])))
            self.table.item(i[0][1], i[0][2]).setFont(QFont(self.font.applicationFontFamilies(0)[0], 25))
    def changestrat(self):
        self.nbs=int(self.box.currentText())
    def runprisonier(self):
        self.textres = """L'exemple phare est le problème du dilemme du prisonnier :\n
Sur un braquage à main armé, deux suspects sont arrêtés par\nla police, qui ont alors deux choix : ils peuvent choisir de se taire ou alors,\ndénoncer leur camarade de jeu.
* Si les deux suspects se dénoncent l'un l'autre, chacun en prendra \npour 5 ans de prison
* Si l'un dénonce et que l'autre se tait, celui qui se tait aura \n10 ans de prison, et l'autre sera relâché
* Si les deux choisissent de se taire, dans le doute, les deux auront 1 an de prison"""
        self.resultat.setText(self.textres)
        self.resultat.setStyleSheet("color:white;")
        self.resultat.setFont(QFont(self.font.applicationFontFamilies(0)[0], 20))
        self.table.setRowCount(2)
        self.table.setColumnCount(2)
        for i in range(2):
            self.table.setColumnWidth(i, 150)
            self.table.setRowHeight(i, 80)
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
        self.table.setFixedSize(151 * 2, 81 * 2)
        self.grid.addWidget(self.table, 1, 1, 3, 1)
        self.grid.addWidget(self.resultat, 0, 0, 1, 3)
        function.anintiri = [
            [{2: 0, 1: 0}, (-1, -1)],
            [{2: 0, 1: 1}, (0, -10)],
            [{2: 1, 1: 0}, (-10, 0)],
            [{2: 1, 1: 1}, (-5, -5)]
        ]
        self.nbs=2
        for i in function.anintiri:
            print(i)
            self.table.setItem(i[0][1],i[0][2],QTableWidgetItem(str(i[1])))
            self.table.item(i[0][1], i[0][2]).setFont(QFont(self.font.applicationFontFamilies(0)[0], 25))
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
            self.resultat.setStyleSheet("color:whitebackground-color: yellow;")
            self.resultat.setFont(QFont(self.font.applicationFontFamilies(0)[0], 25))
    def generation_aleatoire(self):
        self.nbs= int(self.box.currentText())
        self.layoutstack.setCurrentWidget(self.liststack[0])
        self.table.setRowCount(self.nbs)
        self.table.setColumnCount(self.nbs)
        for i in range(self.nbs):
            self.table.setColumnWidth(i, 150)
            self.table.setRowHeight(i, 80)
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
        self.table.setFixedSize(151 * self.nbs, 81 * self.nbs)
        self.grid.addWidget(self.table, 1, 1, 3, 1)
        self.grid.addWidget(self.resultat, 0, 0, 1, 3)
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
    def runNash(self):
        resultat=function.NASH(function.anintiri,2,2,self.nbs)
        print("equilibre de nash",resultat)
        if len(resultat)!=0:
            self.textres = "les équilibres de nash"
            self.resultat.setText(self.textres)
            self.resultat.setStyleSheet("color:white;")
            self.resultat.setFont(QFont(self.font.applicationFontFamilies(0)[0], 25))
            for i in resultat:
                self.table.item(i[0][1], i[0][2]).setBackground(Qt.red)
                print("done")
        else:
            self.textres = "pas d'equilibre de nash en pure"
            self.resultat.setText(self.textres)
            self.resultat.setStyleSheet("color:white;")
            self.resultat.setFont(QFont(self.font.applicationFontFamilies(0)[0], 25))
    def runPareto(self):
        resultat=function.pareto(function.anintiri)
        print("pareto", resultat)
        if len(resultat) != 0:
            self.textres = "les Optimum de pareto"
            self.resultat.setText(self.textres)
            self.resultat.setStyleSheet("color:white;")
            self.resultat.setFont(QFont(self.font.applicationFontFamilies(0)[0], 25))
            for i in resultat:
                self.table.item(i[0][1], i[0][2]).setBackground(Qt.blue)
                print("done")
        else:
            self.textres = "pas d'optimum de pareto"
            self.resultat.setText(self.textres)
            self.resultat.setStyleSheet("color:white;")
            self.resultat.setFont(QFont(self.font.applicationFontFamilies(0)[0], 25))
    def runSecurite(self):
        resultat=function.securite(function.anintiri,2,self.nbs)
        self.textres = "le niveau de securite du joueur 1 est: "+str(resultat[1])+"\nle niveau de securite du joueur 2 est: "+str(resultat[2])
        self.resultat.setText(self.textres)
        self.resultat.setStyleSheet("color:white;")
        self.resultat.setFont(QFont(self.font.applicationFontFamilies(0)[0], 25))
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
        #nj
        self.menuNj=nplayer()
        self.layout.addWidget(self.menuNj)
        self.nj.clicked.connect(self.allerNJ)
        self.menuNj.retour.clicked.connect(self.retourprinc)
    def allerNJ(self):
        self.layout.setCurrentWidget(self.menuNj)
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
class nplayer(QWidget):
    def __init__(self):
        super().__init__()
        self.font = QFontDatabase()
        self.font.addApplicationFont("FrederickatheGreat-Regular.ttf")
        self.nbs=3
        self.nbj=3
        self.layout=QGridLayout()
        self.setLayout(self.layout)
        #retour
        self.retour=QPushButton("")
        self.retour.setIcon(QIcon(QPixmap("back.png")))
        self.retour.setIconSize(QSize(80,80))
        self.retour.setFlat(True)
        self.layout.addWidget(self.retour, 0, 0, 1, 1)
        #stack
        self.textres = ""
        self.resultat = QLabel(self.textres)
        self.scrol = QScrollArea()
        self.scrol.setFrameShape(QFrame.NoFrame)
        self.layout.addWidget(self.scrol, 1, 1, 7, 4)
        self.paneau = QWidget()
        self.scrol.setWidget(self.paneau)
        self.scrollaout = QGridLayout()
        self.paneau.setLayout(self.scrollaout)
        self.scrol.setWidgetResizable(True)
        self.stack = QWidget()
        self.liststack = []
        self.listimage=[]
        self.layoutstack = QStackedLayout()
        self.stack.setLayout(self.layoutstack)
        self.scrollaout.addWidget(self.stack, 0, 0)
        self.pointeur = 0
        #aleatoire
        self.aleatoire=QPushButton("")
        self.aleatoire.setIcon(QIcon(QPixmap("aleatoire.png")))
        self.aleatoire.setIconSize(QSize(220, 100))
        self.aleatoire.setFocusPolicy(Qt.NoFocus)
        self.aleatoire.setFlat(True)
        self.layout.addWidget(self.aleatoire, 0, 7)
        self.aleatoire.clicked.connect(self.generation_aleatoire)
        self.arbre=None
        # box
        self.box2 = QComboBox()
        for i in range(2, 20):
            self.box2.addItem(str(i))
        self.box2.setCurrentIndex(1)
        self.box2.currentTextChanged.connect(self.changej)
        self.box2.setWindowOpacity(0.5)
        self.box2.setStyleSheet("color:blue;")
        self.box2.setFont(QFont(self.font.applicationFontFamilies(0)[0], 25))
        self.layout.addWidget(self.box2, 4, 0)
        # text nombre de strat
        self.j = QLabel("nombre de joeur")
        self.j.setFont(QFont(self.font.applicationFontFamilies(0)[0], 20))
        self.j.setStyleSheet("color:white;")
        self.layout.addWidget(self.j, 3, 0)
        # box
        self.box = QComboBox()
        for i in range(2, 20):
            self.box.addItem(str(i))
        self.box.setCurrentIndex(1)
        self.box.currentTextChanged.connect(self.changestrat)
        self.box.setWindowOpacity(0.5)
        self.box.setStyleSheet("color:blue;")
        self.box.setFont(QFont(self.font.applicationFontFamilies(0)[0], 25))
        self.layout.addWidget(self.box, 2, 0)
        # text nombre de strat
        self.strat = QLabel("nombre de strategie")
        self.strat.setFont(QFont(self.font.applicationFontFamilies(0)[0], 20))
        self.strat.setStyleSheet("color:white;")
        self.layout.addWidget(self.strat, 1, 0)
        # Strictement-Dominante
        self.SD = QPushButton("strategie strictement \ndominante")

        self.SD.setFont(QFont(self.font.applicationFontFamilies(0)[0], 16))
        self.SD.setStyleSheet("color:white;")
        self.SD.setIconSize(QSize(220, 100))
        self.SD.setFlat(True)
        self.layout.addWidget(self.SD, 1, 7)
        self.SD.clicked.connect(self.lancer_SD)
        # ES
        self.ES = QPushButton("élimination successive")
        self.ES.setFont(QFont(self.font.applicationFontFamilies(0)[0], 16))
        self.ES.setStyleSheet("color:white;")
        self.ES.setIconSize(QSize(220, 100))
        self.ES.setFlat(True)
        self.layout.addWidget(self.ES, 2, 7)
        self.ES.clicked.connect(self.runES)
        # Nash
        self.nash = QPushButton("équilibre de nash\n en strategie pure")
        self.nash.setIconSize(QSize(220, 100))
        self.layout.addWidget(self.nash, 3, 7)
        self.nash.show()
        self.nash.setFlat(True)
        self.nash.setFont(QFont(self.font.applicationFontFamilies(0)[0], 16))
        self.nash.setStyleSheet("color:white;")
        self.nash.clicked.connect(self.runNash)
        # pareto
        self.pareto = QPushButton("Optimum de pareto")
        self.pareto.setIconSize(QSize(220, 100))
        self.layout.addWidget(self.pareto, 4, 7)
        self.pareto.show()
        self.pareto.setFlat(True)
        self.pareto.setFont(QFont(self.font.applicationFontFamilies(0)[0], 16))
        self.pareto.setStyleSheet("color:white;")
        self.pareto.clicked.connect(self.runPareto)
        # securite
        self.securite = QPushButton("niveau de securite")
        self.securite.setIconSize(QSize(220, 100))
        self.layout.addWidget(self.securite, 5, 7)
        self.securite.show()
        self.securite.setFlat(True)
        self.securite.setFont(QFont(self.font.applicationFontFamilies(0)[0], 16))
        self.securite.setStyleSheet("color:white;")
        self.securite.clicked.connect(self.runSecurite)
    def lancer_SD(self):
        sd=[]
        print(function.anintiri)
        for i in range(1,self.nbj+1):
            sd.append(function.SDtest(function.anintiri, numjoueur=i))
        text=""
        for i in range(len(sd)):
            if sd[i]==None:
                text=text+"le joueur "+str(i)+"n'a pas de strategie strictement dominante\n"
            else:
                text=text+"la strategie"+str(sd[i])+"du joueur"+str(i)+"est une strategie strictement dominante"
        self.textres = text
        self.resultat.setText(self.textres)
        self.resultat.setStyleSheet("color:white;")
        self.resultat.setFont(QFont(self.font.applicationFontFamilies(0)[0], 25))
        self.layout.addWidget(self.resultat, 0, 1)



    def runES(self):
        pass
    def runNash(self):
        resultat=function.NASH(function.anintiri,self.nbj,self.nbj,self.nbs)
        self.textres = "les equilibre de Nash"+str(resultat)
        self.resultat.setText(self.textres)
        self.resultat.setStyleSheet("color:white;")
        self.resultat.setFont(QFont(self.font.applicationFontFamilies(0)[0], 25))
        self.layout.addWidget(self.resultat, 0, 1)
    def runPareto(self):
        resultat=function.pareto(function.anintiri)
        print(resultat)
        self.textres = "les optimums de pareto" + str(resultat)
        self.resultat.setText(self.textres)
        self.resultat.setStyleSheet("color:white;")
        self.resultat.setFont(QFont(self.font.applicationFontFamilies(0)[0], 25))
        self.layout.addWidget(self.resultat, 0, 1)
    def runSecurite(self):
        resultat = function.securite(function.anintiri, self.nbj, self.nbs)
        self.textres=""
        for i in range(len(resultat)):
            self.textres = self.textres+"le niveau de securite du joueur " + str(i+1) + " est: " + str(resultat[i+1]) + "\n"

        self.resultat.setText(self.textres)
        self.resultat.setStyleSheet("color:white;")
        self.resultat.setFont(QFont(self.font.applicationFontFamilies(0)[0], 25))
        self.layout.addWidget(self.resultat, 0, 1)
    def changestrat(self):
        self.nbs = int(self.box.currentText())

    def changej(self):
        self.nbj= int(self.box2.currentText())
    def generation_aleatoire(self):
        global position
        for i in self.liststack:
            self.layoutstack.removeWidget(i)
            self.liststack.remove(i)
        image=QImage(QSize(2*(self.nbs+self.nbj)*500,(self.nbs+self.nbj)*500),QImage.Format_RGB888)
        image.fill(Qt.black)
        label=QLabel("")
        self.listimage.append(image)
        label.setPixmap(QPixmap.fromImage(image))
        self.liststack.append(label)
        self.layoutstack.addWidget(label)
        self.arbre=function.arbre(self.nbs,self.nbj,self.nbj)
        self.arbre.parcour_cible({})
        image = self.listimage[-1]
        painter = QPainter(image)
        x = self.arbre

        position = [250, 0]
        self.dessiner_arbre(x,image,painter,numjoueur=1)
        label = self.liststack[-1]
        label.setPixmap(QPixmap.fromImage(self.listimage[-1]))
        print(function.anintiri)

    def dessiner_arbre(self,x,image,painter,numjoueur=1):

        global position
        painter.setPen(QColor(255,255, 255))
        if not self.arbre.racine:
         painter.drawEllipse(position[0],position[1],50,50)
        xx=position[0]+25
        yy=position[1]+50
        print(position)

        if isinstance(x.suivant,list):

            for i in range(0,len(self.arbre.suivant)):

                if not self.arbre.racine:
                    painter.drawLine(xx, yy, position[0]-25, position[1] +55)
                    painter.setFont(QFont(self.font.applicationFontFamilies(0)[0], 16))
                    painter.drawText(position[0] - 50 + 25, position[1] + 55 + 25, str(i+1))
                label = self.liststack[-1]
                label.setPixmap(QPixmap.fromImage(image))
                self.arbre=x.suivant[i]
                self.listimage.append(image)

                position[1]=position[1]+55

                position[0] = position[0] - 50

                self.dessiner_arbre(self.arbre,image,painter)
        else:
            painter.setFont(QFont(self.font.applicationFontFamilies(0)[0], 16))
            painter.drawText(position[0]+10,position[1]+70,str(x.suivant))

            position[0] = position[0] +200
if __name__=='__main__':
    app=QApplication(sys.argv)
    ex = WINDOW()
    sys.exit(app.exec_())