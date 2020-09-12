import random
from Utils import numAttacks, printBoard

def findOneSolution(n):
    state = []
    for i in range(n):
        conflicts = []
        for j in range(n):
            conflicts.append(numConflicts(state, i, j, i))
        minConflicts = min(conflicts)
        matches = []
        for j in range(n):
            if conflicts[j] == minConflicts:
                matches.append(j)
        
        state.append(random.choice(matches))
        
    prev = 9999999999999
    laterals = 0
    maxIter = 1000
    
    while True:
        maxIter -= 1
        if maxIter == 0:
            
            return state
        nAttacks = numAttacks(state)

        if nAttacks == 0:
            return state
        
        if nAttacks == prev:
            laterals += 1
            if laterals > 100:
                return state
        else:
            laterals = 0
            
        prev = nAttacks
        
        order = [i for i in range(n)]
        random.shuffle(order)
        for i in order:

            if numConflicts(state, i, state[i], n) == 0:
                continue
        
            conflicts = [999999999 for j in range(n)]
            
            for j in range(n):
                if j == state[i]:
                    continue
                conflicts[j] = numConflicts(state, i, j, n)
                
            minConflicts = min(conflicts)
            matches = []
            for k in range(n):
                if minConflicts == conflicts[k]:
                    matches.append(k)
            j = random.choice(matches)
            state[i] = j

            if numAttacks(state) == 0:
                return state

def numConflicts(state, i, pretend, n):
    conflicts = 0
    for j in range(n):
        if j == i:
            continue

        if state[j] == pretend:
            conflicts += 1
            continue

        if state[j]+j == pretend+i:
            conflicts += 1
            continue

        if state[j]-j == pretend-i:
            conflicts += 1
            continue

        

    return conflicts
