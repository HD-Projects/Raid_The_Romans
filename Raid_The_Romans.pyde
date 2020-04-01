import random        

soldierAlive = [0]
soldierX = [20]
soldierY = [20]
gameMode = 0

def setup():
     fullScreen()
     background(255)
     img = loadImage("castle.png")
     image(img, displayWidth*0.75, displayHeight*0.3, displayHeight*0.25, displayHeight*0.25)
     line(displayWidth*0.7, 0, displayWidth*0.7, displayHeight)
     frameRate(12)
     
def draw():
    global soldierX, soldierY, soldierAlive, gameMode
    background(255)
    for i in range(len(soldierY)):
        img = loadImage("soldier.png")
        image(img, soldierX[i-1], soldierX[i-1], displayWidth*0.1, displayHeight*0.2)
    img = loadImage("castle.png")
    image(img, displayWidth*0.75, displayHeight*0.3, displayHeight*0.25, displayHeight*0.25)
    line(displayWidth*0.7, 0, displayWidth*0.7, displayHeight)
     
     
def mouseClicked():
     if gameMode == 0:
          for i in range(len(soldierAlive)):
               if dist(mouseX, mouseY, (soldierX[i-1]*displayWidth), (soldierY[i-1]*displayWidth))<20:
                    soldierAlive.pop(i-1)
                    soldierX.pop(i-1)
                    soldierY.pop(i-1)
