# Returns any whole number squared

import math
def getSquare(x):
    negative = False
    if x < 0:
        negative = True
    z = 0
    i = []
    for j in range(0, abs(x)):
        i.append(1 + 2 * j)
    for k in i:
        z += k
    if negative:
        return(0 - z)
    else:
        return(z)

# Returns the square root of any whole positive number

import math
def getSquareRoot(x):
    z = 0
    for j in range(0, 1000000):
        z += 1 + 2 * j
        if z == x:
            return(j + 1)
