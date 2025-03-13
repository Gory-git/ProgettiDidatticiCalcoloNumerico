import shutil
from warnings import catch_warnings

import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import re

converge = True
epsilon = 1
'''
passi da seguire:
1)
2)
3)
'''

def plotta(passo):
    plt.figure(figsize=(10, 10))
    plt.plot(x_values, y_values, label='g(x)', color='blue')
    plt.plot(x_values, z_values, label='i(x)', color='red')
    if passo != 0:
        plt.plot(p_values, p2_values, label='iterazioni', color='green')
    plt.title('Grafico della funzione f(x)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid()
    plt.legend()
    plt.savefig("img/passo_" + str(passo + 1) + ".png")
    plt.close()


def i(x):
    return x

def f(x):
    return x ** 3 + 2 * x ** 2 + 10 * x - 20

def g(x):
    if converge:
        return 20 / (x ** 2 + 2 * x + 10) # CONVERGENZA
    else:
        return (20 - 10 * x) / (x ** 2 + 2 * x) # DIVERGENZA
def iterazioni(x, y, asse_x, asse_y):
    asse_x.append(x)
    asse_y.append(y)

    plotta(0)

    max = int(input("inserire il numero massimo di iterazioni: \n"))
    if max <= 0:
        max = 100
    for j in range(max):

        print("\n#--ITERAZIONE NUMERO--#")
        print("\t\t", j)

        asse_x.append(i(asse_x[len(asse_x) - 1]))
        asse_y.append(g(asse_x[len(asse_x) - 2]))

        asse_y.append(i(asse_y[len(asse_y) - 1]))
        asse_x.append(g(asse_x[len(asse_x) - 1]))

        print("x: ", p_values[len(p_values) - 2])
        print("f(x): ", p2_values[len(p2_values) - 2])

        plotta(j)

        if abs(asse_x[len(asse_x) - 2] - asse_y[len(asse_y) - 2]) < epsilon : # condizione di uscita
            return asse_x, asse_y
    return asse_x, asse_y

def extract_number(filename):
    match = re.search(r'_(\d+)', filename)
    return int(match.group(1)) if match else 0

def elabora_video():
    cartella = 'img/'
    video_name = 'output_video.avi'

    images = [img for img in os.listdir(cartella) if img.endswith(".png")]

    images.sort(key=extract_number)

    first_image = cv2.imread(os.path.join(cartella, images[0]))
    height, width, layers = first_image.shape

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video = cv2.VideoWriter(video_name, fourcc, 1, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(cartella, image)))

    video.release()
    cv2.destroyAllWindows()
    if os.path.exists("img/"):
        try:
            shutil.rmtree("img/")
        except:
            pass

def run():
    global p_values
    global p2_values
    global converge
    global y_values
    global epsilon

    converge = "s" == input("Convergenza? \n\tSi = S \n\tNo = N\n").lower()
    if converge:
        x = int(input("inserisci l'ascissa del punto di partenza: \n"))
        y = int(input("inserisci l'ordinata del punto di partenza: \n"))
    else:
        x = 1
        y = 0
        y_values = g(x_values)
    esponente = int(input("inserire il grado di precisione (es. per avere epsilon = 10^-10 inserire il valore -10).\nInserire un valore >= 0 imposta il default 10^-16 (accuratezza massima)\n"))
    if esponente >= 0 or esponente < -16:
        esponente = -16
    epsilon *= 10 ** esponente
    iterazioni(x,y, p_values, p2_values)


    elabora_video()


x_values = np.linspace(-10, 10, 400)  # 400 punti tra -10 e 10
y_values = g(x_values)
z_values = i(x_values)
p_values = []
p2_values = []

if __name__ == '__main__':
    run()
