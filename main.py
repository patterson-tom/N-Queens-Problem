import Backtracking
import Hillclimb
import Beam
import SimulatedAnnealing
import MinConflicts
from Utils import printBoard, numAttacks

import time

def testMethod(method, name, n):
    start = time.time()
    s = method.findOneSolution(n)
    end = time.time()
    print("\n")
    print(name + " result: " + str(numAttacks(s)))
    print("Time taken: " + str(end-start) + "s")
    printBoard(s)

def successRate(method, n, tests):
    count = 0
    for i in range(tests):
        score = numAttacks(method.findOneSolution(n))
        if score == 0:
            count += 1
    return count / tests

#testMethod(Backtracking, "Backtracking", 20)
testMethod(Hillclimb, "Steepest ascent hill climb", 50)
testMethod(Beam, "Local beam search", 50)
testMethod(SimulatedAnnealing, "Simulated Annealing hill climb", 50)
testMethod(MinConflicts, "Minimum conflicts heuristic", 50)

#print("Min Conflicts accuracy: " + str(successRate(MinConflicts, 50, 100)))
#print("Hillclimb accuracy: " + str(successRate(Hillclimb, 10, 100)))
#print("Local beam search accuracy: " + str(successRate(Beam, 10, 100)))
#print("Simulated Annealing accuracy: " + str(successRate(SimulatedAnnealing, 10, 100)))
