from cmu_graphics import *
import math

def onAppStart(app):
    app.width = 1400
    app.height = 800
    sunAndMoonVars(app)
    background(app)
    noteVars(app)
    app.studying = False

def sunAndMoonVars(app):
    app.horizon = app.height*(2/3)
    
    #moon
    app.r = app.width/2 + 20
    app.mx = 30
    app.my = app.height/2 + 100
    app.angle = 0
    app.angularSpeed = 0.05
    app.stepsPerSecond = 24
    app.mSize = 40
    
    #sun
    app.sx = app.width - 30
    app.sy = app.height/2
    app.sAngle = math.pi
    app.sSize = 40

    app.skyGradient = gradient("skyBlue", "lightCyan", start = "top")                                                                    
def background(app):
    app.gy = app.height*(2/3)
def noteVars(app):
    app.noteShowing = False
    app.noteX, app.noteY = 120,80
    app.noteBox = (app.width*(7/8), app.width*(1/20), 
                   app.width*(7/8) + app.noteX , app.width*(1/8) + app.noteY)
    app.toDoList = []
    app.i = len(app.toDoList)
    app.note = ""
    app.noteFill = {0:(None, False)}
    app.x, app.y = app.width*(3/4), app.height/4
    app.dx, app.dy = app.width/8, app.height/2

    app.boxDim = 20
    app.bx, app.by = app.x + 10, app.y + app.dy/6
    app.listDim = [(app.bx, app.by, app.bx + app.boxDim,
                    app.by + app.boxDim)]

def onKeyPress(app, key):
    if len(key) == 1:
        app.note += key
    elif key == "space":
        app.note += " "
    elif key == "backspace":
        app.note = app.note[:-1]
    elif key == "enter" and len(app.toDoList) < 6:
        app.toDoList.append(app.note)
        app.note = ""
        app.i = len(app.toDoList)
        app.listDim.append((app.bx, app.by + (50*app.i), app.bx + app.boxDim,
                            app.by + (50*app.i) + app.boxDim))
        app.noteFill[app.i] = (None, False)
def redrawAll(app):
    drawBackground(app)
    if app.noteShowing == True:
        drawNote(app)
    drawNoteBox(app)
    
def drawBackground(app):
    #background

    drawRect(0,0, app.width, app.gy, fill = app.skyGradient)

    if app.my < app.horizon:
        drawCircle(app.mx, app.my, app.mSize, fill = gradient("gray", "silver", start = "top"))
    
    
    if app.sy < app.horizon:
        drawCircle(app.sx, app.sy, app.sSize, fill = gradient("yellow", 'gold', start = 'top'))
    drawRect(0, app.gy, app.width, app.height-app.gy, fill = gradient("mediumSeaGreen", "darkGreen",
                                                                      start = "top"))
def drawNoteBox(app):
    x0, y0 = app.noteBox[:2]
    drawRect(x0, y0, app.noteX, app.noteY, fill = "papayaWhip")
    if app.noteShowing == False:
        drawLabel("Show To-Do List", x0 + app.noteX/2, y0 + app.noteY/2, size = 14, font = "grenze",
                  bold = True)
    else:
        drawLabel("Hide To-Do List", x0 + app.noteX/2, y0 + app.noteY/2, size = 14, font = "grenze", 
                  bold = True)
def drawNote(app):
    drawRect(app.x, app.y, app.dx, app.dy, fill = "cornSilk",
             border = "gray")
    drawLabel("To-Do List", app.x+app.dx/2, app.y + 20, size = 18, font = "grenze", bold = True)
    drawLabel("Start typing to add a task!", app.x+app.dx/2, app.y + 40, size = 10, font = "grenze")

    #drawing the blank box
    drawRect(app.bx, app.by + (50*app.i), app.boxDim, app.boxDim, fill = app.noteFill[app.i][0], border = "black")
    drawLabel(app.note, app.bx+app.boxDim+10,  app.by + (50*app.i) + app.boxDim/2, font = "grenze"
              ,align = "left")


    for i in range(len(app.toDoList)):
        drawRect(app.bx, app.by + (50*i), app.boxDim, app.boxDim,
                fill = app.noteFill[i][0], border = "black")
        drawLabel(app.toDoList[i], app.bx+app.boxDim+10,  app.by + (50*i) + app.boxDim/2, 
                  font = "grenze", align = "left")
def onMousePress(app, mouseX, mouseY):
    for i in range(len(app.listDim)):
        x0, y0, x1, y1 = app.listDim[i]
        if x0 <= mouseX <= x1 and y0 <= mouseY <= y1:
            if app.noteFill[i][-1] == True:
                app.noteFill[i] = (None, False)
            else:
                app.noteFill[i] = ("seaGreen", True)
    x0,y0, x1, y1 = app.noteBox
    if x0 <= mouseX <= x1 and y0 <= mouseY <= y1:
        app.noteShowing = not app.noteShowing
def onMouseMove(app, mouseX, mouseY):
    for i in range(len(app.listDim)):
        x0, y0, x1, y1 = app.listDim[i]
        if x0 <= mouseX <= x1 and y0 <= mouseY <= y1 and app.noteFill[i][-1] == False:
            app.noteFill[i] = ("lightGreen", False)
        else:
            if app.noteFill[i][-1] == False:
                app.noteFill[i] = (None, False)
def onStep(app):
    app.mx = app.width/2 + app.r * math.cos(app.angle)
    app.my = app.height + app.r * math.sin(app.angle)
    app.angle += app.angularSpeed

    app.sx = app.width/2 + app.r * math.cos(app.sAngle)
    app.sy = app.height + app.r * math.sin(app.sAngle)
    app.sAngle += app.angularSpeed

    if app.my < app.horizon:
        app.skyGradient = gradient("black", "navy", start = 'top')

    if app.sy < app.horizon:
        app.skyGradient = gradient("skyBlue", "lightCyan", start = "top")


def main():
    runApp()

main()