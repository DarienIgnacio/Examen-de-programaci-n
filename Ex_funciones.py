import random
import csv
def menu(titulo,lista):
    print('========================================')
    print(titulo.upper())
    print('========================================')
    while True:
        i=1
        for elem in lista:
            print(i,'.-',elem)
            i+=1
        print(i,'.- Salir')
        opc=input('Ingrese Opción: ')
        if opc.isdigit():
            opc_int=int(opc)
            if opc_int>=1 and opc_int<=i:
                return opc_int
            else:
                print('Debe Ingresar un Número entre 1 y ',i)
        else:
            print('Ingrese Sólo Números')

def sueldos_ale(nombres):
    sueldos=[]
    cantidad=10
    for i in range(cantidad):
        numero=random.randint(300000,2500000)
        sueldos.append(numero)
    trabaj=list(zip(nombres,sueldos))
    return trabaj

trabajadoes=['Juan Peres','Maria Garcia','Carlos Lopez','Ana Martinez','Pedro Rodriguez','Laura Hernandez','Miguel Sanchez','Isabel Gomez','Francisco Diaz','Elena Fernandes']
sueldo_empleados=sueldos_ale(trabajadoes)
