# Программа должна иметь следующий вид:
# <текущее состояние> <символ в текущей ячейке> <записываемый символ> <действие> <новое состояние>
# Пример:
# 0 1 1 r 0
# Действия могут быть l, r, * - влево, вправо и остаться, соответственно
# Состояние H (halt) означает остановку машины

import random

class TuringMachine:
    def __init__(self, alphabet, program, input, state=0):
        self.alphabet = alphabet
        self.tape_len = 100 # длина ленты
        self.trf = {}
        self.state = str(state)
        self.tape = ''.join(['_']*self.tape_len)
        self.head = self.tape_len // 2   # начальное положение головки автомата посередине ленты
        self.tape = self.tape[:self.head] + input + self.tape[self.head:]
        for line in program.splitlines():
            s, a, r, d, s1 = line.split(' ')
            self.trf[s,a] = (r, d, s1)
        a = self.tape[self.head]
        self.next_action = self.trf.get((self.state, a))

    def load_program_from_file(self, path: str):
        f = open(path, 'r')
        program = f.read()
        self.trf = {}
        for line in program.splitlines():
            s, a, r, d, s1 = line.split(' ')
            self.trf[s,a] = (r, d, s1)
    
    def clear_tape(self):
        self.tape = ''.join(['_']*self.tape_len)
    
    def set_random_tape(self):
        letters = self.alphabet
        self.tape = ''.join(random.choice(letters) for i in range(self.tape_len))
    
    def print_tape(self, scatter):
        start = max(0, self.head - scatter)
        end = min(self.head + scatter, self.tape_len)
        out_str = f"\n[{str(start)}]"
        for m in self.tape[start:end]:
            out_str += m
        out_str += f"[{str(end)}]\n"
        out_str += f" " * (self.head - start + (len(str(start)) + 2)) + f"|{str(self.state)}"
        action = self.next_action
        if action:
            r, d, s = action
            out_str += f"\nNext action:  ({self.state}, {self.tape[self.head]}) => ({r}, {d}, {s})\n"
        else:
            out_str += "\nNext action not found\n"
        print(out_str)
    
    def step(self):
        if self.state != 'H':
            # assert self.head >= 0 and self.head < len(self.tape) here
            action = self.next_action
            if(not action):
                return False
            r, d, s1 = action
            self.tape = self.tape[:self.head] + r + self.tape[self.head+1:]
            if d != '*':
                self.head = self.head + (1 if d == 'r' else -1)
            self.state = s1
            a = self.tape[self.head]
            self.next_action = self.trf.get((self.state, a))
            self.print_tape(10)
            return True
            
    def run(self, max_iter=9999):
        iter = 0
        while self.state != 'H' and iter < max_iter:
            if(not self.step()):
                break
            iter += 1

def test():
    f = open('program.txt','r')
    program = f.read()
    input = '1101_101'
    tm = TuringMachine(['0','1'], program, input, 0)
    tape = tm.tape
    tm.run()

test()