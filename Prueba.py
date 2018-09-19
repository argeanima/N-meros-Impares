y =[4,15,24,56]
print "El primero es",y[0],"y el ultimo",y[3]
print (range(7))
for i in range(3):
    print"Hola"
    print"Urielito"
print"Hasta luego" 
y.append("Bye")
print y

# comentariooo :3

x=[100]
for i in range(100):
    x.append(1.01*x[i])
print x

# x=[1,1]
# for i in range(30):
#     x.append(x[i]+x[i+1])
# print x

import matplotlib.pyplot as plt
plt.plot(x)
plt.show(x)

#funciones

def suma(x,y):
    return x+y
suma(2,3)

def prod(x,y):
    return x*y
prod(2,3)

def operacion(x,y,f):
    return f(x,y);
operacion(2,3,suma)

def producto(x):
    return 1.01*x
def ciclo(inicial,iteracion,producto):
    x=[inicial]
    for i in range(iteracion):
        x.append(producto(x[i]))
    return x
def imprime(inicial,iteracion):
    x=ciclo(inicial,iteracion,producto)
    print x
import math
def producto(x):
    return 1.01*x
def ciclo(inicial,iteracion,producto):
    x=[inicial]
    for i in range(iteracion):
        x.append(producto(x[i]))
    return x
def imprime(inicial,iteracion):
    x=ciclo(inicial,iteracion,math.cos)
    print x
imprime (5,20)

import numpy

