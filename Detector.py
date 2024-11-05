class Detector:
    adn = []
    cantidad_mutaciones = 0
    resultado = False

    def __init__(self, adn):
        self.adn = adn
        #self.mostrar_ADN()


    def detectar_mutantes(self,adn):
        self.detectar_diagonal_principal()
        self.detectar_horizontal()
        self.detectar_vertical()
        return self.resultado

    def detectar_horizontal(self):
        for fila in self.adn:
            if self.buscar_mutante(fila):
                self.cantidad_mutaciones += 1
                self.resultado = True
        return self.resultado

    def detectar_vertical(self ):
        muestra=""
        for i in range(6):
            for j in range(6):
                muestra+=muestra.join(self.adn[j][i])
            if self.buscar_mutante(muestra):
                self.cantidad_mutaciones += 1
                self.resultado = True
            muestra =""
        return self.resultado

    def detectar_diagonal_principal(self):
        muestra=""
        for i in range(3):
            for j in range(3):
                for k in range(4):
                    muestra+=muestra.join(self.adn[i+k][j+k])

                if self.buscar_mutante(muestra):
                    self.cantidad_mutaciones += 1
                    self.resultado = True
                muestra =""
        return self.resultado

    def buscar_mutante(self,fila):

        letras = "acgt"
        for letra in letras:
            if letra * 4 in fila:  # Verifica si la letra aparece 4 veces seguidas
                return True

        return False

    def mostrar_ADN(self):
        print("------------------------------------")
        print("Muestra de ADN ingresada")
        print("------------------------------------")
        for i in range(len(self.adn)):
            for j in range(len(self.adn[i])):
                print("[",self.adn[i][j],"]",end="")

            print()