import random

import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from random import sample
import math

# Importer le fichier excel, et définir x et y

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
    plt.scatter(flowerPositions.keys(), flowerPositions.values(), marker="*", edgecolors="red", c="orange")
    plt.scatter(hive.keys(), hive.values(), s=100, edgecolors="yellow", c="orange")
    plt.title("Flower Flied, with * positions of flowers")
    plt.show()


grap = vis()

# Obtenir les chemins aléatoires choisis par chaque abeille

n_population = 101
path = []
flower_list.pop("hive")
print(len(flower_list))
for i in range(n_population - 1):
    plist = sample(list(flower_list.values()), len(flower_list.values()))
    path.append(plist)

# Obtenir un dict qui contient le chemin parcourus par chaque abeille

path_dict = {}
for bee in range(n_population - 1):
    pa = {str(bee + 1): path[bee]}
    path_dict.update(pa)
# for u in path_dict:
# print(u,path_dict[u],"\n")

# Calculer les distances parcourus par chaque abeille depuis le point de départ (hive) passant
# par toutes les fleures et revenant en fin au hive

distances = []


def getDistance():
    for bee in range(n_population - 1):

        p = path[bee]
        exit_distance = math.sqrt((p[0][0] - 500) ** 2 + (p[0][1] - 500) ** 2)
        dis = []
        for fl in range(len(p) - 1):
            distance = math.sqrt((p[fl + 1][0] - p[fl][0]) ** 2 + (p[fl + 1][1] - p[fl][1]) ** 2)
            dis.append(distance)
        in_nodes_distance = sum(dis)
        return_distance = math.sqrt((500 - p[49][0]) ** 2 + (500 - p[49][1]) ** 2)
        total_distance = exit_distance + in_nodes_distance + return_distance
        distances.append(total_distance)


getDistance()
print(len(distances))
print(distances)


#def fitness(bee):
 #   f = distances[bee]
  #  return f
scores = [distances[b] for b in range(n_population -1)]

print("dskdsdskds", scores)

def selection(population, scores, k=3):
    first_selection = random.randint(0,len(population)-1)
    second_selection = sample(range(0,len(population)-1),k-1)
    for selec in second_selection:
        if scores[selec] < scores[first_selection]:
            first_selection = selec
    return population[first_selection]



p_crossover = 1.0

def crossover(queen, parent_2, p_crossover):
    child =  parent_2.copy()
    if random.random() < p_crossover:
        point = 4
        child = queen[:point] + parent_2[point:]

    return [child]


r_mutation = 2.2 * 10 ** (-9)


def mutation(bitstring, r_mutation):
    for i in range(len(bitstring)):
        if random.random() < r_mutation:
            bitstring[i] = 1 - bitstring[i]

genes = 8
generations = 10



def reproduction(fitness, genes, generations, n_population, p_crossover, r_mutation):
    population = []
    for b in range(n_population):
        bts = []
        for i in range(genes):
            bitstring = sample(range(2), 1)
            bts.extend(bitstring)

        population.append(bts)

    print("Initial population of ",len(population),"\n","Members genes: ",population)
    queen = population[0]
    best, best_evaluation = 0, fitness[0]
    population.remove(queen)
    print("Queen doesn't forage, she is the common parent. Number of bees in the race: ", len(population))

    for generation in range(generations):

        scores = [fitness[bee] for bee in range(n_population -1)]
        print("scores " ,scores)
        best_evaluation = min(scores)
        best_bee = scores.index(best_evaluation)
        best = population[best_bee]
        print("-----------------------")
        print("Best record: ")
        print("Generation: ",generation," Bee: ", best," distance: ",best_evaluation)




        selected = [selection(population, scores) for _ in range(n_population)]
        print("Selected parents: ",selected)
        children = list()
        for i in range(0, n_population-1):
            parent_2 = selected[i]

            for child in crossover(queen, parent_2, p_crossover):
                mutation(child, r_mutation)
                children.append(child)


        population = children
        print("Next generation: ",population)
    print([best, best_evaluation])

reproduction(distances,genes,generations,n_population,p_crossover,r_mutation)


