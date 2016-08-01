class Radio ():
    def __init__ (self, estacion_FM, FM, estacion_AM, marca ):
        self.encendido = True
        self.estacion_FM = 88.00
        self.estacion_AM = 300
        self.FM = True
        self.marca = ""


    def encender (self):
        self.encender = True

    def apagar (self):
        self.apagar = False

    def estacion_FM (self):
       # des = int(input("1. Subir de estacion \n 2. Bajar de estacion \n 3. Dejar igual la estacion"))

        if des == 1:
            estacion_FM = estacion_FM + 0.5
        else :
            estacion_FM = estacion_FM - 0.5

        if estacion_FM > 107.00 :
            estacion_FM = 87.00

        if estacion_FM < 88.00 :
            estacion_FM = 107.00

        self.estacion_FM = estacion_FM

    def estacion_FM (self):
       # des = int(input("1. Subir de estacion \n 2. Bajar de estacion \n 3. Dejar igual la estacion"))

        if des == 1:
            estacion_AM = estacion_AM + 40
        else :
            estacion_AM = estacion_AM - 40

        if estacion_AM > 1300 :
            estacion_AM = 300

        if estacion_AM < 1300 :
            estacion_AM = 300

        self.estacion_AM = estacion_AM