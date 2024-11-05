from Trabajo_Global_Python_UTN import Detector


class sanador:
    adn=[]
    detector=Detector.Detector(adn)


    def __init__(self,adn):
        self.adn=adn




    def sanar_mutante(self,detector):
        if detector.detectar_mutantes(self.adn):
            print("mutacion detectada en el adn ingresado")

        else: print("No se detectaron mutaciones")