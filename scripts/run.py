from copy import deepcopy

from tools.linked_list import Graph
from tools.linked_list import Node

n = 5 #number of vertices

graph = Graph(n, directed=False) #create an undirected graph

#insert edges
graph.insert_edge((0, 3), 0, 3) 
graph.insert_edge((1, 3), 1, 3) 
graph.insert_edge((1, 2), 1, 2) 
graph.insert_edge((2, 4), 2, 4) 
graph.insert_edge((3, 4), 3, 4) 

#display graph
graph.display_graph()

# MUTYH: Chr1, 45329242..45340440, complement
#  TOE1: Chr1, 45340170..45343973
# TESK2: Chr1, 45343883..45491163, complement
#  HPDL: Chr1, 45326895..45328710
mutyh = Node(data=("mutyh", 45329242, 45340440))
toe1 = Node(data=("toe1", 45340170, 45343973))
tesk2 = Node(data=("tesk2", 45343883, 45491163))
hpdl = Node(data=("hpdl", 45326895, 45328710))

def overlaps(node1, node2):
    return False if node1.data[1] > node2.data[2] or node1.data[2] < node2.data[1] else True

genes = [mutyh, toe1, tesk2, hpdl]
graph = Graph(len(genes), directed=False) #create an undirected graph

for idx1, current_gene in enumerate(genes):
    if idx1 == len(genes)-1:
        break

    next_gene = genes[idx1 + 1]
    if overlaps(current_gene, next_gene) and current_gene.data != next_gene.data:
        graph.insert_edge((current_gene, next_gene), idx1, idx1 + 1)


print("Graph:")
graph.display_graph(names=[gene.data[0] for gene in genes])
print("================================================================")
print("genomic addresses:")
print([gene for gene in genes])
