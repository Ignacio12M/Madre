import Builder_neural_net.Neura as Neuron
import numpy as np
import json
import time

class Net:
    def __init__(self):
        print("nobre del archibo")
        self.__DataBuilJson = input()
        self.__layer = []
        self.__referen = {}
        self.__Error = None
        self.__Cicle_train = None
        with open(self.__DataBuilJson) as file:
            self.__dataBuild = json.load(file)

        if (self.__dataBuild["new"] == True):
            self.__BuiderNewNet()
        else:
            self.__BuiderNet()

    def __BuiderNewNet(self):
        for layer in self.__dataBuild["layers_data"]:
            neurons = []
            for neurona in layer:
                neuron = Neuron(neurona["syze_inputs"], neurona["function"], neurona["memory"])
                neurons.append(neuron)

                self.__referen[neuron] = [neurona["pos_data_imput"], neurona["references_inputs"]]
            self.__layer.append(neurons)

        #creo las referencias
        for layer in self.__layer:
            for neuron in layer:

                for referencias in self.__referen[neuron][1]:
                    self.__referen[neuron][1].append( [ self.__layer[referencias[0]][referencias[1]],
                                                        referencias[2] ] )
                    del self.__referen[neuron][1][0]


    def __BuiderNet(self):
        for layer in self.__dataBuild["layers_data"]:
            neurons = []
            for neurona in layer:
                neuron = Neuron(neurona["syze_inputs"], neurona["function"], neurona["memory"])
                neuron._w = neurona["w"] # Guado el peso de la neurona
                neuron._b = neurona["b"] # Guarda la balla
                neurons.append(neuron)

                self.__referen[neuron] = [neurona["pos_data_imput"], neurona["references_inputs"]]
            self.__layer.append(neurons)

        #creo las referencias
        for layer in self.__layer:
            for neuron in layer:

                for referencias in self.__referen[neuron][1]:
                    self.__referen[neuron][1].append( [ self.__layer[referencias[0]][referencias[1]],
                                                        referencias[2] ] )
                    del self.__referen[neuron][1][0]

    '''
    def Guadar(self):
        print("Crear copia antes de sobre escribir ?  (Y/N)")
        pregunta = input()

        if pregunta == 'Y':
            with open('Copia.json', 'w') as file:
                json.dump(self.__dataBuild, file)

        print("Comentario: ")
        comen = input()

        self.__dataBuild["descriptions"] = str(comen)
        self.__dataBuild["date"].update({"modificacion":{"day": time.strftime("%d/%m/%y"), "hour":time.strftime("%H:%M:%S")}})
        self.__dataBuild.update({"train": {"size": None, "error": self.__Error, "cicles": self.__Cicle_train}})

        datos_capa = []
        contador = 0
        for layer in self.__layer:
            datos_capa.append(len(layer))
            contador_aux = 0
            for neurona in layer:
                self.__dataBuild["layers_data"][contador][contador_aux].update(neurona._data())
                contador_aux +=1
            contador +=1

        self.__dataBuild["data_characteristics"].update({"layers_lengths": datos_capa, "data_type": None, })

    '''

