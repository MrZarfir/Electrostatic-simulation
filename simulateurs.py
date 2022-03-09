import scipy.optimize as optimize
import numpy as np
import matplotlib.pyplot as plt

#Nombre de particules du système
N = int(input("Vous cherchez à simuler un système de combien de particules? : "))

#Indices ij de chaque différence de position
indices = [(i, j) for i in range(1, N + 1) for j in range(i + 1, N + 1)]

# Définition de la fonction de référence sur l'énergie potentielle initiale
def energie(x):
    n = len(x)
    r = []
    e = 0.0
    unsur = []
    # for i,j in indices:
    #     r.append(abs(x[j-1] - x[i-1]))
    #
    # for index in range(1,len(r)+1):
    #     unsur.append(1/r[index-1])
    # for i in unsur:
    #     if i != 0:
    #         e += i
    #     else:
    #         e += float('inf')
    # return e

    for i,j in indices:
        dif = (abs(x[j-1] - x[i-1]))
        if dif != 0:
            e += (1/dif)
        else:
            e += float('inf')
    return e

#Fonction de référence déterminant la somme des Forces
def forces(x):
    last_index = len(x) - 1
    for i, xi in enumerate(x):
        somme_F = 0
        for j in range(len(x)):
            if i != j:
                delta_x = x[j] - x[i]
                F = 1/delta_x**2
                F = -F*np.sign(delta_x)
                somme_F += F

        print(somme_F)
    return



def main():

# Définition de la l'array contenant toutes les positions initiales des particules du système
    x = []
    for i in range(1, N + 1):
        # print(i)
        if i != 1:
            x.append((i-1) / (N-1))
        if i == 1:
            x.append(0)

    U = energie(x)

#Optimization de la fonction énergie de départ
    meth = 'SLSQP'
    bnds = [(0, 1)]*len(x)
    res = optimize.minimize(energie, x, bounds=bnds, method=meth, tol=1e-10, options={'disp': True, 'maxiter': 1000})


#Différences de position entre chacune des particules (deuxième graphique)
    diffdict = {}
    num = []
    for i in range(len(res.x)):
        if i != 0:
            diff = res.x[i] - res.x[i-1]
            diffdict["{i} - {imin}".format(i=i, imin=(i-1))] = diff

            num.append(i)

    # Création d'une array contenant toutes les différences de positions des particules (deuxième graphique)
    diffval = []
    for value in diffdict.values():
        diffval.append(value)

# """
# Toutes les lignes suivantes font appel à l'affichage (graphiques, printing, etc)
# """
    print("Énergie de départ = " + str(U))
    print(res.x)

    # print(indices)
    # print(len(x))

    plt.figure()
    plt.title("Position des différentes charges sur un fil de 1 mètre")
    plt.hlines(1, 0, 1)
    plt.vlines(0, 0.9, 1.1)
    plt.eventplot(res.x, orientation='horizontal', linewidths=0.5, colors='b')
    plt.axis('off')

    plt.figure()
    plt.title("Différence de position entre chacune des particules chargées")
    plt.scatter(num, diffval)
    plt.show()






main()

