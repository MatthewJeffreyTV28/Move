from PyUI.Screen import Screen
from PyUI.PageElements import *
import random

class BounceScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (0, 0, 0))
        self.upX = 1
        self.upY = 1
        self.speed = random.uniform(0.1, 0.5)
        self.state = {
            "objPos" : (random.randint(100, 400), random.randint(100, 400)),
            "screen" : "BouceScreen"
        }

    def moveObj(self, currPos):
        newX = 0
        newY = 0

        #Update X position
    
        if self.state["objPos"][0] >= 750:
            self.upX = False
        if self.state["objPos"][0] <= 50:
            self.upX = True

        if self.upX == False:
            newX = -self.speed
        if self.upX == True:
            newX = self.speed

        #Update Y position
    
        if self.state["objPos"][1] >= 550:
            self.upY = False
        if self.state["objPos"][1] <= 50:
            self.upY = True

        if self.upY == False:
            newY = -self.speed
        if self.upY == True:
            newY = self.speed
    
        return ((currPos[0] + newX), (currPos[1] + newY))

    def elementsToDisplay(self):
        self.elements = [
            Image(self.state['objPos'], 100, 75, './imgs/Penguin.jpg')
        ]

        #Slide object

        self.state["objPos"] = self.moveObj(self.state["objPos"])
