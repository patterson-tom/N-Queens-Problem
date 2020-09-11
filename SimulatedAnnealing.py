from Utils import numAttacks, findNeighbours
import random
import math

def findOneSolution(n):
    state = []
    for i in range(n):
        state.append(random.randint(0, n-1))
    state = State(state)

    laterals = 0
    T = 100
    cooling = 0.01
    
    while True:
        
        prev = state.fitness
        
        neighbours = findNeighbours(state.state)
        for i in range(len(neighbours)):
            neighbours[i] = State(neighbours[i])
        
        random.shuffle(neighbours)

        tradeAccepted = False
        i = 0
        while not tradeAccepted:
            if neighbours[i].fitness <= prev:
                tradeAccepted = True
            else:
                D = neighbours[i].fitness - prev
                prob = math.exp(-D / T)
                if prob > random.random():
                    tradeAccepted = True
                else:
                    i += 1
                    if i >= len(neighbours):
                        return state.state
                
        state = neighbours[i]

        if state.fitness == 0:
            return state.state

        if state.fitness == prev:
            laterals += 1
            if laterals > 2000:
                print('lateral')
                return state.state
        else:
            laterals = 0

        T *= (1-cooling)
        if T < 0.001:
            print('t')
            return state.state

class State:
    def __init__(self, state):
        self.state = state
        self.fitness = numAttacks(state)
        self.peaked = False
