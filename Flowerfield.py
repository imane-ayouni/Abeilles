import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from random import sample

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

print(len(path))
path_dict = {}
for fl in range(1,len(flower_list.keys())+1):
    pa = {fl: path[fl]}
    path_dict.update(pa)
for u in path_dict:
    print(u,path_dict[u],"\n")








