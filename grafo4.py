import networkx as nx
import matplotlib.pyplot as plt

# Recorrido en anchura del grafo G desde el nodo nodo
def anchura(G, nodo, visitados=None):
    if visitados is None:
        visitados = set()
    cola = [nodo]
    visitados.add(nodo)
    while cola:
        v = cola.pop(0)
        for w in G.neighbors(v):
            if w not in visitados:
                cola.append(w)
                visitados.add(w)
    return visitados

# Recorrido en profundidad del grafo G desde el nodo nodo
def profundidad(G, nodo, visitados=None):
    if visitados is None:
        visitados = set()
    visitados.add(nodo)
    for v in G.neighbors(nodo):
        if v not in visitados:
            profundidad(G, v, visitados)
    return visitados

# Componentes conexas de un grafo con recorrido en anchura
def componentes_conexasA(G):
    visitados = set()
    componentes = []
    for v in G.nodes:
        if v not in visitados:
            comp = anchura(G, v, visitados)
            componentes.append(comp)
    return componentes

# Componentes conexas de un grafo con recorrido en profundidad
def componentes_conexasP(G):
    visitados = set()
    componentes = []
    for v in G.nodes:
        if v not in visitados:
            comp = profundidad(G, v, visitados)
            componentes.append(comp)
    return componentes

def draw_graph(G, pos, node_colors, title):
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=500, font_size=10, font_color='white')
    plt.title(title)
    plt.show()

def componentes_conexasA_visual(G):
    visitados = set()
    componentes = []
    pos = nx.spring_layout(G)
    for v in G.nodes:
        if v not in visitados:
            comp = anchura(G, v, visitados)
            componentes.append(comp)
            node_colors = ['red' if node in visitados else 'blue' for node in G.nodes]
            draw_graph(G, pos, node_colors, f'Anchura - Nodo {v}')
    return componentes

def componentes_conexasP_visual(G):
    visitados = set()
    componentes = []
    pos = nx.spring_layout(G)
    for v in G.nodes:
        if v not in visitados:
            comp = profundidad(G, v, visitados)
            componentes.append(comp)
            node_colors = ['red' if node in visitados else 'blue' for node in G.nodes]
            draw_graph(G, pos, node_colors, f'Profundidad - Nodo {v}')
    return componentes

if __name__ == "__main__":
    G = nx.erdos_renyi_graph(10, 0.3)
    print("Componentes conexas (Anchura):", componentes_conexasA_visual(G))
    print("Componentes conexas (Profundidad):", componentes_conexasP_visual(G))

    # Create a new graph
    G = nx.Graph()
    edges = [(1, 2), (1, 3), (2, 4), (3, 5), (6, 7), (7, 8), (8, 9), (9, 10)]
    G.add_edges_from(edges)

    # Visualize the graph
    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_color='black')
    plt.title('Graph Visualization')
    plt.show()

    # Print connected components using breadth-first search
    print("Componentes conexas (Anchura):", componentes_conexasA_visual(G))

    # Print connected components using depth-first search
    print("Componentes conexas (Profundidad):", componentes_conexasP_visual(G))

    # Print connected components without visualization
    print("Componentes conexas con recorrido en profundidad")
    for i, comp in enumerate(componentes_conexasP(G)):
        print(f"Componente número {i}: {comp}")
    print("Componentes conexas con recorrido en anchura")
    for i, comp in enumerate(componentes_conexasA(G)):
        print(f"Componente número {i}: {comp}")
