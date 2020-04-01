import random        

def setup():
     fullScreen()
     background(255)
     img = loadImage("castle.png")
     image(img, displayWidth*0.75, displayHeight*0.3, displayHeight*0.25, displayHeight*0.25)
     line(displayWidth*0.7, 0, displayWidth*0.7, displayHeight)
     frameRate(12)
     
def draw():
     background(255)
     img = loadImage("castle.png")
     image(img, displayWidth*0.75, displayHeight*0.3, displayHeight*0.25, displayHeight*0.25)
     line(displayWidth*0.7, 0, displayWidth*0.7, displayHeight)
     
     
def mouseClicked():
     if gameMode == 0:
          for i in range(len(soldierAlive)):
               if dist(mouseX, mouseY, soldierX[i-1], soldierY[i-1])<20:
                    soldierAlive[i-1].delete()
                    soldierX[i-1].delete()
                    soldierY[i-1].delete(

