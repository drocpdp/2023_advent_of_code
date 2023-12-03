"""
NOTES:
"""

from base_class import BaseClass

class Day2Part1(BaseClass):

    def __init__(self):
        dt = self.get_data('day2')

        total = {i for i in range(1, len(dt) + 1)}

        maxes = {'red': 12, 'green': 13, 'blue': 14}

        for i, line in enumerate(dt, 1):
            line = line.split(":")[1]
            for pull in line.split(';'):
                for cube in pull.split(','):
                    qc = cube.split(' ')
                    qty = qc[1]
                    color = qc[2]
                    if int(qty) > maxes[color]:
                        if i in total:
                            total.remove(i)
        
        print(sum(total))
                    

if __name__== "__main__":
    Day2Part1()