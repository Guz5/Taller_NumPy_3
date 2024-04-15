import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Importar Axes3D desde mpl_toolkits.mplot3d

# Crear un ndarray de 1 dimensión, 100 elementos equiespaciados, de 0 a 2*pi
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

# Crear una figura tridimensional
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar la función seno en 3D
ax.plot3D(x, y, zs=0, zdir='z', label='seno de x')

# Añadir etiquetas y título
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('seno de x (sen(x))')
ax.set_title('Gráfico tridimensional de seno de x')

# Mostrar el gráfico
plt.show()
