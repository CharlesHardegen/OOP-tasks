# Синхронный JK-триггер со входами тактирования (CLK) асинхронной установки (PRE) и асинхронного сброса (CLR)
# Активный сигнал установки и сброса = 1 (True)
# Переключение CLK с 0 на 1 будет означать положительный перепад напряжения разрешающего импульса
# В этот момент будет происходить срабатывания триггера (Использование J и K)
# Пока CLK = 1 J, K не должны меняться
# Переключение CLK с 1 на 0 будет означать отрицательный перепад напряжения разрешающего импульса
# Для простоты будет использована таблица состояний JK-триггера КМ155ТВ1, которая включает 7 состояний

from numpy import tri


class JK_Combined_Trigger:
    def __init__(self):
        self._J = None
        self._K = None
        self._CLR = None
        self._PRE = None
        self._CLK = None
        self._Q = None
        self._Q_reverse = None

    def print_state(self):
        print("Q = ", self._Q, " /Q = ", self._Q_reverse)

    def set_state(self, J: bool, K: bool, CLK: bool, PRE: bool, CLR: bool):
        if(not type(J) == bool or not type(K) == bool or not type(CLK) == bool 
                or not type(PRE) == bool or not type(CLR) == bool):
            print("Неверно указаны входные параметры")
            return
        self._J = J
        self._K = K
        # Неопределённость
        if(CLR == False and PRE == False):
            self._Q = True
            self._Q_reverse = True
        # Асинхронный сброс
        elif(CLR == True and PRE == False):
            self._Q = False
            self._Q_reverse = True
        # Асинхронная установка
        elif(CLR == False and PRE == True):
            self._Q = True
            self._Q_reverse = False
        elif(CLR == True and PRE == True):
            if(self._CLK == False):
                if(CLK == True):
                    # Хранение (нет изменений). Не имеет смысла, лишь для иллюстрации.
                    if(self._J == False and self._K == False):
                        self._Q = self._Q
                        self._Q_reverse = self._Q_reverse
                    # Загрузка 0 (сброс)
                    if(self._J == False and self._K == True):
                        self._Q = False
                        self._Q_reverse = True
                    # Загрузка 1 (установка)
                    if(self._J == True and self._K == False):
                        self._Q = True
                        self._Q_reverse = False
                    # Переключение
                    if(self._J == True and self._K == True):
                        self._Q = not self._Q
                        self._Q_reverse = not self._Q_reverse
        self._CLK = CLK
    
def test():
    trigger = JK_Combined_Trigger()
    trigger.set_state(J=True, K=False, CLK=False, PRE=True, CLR=False)
    trigger.print_state()
    trigger.set_state(J=True, K=False, CLK=False, PRE=False, CLR=True)
    trigger.print_state()
    trigger.set_state(J=True, K=False, CLK=False, PRE=False, CLR=False)
    trigger.print_state()
    
    trigger.set_state(J=True, K=False, CLK=True, PRE=True, CLR=True)
    trigger.print_state()

    trigger.set_state(J=False, K=True, CLK=False, PRE=True, CLR=True)
    trigger.print_state()
    trigger.set_state(J=False, K=True, CLK=True, PRE=True, CLR=True)
    trigger.print_state()

    trigger.set_state(J=False, K=False, CLK=False, PRE=True, CLR=True)
    trigger.print_state()
    trigger.set_state(J=False, K=False, CLK=True, PRE=True, CLR=True)
    trigger.print_state()

    trigger.set_state(J=True, K=True, CLK=False, PRE=True, CLR=True)
    trigger.print_state()
    trigger.set_state(J=True, K=True, CLK=True, PRE=True, CLR=True)
    trigger.print_state()
    
test()
