class Radio ():
    def __init__ (self, estacion):
        self.encendido = True
        self.estacion = 88.00

    def encender (self):
        self.encender = True

    def apagar (self):
        self.apagar = False

    def estacion (self):
        while input ("Desea subir o bajar de estacion? si/no ") == "si":
            if input("¿Arriba o abajo? ") == "arriba":
                estacion = estacion + 0.5
            else :
                estacion = estacion - 0.5

            if estacion > 107.50 :
                estacion = 88.00

            if estacion < 88.00 :
                estacion = 107.50

        self.estacion = estacion
