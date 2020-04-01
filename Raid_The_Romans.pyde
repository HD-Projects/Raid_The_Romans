import random        

soldierHealth = [0]
soldierX = [1]
soldierY = [1]
gameMode = 0
archerX = []
archerY = []
hp = 50

def setup():
     fullScreen()
     background(255)
     img = loadImage("castle.png")
     image(img, displayWidth*0.75, displayHeight*0.3, displayHeight*0.25, displayHeight*0.25)
     line(displayWidth*0.7, 0, displayWidth*0.7, displayHeight)
     frameRate(12)
     global archerTowerX 
     global archerTowerY 
     global reload
     reload == 1
     archerTowerX = 0 
     archerTowerY = 0
     
def draw():
    global soldierX, soldierY, soldierAlive, gameMode
    background(255)
    for i in range(len(soldierY)):
        img = loadImage("soldier.png")
        image(img, soldierX[i-1]*displayWidth/50, soldierY[i-1]*displayWidth/20, displayWidth*0.035, displayHeight*0.1)
        soldierX[i-1] = soldierX[i-1]+0.5
    for i in range(len(archerY)):
        img = loadImage("archer.png")
        image(img, archerX[i-1], archer[i-1], displayWidth*0.035, displayHeight*0.1)
    img = loadImage("castle.png")
    image(img, displayWidth*0.85, displayHeight*0.3, displayHeight*0.25, displayHeight*0.25)
    line(displayWidth*0.82, 0, displayWidth*0.82, displayHeight)
    fill(10)
    rect(displayWidth*0.865, displayHeight*0.2, displayWidth/10 ,displayHeight/30)
    fill(255) 
    rect(displayWidth*0.867, displayHeight*0.2+2, displayWidth/10.5+(displayWidth/10/1000)*hp,displayHeight/35) 
    
     
     
def mouseClicked():
     if gameMode == 0:
          for i in range(len(soldierHealth)):
               if dist(mouseX, mouseY, (soldierX[i-1]*displayWidth), (soldierY[i-1]*displayWidth))<20:
                    soldierAlive.pop(i-1)
                    soldierX.pop(i-1)
                    soldierY.pop(i-1)
      
#img(archerTower, archerTowerX,archerTowerY)
  
def delayTimer():
    m = millis
    if millis == (m + 100):
        reload = 1
        
    if ((dist(archerTowerX,archerTowerY,soilderX,soilderY) > displayHeight/ 10) and (reload == 1)):
        line(archerTowerX,archerTowerY, soilderX,soilderY)
         
         
    if (dist(mouseX,mouseY,settingsX,settingsY) < height/10):
        text("Low Quality Mode, remcomenned for laptops",settingsX + height/5, settingsY + height/5)
        if (dist(settingsX + height/5, settingsY + height/5,mouseX,mouseY) < height /10):
            frameRate = (frameRate * .7)
        text("Reset Game", settingsX + height/5, settingsY + height/4)
        if (dist(settingsX + height/5, settingsY + height/4,mouseX,mouseY) < height /10):
            exit()        


    if (dist(mouseX,mouseY,settingsX,settingsY) < height/10):
        text("Low Quality Mode, remcomenned for laptops",settingsX + height/5, settingsY + height/5)
        if (dist(settingsX + height/5, settingsY + height/5,mouseX,mouseY) < height /10):
            frameRate = (frameRate * .7)
        text("Reset Game", settingsX + height/5, settingsY + height/4)
        if (dist(settingsX + height/5, settingsY + height/4,mouseX,mouseY) < height /10):
            exit()  
