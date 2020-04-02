import random        

soldierHealth = [2,2,2]
soldierX = [1,1,1,1]
soldierY = [1, 5,7,20]
archerX = []
archerY = []
hp = 100
waveNum = 1
gameMode = 0
frames = 0
score = 0

def setup():
     fullScreen()
     background(255)
     img = loadImage("castle.png")
     image(img, displayWidth*0.75, displayHeight*0.3, displayHeight*0.25, displayHeight*0.25)
     line(displayWidth*0.7, 0, displayWidth*0.7, displayHeight)
     frameRate(24)
     global archerTowerX 
     global archerTowerY 
     global reload
     reload == 1
     archerTowerX = 0 
     archerTowerY = 0
     
def draw():
    global soldierX, soldierY, soldierAlive, gameMode,hp,waveNum, frames, score
    if gameMode == 0:
        frame += 1
        background(255)
        if waveNum == 1 and frames == 480:
            waveNum += 1
            frames = 0
        for i in range(len(soldierY)):
            img = loadImage("soldier.png")
            image(img, soldierX[i-1]*displayWidth/100, soldierY[i-1]*displayWidth/20, displayWidth*0.035, displayHeight*0.1)
            #print("X:"+str(soldierX[i-1]*displayWidth/100)+" Y:"+str(soldierY[i-1]*displayWidth/20))
            if soldierX[i-1] < 76:
                soldierX[i-1] = soldierX[i-1]+0.80
            else:
                hp+=-0.5
        for i in range(len(archerY)):
            img = loadImage("archer.png")
            image(img,  archerX[i-1], archerY[i-1], displayWidth*0.035, displayHeight*0.1)
        if hp <= 0:
            print("Game Over")
            gameMode = 1
            frames = 0
        img = loadImage("castle.png")
        image(img, displayWidth*0.85, displayHeight*0.25, displayHeight*0.25, displayHeight*0.25)
        line(displayWidth*0.82, 0, displayWidth*0.82, displayHeight)
        fill(10)
        rect(displayWidth*0.865, displayHeight*0.2, displayWidth/10 ,displayHeight/30)
        fill(255) 
        rect(displayWidth*0.867, displayHeight*0.2+2, displayWidth/10.5*hp/100,displayHeight/35) 
        textSize(displayWidth/60)
        fill(0)
        text("Wave: "+str(waveNum), displayWidth/40,displayHeight/20)
        score += waveNum
    elif gameMode == 1:
        frames += 1
        if frames == 60:
            gameMode = 0
            hp = 100
        background(0)
        textSize(displayWidth/15)
        fill(255)
        text("  Game\n   Over\n\nScore: "+str(score), displayWidth/3, displayHeight/3)
    else:
        background(0)
        textSize(64)
        fill(255)
        text("Error x00000, gameMode var out of range", displayWidth/10, displayHeight/2)
     
     
def mouseClicked():
    global gameMode
    #if gameMode == 0:
    if mouseX>displayWidth*0.8:
        archerX.append(mouseX-25)
        archerY.append(mouseY-50)
    else:
        for i in range(len(soldierHealth)):
            print("HI, "+str(i)+str(dist(soldierX[i-1]*displayWidth/100, soldierY[i-1]*displayWidth/20,mouseX, mouseY)))
            if dist(int(soldierX[i])*displayWidth/100, int(soldierY[i])*displayWidth/20,mouseX, mouseY<displayWidth/19.2)<displayWidth/5:
                print("Hit Soldier #"+str(i))
                soldierHealth[i] = int(soldierHealth[i])-1
                if soldierHealth[i] > 1:
                    soldierHealth.pop(i)
                    soldierX.pop(i)
                    soldierY.pop(i)
      
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
