import random
import networkx as nx

class Grafo:
    def __init__(self):
        self.vertices = {}
        self.aristas = []

    def agregar_vertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = []

    def agregar_arista(self, origen, destino, etiqueta):
        if origen in self.vertices and destino in self.vertices:
            self.vertices[origen].append((destino, etiqueta))
            self.aristas.append((origen, destino, etiqueta))

    def eliminar_vertices_desconectados(self):
        vertices_conectados = set()
        for origen, destino, _ in self.aristas:
            vertices_conectados.add(origen)
            vertices_conectados.add(destino)
        self.vertices = {v: adj for v, adj in self.vertices.items() if v in vertices_conectados}

    def nodo_mayor_aristas_salen(self):
        max_aristas = 0
        nodos = []
        for v, adj in self.vertices.items():
            if len(adj) > max_aristas:
                max_aristas = len(adj)
                nodos = [v]
            elif len(adj) == max_aristas:
                nodos.append(v)
        return nodos

    def nodo_mayor_aristas_llegan(self):
        conteo_aristas = {v: 0 for v in self.vertices}
        for _, destino, _ in self.aristas:
            conteo_aristas[destino] += 1
        max_aristas = max(conteo_aristas.values())
        return [v for v, count in conteo_aristas.items() if count == max_aristas]

    def vertices_no_accesibles(self):
        accesibles = set()
        for origen, adj in self.vertices.items():
            for destino, _ in adj:
                accesibles.add(destino)
        return [v for v in self.vertices if v not in accesibles]

    def contar_vertices(self):
        return len(self.vertices)

    def ciclos_directos(self):
        return [v for v, adj in self.vertices.items() if any(destino == v for destino, _ in adj)]

    def arista_mas_larga(self):
        max_etiqueta = max(self.aristas, key=lambda x: x[2])[2]
        return [(origen, destino, etiqueta) for origen, destino, etiqueta in self.aristas if etiqueta == max_etiqueta]

# Generar grafo con 15 vértices aleatorios no repetidos
grafo = Grafo()
vertices = random.sample(range(1, 101), 15)
for v in vertices:
    grafo.agregar_vertice(v)

# Agregar 30 aristas no repetidas con etiquetas aleatorias
aristas_agregadas = set()
while len(aristas_agregadas) < 30:
    origen, destino = random.sample(vertices, 2)
    etiqueta = random.randint(1, 100)
    if (origen, destino) not in aristas_agregadas:
        grafo.agregar_arista(origen, destino, etiqueta)
        aristas_agregadas.add((origen, destino))

# Resolver actividades
grafo.eliminar_vertices_desconectados()
print("Nodo(s) con mayor cantidad de aristas que salen de él:", grafo.nodo_mayor_aristas_salen())
print("Nodo(s) con mayor cantidad de aristas que llegan a él:", grafo.nodo_mayor_aristas_llegan())
print("Vértices desde los cuales no se puede acceder a otro vértice:", grafo.vertices_no_accesibles())
print("Cantidad de vértices en el grafo:", grafo.contar_vertices())
print("Vértices con un ciclo directo:", grafo.ciclos_directos())
print("Arista(s) más larga(s):", grafo.arista_mas_larga())
import matplotlib.pyplot as plt

def dibujar_grafo(grafo):
    G = nx.DiGraph()
    for v in grafo.vertices:
        G.add_node(v)
    for origen, destino, etiqueta in grafo.aristas:
        G.add_edge(origen, destino, weight=etiqueta)

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=10, font_weight='bold', arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

dibujar_grafo(grafo)