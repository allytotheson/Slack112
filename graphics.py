from cmu_graphics import *
import math

def onAppStart(app):
    app.width = 1400
    app.height = 800
    sunAndMoonVars(app)
    background(app)
def sunAndMoonVars(app):
    app.horizon = app.height*(2/3)
    
    #moon
    app.r = app.width/2
    app.mx = 30
    app.my = app.height/2 + 100
    app.angle = 0
    app.angularSpeed = 0.05
    app.stepsPerSecond = 24
    app.mSize = 20
    
    #sun
    app.sx = app.width - 30
    app.sy = app.height/2
    app.sAngle = math.pi
    app.sSize = 30

def background(app):
    app.gy = app.height*(2/3)


def onKeyPress(app, key):
    pass
def redrawAll(app):
    #sky
    drawRect(0,0, app.width, app.gy, fill = gradient("skyBlue", "lightCyan", start = "top"))
    if app.my < app.horizon:
        drawCircle(app.mx, app.my, app.mSize, fill = "silver")
    
    if app.sy < app.horizon:
        drawCircle(app.sx, app.sy, app.sSize, fill = 'gold')
    drawRect(0, app.gy, app.width, app.height-app.gy, fill = gradient("mediumSeaGreen", "darkGreen",
                                                                      start = "top"))
    
def onStep(app):
    app.mx = app.width/2 + app.r * math.cos(app.angle)
    app.my = app.height + app.r * math.sin(app.angle)
    app.angle += app.angularSpeed

    app.sx = app.width/2 + app.r * math.cos(app.sAngle)
    app.sy = app.height + app.r * math.sin(app.sAngle)
    app.sAngle += app.angularSpeed



def main():
    runApp()

main()