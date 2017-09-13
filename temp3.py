import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
# Declaramos una funcion que nos devuelva f(x) = x* sin (2011*x)*6
def f(t):
    return t * np.sin(2011*t)*6

# Definimos el rango de dos variables y el intervalo en el que cambian
t1 = np.arange(0.0, 10.0, 0.2)
t2 = np.arange(0.0, 10.0, 0.01)

# Crea el grupo de graficas
plt.figure(1)
# Crea el lienzo con dos renglones, una columna y entra a la primera seccion de esta division.
plt.subplot(211)
# Grafica la variable t1 contra la funcion f(t1) con circulos azules y grafica la variable t2 contra la funcion f(t2) con una linea negra.
plt.plot(t1, f(t1), 'g-p', t2, f(t2), 'b')
# Entra a la segunda seccion del lienzo dividido
plt.subplot(212)
# Grafica la variable t2 contra la funcion sin(2011*x) con una linea punteada roja.
plt.plot(t2, np.sin(2011*t2), 'r*')
# Guardar la grafica
plt.savefig('dosfunciones.png')
# muestra la grafica
plt.show()
