#--------------------CALCULADORA SIMPLE--------------------------------#
# 01/09/2021
# Eddie Casañas
# Santiago, Chile
# JAVA PORT
#----------------------------------------------------------------------#

import PlantillaCalculadora as p
obj = p.Calculadora


while True:
	while True:
		print("\n(1): Suma")
		print("(2): Resta")
		print("(3): Multiplicacion")
		print("(4): Division")
		print("(5): Exponente")
		print("(6): Raiz cuadrada")
		print("(7): Salir")
		
		try:
			opcion = int(input())
			if opcion < 1 or opcion > 7:
				print("\nIngrese una opcion valida\n")
				continue
			else:
				break
		except:
			print("\nIngrese una opcion valida\n")
			continue
		
	if opcion == 1:
		salida = 0
		while salida != 2:
			obj.suma()
			salida = obj.repetir()
				
	elif opcion == 2:
		salida = 0
		while salida != 2:
			obj.resta()
			salida = obj.repetir()
				
	elif opcion == 3:
		salida = 0
		while salida != 2:
			obj.multiplicacion()
			salida = obj.repetir()
				
	elif opcion == 4:
		salida = 0
		while salida != 2:
			obj.division()
			salida = obj.repetir()
				
	elif opcion == 5:
		salida = 0
		while salida != 2:
			obj.exponente()
			salida = obj.repetir()
				
	elif opcion == 6:
		salida = 0
		while salida != 2:
			obj.raizCuadrada()
			salida = obj.repetir()
				
	elif opcion == 7:
		break
					
