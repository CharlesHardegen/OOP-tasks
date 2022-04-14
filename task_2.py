class Glass():
    def __init__(self, volume):
        if(not type(volume) == int):
            return
        self._volume = volume
        self._liquidVolume = 0
        print("Стакан проинициализирован с объемом: " + str(self._volume))

    @property
    def liquidVolume(self):
        return self._liquidVolume
    
    @liquidVolume.setter
    def liquidVolume(self, value):
        if(not type(value) == int):
            self._liquidVolume = value

        if(value > self._volume):
            self._liquidVolume = self._volume
            print("Пролито: ", str(value - self._volume))
        elif(value < 0):
            print("Вылито все: -", self._liquidVolume)
            self._liquidVolume = 0
        elif(value < self._liquidVolume):
            print("Вылито: ", self._liquidVolume - value)
            self._liquidVolume = value
        else:
            print("Налито: ", value - self._liquidVolume)
            self._liquidVolume = value


    def pourInto(self, value):
        self.liquidVolume += value

    def pourFrom(self, value):
        self.liquidVolume -= value
    
    def printLiquidVolume(self):
        print("Объем жидкости: ", self.liquidVolume)
    
def test():
    myGlass = Glass(20)
    myGlass.pourInto(10)
    myGlass.printLiquidVolume()
    myGlass.pourInto(10)
    myGlass.printLiquidVolume()
    myGlass.pourInto(10)
    myGlass.printLiquidVolume()
    myGlass.pourFrom(10)
    myGlass.printLiquidVolume()
    myGlass.pourFrom(10)
    myGlass.printLiquidVolume()

test()

