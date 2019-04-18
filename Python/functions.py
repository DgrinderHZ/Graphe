def orderGraphe(G):
    """ Cette fonction retourne l'ordre de graphe G"""
    return len(G)

def degreeSommet(G, s):
    """Rerourne le degree de sommet s"""
    res = 0
    if grapheOriente(G):
        res = sum(G[s])
        for i in range(len(G)):
            res += G[i][s]
    else:
        for i in range(len(G)):
            if G[i][s]:
                res += 1
        for i in range(len(G)):
            if G[s][i]:
                res += 1
    return res

def grapheOriente(G):
    for i in range(len(G)):
        for j in range(i, len(G)):
            if G[i][j] != G[j][i]:
                return True
    return False



def estSommetAdjacence(G, x, y):
    if G[x][y] or G[y][x]:
        return True
    return False

def estIsole(G, s):
    for i in range(len(G)):
        if G[s][i]:
            return False
    for i in range(len(G)):
        if G[i][s]:
            return False
    return False



def listeAdjacence(G):
    listPrinc = []
    for i in range(len(G)):
        ilist = []
        for j in range(len(G)):
            if G[i][j]:
                ilist.append(j);
        listPrinc.append(ilist)
    return listPrinc

def listArc(G):
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j]:
                print(i, " ---> ", j)
        
def fermetureTrans(G):
    ft = G.copy()
    for i in range(len(ft)):
        for j in range(len(ft)):
            if ft[j][i]:
                for k in range(len(ft)):
                    if(ft[i][k]):
                        ft[j][k] += 1
    return ft

def estChaine(G, s, e):
    FT = fermetureTrans(G)
    if FT[s][e]:
        return True
    return False

def listeAdjacenceRec(G, listPrinc):
    i = len(listPrinc)
    if i < len(G):
        ilist = []
        for j in range(len(G)):
            if G[i][j]:
                ilist.append(j);
        listPrinc.append(ilist)
        listeAdjacenceRec(G, listPrinc)

def successeur(G, s):
    ilist = []
    for j in range(len(G)):
        if G[s][j]:
            ilist.append(j);
    return ilist

def parcoursEnLargeur(G, s):
    #enfiler les successeur de s
    myfile = []
    marque = [0] * len(G)
    myfile.extend(successeur(G, s))
    #marquer s
    marque[s]=1
    print(s)
    while len(myfile):
        s = myfile.pop()
        if marque[s] == 0:
            myfile.extend(successeur(G, s))
            #marquer s
            marque[s]=1
            print(s)

            
            
 def existeVoisinNonVisite(G, marque, s):
    ilist = successeur(G, s)
    for item in ilist:
        if marque[item] == 0:
            return item
    return -1


def parcoursEnProfondeur(G, s):
    #enfiler les successeur de s
    mypile = []
    marque = [0] * len(G)
    mypile.extend(successeur(G, s))
    #marquer s
    marque[s] = 1
    print(s)
    while len(mypile):
        s = existeVoisinNonVisite(G, marque, s)
        marque[s] = 1
        if s != -1:
            mypile.append(s)
            print(s)
        else:
            mypile.remove(mypile[-1])
        
