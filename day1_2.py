"""
NOTES:
"""

from base_class import BaseClass

class Day1Part2(BaseClass):

    def find_a_number(self, search_str, nums):
        for i in range(len(search_str)):
            for j, num in enumerate(nums):
                if search_str[i].isnumeric():
                    return int(search_str[i])
                if search_str[i:].startswith(num):
                    return j%10+1

    def __init__(self):
        dt = self.get_data('day1_1')

        num1, num2 = 0, 0
        
        nums_fwd = ['one','two','three','four','five','six','seven','eight','nine']
        nums_bkd = [n[::-1] for n in nums_fwd]

        total = 0

        for line in dt:
            num1 = self.find_a_number(line, nums_fwd)
            num2 = self.find_a_number(line[::-1], nums_bkd)
            subtotal = num1*10 + num2
            total += subtotal

        print(total)

if __name__== "__main__":
    Day1Part2()