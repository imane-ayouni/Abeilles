import random

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

# Calculer les distances parcourus par chaque abeille depuis le point de départ (hive) passant
# par toutes les fleures et revenant en fin au hive

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


def selection(population,scores,sample = 3):
    first_selection = random.randint(len(population))
    for selec in random.randint(0,len(population),sample-1):
        if scores[selec] < scores[first_selection]:
            first_selection = selec
    return population[first_selection]



def crossover(parent_1,parent_2,p_crossover):
    child_1,child_2 = parent_1.copy(), parent_2.copy()
    if random.random() < p_crossover:
        point = random.randint(1,len(parent_1)-2)
        child_1 = parent_1[:point] + parent_2[point:]
        child_2 = parent_2[:point] + parent_1[point:]
    return [child_1,child_2]

r_mutation = 2.2* 10**(-9)

def mutation(bitstring,r_mutation):
    for i in range(len(bitstring)):
        if random.random() > r_mutation:
            bitstring[i] = 1 - bitstring[i]



def reproduction(fitness,genes,generations,n_population,p_crossover,r_mutation):
    population = [random.randint(0,2,genes).tolist() for _ in range(n_population)]
    for generation in range(generations):
        scores = [fitness(bee) for bee in population]
        selected = [selection(population,scores) for _ in range(n_population)]
        children = list()
        for i in range(0,n_population,2):
            parent_1,parent_2 = selected[i],selected[i+1]
            for child in crossover(parent_1,parent_2,p_crossover):
                mutation(child,r_mutation)
                children.append(child)

        population = children

















