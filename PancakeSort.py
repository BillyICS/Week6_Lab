# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 22:46:52 2017

@author: Gu
"""

# Week 6, In class exercise, Pancake sort
import random

random.seed(0)
SIZE = 10
LOGGING = True


class PancakeStake():
    
    def __init__(self, stack=None):
        self.stack = stack
        
    def get_size(self):
        return len(self.stack)
    
    def find_largest_pancake(self, end_index):
        largest_index = end_index
        for i in range(end_index):
            if self.stack[i] > self.stack[largest_index]:
                largest_index = i
        return largest_index
    
    def flip(self, index):
        new_stack = self.stack[:(index+1)]
        new_stack.reverse()
        new_stack += self.stack[(index+1):]
        self.stack = new_stack
        return
    

def sort_pancakes(pancakes):
    pancakes_size = pancakes.get_size()
    for i in reversed(range(pancakes_size)):
        flip_index = pancakes.find_largest_pancake(i)
        #flip up
        pancakes.flip(flip_index)
        #flip down
        pancakes.flip(i)
    return pancakes.stack

if __name__ == "__main__":
    my_stack = random.sample(range(1, 20), SIZE)
    print("Unsorted pancakes", my_stack)
    case_one = PancakeStake(my_stack)
    print("Final order of pancakes: ", sort_pancakes(case_one))
            
        
        