from constraint import Problem, AllDifferentConstraint

def solve_n_queens(n):
    problem = Problem()
    variables = range(n)
    domain = range(n)
    
    # Adiciona as variáveis ao problema
    problem.addVariables(variables, domain)
    
    # Adiciona a restrição de que todas as rainhas devem estar em colunas diferentes
    problem.addConstraint(AllDifferentConstraint())
    
    # Adiciona as restrições diagonais
    for i in variables:
        for j in variables:
            if i != j:
                problem.addConstraint(lambda x, y, i=i, j=j: abs(x-y) != abs(i-j), (i, j))
    
    # Resolve o problema
    solutions = problem.getSolutions()
    
    # Retorna as soluções encontradas
    return solutions

# Exemplo de uso
solutions = solve_n_queens(8)
for solution in solutions:
    print(solution)
