import random, csv
import Ex_funciones as f 

while True:
    opc=f.menu('menu principal',['Asignar sueldos aleatorios','Clasificar sueldos','Ver estadìsticas','Reporte de sueldos'])
    if opc==1:
        print(f.sueldo_empleados)
    elif opc==2:
        print('\n''Sueldos menores a $800.000:')
        print('Nombre         Sueldo')
        for nombres,sueldo in f.sueldo_empleados:  
            if sueldo<800000:      
                print(f'{nombres}  {sueldo}')

        print('\n''Sueldos entre 800.000 y 2.000.000:')
        print('Nombre         Sueldo')       
        for nombres,sueldo in f.sueldo_empleados:     
            if sueldo>=800000 and sueldo<=2000000:             
                print(f'{nombres}  {sueldo}')

        print('\n''Sueldos superiores a 2.000.000:')
        print('Nombre         Sueldo')
        for nombres,sueldo in f.sueldo_empleados:          
            if sueldo>2000000:
                print(f'{nombres}  {sueldo}')
    elif opc==3:
        print('No hay estadisticas')
    elif opc==4:
        print('Nombre     //    Sueldo base  //  Descuento salud  //    Descuento AFP  //  Sueldo Liquido')
        for nombre, sueldo in f.sueldo_empleados:
            print(f'{nombre}  //  ${sueldo}   //    ${sueldo*0.07}  //    ${sueldo*0.12}  //  ${sueldo*0.81}')
    else:
        print('Finalizando programa')
        print('Desarrollado por Darien Urrutia')
        print('21.848.879-k')
        break
