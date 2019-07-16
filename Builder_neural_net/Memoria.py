class Memory():
    def __init__(self, longitud):
        self.__pointer = 0 # Apunta a la siguiente porsicion libre
        self.__memory = []
        self._length = longitud

        if type(longitud) == int:
            for i in (self.__length):
                self.__memory[i] = 0
        else:
            self.__memory = longitud
            self._length = len(longitud)

    @property
    def memoria(self):
        return list(reversed(self.__memory))


    @memoria.setter
    def memoria(self, data):
        self.__memory.append(data)
        del self.__memory[0]
