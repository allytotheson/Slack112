from cmu_graphics import *
import math

def onAppStart(app):

    app.horizon = 200
    
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




def onKeyPress(app, key):
    pass
def redrawAll(app):
    if app.my < app.horizon:
        drawCircle(app.mx, app.my, app.mSize, fill = "silver")
    
    if app.sy < app.horizon:
        drawCircle(app.sx, app.sy, app.sSize, fill = 'gold')
def onStep(app):
    app.mx = app.width/2 + app.r * math.cos(app.angle)
    app.my = app.height/2 + app.r * math.sin(app.angle)
    app.angle += app.angularSpeed

    app.sx = app.width/2 + app.r * math.cos(app.sAngle)
    app.sy = app.height/2 + app.r * math.sin(app.sAngle)
    app.sAngle += app.angularSpeed



def main():
    runApp()

main()