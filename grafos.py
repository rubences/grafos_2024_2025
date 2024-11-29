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
bfs_recorrido = list(nx.bfs_edges(G, source="Ávila"))
bfs_nodos = ["Ávila"] + [v for u, v in bfs_recorrido]
print(bfs_nodos)
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
bfs_recorrido = list(nx.bfs_edges(G, source="Ávila"))
bfs_distancia_total = 0
for u, v in bfs_recorrido:
    distancia = G[u][v]['weight']
    bfs_distancia_total += distancia
    print(f"De {u} a {v}: {distancia} km")
print(f"Distancia total en BFS: {bfs_distancia_total} km")
bfs_nodos = ["Ávila"] + [v for u, v in bfs_recorrido]
print(bfs_nodos)
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

# Dijkstra: camino mínimo de un vértice al resto de los vértices del grafo desde Ávila hasta Zamora
print("Dijkstra: Camino mínimo desde Ávila hasta Zamora")
dijkstra_path = nx.dijkstra_path(G, source="Ávila", target="Zamora", weight='weight')
dijkstra_distancia = nx.dijkstra_path_length(G, source="Ávila", target="Zamora", weight='weight')
print(f"Camino: {dijkstra_path}")
print(f"Distancia total: {dijkstra_distancia} km")

# Crear un subgrafo con el camino Dijkstra
subgrafo_dijkstra = G.subgraph(dijkstra_path)

# Dibujar el subgrafo Dijkstra
pos_dijkstra = nx.spring_layout(subgrafo_dijkstra)
nx.draw(subgrafo_dijkstra, pos_dijkstra, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray")
labels_dijkstra = nx.get_edge_attributes(subgrafo_dijkstra, 'weight')
nx.draw_networkx_edge_labels(subgrafo_dijkstra, pos_dijkstra, edge_labels=labels_dijkstra)

plt.title("Camino mínimo (Dijkstra) desde Ávila hasta Zamora")
plt.show()

# Floyd-Warshall: camino mínimo entre dos nodos cualesquiera de la red (Zamora a Valladolid)
print("Floyd-Warshall: Camino mínimo entre Zamora y Valladolid")
floyd_distancias = dict(nx.floyd_warshall(G, weight='weight'))

# Mostrar las distancias calculadas por Floyd-Warshall
print("Distancias calculadas por Floyd-Warshall:")
for origen, destinos in floyd_distancias.items():
    for destino, distancia in destinos.items():
        print(f"De {origen} a {destino}: {distancia} km")

# Reconstruir el camino mínimo entre Zamora y Valladolid
floyd_path = nx.reconstruct_path("Zamora", "Valladolid", floyd_distancias)
floyd_distancia = floyd_distancias["Zamora"]["Valladolid"]
print(f"Camino: {floyd_path}")
print(f"Distancia total: {floyd_distancia} km")

# Crear un subgrafo con el camino Floyd-Warshall
subgrafo_floyd = G.subgraph(floyd_path)

# Dibujar el subgrafo Floyd-Warshall paso a paso
print("Visualización paso a paso del camino mínimo (Floyd-Warshall) entre Zamora y Valladolid")
for i in range(len(floyd_path) - 1):
    subgrafo_parcial = G.subgraph(floyd_path[:i + 2])
    pos_floyd = nx.spring_layout(subgrafo_parcial)
    nx.draw(subgrafo_parcial, pos_floyd, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray")
    labels_floyd = nx.get_edge_attributes(subgrafo_parcial, 'weight')
    nx.draw_networkx_edge_labels(subgrafo_parcial, pos_floyd, edge_labels=labels_floyd)
    plt.title(f"Paso {i + 1}: Camino mínimo (Floyd-Warshall) entre Zamora y Valladolid")
    plt.show()

