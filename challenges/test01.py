new_list = []

def es_entero(variable):
	try:
		int(variable)
		return True
	except:
		return False

while(True):
    option = input('Ingrese Número o marque "x" para operar y salir: ')
    print("número a insertar es:" ,option)
    if option == "X" or option == "x":
        print("Lista de enteros introducidos:",new_list)
        new_list.sort()
        print("El menor número es:",new_list[0])
        exit(1)
    elif es_entero(option):
        new_list.append(option)
    else:
        print("Pelotudo, Ingresa un número entero!")