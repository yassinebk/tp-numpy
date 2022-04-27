#! /usr/bin/python3
import numpy as np

a = np.arange(start=100,stop=200,step=10).reshape(2,5)
print("Le table resultat :\n" ,a,end="\n\n")
print("Troisieme colonne de chaque ligne ",a[:,3])

arrayOne=np.array([[5,6,9],[21,18,27]])
arrayTwo=np.array([[15,33,24],[4,7,1]])
print(np.concatenate((arrayOne**2,arrayTwo**2)),end="\n\n")

a= np.arange(start=10,stop=34,step=1).reshape(8,3)
print("Tableau genere:\n" ,a,end="\n\n")
print("4 Tableaux apres la division \n",np.split(a,4))
