import turtle
import math

#1.
#SolarSystem
#Constructors: __init__,
#Mutators: addPlanet, addSun
#Accessors: showPlanets, movePlanets

#Sun
#Constructors: __init__
#Accessors: getMass, getXPos, getYPos, __lt__, __str__

#Planet
#Constructors: __init__
#Mutators: setXVel, setYVel
#Accessors: getXPos, getYPos, getXVel, getYVel, moveTo

#2.
#A larger mass for the sun makes the planets pull very close to it and slingshot them around at a must fater rate

#3.
#Before: <__main__.Planet object at 0x00000207556E2310>
#After: {Name: Jupiter Radius: 100 Mass: 49000 Distance: 0.7}
#One prints an object, and the other prints a string
#List of planets
#Before: [<__main__.Planet object at 0x0000017D5AF22310>, <__main__.Planet object at 0x0000017D5AF28370>, <__main__.Planet object at 0x0000017D5AF28460>, <__main__.Planet object at 0x0000017D5AF2B9D0>]
#After: [{Name: Jupiter Radius: 100 Mass: 49000 Distance: 0.7}, {Name: Mars Radius: 50 Mass: 9000 Distance: 0.5}, {Name: Earth Radius: 47.5 Mass: 5000 Distance: 0.3}, {Name: Mercury Radius: 19.5 Mass: 1000 Distance: 0.25}]

#4.
#Before: TypeError: '<' not supported between instances of 'Planet' and 'Planet'
#After: [{Name: Mars Radius: 50 Mass: 9000 Distance: 0.5}, {Name: Earth Radius: 47.5 Mass: 5000 Distance: 0.3}, {Name: Jupiter Radius: 100 Mass: 1000 Distance: 0.7}, {Name: Mercury Radius: 19.5 Mass: 1000 Distance: 0.25}]
#One sorts by mass the other doesn't run

class SolarSystem:
    def __init__(self, width, height):
        self.__theSun = None
        self.__planets = []
        self.__ssTurtle = turtle.Turtle()
        self.__ssTurtle.hideturtle()
        self.__ssScreen = turtle.Screen()
        self.__ssScreen.setworldcoordinates(-width / 2.0, -height / 2.0,
                                            width / 2.0, height / 2.0)

    def addPlanet(self, aPlanet):
        self.__planets.append(aPlanet)

    def addSun(self, aSun):
        self.__theSun = aSun

    def showPlanets(self):
        for aPlanet in self.__planets:
            print(aPlanet)

    def movePlanets(self):
        G = .1
        dt = .001

        for p in self.__planets:
            p.moveTo(p.getXPos() + dt * p.getXVel(),
                     p.getYPos() + dt * p.getYVel())

            rX = self.__theSun.getXPos() - p.getXPos()
            rY = self.__theSun.getYPos() - p.getYPos()

            r = math.sqrt(rX ** 2 + rY ** 2)

            accX = G * self.__theSun.getMass() * rX / r ** 3
            accY = G * self.__theSun.getMass() * rY / r ** 3

            p.setXVel(p.getXVel() + dt * accX)
            p.setYVel(p.getYVel() + dt * accY)

    def freeze(self):
        self.__ssScreen.exitonclick()


class Sun:
    def __init__(self, iName, iRad, iM, iTemp):
        self.__name = iName
        self.__radius = iRad
        self.__mass = iM
        self.__temp = iTemp
        self.__x = 0
        self.__y = 0

        self.__sTurtle = turtle.Turtle()
        self.__sTurtle.shape("circle")
        self.__sTurtle.color("yellow")

    def getMass(self):
        return self.__mass

    def getXPos(self):
        return self.__x

    def getYPos(self):
        return self.__y

    def __lt__(self, other):
        return self.__mass < other.__mass

    def __str__(self):
        return self.__name + str(self.__mass)


class Planet:
    __name: object

    def __init__(self, iName, iRad, iM, iDist, iVx, iVy, iC):
        self.__name = iName
        self.__radius = iRad
        self.__mass = iM
        self.__distance = iDist
        self.__velX = iVx
        self.__velY = iVy

        self.__x = self.__distance
        self.__y = 0
        self.__color = iC

        self.__pTurtle = turtle.Turtle()

        self.__pTurtle.color(self.__color)
        self.__pTurtle.shape("circle")

        self.__pTurtle.up()
        self.__pTurtle.goto(self.__x, self.__y)
        self.__pTurtle.down()

    def __repr__(self):
        return '{Name: ' + self.__name+' Radius: ' + str(self.__radius)+' Mass: '+str(self.__mass)+' Distance: '+str(self.__distance)+'}'

    #def __lt__(self, other):
    #    return self.__mass > other.__mass

    def getXPos(self):
        return self.__x

    def getYPos(self):
        return self.__y

    def moveTo(self, newX, newY):
        self.__x = newX
        self.__y = newY
        self.__pTurtle.goto(self.__x, self.__y)

    def getXVel(self):
        return self.__velX

    def getYVel(self):
        return self.__velY

    def setXVel(self, newVx):
        self.__velX = newVx

    def setYVel(self, newVy):
        self.__velY = newVy


def createSSandAnimate():
    #Constructor
    ss = SolarSystem(2, 2)
    # Constructor
    planets = []
    # Constructor
    sun = Sun("Sun", 5000, 100, 5800)
    #Mutator
    ss.addSun(sun)

    #Constructor
    m = Planet("Jupiter", 100, 1000, 0.7, 0, 1, "black")
    #Mutator
    ss.addPlanet(m)
    #Mutator
    planets.append(m)

    #Same for rest

    m = Planet("Mars", 50, 9000, 0.5, 0, 1.63, "red")
    ss.addPlanet(m)
    planets.append(m)

    m = Planet("Earth", 47.5, 5000, 0.3, 0, 2.0, "green")
    ss.addPlanet(m)
    planets.append(m)

    m = Planet("Mercury", 19.5, 1000, .25, 0, 2, "blue")
    ss.addPlanet(m)
    planets.append(m)

    print(planets)
    print(sorted(planets))

    numTimePeriods = 2000
    for aMove in range(numTimePeriods):
        ss.movePlanets()

    ss.freeze()

createSSandAnimate()
