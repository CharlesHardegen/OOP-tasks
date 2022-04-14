import matplotlib.pyplot as plt
import math
import datetime

class SineWaveGenerator:
    def __init__(self, A, F):
        self.set_params(A,F)

    def set_params(self, A, F):
        self._A = A
        self._F = F
        self._oldTime  = datetime.datetime.now()
    
    def get_value(self):
        newTime  = datetime.datetime.now()
        self.dt = (newTime - self._oldTime).total_seconds()
        return(self.sin_func(self.dt))
    
    def sin_func(self, t):
        return(self._A * math.sin((self._F * t * 2 * math.pi)))
    
def test():
    g = SineWaveGenerator(1, 50)
    
    t_values = []
    amplitude_values = []
    
    for i in range(50000):
        amplitude_values.append(g.get_value())
        t_values.append(g.dt)
    
    plt.plot(t_values, amplitude_values)
    plt.show()

test()
