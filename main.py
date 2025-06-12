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

#Conteo repeticion de digitos en numero ingresado
print("En esta parte del programa se cuenta las veces que se repiten los digitos en un numero")
dni=(int(input("Ingrese el numero de su DNI: ")))
print("Se muestra la cantidad de veces que se repite cada digito: ")
print(rep_dig(dni))

#Conteo de cantidad de digitos que posee un numero
print("Ahora vamos a contar cuantos digitos posee un numero")
dni=(input("Ingrese el numero de su DNI: "))
print(f"El numero de DNI {dni} posee {conteo_dig(dni)} digitos")

#Evaluacion de condicion si el conjunto generado a partir de un DNI posee diversidad numerica
print("En este apartado veremos si se cumple la condicion de diversidad numerica en un conjunto")
dni=input("Ingrese un DNI: ")
A=(generador_conj(dni))
print("Conjunto A=",(A))
print(f"La condicion {diver(A)}")


