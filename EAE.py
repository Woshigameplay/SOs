import random

# Gera um número aleatório entre 1 e 100
numero_aleatorio = random.randint(1, 100)

# Gera uma string aleatória com 10 caracteres
string_aleatoria = ''.join(random.choice(string.ascii_letters) for i in range(10))

# Gera uma lista de 5 números aleatórios entre 1 e 20
lista_aleatoria = [random.randint(1, 20) for i in range(5)]

# Escolhe um elemento aleatório da lista
elemento_aleatorio = random.choice(lista_aleatoria)

# Embaralha a lista
random.shuffle(lista_aleatoria)

# Imprime os resultados
print(f"Número aleatório: {numero_aleatorio}")
print(f"String aleatória: {string_aleatoria}")
print(f"Lista aleatória: {lista_aleatoria}")
print(f"Elemento aleatório: {elemento_aleatorio}")
