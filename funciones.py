#Aqui se van a escribir las funciones necesarias para el funcionamiento de Programa principal main.py
#Generador de conjuntos con digitos unicos
def generador_conj(numero):
    conjunto=[] #inicializa la lista vacia
    #numero_st=str(numero) #pasa el numero a str para poder recorrer mas facil el numero
    for dig in numero: #dig seria el digito y recorrer el str del numero
        if dig not in conjunto: #si no esta en el conjunto 
            conjunto.append(dig) #se agrega al conjunto que queda en str

    return conjunto #retorna el conjunto creado

#Union
def union(lista1, lista2):
    lista_u = [] #se crea una lista vacia para crear la de union
    for elemento in lista1:
        if elemento not in lista_u: #controla si un elemento de lista 1 no esta en la union
            lista_u.append(elemento) #agrega elemento controlado
    for elemento in lista2:
        if elemento not in lista_u: #controla si un elemento de lista 2 no esta en la union
            lista_u.append(elemento) #agrega elemento controlado
    return lista_u

#Interseccion
def inter(lista1, lista2):
    lista_i = [] #se crea una lista vacia para crear la de interseccion
    for elemento in lista1 and lista2:
        if elemento in lista1 and lista2: #controla si un elemento de ambas listas es igual
            lista_i.append(elemento) #agrega elemento controlado
    return lista_i

#Diferencia
def dif(lista1, lista2):
    lista_d = [] #se crea una lista vacia para crear la de diferencia
    for elemento in lista1:
        if elemento not in lista2: #controla si un elemento de lista1 no esta en lista2
            lista_d.append(elemento) #agrega elemento controlado
    return lista_d

#Diferencia simetrica
def difsim(lista1, lista2):
    lista_ds = [] #se crea una lista vacia para crear la de interseccion
    for elemento in lista1:
        if elemento not in lista2: #controla si un elemento de lista 1 no esta en lista 2
            lista_ds.append(elemento) #agrega elemento controlado
    for elemento in lista2:
        if elemento not in lista1: #controla si un elemento de lista 2 no esta en lista 1
            lista_ds.append(elemento) #agrega elemento controlado
    return lista_ds

#Conteo de repeticion de digitos en numero DNI 
def rep_dig(num, cont={}):
    if num==0:  # caso base
        return cont 
    ultimo=num%10 #busca el ultimo digito
    if ultimo in cont:
        cont[ultimo] += 1 #suma 1 si lo encuentra
    else:
        cont[ultimo] = 1 #deja el valor 1 si no se encuentran mas
    return rep_dig(num//10,cont) #llamada recursiva de la funcion

#Conteo de cantidad de digitos del numero
def conteo_dig(num):
    return len(str(num)) #se cuenta como str los digitos

#Evaluacion de condicion si un conjunto posee diversidad numerica
def diver(lista):
    if len(lista) >= 6:
        return "Se cumple!"
    else:
        return "No se cumple"

#Suma de los digitos del DNI
def suma_digitos(num):
    return sum(int(digito) for digito in str(num))


#Operaciones con años de nacimiento

def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def ingresar_anios():
    anios = []
    n = int(input("¿Cuántos integrantes hay en el grupo? "))
    for i in range(n):
        anio = int(input(f"Ingrese el año de nacimiento del integrante {i+1}: "))
        anios.append(anio)
    return anios

def contar_pares_impares(anios):
    pares = sum(1 for anio in anios if anio % 2 == 0)
    impares = len(anios) - pares
    return pares, impares

def todos_post_2000(anios):
    return all(anio > 2000 for anio in anios)

def alguno_bisiesto(anios):
    return any(es_bisiesto(anio) for anio in anios)

def calcular_edades(anios, anio_actual):
    return [anio_actual - anio for anio in anios]

def producto_cartesiano(anios, edades):
    return [(anio, edad) for anio in anios for edad in edades]

