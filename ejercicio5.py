# Codigo para extraer subtrings y convertilo a número

cadena = "El dia 5 de octubre sali de vacaciones"
subcadena= cadena[12:19]
 #Toma los espacios como letras, por lo cual se debe saber la posicion de la letra que queremos saber
print (subcadena + " tiene " + str(len(subcadena)) + " letras")
