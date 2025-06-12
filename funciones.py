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

