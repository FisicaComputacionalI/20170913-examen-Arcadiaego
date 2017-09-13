import scipy as sp
import matplotlib.pyplot as plt

# Creamos el array x de cero a cien con cien puntos
x = sp.linspace(0, 10,)

# Creamos el array y donde cada punto es el seno de cada elemento de x
y = sp.sin(2011*x)*6

# Nombre de los ejes

plt.xlabel('valores de x')
plt.ylabel('Amplitud')

# Representamos
plt.plot(x,y,'k--p')

#Titulo
plt.title(u'Grafica del seno') 

#Titulo superior
plt.suptitle(u'Examen de F. Moises')

#Guardar la grafica en formato png
plt.savefig('temp2.png')

# Mostramos en pantalla
plt.show()
