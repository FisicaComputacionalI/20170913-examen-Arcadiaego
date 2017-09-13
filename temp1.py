import numpy as np
import pylab as pl
# Edad en X
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
# Anio en Y
y = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
# Dar nombre a los ejes
pl.ylabel('Anios')
pl.xlabel('Edad')
#Titulo
pl.title(u'Faustino Moises Amador Garcia') 
#Titulo superior
pl.suptitle(u'Examen de F. Moises')
# Colocamos los rangos
pl.axis([-1,28, 1989,2020])
# Grafica el vector x contra el vector y
pl.plot(x, y, 'b--p')
#Guardar la grafica en formato png
pl.savefig('temp1.png')
#mostrar 
pl.show()
