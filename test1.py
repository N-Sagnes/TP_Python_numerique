import numpy as np
import matplotlib.pyplot as plt
import random as rd

im = plt.imread('data/les-mines.jpg') #on lit le fichier image
im2 = im.copy()
print(bool(im2.flags.writeable)) #on vérifie si l'image est modifiable
print(type(im2)) #on vérifie le type de l'objet

image =np.empty((91,91,3),dtype=np.uint8) #on crée une image normalisée
#image[:] = [0,255,0]
#print(image[0,0],image[-1,-1])
image[::10] = [0,0,255] # on trace les lignes en bleu
image[:,::10] = [0,0,255] #on trace les colonnes en bleu

#plt.imshow(image)# on affiche l'image colorée
plt.imshow(im) #on affiche l'image des mines
#plt.show()
