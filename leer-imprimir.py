try:
    archivo = input ("Ingrese el nombre del archivo: ")
    fhandle = open(archivo, "r") 
    # la letra "r" me indica que me va imprimir documentos, es decir, letras
    for linea in fhandle:
        print(linea.upper())
except:
    print ("Error, archivo no existente")
