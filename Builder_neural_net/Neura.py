import numpy as np
import Builder_neural_net.Memoria.Memory
import Net.Functions

class Neuron:

    def __init__(self, entradas, funcion, length_memory):
        #Las recurrencia se definen como entradas a 1 (Memoria) la relaciones exteranas a capas superiores de relacionan como
        #una tupla (capa,neurona)

        # entradas almacena el parametro de entrada de la neurona
        self._w = np.random.rand(entradas) #gennera un array de numeros rando en relacion con la entrada.
        self._b = np.random.rand() #genera un solo numero random
        self.__funcion = Net.Functions.setFuncion(funcion) #Almacena la funcion de actibacion de la neura
        self._memory = Net.Memory(length_memory)
        self._error = None
        self._live = True

    def correccion(self, erro):
        self._w = erro[0]
        self._b = erro[1]

    def calcular(self, dataInt):
        value = self.__funcion[0](dataInt @ self._w + self._b)
        self.__insertMemory(value)
        return  value

    def __insertMemory(self, value):
        self._memory = value


    def _data(self):
        return {"syze_inputs": len(self._w),
                "memory": self._memory,
                "weight": self._w,
                "balla": self._b,
                }
