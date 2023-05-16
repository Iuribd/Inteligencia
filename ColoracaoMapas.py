from constraint import Problem, AllDifferentConstraint

def solve_map_coloring(colors, neighbors):
    problem = Problem()
    
    # Adiciona as variáveis ao problema (países)
    for country in neighbors.keys():
        problem.addVariable(country, colors)
    
    # Adiciona a restrição de que países vizinhos não podem ter a mesma cor
    for country, adjacent_countries in neighbors.items():
        problem.addConstraint(AllDifferentConstraint(), [country] + adjacent_countries)
    
    # Resolve o problema
    solutions = problem.getSolutions()
    
    # Retorna as soluções encontradas
    return solutions

# Exemplo de uso
colors = ["Red", "Green", "Blue"]
neighbors = {
    "Brazil": ["Argentina", "Bolivia", "Paraguay", "Peru", "Uruguay"],
    "Argentina": ["Brazil", "Bolivia", "Chile", "Paraguay", "Uruguay"],
    "Bolivia": ["Argentina", "Brazil", "Chile", "Paraguay", "Peru"],
    "Chile": ["Argentina", "Bolivia", "Peru"],
    "Paraguay": ["Argentina", "Brazil", "Bolivia"],
    "Peru": ["Brazil", "Bolivia", "Chile"],
    "Uruguay": ["Argentina", "Brazil"]
}

solutions = solve_map_coloring(colors, neighbors)
for solution in solutions:
    print(solution)
