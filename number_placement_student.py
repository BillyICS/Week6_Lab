import random
NUM_INT = 10

class MinMaxQueue:
    def __init__(self, l=None):
        l.sort()
        self.sorted_q = l

    def pop_min(self):
        #perform on the min
        x = self.sorted_q[0]
        del self.sorted_q[0]
        return x

    def pop_max(self):
        #perform on the max
        x = self.sorted_q[-1]
        del self.sorted_q[-1]
        return x

def main():
    #create the lists of integers and signs, respectively
    li = [random.randint(0, 20) for i in range(NUM_INT)]
    li = list(set(li))
    sign_array = ["<" if random.randint(0, 1) else ">" for i in range(len(li) - 1)]
    mmq = MinMaxQueue(li)

    result = []
    #decide if you'd take out the min or max of the integer list
    #and append corresponding sign after it

    print(result)

main()


