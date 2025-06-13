from funciones import *
from datetime import datetime


def operaciones_dni():
    # Solicitud datos y obtencion de conjuntos (listas)
    dni=input("Ingrese su DNI: ")
    A=(generador_conj(dni))
    print("Conjunto A=",(A))
    dni=input("Ingrese otro DNI: ")
    B=(generador_conj(dni))
    print("Conjunto B=",(B))

    # Union
    lista_u=union(A,B)
    print("La union de los conjuntos A y B es: ",lista_u)

    # Interseccion
    lista_i=inter(A,B)
    print("La intersección de los conjuntos A y B es: ",lista_i)

    # Diferencia
    lista_d=dif(A,B)
    print("La diferencia del conjunto A respecto al B es: ",lista_d)

    # Diferencia Simetrica
    lista_ds=difsim(A,B)
    print("La diferencia simetrica de los conjuntos A y B es: ",lista_ds)

    # Conteo repeticion de digitos en numero ingresado
    print("En esta parte del programa se cuenta las veces que se repiten los digitos en un numero")
    dni=(int(input("Ingrese el numero de su DNI: ")))
    print("Se muestra la cantidad de veces que se repite cada digito: ")
    print(rep_dig(dni))

    # Conteo de cantidad de digitos que posee un numero
    print("Ahora vamos a contar cuantos digitos posee un numero")
    dni=(input("Ingrese el numero de su DNI: "))
    print(f"El numero de DNI {dni} posee {conteo_dig(dni)} digitos")

    # Suma total de digitos que posee un numero
    print("Ahora vamos a sumar los digitos posee el numero")
    dni=(input("Ingrese el numero de su DNI: "))
    print(f"La suma total de los digitos del DNI {dni} es {suma_digitos(dni)}")

    # Evaluacion de condicion si el conjunto generado a partir de un DNI posee diversidad numerica
    print("En este apartado veremos si se cumple la condicion de diversidad numerica en un conjunto")
    dni=input("Ingrese un DNI: ")
    A=(generador_conj(dni))
    print("Conjunto A=",(A))
    print(f"La condicion {diver(A)}")


#Calculos con años de nacimiento

def operaciones_anios():
    anios = ingresar_anios()
    pares, impares = contar_pares_impares(anios)
    print(f"Nacidos en años pares: {pares}")
    print(f"Nacidos en años impares: {impares}")

    if todos_post_2000(anios):
        print("Grupo Z")
    if alguno_bisiesto(anios):
        print("Tenemos un año especial")

    actual = datetime.now().year
    edades = calcular_edades(anios, actual)
    print("Edades actuales:", edades)

    print("Producto cartesiano (Año, Edad):")
    for par in producto_cartesiano(anios, edades):
        print(par)

#Menu de ejecucion del programa

def menu():
    print("Seleccione una opcion:")
    print("1. Operaciones con conjuntos de DNI")
    print("2. Operaciones con años de nacimiento")
    print("3. Salir")
    opcion = input("Ingrese su opcion: ")
    return opcion


if __name__ == "__main__":
    print("Bienvenido al TP Integrador II de Matematica")
    while True:
        opcion = menu()
        if opcion == "1":
            operaciones_dni()
        elif opcion == "2":
            operaciones_anios()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opcion invalida. Intente nuevamente.")