# coding:utf-8

from sedar_007 import *


sedar_007()
a=0
b=1
i=1

nombre =0
while nombre <= 0:
    nombre=input("Entrer le nombre (nombre positif): ")
    nombre=int(nombre)
if nombre==1:
    c=1


else :
    while i<nombre:
        c=a+b
        a=b
        b=c
    
        i=i+1
print("Pour le nombre {} la reponse est: {}".format(nombre, c))
