from cmu_graphics import *

def onAppStart(app):
    app.toDoList = []



def redrawAll(app):
    drawPolygon(app.width/4,0, app.width, 0, app.width, app.height, app.width/4, app.height, fill = 'grey')
    drawPolygon(app.width/16, app.height/16, app.width/(16/3), app.height/16, app.width/(16/3), app.height/(16/3), app.width/16, app.height/(16/3)
                , fill = 'lightGreen')
    for i in range(len(app.toDoList)):
        drawLabel(app.toDoList[i], app.width/2, i * 30, size = 16)


    

def distance(x0, y0, x1, y1):
    pass
    

def onMousePress(app, mouseX, mouseY):
    if clickedAddButton(app, mouseX, mouseY):
        task = input('Enter a task:')
        app.toDoList.append(task)



def clickedAddButton(app,mouseX,mouseY):
    if app.width/16 <= mouseX and mouseX <= app.width/(16/3):
        if app.height/16 <= mouseY and mouseY <= app.height/(16/3):
            return True
    return False


    
    
    

def main():
    runApp()

main()