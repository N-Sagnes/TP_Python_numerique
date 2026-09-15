"""importation des bibliothèques/modules"""


import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Audio,display
from scipy.io import wavfile


RATE = 44_100
LA = 440
DO = 523.25

""" Questions : 
1) Pour échantilloner un son de 440Hz, il faut 440 échantillons par seconde
2)  position = A*sin(2*np.pi*phi*t), avec A l'amplitude de la vibration 
"""
#3)

n=440 #le nombre de points 
abscisses = np.linspace(0,0.05,n)
ordonnées = np.sin(2*np.pi*LA*abscisses)

plt.plot(abscisses, ordonnées)
plt.show()

display(Audio(ordonnées,440))

#4) 
"""
def display_signal(signal, freq, signal, width) :
    abs = np.linspace(0,1,freq)
    ord = signal(2*np.pi*freq*abs)
    plt.plot(abs, ord)
    plt.show()

"""