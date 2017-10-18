# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 22:13:54 2017

@author: Gu
"""

# Week 6 Inclass Exercise, Number Replacement

import random
NUM_INT = 10


class MinMaxQueue:
    
    def __init__(self, l=None):
        l.sort()
        self.sorted_q = l
        
    def pop_min(self):
        return self.sorted_q.pop(0)
    
    def pop_max(self):
        return self.sorted_q.pop()
    

def main():
    li = [random.randint(0, 20) for i in range(NUM_INT)]
    li = list(set(li))
    sign_array = ["<" if random.randint(0, 1) else ">" for i in range(len(li) - 1)]
    mmq = MinMaxQueue(li)
    result = []
    for sign in sign_array:
        if sign == "<":
            result.append(mmq.pop_min())
        else:
            result.append(mmq.pop_max())
        result.append(sign)
    result.append(mmq.pop_max())
    print(result)
    return(result)


main()
    