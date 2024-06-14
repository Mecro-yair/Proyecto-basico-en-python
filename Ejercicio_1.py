nombre=input("INGRESE EL NOMBRE DEL ALUMNO:\n")
nota1= float(input("Digite su primera calificación:\n"))
nota2= float(input("Digite su primera calificación:\n"))
nota3= float(input("Digite su tercera calificación:\n"))

promedio = (nota1+ nota2 +nota3)/3
#se agregó entrada y salida de nombre del estudiante
print(nombre)
#Se agregó una validación de notas
#Se actualizó la condicional de notas
if nota1>=0 and nota1<=20 and nota2>=0 and nota2<=20 and nota3>=0 and nota3<=20:
    if promedio >=10.5 :
        print("Aprobo el curso ")
    else:
        print("Reprobo el curso ")
else:
    print("ERROR!_NUMBER")
