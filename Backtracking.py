from Utils import numAttacks

solutions = []

def findOneSolution(n):
    return backtrack([], n, False)

def findAllSolutions(n):
    backtrack([], n, True)
    return solutions

def backtrack(state, n, keep_going):
    if (numAttacks(state) != 0):
        return False
    if len(state) == n:
        if keep_going:
            solutions.append(state)
            return False
        return state

    for i in range(n):
        result = backtrack(state + [i], n, keep_going)
        if not result:
            continue
        return result
    
