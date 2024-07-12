import random
from random import randint
import csv
separador=("=======================================================================")
trabajadores=["Juan Pérez","María García,","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernandez","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
trabajador=[]
promediosueldo=0
for t in trabajadores:
    trabajador.append({"Nombre Trabajador":t,"Sueldo Bruto":randint(300000, 2500000)})

def asignar_sueldos():
    for i in range(len(trabajador)):
        print(f"{trabajador[i]}")
        print(separador)
    
    return trabajador

def clasificar_sueldos():
    menores= [(trabajador[i],
            trabajador[i]) 
            for i in range(len(trabajador)) 
            if trabajador[i] < 800000]
    medio= [(trabajador[i],
            trabajador[i]) 
            for i in range(len(trabajador))
            if 800000 <= trabajador[i] <= 2000000]
    mayores= [(trabajador[i],
            trabajador[i])
            for i in range(len(trabajador))
            if trabajador[i] > 2000000]
    
    print(f"Sueldos menores a $800.000\nTOTAL: {len(menores)}")
    for trabajador, sueldo in menores:
        print(f"{trabajador}: ${sueldo}")
        print(separador)
        
    print(f"Sueldos entre $800.000 a $2.000.000\nTOTAL: {len(medio)}")
    for trabajador, sueldo in medio:
        print(f"{trabajador}: ${sueldo}")
        print(separador)
        
    print(f"Sueldos superiores a $2.000.000\nTOTAL: {len(mayores)}")
    for trabajador, sueldo in mayores:
        print(f"{trabajador}: ${sueldo}")
        print(separador)


def ver_estadistica():
    try:
        while True:
            print("1. Sueldo más bajo")
            print("2. Sueldo más alto")
            print("3. Promedio de sueldos")
            print("4. Media geométrica")
            print("5. Volver al menú")
            op1=int(input("Ingrese una de las opciones\n> "))
            
            match op1:
                case 1:
                    sueldomasbajo=min.trabajador[i]
                    print(f"El sueldo más bajo es: ${sueldomasbajo}")
                case 2:
                    sueldomasalto=max.trabajador[i]
                    print(f"EL sueldo mas alto es: {sueldomasalto}")
                case 3:
                    promediosueldos=trabajador[i]/10
                case 5:
                    print("Voviendo al menú...")
                    print(separador)
                    break
                case _:
                    print("debe ingresar una opción válida")
    except ValueError:
        print("Debes ingresar un valor númerico")

descuentosalud=[]
descuentoAFP=[]
sueldoliquido=[]

def reporte_sueldos():
    with open('reporte_sueldos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado","Sueldo Base","Descuento Salud","Descuento AFP","Sueldo Líquido"])
        for i in range(len(trabajadores)):
            descuentosalud = trabajador[1]* 0.07
            descuentoAFP = trabajador[1]* 0.12
            sueldoliquido = trabajador[1]-descuentosalud-descuentoAFP
            print(f"{trabajadores[i]},${descuentosalud},${descuentoAFP},${sueldoliquido}")
    print("Se ha actualizado con éxito.")
        
while True:
    try:
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas.")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        op=int(input(f"Defina una de las opciones\n>"))
        
        match op:
            case 1:
                trabajador=asignar_sueldos()
            case 2:
                clasificar_sueldos(trabajador)
            case 3:
                ver_estadistica()
            case 4:
                reporte_sueldos()
            case 5:
                print("Finalizando programa...")
                print("desarrollador por: Tomás Ponce")
                print("RUT 22.070.650-8")
                break
            case _:
                print("Debes ingresar una opción válida")
                print(separador)
    except ValueError:
        print("debes ingresar un valor númerico")
        