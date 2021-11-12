import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from random import sample,choice
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

flower_list.pop("hive")


def vis():
    plt.scatter(flowerPositions.keys(), flowerPositions.values(), marker="*", edgecolors="red", c="orange")
    plt.scatter(hive.keys(), hive.values(), s=100, edgecolors="yellow", c="orange")
    plt.title("Flower Flied, with * positions of flowers")
    plt.show()


grap = vis()

# Obtenir les chemins aléatoires choisis par chaque abeille

n_population = 101


def selection(population,scores):
    selected = []
    average = sum(scores)/len(scores)
    for i in range(len(scores)):
        if scores[i] < average:
            selected.append(population[i])
    parent_2 = choice(selected)
    return parent_2


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
generations = 20


Best = []

def reproduction( genes, generations, n_population, p_crossover, r_mutation):

    population = []
    for b in range(n_population):
        bts = []
        for i in range(genes):
            bitstring = sample(range(2), 1)
            bts.extend(bitstring)

        population.append(bts)
    dic_population = {}
    for i in range(n_population):
        allocate = {str(i+1):population[i]}
        dic_population.update(allocate)



    print("Initial population of ",len(population))
    print("Population : ")
    for m in dic_population:
        print(m,dic_population[m])

    queen = population[0]
    population.remove(queen)
    print("-----------------------")
    print("Queen doesn't forage, she is the common parent. Number of bees in the race: ", len(population))

    best_of = []

    for generation in range(generations):

        path = []
        for i in range(len(population)):
            plist = sample(list(flower_list.values()), len(flower_list.values()))
            path.append(plist)
        print(len(path))
        print("paths: ",path)

        def visPath():
            bee = int(input("choose the bee: "))
            path_dict = {}
            beePath = path[bee-1]

            for i in range(len(beePath)):

                if beePath[i] in flower_list.values():
                    keys = list(flower_list.keys())
                    values = list(flower_list.values())
                    position = values.index(beePath[i])
                    f = {str(keys[position]):values[position]}
                    path_dict.update(f)
            print("Path chosen by this bee: ", path_dict)



            g = nx.Graph()

            tuple_list = []
            k_list = list(path_dict.keys())
            for i in range(0,len(k_list)-1,2):
                tup = (k_list[i],k_list[i+1])
                tuple_list.append(tup)
            g.add_edges_from(tuple_list)
            fixed_positions = {}
            for po in path_dict:
                h = {int(po):tuple(path_dict[po])}
                fixed_positions.update(h)
            fixed_nodes = fixed_positions.keys()




            pos = nx.spring_layout(g,pos = fixed_positions)

            nx.draw_networkx(g,pos)
            plt.show()




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


        scores = [fitness[bee] for bee in range(n_population -1)]



        best_evaluation = min(scores)
        best_bee = scores.index(best_evaluation)
        best = population[best_bee]
        print("-----------------------")
        print("Best record: ")
        print("Generation: ",generation+1," Bee: ",best_bee+1,", distance: ",best_evaluation)

        best_of.append(best_evaluation)


        selected = [selection(population, scores) for _ in range(n_population-1)]
        print("selected parents: ",selected)
        print("Each of the selected parent will make one child with the queen ")

        children = list()
        for i in range(0, n_population-1):
            parent_2 = selected[i]

            for child in crossover(queen, parent_2, p_crossover):
                mutation(child, r_mutation)
                children.append(child)


        population = children
        print("Next generation has: ",len(population)+1," members, whose genes are: ",population)
        visPath()

    Best.extend(best_of)

play = reproduction(genes,generations,n_population,p_crossover,r_mutation)




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


