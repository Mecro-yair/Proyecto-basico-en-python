import os
from time import sleep

def clear_screen():
    # Comando para limpiar la pantalla en Windows
    os.system('cls')
def Promedio(x,y,z):
    promedio = (x+ y +z)/3
    return promedio

def calificacion_en_base20(x,y,z):
    if 0<=x and x<=20 and 0<=y and y<=20 and 0<=z and z<=20:
        cumple_base20= True
    else:
        cumple_base20=False
    return cumple_base20

def notas_porcentaje(c,p,d,pc,pp,pd):
    nc=c*pc/100
    np=p*pp/100
    nd=d*pd/100
    nf=nc+np+nd
    return nf
def validación_nota(q,e,n,):
    if q>=0 and q>=20 and e>=0 and e<=20 and n>=0 and n<=20:
        Cumple_base20=True
    else:
        Cumple_base20=False
    return Cumple_base20   
            
"""
Se agregó una validación de notas
Se actualizó la condicional de notas
se agregó entrada y salida de nombre del estudiante
Se optimizo el codigo añadiendo una funciones
Se agrego un bucle para preguntar si se desea continuar con el programa
Se agrego un menu de opciones
se agrego la opcion "Calcular promedio ponderado"
se soluciono un problema al ingresar un numero invalido en el promedio de 3 notas
"""
#Menu de opciones
while True:
    clear_screen()
    #Validacion de entrada
    try:
        print("MENU DE OPCIONES\n1.Calcular el promedio de 3 notas.\n2.Calcular promedio ponderado.\n3.Salir.")
        op=int(input("\n*Elija una opción\n"))
        if op==1:
            clear_screen()
            #Bucle pregunta
            while True:
                clear_screen()
                print("PROMEDIO DE 3 NOTAS")
                nombre=input("INGRESE EL NOMBRE DEL ALUMNO:\n")
                nota1= float(input("Digite su primera calificación:\n"))
                nota2= float(input("Digite su primera calificación:\n"))
                nota3= float(input("Digite su tercera calificación:\n"))
                #Almaceno funciones
                promedio=Promedio(nota1,nota2,nota3)
                base20=calificacion_en_base20(nota1,nota2,nota3)
                if base20==True:
                    if promedio>=10.5:
                        print(nombre)
                        print("Aprobó el curso ")   
                    else:
                        print(nombre)
                        print("Reprobó el curso ")       
                else:
                    print("ERROR!_NUMBER")
                quest=input("Continuar? si/no:\n")
                if quest!="si":
                    break
        if op==2:
            #Bucle pregunta
            while True:
                clear_screen()
                print("PROMEDIO PONDERADO")
                nombre=input("INGRESE EL NOMBRE DEL ALUMNO:\n")
                porcent_C=float(input("Ingrese el Porcentaje de la nota de Conocimiento:\n"))
                nota_C= float(input("Digite su nota de conocimiento:\n"))
                porcent_P=float(input("Ingrese el Porcentaje de la nota de Producto:\n"))
                nota_P= float(input("Digite su nota de producto:\n"))
                porcent_D=float(input("Ingrese el Porcentaje de la nota de Desempeño:\n"))
                nota_D= float(input("Digite su nota de desempeño:\n"))
                #Agregando validación de entrada de nota
                valida=validación_nota(nota_C, nota_D, nota_P)
                if valida==True:
                    
                #Almacena 
                    Nota_Final=notas_porcentaje(nota_C,nota_P,nota_D,porcent_C,porcent_P,porcent_D)
                    if  Nota_Final>=10.5 :
                            clear_screen()
                            print(nombre)
                            print(str(Nota_Final)+" Aprobó el curso ")   
                    else:
                            clear_screen()
                            print(nombre)
                            print(str(Nota_Final)+" Reprobó el curso ")
                    quest=input("Continuar? si/no:\n")
                    if quest!="si":
                        break
                else:
                    clear_screen()
                    print("ERROR")
                    sleep(1.2)    
        if op<1 or op>3:
            clear_screen()
            print("Invalido")
            sleep(1)    
        if op==3:
            break
    except:
        clear_screen()
        print("Ingrese una opción válida")
        sleep(1)