import matplotlib.pyplot as plt
import numpy as np

'''
passi da seguire:
1)
2)
3)
'''

def i(x):
    return x

def f(x):
    return x ** 3 + 2 * x ** 2 + 10 * x - 20

def g(x):
    return 20 / (x ** 2 + 2 * x + 10) # CONVERGENZA
    # return (20 - 10 * x) / (x ** 2 + 2 * x) # DIVERGENZA
def iterazioni(x, y):
    asse_x = [x, i(x)]
    asse_y = [y, g(x)]
    epsilon = 0.00000000000000001
    for j in range(100):

        print(j)
        print()

        asse_x.append(i(asse_y[len(asse_y) - 1]))
        asse_y.append(g(asse_x[len(asse_x) - 2]))

        asse_y.append(g(asse_x[len(asse_x) - 1]))
        asse_x.append(i(asse_y[len(asse_y) - 2]))

        asse_x.append(i(asse_y[len(asse_y) - 1]))
        asse_y.append(g(asse_x[len(asse_x) - 2]))



        if abs(asse_x[len(asse_x) - 1] - asse_y[len(asse_y) - 1]) + abs(asse_x[len(asse_x) - 2] - asse_y[len(asse_y) - 2]) < epsilon :
            print(asse_x)
            print(asse_y)
            return asse_x, asse_y
    print(asse_x)
    print(asse_y)
    return asse_x, asse_y

def run():
    x_values = np.linspace(-10, 10, 400)  # 400 punti tra -10 e 10
    y_values = g(x_values)
    z_values = i(x_values)
    p_values, p2_values = iterazioni(1,0)

    print(p_values[len(p_values) - 1])
    print(p2_values[len(p2_values) - 1])


    plt.figure(figsize=(30, 30))
    plt.plot(x_values, y_values, label='g(x)', color='blue')
    plt.plot(x_values, z_values, label='i(x)', color='red')
    plt.plot(p_values, p2_values, label='spirale', color='green')
    plt.title('Grafico della funzione f(x)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid()
    plt.legend()
    plt.show()

    plt.close()


if __name__ == '__main__':
    run()
    # coefficients = [1, 2, 10, -20]  # corrisponde a x^2 + 0*x - 4
    #
    # # Trova le radici
    # radici = np.roots(coefficients)
    #
    # # Crea una lista di funzioni per ciascuna radice
    # funzioni_radici = [lambda x, r=r: r for r in radici]
    #
    # # Usa le funzioni per ottenere le radici
    # for i, funzione_radice in enumerate(funzioni_radici):
    #     print(f"La radice {i + 1} è:", funzione_radice(0))
