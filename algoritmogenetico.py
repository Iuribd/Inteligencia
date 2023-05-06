import random

# define o tamanho da população e do genoma
POPULATION_SIZE = 50
GENOME_LENGTH = 20

# define a taxa de mutação
MUTATION_RATE = 0.1

# define o número máximo de gerações
MAX_GENERATIONS = 100

# define a função de fitness
def fitness(genome):
    # aqui, a função de fitness é simplesmente a soma dos valores do genoma
    return sum(genome)

# cria uma população inicial de genomas aleatórios
population = [[random.randint(0, 1) for _ in range(GENOME_LENGTH)] for _ in range(POPULATION_SIZE)]

# executa o algoritmo genético por um número máximo de gerações
for generation in range(MAX_GENERATIONS):
    # avalia a fitness de cada genoma na população
    scores = [(fitness(genome), genome) for genome in population]
    # ordena os genomas por fitness
    scores.sort(reverse=True)
    # exibe o genoma mais apto na geração atual
    print("Generation:", generation, "Best genome:", scores[0][1], "Fitness:", scores[0][0])
    # se encontrarmos um genoma com fitness máxima, interrompemos a execução
    if scores[0][0] == GENOME_LENGTH:
        break
    # seleciona os pais para a próxima geração
    parents = [scores[i][1] for i in range(POPULATION_SIZE//2)]
    # cria a próxima geração a partir dos pais selecionados
    population = parents.copy()
    for i in range(POPULATION_SIZE//2, POPULATION_SIZE):
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)
        child = []
        for j in range(GENOME_LENGTH):
            if random.random() < MUTATION_RATE:
                child.append(random.randint(0, 1))
            else:
                if random.random() < 0.5:
                    child.append(parent1[j])
                else:
                    child.append(parent2[j])
        population.append(child)
import random

# define o tamanho da população e do genoma
POPULATION_SIZE = 50
GENOME_LENGTH = 20

# define a taxa de mutação
MUTATION_RATE = 0.1

# define o número máximo de gerações
MAX_GENERATIONS = 100

# define a função de fitness
def fitness(genome):
    # aqui, a função de fitness é simplesmente a soma dos valores do genoma
    return sum(genome)

# cria uma população inicial de genomas aleatórios
population = [[random.randint(0, 1) for _ in range(GENOME_LENGTH)] for _ in range(POPULATION_SIZE)]

# executa o algoritmo genético por um número máximo de gerações
for generation in range(MAX_GENERATIONS):
    # avalia a fitness de cada genoma na população
    scores = [(fitness(genome), genome) for genome in population]
    # ordena os genomas por fitness
    scores.sort(reverse=True)
    # exibe o genoma mais apto na geração atual
    print("Generation:", generation, "Best genome:", scores[0][1], "Fitness:", scores[0][0])
    # se encontrarmos um genoma com fitness máxima, interrompemos a execução
    if scores[0][0] == GENOME_LENGTH:
        break
    # seleciona os pais para a próxima geração
    parents = [scores[i][1] for i in range(POPULATION_SIZE//2)]
    # cria a próxima geração a partir dos pais selecionados
    population = parents.copy()
    for i in range(POPULATION_SIZE//2, POPULATION_SIZE):
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)
        child = []
        for j in range(GENOME_LENGTH):
            if random.random() < MUTATION_RATE:
                child.append(random.randint(0, 1))
            else:
                if random.random() < 0.5:
                    child.append(parent1[j])
                else:
                    child.append(parent2[j])
        population.append(child)
