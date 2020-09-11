from Utils import numAttacks, findNeighbours
import random

def findOneSolution(n):
    k = 30

    states = []
    for i in range(k):
        state = []
        for i in range(n):
            state.append(random.randint(0, n-1))
        states.append(State(state))

    laterals = 0
    while True:
        prev = max(states, key=(lambda key: key.fitness)).fitness
        
        neighbours = states.copy()
        for s in states:
            neighbours += getNeighbours(s)
        neighbours.sort(key=(lambda key: key.fitness))

        states = neighbours[:k]
        if states[0].fitness == 0:
            return states[0].state

        if states[0].fitness == prev:
            laterals += 1
            if laterals > 20:
                return states[0].state
        else:
            laterals = 0
        

def getNeighbours(state):
    
    neighbours = findNeighbours(state.state)
    for i in range(len(neighbours)):
        neighbours[i] = State(neighbours[i])

    return neighbours

class State:
    def __init__(self, state):
        self.state = state
        self.fitness = numAttacks(state)
        self.peaked = False
