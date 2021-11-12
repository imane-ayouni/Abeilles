import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from random import sample,choice
import math

# Importer le fichier excel, et définir x et y

flowerField = pd.read_excel(r'C:\Users\imane\OneDrive\Desktop\Abeilles\flowers.xlsx')
x = list(flowerField['x'])
y = list(flowerField['y'])


# Obtenir une liste qui contient les positions des fleurs

flowerPositions = {x[i]: y[i] for i in range(len(x))}
fpos = []
for key in flowerPositions:
    position = [key, flowerPositions[key]]
    fpos.append(position)


# Obtenir le numéro et position de chaque fleure

flower_list = {}
count = 0
for i in range(0, len(fpos)):
    pos = fpos[i]
    flower = {str(count): pos}
    count += 1
    flower_list.update(flower)
flower_list.update({"hive": [500, 500]})
print(flower_list)


hive = {500: 500}

flower_list.pop("hive")

# Visualiser le champs

def vis():
    plt.scatter(flowerPositions.keys(), flowerPositions.values(), marker="*", edgecolors="red", c="orange")
    plt.scatter(hive.keys(), hive.values(), s=100, edgecolors="yellow", c="orange")
    plt.title("Flower Field, with * positions of flowers")
    plt.show()


grap = vis()

# Obtenir les chemins aléatoires choisis par chaque abeille

n_population = 101

# Définir la fonction qui séléctionne les parents en se basant sur leurs distances parcourus

def selection(scores):
    selected = []
    average = sum(scores)/len(scores)
    for i in range(0,len(scores),2):
        if scores[i] < average:
            selected.append(i)
    parent_1 = choice(selected)
    parent_2 = choice(selected)
    return [parent_1,parent_2]




p_crossover = 1.0

# Définir la fonction de croisement qui réorganiser les genes des parents pour les obtenir les enfants

def crossover(parent_1, parent_2, p_crossover):
    child_1 =  parent_1.copy()
    child_2 = parent_2.copy()
    fl_numbers_list = list(flower_list.keys())
    value_list = list(flower_list.values())


    if random.random() < p_crossover:
        point = 30
        child_1 = parent_1[:point] + parent_2[point:]
        child_2 = parent_2[:point] + parent_1[point:]


        passage_flowers1 = []
        for g in child_1:
            ind = fpos.index(g)
            passage_flowers1.append(str(ind))

        passage_flowers2 = []
        for g in child_2:
            ind = fpos.index(g)
            passage_flowers2.append(str(ind))


        child_1 = list(dict.fromkeys(passage_flowers1))


        child_2 = list(dict.fromkeys(passage_flowers2))

        difference1 = [item for item in fl_numbers_list if item not in child_1]
        difference2 = [item for item in fl_numbers_list if item not in child_2]

        child_1.extend(difference1)

        child_2.extend(difference2)

        final_list_1 = []
        for i in child_1:
            j = int(i)
            index = value_list[j]
            final_list_1.append(index)
        child_1 = final_list_1
        final_list_2 = []
        for i in child_2:
            j = int(i)
            index = value_list[j]
            final_list_2.append(index)
        child_2 = final_list_2
    return [child_1,child_2]



r_mutation = 2.2 * 10 ** (-9)


# Définir la fonction de mutation qui changera un des genes

def mutation(bitstring, r_mutation):
    for i in range(len(bitstring)):
        if random.random() < r_mutation:
            bitstring[i] = bitstring[i+1]


generations = 40


Best = []

# Définir la classe reproduction qui produit la population initiale,
# défini le chemin suivi par chaque abeille, calcule les distances
# et produit les générations suivantes
# Cette fonction va garder les meilleurs score de chauque génération et va ploter l'évolution des resultat avec les génarations

def reproduction(generations, n_population, p_crossover, r_mutation):

    print("Initial population of ",n_population)
    print("Queen doesn't forage for food, her fitness is not included")

    path = []
    for i in range(n_population - 1):
        plist = sample(list(flower_list.values()), len(flower_list.values()))
        path.append(plist)

    print("paths: ", path)

    best_of = []


    for generation in range(generations):


        fitness = []
        for p in range(len(path)):
            dis = path[p]
            exit_distance = math.sqrt((dis[0][0] - 500) ** 2 + (dis[0][1] - 500) ** 2)
            dist = []
            for fl in range(len(dis) - 1):
                distance = math.sqrt((dis[fl + 1][0] - dis[fl][0]) ** 2 + (dis[fl + 1][1] - dis[fl][1]) ** 2)
                dist.append(distance)
            in_nodes_distance = sum(dist)
            return_distance = math.sqrt((500 - dis[49][0]) ** 2 + (500 - dis[49][1]) ** 2)
            total_distance = exit_distance + in_nodes_distance + return_distance
            fitness.append(total_distance)
        print(len(fitness))
        print("fitness: ",fitness)


        scores = [fitness[bee] for bee in range(n_population-1)]



        best_evaluation = min(scores)
        best_bee = scores.index(best_evaluation)

        print("-----------------------")
        print("Best record: ")
        print("Generation: ",generation+1," Bee: ",best_bee+1,", distance: ",best_evaluation)

        best_of.append(best_evaluation)


        selected = [selection(scores) for _ in range(n_population-1)]



        children = list()
        for i in range(0, n_population+-1,2):
            parent_1 = selected[i][0]
            parent_2 = selected[i][1]

            for child in crossover(path[parent_1-1], path[parent_2-1], p_crossover):
                mutation(child, r_mutation)
                children.append(child)





        path = children

    Best.extend(best_of)

play = reproduction(generations,n_population,p_crossover,r_mutation)




def visImprovement():
    height = [s for s in Best]
    l = []

    for g in range(generations):
        n = str(g+1)
        l.append(n)
    bars = tuple(l)

    y_pos = np.arange(len(bars))
    plt.bar(y_pos,height)
    plt.xticks(y_pos,bars)
    plt.show()



visImprovement()


