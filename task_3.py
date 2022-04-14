import math

class CoefIsNone(Exception):
    def __init__(self, coefName):
        self.coefName = coefName
 
    def __str__(self):
        return "Указано неверное значение коэффициента " + self.coefName

class QuadroEquation():
    def __init__(self, a, b, c):
        self._rootCount = 0
        self.set_coefficients(a, b, c)

    def get_a(self):
        if not hasattr(self, "_a"):
            self._a = None
        return self._a

    def set_a(self, value):
        if(not type(value) == float and not type(value) == int):
            self._a = None
            raise CoefIsNone("a")
        self._a = value

    def get_b(self):
        if not hasattr(self, "_b"):
            self._b = None
        return self._b

    def set_b(self, value):
        if(not type(value) == float and not type(value) == int):
            self._b = None
            raise CoefIsNone("b")
        self._b = value
        
    def get_c(self):
        if not hasattr(self, "_c"):
            self._c = None
        return self._c

    def set_c(self, value):
        if(not type(value) == float and not type(value) == int):
            self._c = None
            raise CoefIsNone("c")
        self._c = value
        
    def printCoefficients(self):
        print("a = ", self._a, " b = ", self._b, " c = ", self._c)
    
    def set_coefficients(self, a, b, c):
        self.set_a(a)
        self.set_b(b)
        self.set_c(c)

    def calculate(self):
        if(self._a is None or self._b is None or self._c is None):
            print("Ошибка вычисления. Проверьте значения коэффициентов")
            self.printCoefficients()
            return
        self._discr = self._b ** 2 - 4 * self._a * self._c
        if self._discr > 0:
            self._x1 = (-self._b + math.sqrt(self._discr)) / (2 * self._a)
            self._x2 = (-self._b - math.sqrt(self._discr)) / (2 * self._a)
            self._rootCount = 2
        elif self._discr == 0:
            self._x1 = -self._b / (2 * self._a)
            self._rootCount = 1
        else:
            self._rootCount = 0

    def printRoots(self):
        if(self._rootCount == 2):
            print("x1 = %.2f \nx2 = %.2f" % (self._x1, self._x2))
        elif(self._rootCount == 1):
            print("x = %.2f" % self._x1)
        elif(self._rootCount == 0):
            print("Корней нет")
    
def test():
    qe = QuadroEquation(2,4,2)
    qe.printCoefficients()
    qe.calculate()
    qe.printRoots()
    qe.set_coefficients(-1, 6, 1)
    qe.printCoefficients()
    qe.printRoots()
    qe.calculate()
    qe.printRoots()
    
test()