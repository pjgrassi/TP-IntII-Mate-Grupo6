#Aplicacion main
from funciones import *

#Para esta primer parte tomamos dos DNI ingresados por el usuario

#Solicitud datos y obtencion de conjuntos (listas)

print("Bienvenido al TP Integrador II de Matematica")
dni=input("Ingrese su DNI: ")
A=(generador_conj(dni))
print("Conjunto A=",(A))
dni=input("Ingrese otro DNI: ")
B=(generador_conj(dni))
print("Conjunto B=",(B))

#Union
lista_u=union(A,B)
print("La union de los conjuntos A y B es: ",lista_u)

#Interseccion
lista_i=inter(A,B)
print("La intersección de los conjuntos A y B es: ",lista_i)

#Diferencia
lista_d=dif(A,B)
print("La diferencia del conjunto A respecto al B es: ",lista_d)

#Diferencia Simetrica
lista_ds=difsim(A,B)
print("La diferencia simetrica de los conjuntos A y B es: ",lista_ds)

#

