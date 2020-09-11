from Utils import numAttacks, findNeighbours
import random

def findOneSolution(n):
    state = []
    for i in range(n):
        state.append(random.randint(0, n-1))
    state = State(state)

    laterals = 0
    while True:
        prev = state.fitness
        
        neighbours = findNeighbours(state.state)
        for i in range(len(neighbours)):
            neighbours[i] = State(neighbours[i])
        neighbours.append(state)
        
        neighbours.sort(key=(lambda key: key.fitness))

        state = neighbours[0]

        if state.fitness == 0:
            return state.state

        if state.fitness == prev:
            laterals += 1
            if laterals > 20:
                return state.state
        else:
            laterals = 0

class State:
    def __init__(self, state):
        self.state = state
        self.fitness = numAttacks(state)
        self.peaked = False
