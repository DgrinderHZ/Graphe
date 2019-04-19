
import math

inf = math.inf

def sommetAvecdistMinimal(dist, sommets):
    pos = sommets[0]
    for i in sommets:
        if dist[i] < dist[pos]:
            pos = i
    return pos

def dijkstra(Glist, s0):
    n = len(Glist)
    dist = [inf] * n
    pere = [-1 for i in range(n)] #le prédecesseur de chaque sommet initialisé à -1
    #chemin = []
    marque = []
    nonMarquer = [s for s in range(n)]
    dist[s0] = 0
    while(len(nonMarquer)):
        sdm = sommetAvecdistMinimal(dist, nonMarquer)
        marque.append(sdm)
        nonMarquer.remove(sdm)
        for item in nonMarquer:
            if dist[sdm] + Glist[sdm][item] < dist[item]:
                dist[item] = dist[sdm] + Glist[sdm][item]
                pere[item] = sdm
    
    return dist, pere






