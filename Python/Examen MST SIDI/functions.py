

"""
@author Hassan Zekkouri
MST SIDI 2018/2019
Controle pratique - Graphes en Python
Vendredi 19 Avril 2019 - 16:00

"""
#Question 1
G = [[0, 1, 1, 1],
     [1, 0, 1, 0],
     [1, 1, 0, 1],
     [1, 0, 1, 0]]

#Question 2
def degreeSommet(G, s):
    """
    Rerourne le degree de sommet
    le graphe est non oriente donc le degree
    c'est la somme de la ligne s
    :param G: Matrice d'adjacence
    :param s: sommet
    :return: degree(s)
    """
    res = sum(G[s]) # degree(s)
    return res

#Duestion 3
def estIsole(G, s):
    """
    Le graphe est non oriente donc la
    matrice est symetrique et on test la ligne seulement

    :param G: Matrice d'adjacence
    :param s: sommet
    :return: True or False
    """
    for i in range(len(G)):
        if G[s][i]:
            return False
    return True


#Duestion 4
def chaineEulerienne(G):
    """
    Test si le graphe est eulerienne ou non
    :param G: Matrice d'adjacence
    :return: True or false
    """
    cpt = 0
    for i in range(len(G)):
        if degreeSommet(G, i) % 2:
            cpt += 1
    if cpt == 0 or cpt == 2:
        return True
    else:
        return False

#Question 5
def listeAdjacence(G):
    listPrincipal = []
    for i in range(len(G)):
        ilist = []
        for j in range(len(G)):
            if G[i][j]:
                ilist.append(j);
        listPrincipal.append(ilist)
    return listPrincipal

#Question 6
def sommetsAdj(L, s):
    """
    retourne
    :param L: liste d'adjacence
    :param s: sommet pour laquel on retourne L
    :return: L[s]
    """
    return L[s]

#Question 7
def estComplet(L):
    """
    On test chaque liste elementaire L[s]
    si elles contient toutes les sommets different a s
    alors le graphe est complet
    :param L: Listes D'adjacence
    :return: True or False
    """
    n = len(L)
    for s in range(n):
        cpt = 0
        for succ in L[s]:
            if succ != s: # eliminer les boucles {s,s}
                cpt += 1
        if cpt < n - 1:
            return False
    return True

#Question 8


def estChaine(G, e, s):
    # si l'un des deux sommets est isolé,
    # alors return False
    if (estIsole(G, e) or estIsole(G, s)):
        return False
    else:
        ft = G.copy() # fermeture transitive
        Gtemp = produit(ft, ft)
        while(GequalsGtemp(ft, Gtemp) == False):
            ft = Gtemp
            Gtemp = produit(Gtemp, ft)
            if Gtemp[e][s] : # graphe non oriente
                return True
    return False

def produit(matrix1, matrix2):
    n = len(matrix2)
    res = [ [0 for i in range(n)] for i in range(n) ]
    for i in range(n):
        for j in range(n):
            s = 0
            for k in range(n):
                s += matrix1[i][k] * matrix2[k][j]
            if s:
                res[i][j] = 1
    return res

def GequalsGtemp(matrix1, matrix2):
    n = len(matrix2)
    for i in range(n):
        for j in range(n):
            if matrix1[i][j] != matrix2[i][j]:
                return False
    return True




#Question 8 avec algorithme de Warshall
def estChaineBis(G, s, e):
    """
    Test si s et e forme une chaîne
       :param G: Matrice d'adjacence
       :param e: extrimite initiale
       :param s:  extrimite finale
       :return: True or False
       """
    if estIsole(G, s) or estIsole(G, e):
        return False
    #Warshall - fermeture transitive
    FT = fermetureTrans(G)
    print(FT)
    if FT[s][e]:
        return True
    return False

def fermetureTrans(G):
    ft = G.copy()
    for i in range(len(ft)):
        for j in range(len(ft)):
            if ft[j][i]:
                for k in range(len(ft)):
                    if ft[i][k]:
                        ft[j][k] += 1
    return ft




#test

L = listeAdjacence(G)
for i in range(len(G)):
     print("Degree(", i, ") = ", degreeSommet(G, i))
     print("Successeur de ", i, ": ", sommetsAdj(L, i))
     print("Isole ou non", estIsole(G, i))


print("Graph eulerienne ou non! ", chaineEulerienne(G))

print("Liste d'adjacence: ", listeAdjacence(G))

print("Graphe complet ou non: ", estComplet(L))

print("PArtie est chaine: \n")

for i in range(len(G)):
     for j in range(len(G)):
          print("{", i, ",", j, "} est chaine ou non! : ", estChaine(G, i, j))
