import networkx as nx
from networkx.algorithms import tree

#Montando o grafo
G = nx.Graph()
G.add_edge("A", "B", weight=9)
G.add_edge("A", "C", weight=3)
G.add_edge("A", "E", weight=8)
G.add_edge("A", "F", weight=3)
G.add_edge("A", "G", weight=4)
G.add_edge("B", "C", weight=10)
G.add_edge("B", "F", weight=6)
G.add_edge("C", "D", weight=6)
G.add_edge("C", "F", weight=4)
G.add_edge("C", "G", weight=5)
G.add_edge("C", "H", weight=7)
G.add_edge("D", "E", weight=6)
G.add_edge("D", "H", weight=3)
G.add_edge("E", "H", weight=5)

pos=nx.planar_layout(G) # definindo a váriavel 'pos' como um layout circular 
s = nx.get_edge_attributes(G,'weight') # pegando os pesos das arestas
nx.draw_networkx(G,pos) # desenhando o grafo 
nx.draw_networkx_edge_labels(G,pos,edge_labels=s) # desenhando os pesos das arestas
print("Grafo resultante da modelagem do problema.") 

T = nx.minimum_spanning_tree(G) # gerando a árvore geradora miníma 'MST'

pos=nx.planar_layout(T) # definindo a váriavel 'pos' como um layout planar
s = nx.get_edge_attributes(T,'weight') # pegando os pesos das arestas
nx.draw_networkx(T,pos)  # desenhando o grafo 
nx.draw_networkx_edge_labels(T,pos,edge_labels=s)  # desenhando os pesos das arestas
print(" O menor risco  para que uma mensagem seja repassada para todos os conspiradores é :",T.size(weight="weight"))
