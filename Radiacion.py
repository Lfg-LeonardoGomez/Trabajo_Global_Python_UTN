from Mutador import Mutador


class Radiacion(Mutador):
    orientacion=""
    fila=0
    columna=0
    def __init__(self, base_nitrogenada,adn,posicion_inicial,orientacion):
        super().__init__(base_nitrogenada,adn,posicion_inicial)
        self.orientacion = orientacion


    def crear_mutante(self):
        if self.orientacion=="h":
            self.crear_mutante_horizontal()
        elif (self.orientacion=="v"):
            self.crear_mutante_vertical()

    def crear_mutante_horizontal (self):
        fila,columna=self.posicion_inicial
        fila_modificada=list(self.adn[fila])
        for i in range(4):
            fila_modificada[columna+i]=self.base_nitrogenada

        self.adn[fila] = ''.join(fila_modificada)

        self.mostrar_ADN()

    def crear_mutante_vertical(self):
        fila,columna = self.posicion_inicial

        for i in range(4):
            fila_modificada = list(self.adn[fila + i])
            fila_modificada[columna] = self.base_nitrogenada
            self.adn[fila + i] = ''.join(fila_modificada)

        self.mostrar_ADN()