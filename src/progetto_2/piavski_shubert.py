import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize_scalar

'''
passi da seguire:
1)
2)
3)
'''

# Definisci la funzione
def f(x):
    return x**2 + 2*x + 1  # Esempio: f(x) = x^2 + 2x + 1

# Definisci la derivata della funzione
def derivata(x):
    return 2*x + 2  # Derivata di f(x)

# Trova il coefficiente di Lipschitz su un intervallo [a, b]
def coefficiente_lipschitz(derivata, a, b):
    # Trova il massimo della derivata nell'intervallo [a, b]
    res = minimize_scalar(lambda x: -derivata(x), bounds=(a, b), method='bounded')
    return -res.fun  # Restituisce il massimo valore della derivata

# Definisci l'intervallo
a = -10
b = 10

# Calcola il coefficiente di Lipschitz
L = coefficiente_lipschitz(derivata, a, b)
print("Il coefficiente di Lipschitz è:", L)