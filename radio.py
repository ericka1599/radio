class Radio ():
    def __init__ (self, marca ):
        self.encendido = True
        self.estacion_FM = 88.00
        self.estacion_AM = 300
        self.en_FM = True
        self.marca = ""
        self.volumen = 0


    def encender (self):
        self.encendido = True
        return "Encendido"

    def apagar (self):
        self.encendido = False
        return "Apagado"

    def en_FM (self):
        self.en_FM  = True
        return "En FM"

    def en_AM (self):
        self.en_FM  = False
        return "En AM"

    def subir_estacion (self):
        if en_FM == True:
            estacion_FM = estacion_FM + 0.5

            if estacion_FM > 107.00 :
                estacion_FM = 87.00

            estacion_FM = estacion_FM
            print ("La emisora es " + estacion_FM)

        else: 
            estacion_AM = estacion_AM + 40

            if estacion_AM > 1300 :
                estacion_AM = 300

            estacion_AM = estacion_AM
            print ("La emisora es " + estacion_AM)

    def bajar_estacion (self):
        if en_FM == True:
            estacion_FM = estacion_FM - 0.5

            if estacion_FM < 88.00 :
                estacion_FM = 107.00

            self.estacion_FM = estacion_FM
            print ("La emisora es " + estacion_FM)

        else:
            estacion_AM = estacion_AM - 40
            if estacion_AM < 1300 :
                estacion_AM = 300

            self.estacion_AM = estacion_AM
            print ("La emisora es " + estacion_AM)


    def subir_volumen (self):

        if subir_volumen == True:
            volumen = volumen + 10

            if volumen > 100:
                volumen = 100
        self.volumen = volumen 
        print ("El volumen es " + volumen)

    def bajar_volumen (self):
        if subir_volumen == False:
            volumen = volumen - 10

            if volumen < 0:
                volumen = 0
        print ("El volumen es " + volumen)


        
       