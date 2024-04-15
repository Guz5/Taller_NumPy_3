import numpy as np

# Matplotlib tiene muchos módulos

import matplotlib.pyplot as plt

# Crear un ndarray de 1 dimensión, 100 elimentos equiespaciados, de 0 a 2*pi

x = np.linspace(0,2*np.pi,100) # El primer dato aquí es el inicio, el segundo es el fin, el tercer dato es el número de elementos. Es decir x = np.linspace(inicio,fin,elementos)

y = np.sin(x)

#Usar matplotlib

plt.figure(figsize=(8,4))
plt.plot(x,y)
plt.title("Mi primer gráfico científico en programación")
plt.xlabel("x")
plt.ylabel("seno de x (sen(x))")
plt.grid(True)
plt.show()