# REVERSE POLISH NOTATION CALCULATOR
from typing import List, Union
class stack:
    def __init__(self, arr=[]):
        self.stack_arr: List[Union[int, float]] = arr
    def add(self) -> None:
        if len(self.stack_arr) > 1:
            y, x = self.stack_arr.pop(), self.stack_arr.pop()
            self.stack_arr.append(x + y)
    def sub(self) -> None:
        if len(self.stack_arr) > 1:
            y, x = self.stack_arr.pop(), self.stack_arr.pop()
            self.stack_arr.append(x - y)
    def mult(self) -> None:
        if len(self.stack_arr) > 1:
            y, x = self.stack_arr.pop(), self.stack_arr.pop()
            self.stack_arr.append(x * y)
    def div(self) -> None:
        if len(self.stack_arr) > 1:
            y, x = self.stack_arr.pop(), self.stack_arr.pop()
            self.stack_arr.append(0) if y == 0 else self.stack_arr.append(x / y)
    def clear(self) -> None:
        self.stack_arr[0] = 0
    def all_clear(self) -> None:
        self.stack_arr = [0]
    def swap(self) -> None:
        if len(self.stack_arr) > 1:
            self.stack_arr[0], self.stack_arr[1] = self.stack_arr[1], self.stack_arr[0]
    def rot(self) -> None:
        if len(self.stack_arr) > 1:
            x = self.stack_arr.pop(0)
            self.stack_arr.append(x)
def print_stack(stack: stack) -> None:
        print('\n\n' + '\n'.join(map(str,stack.stack_arr)),'\n______________________')
def handle_input(stack: stack) -> bool:
    cmd = input()
    if cmd == '' or cmd == 'r' or cmd == 'rot':
        stack.rot()
    elif cmd == 'q' or cmd == 'quit':
        return False
    elif cmd == 'c':
        stack.clear()
    elif cmd == 'ac':
        stack.all_clear()
    elif cmd == 's' or cmd == 'swp':
        stack.swap()
    elif cmd == 'p' or cmd == 'pop':
        stack.stack_arr.pop()
    elif cmd == '+':
        stack.add()
    elif cmd == '-':
        stack.sub()
    elif cmd == '*':
        stack.mult()
    elif cmd == '/':
        stack.div()
    elif cmd.isnumeric() or (len(cmd) > 1 and cmd[1:].isnumeric()):
        stack.stack_arr.append(float(cmd))
    return True
if __name__ == '__main__':
    s = stack()
    print('\n---RPN Calculator---\n\nCommands:\n\tq: quit\n\tc: clear\n\tac: all clear\n\ts: swap\n\tr: rotate\n\tp: pop\n\t')
    run = True
    while(run):
        print_stack(s)
        run = handle_input(s)
