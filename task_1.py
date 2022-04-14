class DoorWithCodeLock():
    def __init__(self, code):
        self._code = code
        self._isOpen = False
        print("Вы поставили код на дверь: " + str(self._code))

    def Open(self, code):
        if(self._code == code):
            self._isOpen = True
            print("Дверь открылась")
        else:
            print("Неверный код")

    def Close(self, code):
        if(self._isOpen):
            self._code = code
            self._isOpen = False
            print("Дверь закрылась")
        else:
            print("Дверь не открыта")

    def CheckLock(self):
        if(self._isOpen):
            print("Дверь сейчас открыта")
        if(not self._isOpen):
            print("Дверь сейчас закрыта")

def test():
    myNewDoor = DoorWithCodeLock(1234)
    myNewDoor.Open(234)
    myNewDoor.CheckLock()
    myNewDoor.Open(1234)
    myNewDoor.CheckLock()
    myNewDoor.Close(5233)
    myNewDoor.CheckLock()
    myNewDoor.Open(1234)
    myNewDoor.CheckLock()
    myNewDoor.Open(5233)
    myNewDoor.CheckLock()

test()
