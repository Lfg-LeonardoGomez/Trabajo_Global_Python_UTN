import os

import Detector,Radiacion
class menu:
    adn=["aaaatc","tacgag","ttatga","tatgcc","tggtac","ggtaaa"]
    analizar=Detector.Detector(adn)
    def __init__(self):
        pass


    def menu_inicio(self):

        print("------Bienvenido al Programa de deteccion de mutaciones------\n\n\n"
             
                "Para iniciar necesita una muestra de ADN... \n"
                "seleccione una de las siguientes opciones: \n"
                "1-ingresar una muestra manualmente\n"
                "2-usar la muestra pre-guardada\n")

        while True:
            opcion=input()
            if opcion=="1":
                self.guardar_ADN()
                break
            elif opcion=="2":
                self.mostrar_ADN()
                break
            else:
                    print("opcion invalida, por favor una de las siguientes opciones...\n"
                        "1-ingresar una muestra manualmente\n"
                        "2-usar la muestra pre-guardada\n")

    def menu_acciones(self):
        while True:
            opcion=input("\nseleccione una de las siguientes opciones para su muestra de ADN: \n"
              "1-Detectar mutaciones...\n"
              "2-Generar una mutacion por radiacion...\n"
              "3-Generar una mutacion por virus...\n"
              "4-Sanar mutacion...\n")
            if opcion not in "1234":
                print("opcion no valida, por favor ingrese una de las siguientes opciones...\n")
            elif opcion=="1":
                print(self.analizar.detectar_mutantes(self.adn))
                break
            elif opcion=="2":
                self.crear_mutacion_radiacion()
                break

    def guardar_ADN(self):
        fila=0
        print("Por favor ingrese una muestra de ADN...\n"
              "A=adenina T=timina C=citocina G=guanina\n")

        while fila<6:
            string=input(f"ingrese los 6 caracteres de la fila {fila+1}:  ")
            self.adn[fila]=string
            fila+=1
        self.mostrar_ADN()

    def mostrar_ADN(self):
        
        print("\n------ADN ingresado------  \n")
        for i in range(len(self.adn)):
            for j in range(len(self.adn[i])):
                print("[",self.adn[i][j],"]",end="")

            print()

    def crear_mutacion_radiacion(self):
        base_nitrogenada=input("\nIngrese la base nitrogenada con la que desea mutar: ")
        print("\ningrese las coordenas para el inicio de la mutacion:")
        posicion_inicial_fila=int(input("\nFila: "))
        posicion_inicial_columna=int(input("\nColumna: "))
        orientacion=input("\nOrientacion: v/h (vertical/Horizontal")
        mutar_por_mutacion=Radiacion.Radiacion(base_nitrogenada,self.adn,
                                               [posicion_inicial_fila,posicion_inicial_columna],orientacion)
        mutar_por_mutacion.crear_mutante()