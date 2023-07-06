import numpy as np
from usuario import *
from funciones import *
ciclo= True


llenar(arreglo)


while ciclo:


    print("BIENVENIDOS AL MENU CREATIVOS")
    print("-------------------------------")
    print("1)comprar entrada")
    print("2)mostrar ubicaciones disponibles")
    print("3)ver listado de los asistentes")
    print("4)mostrar ganancias")
    print("5)salir")
    try:
        op=int(input("seleccione del 1 al 5"))
        match op:
            case 1:
                print("comprar")
                comprarEntrada(arreglo,lista_usuarios)
            case 2:
                print("lista de ubicaciones disponibles")
                lista_usuarios(arreglo)
            case 3:
                print("lsita de asistentes")
                lista_usuarios(lista_usuarios)
            case 4:
                print("mostrar ganancias totales ")
                totales(lista_usuarios)
            case 5:
                print("salir")
                salir()
            case _:
                ciclo= salir()

    except BaseException as error:
        print(f"ERROR{error}")