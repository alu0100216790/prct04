#!/usr/bin/python
#!encoding: UTF-8
'''¿Que hace el siguiente programa cuando el valor de la variable
a
es cero? Haga una propuesta
para solucionar el error que se produce en tiempo de ejecuci
on.
a = float(raw_input("Valor de a: "))
b = float(raw_input("Valor de b: "))
x = -b/a
print "Solucion: ", x'''

a = float(raw_input("Valor de a: "))
b = float(raw_input("Valor de b: "))
if (a!=0):
  x = -b/a
  print "Solucion: ", x
else:
  print "no se puede divivir por cero"
