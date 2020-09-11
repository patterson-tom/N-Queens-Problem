def printBoard(state):
    print("")
    for s in state:
        print(' '.join(['-' if i != s else 'Q' for i in range(len(state))]))

def numAttacks(state):
    count = 0
    count += len(state) - len(set(state))

    diag_state1 = [state[i] - i for i in range(len(state))]
    diag_state2 = [state[i] + i for i in range(len(state))]
    count += len(diag_state1) - len(set(diag_state1))
    count += len(diag_state2) - len(set(diag_state2))
    
    return count

def findNeighbours(state):
    neighbours = []
    for i in range(len(state)):
        for j in range(len(state)):
            if state[i] == j:
                continue

            new_state = state.copy()
            new_state[i] = j
            neighbours.append(new_state)

    return neighbours
