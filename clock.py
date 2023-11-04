from cmu_graphics import *


def onAppStart(app):
    app.width = 1920
    app.height = 1080
    app.gx = 0
    app.gy = (2/3)*app.height


def onKeyPress(app, key):
    pass
def redrawAll(app):
    drawRect(app.gx, app.gy, app.width, app.height, fill = "darkSeaGreen")

def main():
    runApp()

main()