import random        

soldierHealth = [5, 5]
soldierX = [1,1]
soldierY = [1, 5]
archerX = []
archerY = []
hp = 100
#waveNum = 1
gameMode = 0

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
    global soldierX, soldierY, soldierAlive, gameMode,hp
    if gameMode == 0:
        background(255)
        for i in range(len(soldierY)):
            img = loadImage("soldier.png")
            image(img, soldierX[i-1]*displayWidth/50, soldierY[i-1]*displayWidth/20, displayWidth*0.035, displayHeight*0.1)
            if soldierX[i-1] < 38:
                soldierX[i-1] = soldierX[i-1]+0.5
            else:
                hp+=-1
        for i in range(len(archerY)):
            img = loadImage("archer.png")
            image(img,  archerX[i-1], archerY[i-1], displayWidth*0.035, displayHeight*0.1)
        if hp == 0:
            print("Game Over")
            gameMode = 1
        img = loadImage("castle.png")
        image(img, displayWidth*0.85, displayHeight*0.3, displayHeight*0.25, displayHeight*0.25)
        line(displayWidth*0.82, 0, displayWidth*0.82, displayHeight)
        fill(10)
        rect(displayWidth*0.865, displayHeight*0.2, displayWidth/10 ,displayHeight/30)
        fill(255) 
        rect(displayWidth*0.867, displayHeight*0.2+2, displayWidth/10.5*hp/100,displayHeight/35) 
        textSize(displayWidth/60)
        fill(0)
        text("Wave: "+str(waveNum), displayWidth/40,displayHeight/20)
    elif gameMode == 1:
        background(0)
        textSize(displayWidth/15)
        fill(255)
        text("  Game\n   Over\n\nScore: ", displayWidth/3, displayHeight/3)
    else:
        background(0)
        textSize(64)
        fill(255)
        text("Error x00000, gameMode var out of range", displayWidth/10, displayHeight/2)
     
     
def mouseClicked():
    global gameMode
    if gameMode == 0:
        if mouseX>displayWidth*0.7:
            archerX.append(mouseX-25)
            archerY.append(mouseY-50)
        else:
            for i in range(len(soldierHealth)):
                print("HI, "+str(dist((soldierX[i-1]*displayWidth), (soldierY[i-1]*displayWidth),mouseX, mouseY)))
                if (dist(soldierX[i-1]*displayWidth, soldierY[i-1]*displayWidth,mouseX, mouseY)<displayWidth/19.2):
                    print("Hit Soldier #"+i)
                    soldierHealth[i-1] += -1
                    if soldierHealth[i-1] > 1:
                        soldierHealth.pop(i-1)
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
