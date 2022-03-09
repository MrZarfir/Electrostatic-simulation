
import numpy as np
import matplotlib.pyplot as plt

# données brute (en colonne ou en une ligne):
temps = '''
1
2
3
4
5
7
8
8.1
8.5
9
'''

courant = '1,99 1,85 1,8 1,7 1,2 1,15 1,1 1,02 1, 0,8' # en mA, remplacez par vos valeurs!
tension = '0.8 0.77 0.7 0.65 0.65 0.6 0.5 0.45 0.4 0.35' # en V, remplacez par vos valeurs!


############################ 

# ceci va remplacer les virgules par des points pour les décimales, au besoin:
temps = temps.replace(',','.')
courant = courant.replace(',','.')
tension = tension.replace(',','.')

# ceci va transformer les strings en array numpy: 
courant = np.fromstring(courant, dtype=float, sep=' ')
temps = np.fromstring(temps, dtype=float, sep=' ')
tension = np.fromstring(tension, dtype=float, sep=' ')

# data validation: même nombre de données?
nombres_data = [len(elem) for elem in [temps, courant, tension]]
if len(set(nombres_data)) != 1:
    print('Vérifiez le nombre de données: %s'%nombres_data)
    raise ValueError()

# calcul de la puissance:
puissance = courant * tension # en mW


# incertitudes:
incert_courant_abs = 0.01 + 0.02 * courant # à substituer par vos valeurs pour UNI-T
incert_tension_abs = 0.02 + 0.01 * tension # à substituer par vos valeurs pour Amprobe

incert_courant_rel = incert_courant_abs / courant
incert_tension_rel = incert_tension_abs / tension
incert_puissance_rel = incert_tension_rel + incert_courant_rel
incert_puiss_abs = incert_puissance_rel * puissance
incert_temps = 2/60. # 2 secondes (généreux)

# figure:
plt.figure(figsize=(5,3))
plt.errorbar(temps, puissance, xerr = incert_temps, marker='o', ls='none',
             yerr = incert_puiss_abs, ms=3)
plt.title("Décharge d'une cellule galvanique Zn-Cu")
plt.ylabel('Puissance (mW)')
plt.xlabel('Temps (min)')
plt.savefig('graphe_pile.pdf', bbox_inches='tight') # sauvegardé dans le rep
plt.show()