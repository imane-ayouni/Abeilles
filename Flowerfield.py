import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from random import sample
import math

flowerField = pd.read_excel(r'C:\Users\imane\OneDrive\Desktop\Abeilles\flowers.xlsx')
x = list(flowerField['x'])
y = list(flowerField['y'])


flowerPositions = {x[i]: y[i] for i in range(len(x))}
fpos = []
for key in flowerPositions:
    position = [key, flowerPositions[key]]
    fpos.append(position)
print(fpos)

# Obtenir le numéro et position de chaque fleure
flower_list = {}
count = 1
for i in range(0, len(fpos)):
    pos = fpos[i]
    flower = {str(count): pos}
    count += 1
    flower_list.update(flower)
flower_list.update({"hive": [500, 500]})
print(flower_list)
print(len(flower_list))

hive = {500: 500}




def vis():
    #graph = nx.Graph()
    #graph.add_nodes_from(flower_list.keys())
    plt.scatter(flowerPositions.keys(),flowerPositions.values(),marker="*",edgecolors="red",c="orange")




    plt.scatter(hive.keys(), hive.values(), s=100, edgecolors="yellow", c="orange")
    # plt.title("Flower Flied, with * positions of flowers")
    plt.show()


grap = vis()

# Obtenir les chemins aléatoires choisis par chaque abeille

n_population = 101
path = []
flower_list.pop("hive")
print(len(flower_list))
for i in range(n_population-1):
    plist = sample(list(flower_list.values()), len(flower_list.values()))
    path.append(plist)


# Obtenir un dict qui contient le chemin parcourus par chaque abeille

path_dict = {}
for bee in range(n_population-1):
    pa = {str(bee+1): path[bee]}
    path_dict.update(pa)
for u in path_dict:
    print(u,path_dict[u],"\n")

distances = []
def getDistance():

    for bee in range(n_population-1):

        p = path[bee]
        exit_distance = math.sqrt((p[0][0]-500)**2 +(p[0][1] - 500)**2)
        dis = []
        for fl in range(len(p)-1):
            distance = math.sqrt((p[fl+1][0]-p[fl][0])**2 + (p[fl+1][1] - p[fl][1])**2)
            dis.append(distance)
        in_nodes_distance = sum(dis)
        return_distance = math.sqrt((500 - p[49][0])**2 + (500 - p[49][1])**2)
        total_distance = exit_distance + in_nodes_distance + return_distance
        distances.append(total_distance)

getDistance()
print(len(distances))
print(distances)












