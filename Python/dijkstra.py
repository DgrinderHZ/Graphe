
import math

inf = math.inf

def sommetAvecdistMinimal(dist, sommets):
    """ retur le sommet avec la distance minimale """
    pos = sommets[0]
    for i in sommets:
        if dist[i] < dist[pos]:
            pos = i
    return pos

def dijkstra(Glist, s0):
    n = len(Glist)
    dist = [inf] * n
    pere = [-1 for i in range(n)] #le prédecesseur de chaque sommet initialisé à -1
    marque = [] # visited
    nonMarquer = [s for s in range(n)] # not visited
    dist[s0] = 0
    while(len(nonMarquer)):
        sadm = sommetAvecdistMinimal(dist, nonMarquer)
        marque.append(sadm)
        nonMarquer.remove(sadm)
        for item in nonMarquer:
            if dist[sadm] + Glist[sadm][item] < dist[item]:
                dist[item] = dist[sadm] + Glist[sadm][item]
                pere[item] = sadm
    
    return dist, pere






