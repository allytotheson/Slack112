from cmu_graphics import *

def onAppStart(app):
    app.width = 1400
    app.height = 800
    noteVars(app)
def noteVars(app):
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
    

def drawNote(app):
    drawRect(app.x, app.y, app.dx, app.dy, fill = "cornSilk",
             border = "gray")
    drawLabel("To-Do List", app.x+app.dx/2, app.y + 20, size = 18, font = "monospace", bold = True)
    drawLabel("Start typing to add a task!", app.x+app.dx/2, app.y + 40, size = 10, font = "monospace")

    #drawing the blank box
    drawRect(app.bx, app.by + (50*app.i), app.boxDim, app.boxDim, fill = app.noteFill[app.i][0], border = "black")
    drawLabel(app.note, app.bx+app.boxDim+10,  app.by + (50*app.i) + app.boxDim/2, font = "monospace"
              ,align = "left")


    for i in range(len(app.toDoList)):
        drawRect(app.bx, app.by + (50*i), app.boxDim, app.boxDim,
                fill = app.noteFill[i][0], border = "black")
        drawLabel(app.toDoList[i], app.bx+app.boxDim+10,  app.by + (50*i) + app.boxDim/2, 
                  font = "monospace", align = "left")

def redrawAll(app):
    drawNote(app)

def onStep(app):
    pass

def distance(x0, y0, x1, y1):
    return ((x0-x1)**2+(y0-y1)**2)**0.5
    

def onMousePress(app, mouseX, mouseY):
    for i in range(len(app.listDim)):
        x0, y0, x1, y1 = app.listDim[i]
        if x0 <= mouseX <= x1 and y0 <= mouseY <= y1:
            if app.noteFill[i][-1] == True:
                app.noteFill[i] = (None, False)
            else:
                app.noteFill[i] = ("seaGreen", True)
        

def onMouseMove(app, mouseX, mouseY):
    for i in range(len(app.listDim)):
        x0, y0, x1, y1 = app.listDim[i]
        if x0 <= mouseX <= x1 and y0 <= mouseY <= y1 and app.noteFill[i][-1] == False:
            app.noteFill[i] = ("lightGreen", False)
        else:
            if app.noteFill[i][-1] == False:
                app.noteFill[i] = (None, False)
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

def main():
    runApp()

main()