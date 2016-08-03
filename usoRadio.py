from radio import Radio
radio1 = Radio("Sony")
continuar = int(input("Quieres usar el radio? \n 1. Si \n 2. No "))
if continuar == 1:
	continuar = True
else: 
	continuar = False
	print ("Adios!")

radio1.encendido = False
while continuar == True:
	if radio1.encendido == True:
		des = int(input(" 1. Subir volumen \n 2. Bajar volumen \n 3. Subir estacion \n 4. Bajar estacion \n 5. Cambiar frecuencia \n 6. Apagar "))

		if des == 1:
			radio1.subir_volumen

		elif  des == 2:
			radio.bajar_volumen

		elif des == 3:
			radio1.subir_estacion 

		elif des == 4:
			radio1.bajar_estacion

		elif des == 5:
			if en_FM == True:
				radio1.en_AM
			else:
				radio1.en_FM
		elif des == 6:
			if encendido == True:
				radio1.apagar
			else:
				radio1.encender 
	else: 
		en = int(input("1. Encender \n2. Salir "))

		if en == 1:
			radio1.encendido = True
		else:
			continuar = False




