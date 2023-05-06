import heapq

def astar(grafo, inicio, objetivo, heuristica):
    fila = [(0, inicio)]
    custo = {inicio: 0}
    pai = {inicio: None}
    
    while fila:
        _, vertice_atual = heapq.heappop(fila)
        if vertice_atual == objetivo:
            caminho = []
            while vertice_atual is not None:
                caminho.append(vertice_atual)
                vertice_atual = pai[vertice_atual]
            caminho.reverse()
            return caminho
        
        for vizinho, custo_aresta in grafo[vertice_atual].items():
            novo_custo = custo[vertice_atual] + custo_aresta
            if vizinho not in custo or novo_custo < custo[vizinho]:
                custo[vizinho] = novo_custo
                prioridade = novo_custo + heuristica(vizinho, objetivo)
                heapq.heappush(fila, (prioridade, vizinho))
                pai[vizinho] = vertice_atual
    
    return None
