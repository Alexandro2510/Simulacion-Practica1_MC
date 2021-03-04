from random import uniform
from statistics import mean
from math import exp
from math import cos

'''
Definimos una funcion "integral" que nos ayudara para agregar
los limites de la integral y el numero de variables aleatorias
'''

def integral (funcion,k):
    '''

    Parameters
    ----------
    funcion : TYPE
        funcion f(x) que vamos a integrar.
    k : TYPE
        numero de variables aleatorioas distribuidad 
        uniformemente  entre (0,1).

    Returns
    -------
    Valor aproximado a la interal de f(x)

    '''
    L1 = []
    for i in range (k):
        L1.append(uniform(0,1))
    
    L2 = []
    for j in range (k):
        L2.append(funcion((1/(L1[j]))-1)/L1[j]**2)
    
    return mean(L2)
  
'''
Definimos la funcion que queremos utilizar con las variables aleatorias
'''
  
def f (x):
    return 1/(1+x**2)

'''
Valor de la integral dado por Wolfram Alfa: 1.570796
'''

'''
Empezamos con el contador k igual a uno, para comenzar con una variable
aleatoria y definimos una nueva lista para el numero de variables aleatorias
necesarias para la exactitud deseada
'''

k = 1

'''
Para 2 decmiales
'''

L3 = []

'''
Utilizamos un ciclo while porque no sabes cuantas variables aleatorias
seran necesarias para lograr las 2 decimasles
'''

while True:
    y = integral(f, k)
    y2 = str(y)[0:4]
    if len(L3) == 10:
        break
    elif y2 == '1.57':
        L3.append(k)
        k = 1
    else:
        k = k+1

'''
Para 3 decmiales
'''

L4 = []

'''
Utilizamos un ciclo while porque no sabes cuantas variables aleatorias
seran necesarias para lograr las 3 decimasles
'''

while True:
    y = integral(f, k)
    y2 = str(y)[0:5]
    if len(L4) == 10:
        break
    elif y2 == '1.570':
        L4.append(k)
        k = 1
    else:
        k = k+1
        
'''
Para 4 decmiales
'''

L5 = []

'''
Utilizamos un ciclo while porque no sabes cuantas variables aleatorias
seran necesarias para lograr las 4 decimasles
'''

while True:
    y = integral(f, k)
    y2 = str(y)[0:6]
    if len(L5) == 10:
        break
    elif y2 == '1.5707':
        L5.append(k)
        k = 1
    else:
        k = k+1

'''
Para 5 decmiales
'''

L6 = []

'''
Utilizamos un ciclo while porque no sabes cuantas variables aleatorias
seran necesarias para lograr las 5 decimasles
'''

while True:
    y = integral(f, k)
    y2 = str(y)[0:7]
    if len(L6) == 10:
        break
    elif y2 == '1.57079':
        L6.append(k)
        k = 1
    else:
        k = k+1
        
        
'''
Imprimimos las listas
'''

print(L3)
print(L4)
print(L5)
print(L6)

'''
Tomaremos el valor maximo de variables aleatorias que obtuvimos
y haremos 1000 replicas para ver en cuantas ocaciones nos vuelven a dar
el mismo numero (o mayor) de digitos de exactitud
'''

'''
Para 2 digitos
'''

c1 = 0


for i in range (1000):
    y = integral(f, max(L3))
    y2 = str(y)[0:4]
    if y2 == '1.57':
        c1 = c1 + 1
        
'''
Para 3 digitos
'''

c2 = 0


for i in range (1000):
    y = integral(f, max(L4))
    y2 = str(y)[0:5]
    if y2 == '1.570':
        c2 = c2 + 1

'''
Para 4 digitos
'''

c3 = 0


for i in range (1000):
    y = integral(f, max(L5))
    y2 = str(y)[0:6]
    if y2 == '1.5707':
        c3 = c3 + 1

'''
Para 5 digitos
'''

c4 = 0


for i in range (1000):
    y = integral(f, max(L6))
    y2 = str(y)[0:7]
    if y2 == '1.57079':
        c4 = c4 + 1

'''
Imprimimos los exitos
'''

print(c1)
print(c2)
print(c3)
print(c4)
