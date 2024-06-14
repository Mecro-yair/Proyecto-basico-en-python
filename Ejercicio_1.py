nota1= float(input("Digite su primera calificación:\n"))
nota2= float(input("Digite su primera calificación:\n"))
nota3= float(input("Digite su tercera calificación:\n"))
promedio = (nota1+ nota2 +nota3)/3
#Se agrego una validacion de notas
if nota1>=0 and nota2>=0 and nota3>=0:
    if promedio >=70 :
        print("Aprobo el curso ")
    else:
        print("Reprobo el curso ")
else:
    print("ERROR!_INVALID_NEGATIVE_NUMBER")
