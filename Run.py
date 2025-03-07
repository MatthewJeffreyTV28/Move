from PyUI.Window import Window
from BounceScreen import BounceScreen
from MenuScreen import MenuScreen
from DrawScreen import DrawScreen

window = Window("Moving Guy", (0,255,0))

bounceScreen = BounceScreen(window)
drawScreen = DrawScreen(window)
menuScreen = MenuScreen(window)

screen = menuScreen

while True:

    window.checkForInput(screen)
    window.update(screen)
    if screen.state["screen"] == "MenuScreen":
        screen = menuScreen
    elif screen.state["screen"] == "BounceScreen":
        screen = bounceScreen
    elif screen.state["screen"] == "DrawScreen":
        screen = drawScreen
