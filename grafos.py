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