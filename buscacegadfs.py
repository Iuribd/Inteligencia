def dfs(grafo, inicio, objetivo, visitado=None):
    if visitado is None:
        visitado = set()
    
    visitado.add(inicio)
    if inicio == objetivo:
        return True
    
    for vizinho in grafo[inicio]:
        if vizinho not in visitado:
            if dfs(grafo, vizinho, objetivo, visitado):
                return True
    
    return False
