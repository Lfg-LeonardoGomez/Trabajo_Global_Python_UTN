class Mutador:
    base_nitrogenada=""
    posicion_inicial=[]
    adn=[]

    def __init__(self, base_nitrogenada,adn,posicion_inicial):
        self.base_nitrogenada = base_nitrogenada
        self.adn = adn
        self.posicion_inicial = posicion_inicial
    def crear_mutante(self):
        pass

    def mostrar_ADN(self):
        for i in range(len(self.adn)):
            for j in range(len(self.adn[i])):
                print("[",self.adn[i][j],"]",end="")

            print()

