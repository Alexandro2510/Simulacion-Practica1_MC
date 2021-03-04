from random import uniform
from statistics import mean
from math import exp

'''
Definimos una funcion "integral" que nos ayudara para agregar
los limites de la integral y el numero de variables aleatorias
'''

def integral (funcion,a,b,k):
    '''

    Parameters
    ----------
    funcion : TYPE
        funcion f(x) que vamos a integrar.
    a : TYPE
        limite inferior.
    b : TYPE
        limite superior.
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
        L2.append((b-a)*funcion(a+(b-a)*L1[j]))
    
    return mean(L2)
  
'''
Definimos la funcion que queremos utilizar con las variables aleatorias
'''
  
def f (x):
    return 1/(exp(x)+exp(-x))

'''
Valor de la integral dado por Wolfram Alfa: 0.048834
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
    y = integral(f, 3, 7, k)
    y2 = str(y)[0:4]
    if len(L3) == 10:
        break
    elif y2 == '0.04':
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
    y = integral(f, 3, 7, k)
    y2 = str(y)[0:5]
    if len(L4) == 10:
        break
    elif y2 == '0.048':
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
    y = integral(f, 3, 7, k)
    y2 = str(y)[0:6]
    if len(L5) == 10:
        break
    elif y2 == '0.0488':
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
    y = integral(f, 3, 7, k)
    y2 = str(y)[0:7]
    if len(L6) == 10:
        break
    elif y2 == '0.04883':
        L6.append(k)
        k = 1
    else:
        k = k+1

'''
Para 6 decmiales
'''

L7 = []

'''
Utilizamos un ciclo while porque no sabes cuantas variables aleatorias
seran necesarias para lograr las 6 decimasles
'''

while True:
    y = integral(f, 3, 7, k)
    y2 = str(y)[0:8]
    if len(L7) == 10:
        break
    elif y2 == '0.048834':
        L7.append(k)
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
print(L7)

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
    y = integral(f, 3, 7, max(L3))
    y2 = str(y)[0:4]
    if y2 == '0.04':
        c1 = c1 + 1
        
'''
Para 3 digitos
'''

c2 = 0


for i in range (1000):
    y = integral(f, 3, 7, max(L4))
    y2 = str(y)[0:5]
    if y2 == '0.048':
        c2 = c2 + 1

'''
Para 4 digitos
'''

c3 = 0


for i in range (1000):
    y = integral(f, 3, 7, max(L5))
    y2 = str(y)[0:6]
    if y2 == '0.0488':
        c3 = c3 + 1

'''
Para 5 digitos
'''

c4 = 0


for i in range (1000):
    y = integral(f, 3, 7, max(L6))
    y2 = str(y)[0:7]
    if y2 == '0.04883':
        c4 = c4 + 1

'''
Para 6 digitos
'''

c5 = 0


for i in range (1000):
    y = integral(f, 3, 7, max(L7))
    y2 = str(y)[0:8]
    if y2 == '0.048834':
        c5 = c5 + 1

'''
Imprimimos los exitos
'''

print(c1)
print(c2)
print(c3)
print(c4)
print(c5)