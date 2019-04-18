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
