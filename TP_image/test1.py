import numpy as np
import matplotlib.pyplot as plt
import random as rd

image =np.empty((91,91,3),dtype=np.uint8) #on crée une image normalisée
#image[:] = [0,255,0]
#print(image[0,0],image[-1,-1])
image[::10] = [0,0,255] # on trace les lignes en bleu
image[:,::10] = [0,0,255] #on trace les colonnes en bleu

"""---Partie image---"""

im = plt.imread('data/les-mines.jpg') #on lit le fichier image
im2 = im.copy()
"""
#print(bool(im2.flags.writeable)) #on vérifie si l'image est modifiable
print('type' ,type(im2)) #on vérifie le type de l'objet
print('dimenson :',im2.ndim) #on affiche les dimensions de l'objet
print(im2.shape[:2])# largeur et hauteur de l'image
print('nb d-octet par pixel :',im2.itemsize) #octets par pixel
print(im2.dtype) # type des pixels
print(im2.max(),im2.min()) #affiche le max et min
"""
def isolement_im(l,c):
    x,y = im2.shape[:2]
    tab=im2[x//2-l//2:x//2+l//2:,y//2-c//2:y//2+c//2]
    return tab

"""---canaux RGB---"""

imred= im2[::,::,0]
imgreen= im2[::,::,1]
imblue= im2[::,::,2]
# on observe que les couleurs affichées ne sont pas les bonnes

im3= im.copy()
im3[-200:,-200:] = [219,112,147]

"""---affichage---"""
#plt.imshow(im2[:10,:10]) # on slice le tableau et on affiche le coin du haut en 10*10
#for i in [2,5,10,20]: #on crée chaque image successivement
#    plt.imshow(im2[::i,::i])
 #   plt.show()
#plt.imshow(isolement_im(100,200))


"""
plt.imshow(im3)
plt.show()
plt.imshow(imred,cmap='Reds')
plt.show()
plt.imshow(imred,cmap='Greens')
plt.show()
plt.imshow(imred,cmap='Blues')
"""
#plt.imshow(image)# on affiche l'image colorée
#plt.imshow(im) #on affiche l'image des mines
plt.show()
