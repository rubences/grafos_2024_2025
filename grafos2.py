#Grafos en Python: módulo networkx
#instalación: %pip install networkx
#documentación: https://networkx.github.io/documentation/stable/tutorial.html
# Instalación del módulo:


import networkx as nx
import matplotlib.pyplot as plt

# Creación de un grafo no dirigido:
G = nx.Graph()

# Añadir nodos y aristas:
G.add_node("a")
G.add_node("b")
G.add_edge("a", "b")

# Añadir atributos
G.nodes["a"]["nombre"] = "Pepe"
G.nodes["b"]["nombre"] = "Ana"
G.edges["a", "b"]["fecha"] = "25-05-2003"

# Imprimir conjunto de nodos y aristas:
print("Nodos:", G.nodes(data=True))
print("Aristas:", G.edges(data=True))

# Dibujar el grafo usando matplotlib
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=20, font_color='black')

# Añadir etiquetas de atributos
node_labels = nx.get_node_attributes(G, 'nombre')
edge_labels = nx.get_edge_attributes(G, 'fecha')
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=15, font_color='red')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=15, font_color='green')

plt.title("Grafo con NetworkX y Matplotlib")
plt.show()

# Guardar grafo
nx.write_graphml(G, "parejas.graphml")

# Cargar grafo
G2 = nx.read_graphml("parejas.graphml")
