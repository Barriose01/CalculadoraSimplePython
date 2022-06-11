#--------------------Plantilla Calculadora-----------------------------#
# 01/09/2021
# Eddie Casañas
# Santiago, Chile
# JAVA PORT
#----------------------------------------------------------------------#


class Calculadora:
	def suma():
		while True:
			print("\nIngrese el primer numero: ")
			try:
				numero1 = float(input())
			except:
				print("\nIngrese un numero valido")
				continue
			print("Ingrese el segundo numero: ")
			try:
				numero2 = float(input())
				suma = numero1 + numero2
				print("\n" + str(numero1) + " + " + str(numero2) + " = " 
				+ str(suma))
				break
			except:
				print("\nIngrese un numero valido")
	
	
	def resta():
		while True:
			print("\nIngrese el primer numero: ")
			try:
				numero1 = float(input())
			except:
				print("\nIngrese un numero valido")
				continue
			print("Ingrese el segundo numero: ")
			try:
				numero2 = float(input())
				resta = numero1 - numero2
				if numero2 < 0:
					print("\n" + str(numero1) + " - (" + str(numero2) 
					+ ") = " + str(resta))
					break
				else:
					print("\n" + str(numero1) + " - " + str(numero2) 
					+ " = " + str(resta))
					break
			except:
				print("\nIngrese un numero valido")
	
	
	def multiplicacion():
		while True:
			print("\nIngrese el primer numero: ")
			try:
				numero1 = float(input())
			except:
				print("\nIngrese un numero valido")		
				continue	
			print("Ingrese el segundo numero: ")
			try:
				numero2 = float(input())
				multiplicacion = numero1 * numero2
				print("\n" + str(numero1) + " * " + str(numero2) + " = " 
				+ str(multiplicacion))
				break
			except:
				print("\nIngrese un numero valido")
				
				
	def division():
		while True:
			print("\nIngrese el primer numero: ")
			try:
				numero1 = float(input())
			except:
				print("\nIngrese un numero valido")
				continue
			print("Ingrese el segundo numero: ")
			try:
				numero2 = float(input())
				if numero2 == 0 or numero2 == 0.0:
					print("\nNo se puede dividir entre 0")
					continue
				else:
					division = numero1 / numero2
					print("\n" + str(numero1) + " / " + str(numero2) 
					+ " = " + str(division))
					break
			except:
				print("\nIngrese un numero valido")
				
				
	def exponente():
		while True:
			print("\nIngrese el primer numero: ")
			try:
				numero1 = float(input())
			except:
				print("\nIngrese un numero valido")
				continue
			print("Ingrese el exponente: ")
			try:
				exponente = float(input())
				resultado = (numero1 ** exponente)
				print("\n" + str(numero1) + " ^ " + str(exponente) 
				+ " = " + str(resultado))
				break
			except:
				print("\nIngrese un numero valido")
				
				
	def raizCuadrada():
		while True:
			print("\nIngrese el numero: ")
			try:
				numero = float(input())
				if numero < 0:
					print("\nIngrese solo numeros positivos")
					continue
			except:
				print("\nIngrese un numero valido\n")
				continue
			try:
				raiz = numero ** (1/2)
				print("\nLa raiz cuadrada de " + str(numero) + " es: " 
				+ str(raiz))
				break
			except:
				print("\nError en el calculo")
				
				
	def repetir():
		while True:
			print("\n(1): Repetir")
			print("(2): Volver al menu principal")
			opcion = input()
			if opcion.strip() != "1" and opcion.strip() != "2":
				print("\nIngrese una opcion valida")
				continue
			elif opcion.strip() == "1":
				return 1
			elif opcion.strip() == "2":
				return 2
				



				

			
