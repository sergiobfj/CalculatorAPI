#########################################################
# Código criado para organizar as funções de matemática #
#########################################################

def sum(a, b):
    """Retorna a soma de a e b."""
    return a + b

def subtract(a, b):
    """Retorna a subtração de a e b."""
    return a - b

def multiply(a, b):
    """Retorna a multiplicação de a e b."""
    return a * b

def divide(a, b):
    """Retorna a divisão de a por b. Lança um erro se b for zero."""
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

