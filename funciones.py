import numpy as np
from usuario import *
arreglo = np.full((10,10),'---')
lista_usuarios=[]

def llenar (arreglo):
    x=0
    for f in range(10):
        for c in range(10):
            x = x+1
            arreglo[f][c]=str(x)

def mostrar(arreglo):
    for f in range(10):
        fila=''
        for c in range(10):
            fila=fila+'  '+arreglo[f][c]
        print(fila)


def comprarAsiento(arreglo,num_asiento):

    x=0
    for f in range(10):
        for c in range(10):
            x = x + 1
            if str(x) == str(num_asiento):
                arreglo[f][c]='XX'
def comprobar(arreglo,num_asiento):
    x=0
    for f in range(10):
        for c in range(10):
            x=x+1
            if str(x)== str(num_asiento):
                if arreglo[f][c]=='XX':
                    return False
    return True
def agregar(lista_usuario,num_asiento):
    c = usuario()
    c.run = int(input("ingrese el run sin guion"))
    c.num_asiento = num_asiento
    if num_asiento>=1 and num_asiento<=20:
        c.valor=120000
    if num_asiento>=21 and num_asiento<=50:
        c.valor=80000
    if num_asiento>=51 and num_asiento<=100:
        c.valor=50000
    else:
        print("entrada comprada con exito")
    lista_usuario.append(c)

def comprarEntrada(arreglo,lista_usuarios):
    try:
        cantidad = int(input("ingrese la cantidad de entradas(1-3)"))
        if cantidad >=1 and cantidad <=3:
            comprarAsiento = 0
            while comprarAsiento < cantidad:
                mostrar(arreglo)
                num_asiento = int(input("seleccione el asiento"))
                if num_asiento>=1 and num_asiento <= 100:
                    disponible = comprobar(arreglo,num_asiento)
                    if disponible==True:
                        agregar(lista_usuarios,num_asiento)
                        comprarAsiento(arreglo,num_asiento)
                        comprarAsiento = comprarAsiento + 1
                    else:
                        print("no valido")

                else:
                    print("asiento desde e 1 al 100")
        else:
            print("ubicacion erronea")
    except BaseException as error:
        print(f"error{error}")

def listaEntrada(lista_usuario):
    for usuario in lista_usuario:
        print(f"run :{usuario.run}")
        print(f"valor :{usuario.valor}")
        print(f"n° asiento :{usuario.num_asiento}")
        print("####################################")

def totales(lista_usuario):
    platinum=0
    gold=0
    silver=0
    total_platinum=0
    total_gold=0
    total_silver=0
    for pa in lista_usuario:
        if int(pa.valor)==120000:
            platinum=platinum+1
            total_platinum=total_platinum + 120000
        if int(pa.valor)==80000:
            gold=gold+1
            total_gold=total_gold + 80000
        if int(pa.valor)==50000:
            silver=silver+1
            total_silver=total_silver + 50000
    print(f"platinum: cantidad platinum: {platinum}total:platinum{total_platinum}")
    print(f"gold : cantidad gold : {gold}total:gold{total_gold}")
    print(f"silver : cantidad silver  : {silver}total:gold{total_silver}")
    total= total_platinum + total_gold + total_silver
    print(f"total general :${total}")
def salir():
    print("Carlo Apeleo_PGY1121_002_D fecha 6/07/2023")
