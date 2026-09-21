# Returns any whole number squared

def getSquare(inputNumber):
    total = 0
    for loopVar in range(0, abs(inputNumber)):
        total += 1 + loopVar + loopVar
    return(total)

# Returns the square root of any whole positive number

def getSquareRoot(inputNumber):
    total = 0
    for loopVar in range(0, 1000000):
        total += 1 + loopVar + loopVar
        if total == inputNumber:
            return(loopVar + 1)
