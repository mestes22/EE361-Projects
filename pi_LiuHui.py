from math import *

def pi_LiuHui(epsilon):
    M = 1.00    # radius of circle
    numS = 6    # number of sides for starting hexagon
    A1 = 1      # Area of original polygon
    A2 = 2      # Area of polygon with twice number of sides as original polygon

    while (A2 - A1 > epsilon):
        g = sqrt(1 - (M**2)/4)  # radius to center of n side length
        A1 = 0.5*M*g*numS       # area of original polygon
        A2 = 0.5*M*numS         # area of polygon with twice number of sides as original polygon

        numS = numS * 2         # double the number of sides

        M = sqrt(((M / 2) ** 2) + ((1 - sqrt(1 - ((M ** 2) / 4))) ** 2))    # find new side length
    return A2

print(pi_LiuHui(0.001))

#Test Case:
#Input = pi_LiuHui(0.000001)
#Output = 3.1415925166921577
#Input = pi_LiuHui(0.001)
#Output = 3.1414524722854624

