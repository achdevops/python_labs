
# inicializo mi lista de números
new_list = []

#función que me ayudara a validar si es un entero el valor
def es_entero(variable):
	try:
		int(variable)
		return True
	except:
		return False
# loop para introducir mis números
while(True):
    option = input('Ingrese Número o marque "x" para operar y salir: ')
    print("número a insertar es:" ,option)

    #válido la salida del programa y calculo del mejor
    if option == "X" or option == "x":
        print("Lista de enteros introducidos:",new_list)

        #ordeno mi lista de menor a mayor
        new_list.sort()

        #imprimo el menor de la lista
        print("El menor número es:",new_list[0])
        exit(1)

    elif es_entero(option):
        #agrego el número a la lista, ya realizada las validaciones
        new_list.append(option)
    else:
        print("Pelotudo, Ingresa un número entero!")