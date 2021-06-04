
"""# TEST IDEE DE MERDE"""

import random as rd


def randtup(low=-10, high=10, nb_joueur=2):
    issue = ()
    for i in range(nb_joueur):
        issue = issue + (rd.randint(low, high),)
    return issue


anintiri = []


# class arbre qui aide a la creation de la forme normal
class arbre:
    def __init__(self, nbstrat=3, nbjoueur=3, joueur=3, racine=True, score=None):
        # une liste variable global qui vas contenir a forme normal NB:changer le nom apres
        global anintiri
        self.suivant = None
        self.nbjoueur = nbjoueur
        # la racine ne contient rien , elle pointe juste vers les strategie du premier joueur
        if racine:
            self.racine = racine
            self.suivant = []
            self.suivant.append(arbre(nbstrat=nbstrat, nbjoueur=self.nbjoueur, joueur=joueur, racine=False))
        else:
            self.racine = racine
            # pour voir si on a atteint les feuilles
            if joueur != 0:
                self.suivant = []
                for i in range(nbstrat):
                    # le numero du joueur
                    self.joueur = joueur
                    # pointé vers les strategie du joueur suivant
                    self.suivant.append(arbre(nbstrat=nbstrat, nbjoueur=self.nbjoueur, joueur=joueur - 1, racine=False))
            else:
                # les feuilles (tuple)
                self.suivant = randtup(nb_joueur=self.nbjoueur)

    def parcour_cible(self, combo={}):
        # la fonction qui creer norte forme normal (le format est un dict qui contient le num de strategie de chaque joueur + l"issue du jeu)
        # exemple [{4: 1, 3: 0, 2: 0, 1: 1}, (3, 5, 10, 9)] pour joueur 4 joue la strat 1, joueur 3 joue la strat 0 .... et l issue du jeu dans un tuple
        # chaque couple dict tuple est dans la list anintiri
        global anintiri
        if not self.racine:
            # voir si c'est une list ou un tuple if list ==>parcour rec
            if isinstance(self.suivant, list):
                for i in range(len(self.suivant)):
                    x = combo.copy()
                    x[self.joueur] = i
                    # creation lu dict
                    self.suivant[i].parcour_cible(combo=x)
            else:
                # append le couple dict tuple
                anintiri.append([combo, self.suivant])
        else:
            for i in self.suivant:
                i.parcour_cible()


nbj = 4
nbs = 2





def SDtest(FN, numjoueur=1, nbstrat=2):
    # trouvé une strategie SD logique comme le cas de 2 joueur
    # on lui donne en parametre le numero du joueur pour voir les strategie d'ou l utilité du dict
    for j in range(nbstrat):
        var = FN.copy()
        strat = []
        # on parcour les strategie , on prend a chaque fois une strategie dans la list strat le rest dans la list var
        for i in FN:
            if i[0][numjoueur] == j:
                strat.append(i)
                var.remove(i)
        dominante = True
        i = 0
        # le parcour comme le cas de 2 joueur a quelque detailles
        while i < len(var) and dominante:
            if i == numjoueur:
                pass
            else:
                k = 0
                while k < len(strat) and dominante:

                    if strat[k][1][numjoueur - 1] < var[i + k][1][numjoueur - 1]:
                        dominante = False
                    k = k + 1
                i
            i = i + len(strat)
        if dominante:
            return strat[0][0][numjoueur]
    return None





def FDtest(FN, numjoueur=1, nbstrat=2):
    FD = []
    for j in range(nbstrat):
        # trouvé une strategie FD logique comme le cas de 2 joueur
        var = FN.copy()
        strat = []
        for i in FN:
            if i[0][numjoueur] == j:
                strat.append(i)
                var.remove(i)
        dominante = True
        i = 0
        # separation comme la fonction precedente
        while i < len(var) and len(strat) != 0 and dominante:
            if i == numjoueur:
                pass
            else:
                k = 0
                while k < len(strat) and len(strat) != 0 and dominante:

                    if strat[k][1][numjoueur - 1] < var[i + k][1][numjoueur - 1]:
                        dominante = False
                    k = k + 1
                if dominante:
                    if strat not in FD:
                        # si strat domine une strat de var , on garde le couple strategie faible dominante ,faible dominé pour l'elimination successive
                        FD.append([strat, var])
            i = i + len(strat)

    return FD




def ES(FN, nb_joueur, nbstrat):
    # on lance FD pour chaque joueur et on delete les strategie faible dominé
    for i in range(1, nb_joueur + 1):
        if len(FDtest(FN, numjoueur=i, nbstrat=nbstrat)) != 0:

            for j in FDtest(FN, numjoueur=i, nbstrat=nbstrat):

                for k in j[1]:
                    FN.remove(k)
            # appel recursif jusque a la fin du parcour
            ES(FN, nb_joueur, nbstrat)

    return FN




dilemeP = [
    [{2: 0, 1: 0}, (-1, -1)],
    [{2: 0, 1: 1}, (0, -10)],
    [{2: 1, 1: 0}, (-10, 0)],
    [{2: 1, 1: 1}, (-5, -5)]
]

print(SDtest(dilemeP, 1))
print(SDtest(dilemeP, 2))
print(ES(dilemeP, 2, 2))