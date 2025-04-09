import random
import string

target = "PEDRO PAULO SOARES"  
population_size = 500
mutation_rate = 0.01     

def generate_individual(length):
    return ''.join(random.choice(string.ascii_uppercase + ' ') for _ in range(length))

def generate_population(size, length):
    return [generate_individual(length) for _ in range(size)]

def fitness(individual):
    return sum(1 for i, j in zip(individual, target) if i == j)

def fitness_percentage(individual):
    return (fitness(individual) / len(target)) * 100

def select_parents(population):
    return random.choices(population, weights=[fitness(ind) for ind in population], k=2)

def crossover(parent1, parent2):
    point = random.randint(0, len(parent1) - 1)
    return parent1[:point] + parent2[point:]

def mutate(individual):
    individual = list(individual)
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = random.choice(string.ascii_uppercase + ' ')
    return ''.join(individual)

def genetic_algorithm():
    population = generate_population(population_size, len(target))
    generation = 0
    
    while True:
        population = sorted(population, key=fitness, reverse=True)
        best_individual = population[0]
        best_fitness = fitness(best_individual)
        best_percentage = fitness_percentage(best_individual)
        
        print(f'Geração {generation}: {best_individual} (Fitness: {best_fitness}, Adaptação: {best_percentage:.2f}%)')
        
        if best_individual == target:
            break
        
        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = select_parents(population)
            i1 = mutate(crossover(parent1, parent2))
            i2 = mutate(crossover(parent2, parent1))
            new_population.extend([i1, i2])
        
        population = new_population
        generation += 1

# Executa o algoritmo
genetic_algorithm()
