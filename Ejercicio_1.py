import os

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
"""
Se agregó una validación de notas
Se actualizó la condicional de notas
se agregó entrada y salida de nombre del estudiante
Se optimizo el codigo añadiendo una funciones
Se agrego un bucle para preguntar si se desea continuar con el programa
"""
#Bucle pregunta
while True:
    nombre=input("INGRESE EL NOMBRE DEL ALUMNO:\n")
    nota1= float(input("Digite su primera calificación:\n"))
    nota2= float(input("Digite su primera calificación:\n"))
    nota3= float(input("Digite su tercera calificación:\n"))
    #Almaceno funciones
    promedio= Promedio(nota1,nota2,nota3)
    base20=calificacion_en_base20(nota1,nota2,nota3)
    if base20==True:
        if promedio >=10.5 :
            print(nombre)
            print("Aprobo el curso ")   
        else:
            print("Reprobo el curso ")       
    else:
        input(print("ERROR!_NUMBER"))
        exit(0)
    
    quest=input("Continuar con otro alumno? si/no:\n")
    
    if quest!="si":
        input(print("FIN DEL PROGRAMA"))
        exit(0)
    clear_screen()