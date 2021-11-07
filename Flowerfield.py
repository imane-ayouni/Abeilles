import  pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

flowerField = pd.read_excel(r'C:\Users\imane\OneDrive\Desktop\Abeilles\flowers.xlsx')
x = list(flowerField['x'])
y = list(flowerField['y'])


flowerPositions = {x[i]:y[i] for i in range(len(x))}

for key in flowerPositions:
    position = [key, flowerPositions[key]]
    print(position)


def vis():
    graph = nx.Graph()
    graph.add_nodes_from(flowerPositions)
    plt.scatter(flowerPositions.keys(),flowerPositions.values(),marker="*",edgecolors="red",c="orange")
    plt.title("Flower Flied, with * positions of flowers")
    plt.show()
grap = vis()



# plt.scatter(x,y,marker="*",edgecolors="red",c="orange")

# plt.title("Flower Flied, with * positions of flowers")
# plt.show()
