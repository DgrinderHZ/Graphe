
import math

inf = math.inf

def sommetAvecdistMinimal(dist, sommets):
    pos = 0
    for i in range(len(sommets)):
        if dist[i] > dist[pos]:
            pos = i
    return sommets[pos]

def dijkstra(Glist, s0):
    n = len(Glist)
    dist = [inf] * n
    pere = [-1 for i in range(n)] #le prédecesseur de chaque sommet initialisé à -1
    chemin = []
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

G =[[0,10,5,inf,inf],
    [10,0,4,3,inf],
    [5,4,0,1,inf],
    [inf,3,1,0,6],
    [inf,inf,inf,6,0]
]

dist, pere = dijkstra(G, 1)

for item, item1 in zip(dist, pere):
    print(item , ' pere ', item1)



