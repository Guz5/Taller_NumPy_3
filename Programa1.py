#Taller NumPy

#NumPy: Biblioteca para realizar calculos numéricos n dimensionales

#Crear ndarray de dos dimensiones a partir de una lista 

import numpy as np

A = np.array([[1,5],[7,9]])

D = np.array([[2,0],[1,3]])



C = np.dot(A,D)

print(C)

#SOlución de un sistema d ecuaciones con NumPy
m_solucion = np.array([5,17])

m = np.linalg.solve(A,m_solucion)

print(m)
