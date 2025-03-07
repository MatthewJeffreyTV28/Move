from PyUI.Screen import Screen
from PyUI.PageElements import *

class MenuScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (30,120,200))
        self.state = {
            "screen" : "MenuScreen"
        }

    def elementsToDisplay(self):
        self.elements = [
            Label((400, 100), 200, 100, "Choose an option", 50, (150,180,235)),
            MenuButton((400, 250), "BounceScreen"),
            MenuButton((400, 350), "DrawScreen")
        ]

class MenuButton(Button):
    def __init__(self, topLeftLoc, goTo):
        super().__init__(topLeftLoc, 100, 70, goTo)
        self.goTo = goTo
    
    def onClick(self, screen):
        screen.state["screen"] = self.goTo
        