from cmu_graphics import *


def onAppStart(app):
    app.width = 1400
    app.height = 800
    app.gx = 0
    app.gy = (2/3)*app.height

    app.sy = app.gy
    print(app.sy)
    

    app.studyLength = 25
    app.totalSeconds = app.studyLength * 60


    app.moonR = 30
    app.cx = app.moonR
    app.cy = app.gy - app.moonR
    app.goingUp = True

def onKeyPress(app, key):
    pass
def redrawAll(app):
    drawRect(app.gx, app.gy, app.width, app.height, fill = "darkSeaGreen")
    drawRect(0, 0, app.width, app.sy, fill = "lightBlue")
    drawCircle(app.cx, app.cy, app.moonR, fill = "silver")
def onStep(app):
    app.stepsPerSecond = 10


    app.cx += app.width/(app.totalSeconds*app.stepsPerSecond)

    if app.cy <= 30:
        app.goingUp = not app.goingUp

    #JAYDEN AND HARRY FIX THIS!#
    if app.goingUp:
        app.cy -= app.sy/(0.5*app.totalSeconds*app.stepsPerSecond)
    else:
        app.cy += app.sy/(0.5*app.totalSeconds*app.stepsPerSecond)


def main():
    runApp()

main()