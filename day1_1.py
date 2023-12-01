"""
NOTES:
"""

from base_class import BaseClass

class Day1Part1(BaseClass):

    def __init__(self):
        dt = self.get_data('day1_1')
        total = 0
        for line in dt:
            stack = []
            for ch in line:
                if ch.isnumeric():
                    stack.append(int(ch))
            total += stack[0]*10 + stack[-1]
        print(total)


if __name__== "__main__":
    Day1Part1()