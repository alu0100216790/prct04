#!/usr/bin/python
#!encoding: UTF-8

from math import sqrt                                                      #desde el paquete de matematicas importame la raiz cuadrada
									     #Si colocamos from math * , copiamos todo el paquete matematicas

a = float(raw_input("Valor de a: "))
b = float(raw_input("Valor de b: "))
c = float(raw_input("Valor de c: "))
for i in range (1,n)
if (a != 0):
  x1 = (-b + sqrt(b**2 - 4*a*c)) / (2 * a)
  x2 = (-b - sqrt(b**2 - 4*a*c)) / (2 * a)
  print "los valores que introdujo el usuario , ha sido: a=%4.3f ,b=%4.3f ,c=%4.3f Las soluciones de la ecuacion son: x1=%4.3f y x2=%4.3f" % (a,b,c,x1, x2)
else:
  if( b != 0):
    x = -c / b
    print "La solucion de la ecuacion es: x=%4.3f" % x
  else:
    if (c != 0):
      print "La ecuacion no tiene solucion"
    else:
      print "La ecuacion tiene infinitas soluciones"