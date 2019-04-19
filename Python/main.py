from functions import *
from dijkstra import *

G = [[0, 1,0,0,1,0], [0,0,1,1,0,0], [0,0,0,1,0,0], [0,0,0,0,0,0], [0,0,0,0,0,1], [0,0,0,0,0,0]]
print("Largeur")
parcoursEnLargeur(G, 0)
print("\nProfondeur")
parcoursEnProfondeur(G, 0)

G =[[0,10,5,inf,inf],
    [10,0,4,3,inf],
    [5,4,0,1,inf],
    [inf,3,1,0,6],
    [inf,inf,inf,6,0]
]

print("\n Dijkstra :")
dist, pere = dijkstra(G, 0)
i = 0
for item, item1 in zip(dist, pere):
    print("Sommet S(", i, ") : dist ", item, ' pere ', item1)
    i += 1