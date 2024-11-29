import networkx as nx

import matplotlib.pyplot as plt

# Definimos las capitales de provincia de Castilla y León y las distancias entre ellas
capitales = [
    "Ávila", "Burgos", "León", "Palencia", "Salamanca", 
    "Segovia", "Soria", "Valladolid", "Zamora"
]

distancias = {
    ("Ávila", "Salamanca"): 103,
    ("Ávila", "Segovia"): 67,
    ("Ávila", "Valladolid"): 130,
    ("Burgos", "León"): 179,
    ("Burgos", "Palencia"): 86,
    ("Burgos", "Soria"): 132,
    ("Burgos", "Valladolid"): 121,
    ("León", "Palencia"): 124,
    ("León", "Zamora"): 137,
    ("Palencia", "Valladolid"): 47,
    ("Salamanca", "Segovia"): 161,
    ("Salamanca", "Zamora"): 65,
    ("Segovia", "Soria"): 146,
    ("Segovia", "Valladolid"): 117,
    ("Soria", "Valladolid"): 210,
    ("Valladolid", "Zamora"): 92
}

# Crear el grafo
G = nx.Graph()

# Añadir nodos
for capital in capitales:
    G.add_node(capital)

# Añadir aristas con las distancias
for (origen, destino), distancia in distancias.items():
    G.add_edge(origen, destino, weight=distancia)

# Dibujar el grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray")
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title("Grafo de distancias entre capitales de provincia de Castilla y León")
plt.show()

#quiero saber la distancia minima entre Avila y Zamora
# Calcular la distancia mínima entre Ávila y Zamora pasando por Salamanca, Segovia y Valladolid
ruta = ["Ávila", "Salamanca", "Segovia", "Valladolid", "Zamora"]
distancia_total = 0
for i in range(len(ruta) - 1):
    distancia_total += nx.shortest_path_length(G, source=ruta[i], target=ruta[i+1], weight='weight')

print(f"La distancia mínima entre Ávila y Zamora pasando por Salamanca, Segovia y Valladolid es {distancia_total} km")
print(f"Ruta: {ruta}")

# Crear un subgrafo con la ruta
subgrafo = G.subgraph(ruta)

# Dibujar el subgrafo
pos = nx.spring_layout(subgrafo)
nx.draw(subgrafo, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray")
labels = nx.get_edge_attributes(subgrafo, 'weight')
nx.draw_networkx_edge_labels(subgrafo, pos, edge_labels=labels)

plt.title("Ruta mínima entre Ávila y Zamora pasando por Salamanca, Segovia y Valladolid")
plt.show()
distancia_minima = nx.shortest_path_length(G, source="Ávila", target="Zamora", weight='weight')
print(f"La distancia mínima entre Ávila y Zamora es {distancia_minima} km")


#Recorrer un grafo consiste en visitar todos los vértices  alcanzables a partir de uno dado. generamelo desde Avila
# Recorrido en profundidad (DFS) desde Ávila
print("Recorrido en profundidad (DFS) desde Ávila:")
dfs_recorrido = list(nx.dfs_preorder_nodes(G, source="Ávila"))
print(dfs_recorrido)

# Recorrido en anchura (BFS) desde Ávila
print("Recorrido en anchura (BFS) desde Ávila:")
bfs_recorrido = list(nx.bfs_tree(G, source="Ávila"))
print(bfs_recorrido)
# Recorrido en profundidad (DFS) desde Ávila con paso a paso y suma de aristas
print("Recorrido en profundidad (DFS) desde Ávila con paso a paso y suma de aristas:")
dfs_recorrido = list(nx.dfs_preorder_nodes(G, source="Ávila"))
dfs_distancia_total = 0
for i in range(len(dfs_recorrido) - 1):
    distancia = G[dfs_recorrido[i]][dfs_recorrido[i + 1]]['weight']
    dfs_distancia_total += distancia
    print(f"De {dfs_recorrido[i]} a {dfs_recorrido[i + 1]}: {distancia} km")
print(f"Distancia total en DFS: {dfs_distancia_total} km")
print(dfs_recorrido)

# Crear un subgrafo con el recorrido DFS
subgrafo_dfs = G.subgraph(dfs_recorrido)

# Dibujar el subgrafo DFS
pos_dfs = nx.spring_layout(subgrafo_dfs)
nx.draw(subgrafo_dfs, pos_dfs, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray")
labels_dfs = nx.get_edge_attributes(subgrafo_dfs, 'weight')
nx.draw_networkx_edge_labels(subgrafo_dfs, pos_dfs, edge_labels=labels_dfs)

plt.title("Recorrido en profundidad (DFS) desde Ávila")
plt.show()

# Recorrido en anchura (BFS) desde Ávila con paso a paso y suma de aristas
print("Recorrido en anchura (BFS) desde Ávila con paso a paso y suma de aristas:")
bfs_recorrido = list(nx.bfs_tree(G, source="Ávila"))
bfs_distancia_total = 0
for i in range(len(bfs_recorrido) - 1):
    distancia = G[bfs_recorrido[i]][bfs_recorrido[i + 1]]['weight']
    bfs_distancia_total += distancia
    print(f"De {bfs_recorrido[i]} a {bfs_recorrido[i + 1]}: {distancia} km")
print(f"Distancia total en BFS: {bfs_distancia_total} km")
print(bfs_recorrido)

# Crear un subgrafo con el recorrido BFS
subgrafo_bfs = G.subgraph(bfs_recorrido)

# Dibujar el subgrafo BFS
pos_bfs = nx.spring_layout(subgrafo_bfs)
nx.draw(subgrafo_bfs, pos_bfs, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray")
labels_bfs = nx.get_edge_attributes(subgrafo_bfs, 'weight')
nx.draw_networkx_edge_labels(subgrafo_bfs, pos_bfs, edge_labels=labels_bfs)

plt.title("Recorrido en anchura (BFS) desde Ávila")
plt.show()



