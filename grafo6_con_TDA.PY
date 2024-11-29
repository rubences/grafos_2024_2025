import heapq
import networkx as nx

class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = [[] for _ in range(vertices)]
        self.aristas = []

    def agregar_arista(self, u, v, peso):
        self.grafo[u].append((v, peso))
        self.aristas.append((peso, u, v))

    def agregar_arco(self, u, v):
        self.grafo[u].append((v, 0))

    def representacion_arreglo_listas(self):
        return self.grafo

    def representacion_lista_listas(self):
        lista_listas = [[] for _ in range(self.V)]
        for i in range(self.V):
            for (v, peso) in self.grafo[i]:
                lista_listas[i].append(v)
        return lista_listas

    def encontrar_arbol_expansion_minima(self):
        self.aristas.sort()
        padre = list(range(self.V))
        rango = [0] * self.V

        def encontrar(u):
            if padre[u] != u:
                padre[u] = encontrar(padre[u])
            return padre[u]

        def union(u, v):
            raiz_u = encontrar(u)
            raiz_v = encontrar(v)
            if rango[raiz_u] > rango[raiz_v]:
                padre[raiz_v] = raiz_u
            else:
                padre[raiz_u] = raiz_v
                if rango[raiz_u] == rango[raiz_v]:
                    rango[raiz_v] += 1

        arbol_expansion_minima = []
        for peso, u, v in self.aristas:
            if encontrar(u) != encontrar(v):
                union(u, v)
                arbol_expansion_minima.append((u, v, peso))
        return arbol_expansion_minima

    def camino_mas_corto(self, inicio, fin):
        distancias = [float('inf')] * self.V
        distancias[inicio] = 0
        cola_prioridad = [(0, inicio)]
        while cola_prioridad:
            distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
            if nodo_actual == fin:
                return distancia_actual
            for vecino, peso in self.grafo[nodo_actual]:
                distancia = distancia_actual + peso
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    heapq.heappush(cola_prioridad, (distancia, vecino))
        return float('inf')

# Ejemplo de uso
grafo = Grafo(5)
grafo.agregar_arista(0, 1, 10)
grafo.agregar_arista(0, 2, 3)
grafo.agregar_arista(1, 2, 1)
grafo.agregar_arista(1, 3, 2)
grafo.agregar_arista(2, 1, 4)
grafo.agregar_arista(2, 3, 8)
grafo.agregar_arista(2, 4, 2)
grafo.agregar_arista(3, 4, 7)
grafo.agregar_arista(4, 3, 9)

# Agregar arco de E a C (4 a 2)
grafo.agregar_arco(4, 2)

print("Representación como arreglo de listas de adyacencias:")
print(grafo.representacion_arreglo_listas())

print("Representación como lista de listas de adyacencias:")
print(grafo.representacion_lista_listas())

print("Árbol de expansión mínima:")
print(grafo.encontrar_arbol_expansion_minima())

print("Camino más corto de A a D (0 a 3):")
print(grafo.camino_mas_corto(0, 3))
import matplotlib.pyplot as plt

def dibujar_grafo(grafo):
    G = nx.DiGraph()
    for u in range(grafo.V):
        for v, peso in grafo.grafo[u]:
            G.add_edge(u, v, weight=peso)
    
    pos = nx.spring_layout(G)
    edges = G.edges(data=True)
    weights = [edge[2]['weight'] for edge in edges]
    
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold', arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f'{peso}' for u, v, peso in edges})
    plt.show()

# Dibuja el grafo
dibujar_grafo(grafo)