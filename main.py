import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()
G.add_edges_from([(1,2),(2,3),(3,1),(1,4)]) #define G
fixed_positions = {1:(0,0),2:(-1,2)}#dict with two of the positions set
fixed_nodes = fixed_positions.keys()
pos = nx.spring_layout(G,pos=fixed_positions, fixed = fixed_nodes)
nx.draw_networkx(G,pos)
plt.show()




