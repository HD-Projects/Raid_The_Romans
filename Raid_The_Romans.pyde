import random        

soldierHealth = []
soldierX = []
soldierY = []
archerX = []
archerY = []
hp = 100
waveNum = 1
gameMode = 0
frames = 0
score = 0
formNum = random.randint(0, 5)
soldierX = [1,1,1,1,1,1]
soldierY = [1, 3, 5,7, 10,12]


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
    global soldierX, soldierY, soldierAlive, gameMode,hp,waveNum, frames, score, formNum
    if gameMode == 0:
        frames += 1
        background(255)
        if frames/300 == waveNum:
            formNum = 0#random.randint(0, 4)
            if formNum == 0:
                soldierX = [1,1,1,1,1,1]
                soldierY = [1, 3, 5,7, 10,12]
            elif formNum == 1:
                soldierX = []
                soldierY = []
            elif formNum == 2:
                soldierX = []
                soldierY = []
            elif formNum == 3:
                soldierX = []
                soldierY = []
            elif formNum == 4:
                soldierX = []
                soldierY = []
        #if formNum == 0:
            #print("Form 1")
        if soldierX:
            for i in range(len(soldierY)):
                img = loadImage("soldier.png")
                image(img, soldierX[i]*displayWidth/100, soldierY[i]*displayHeight/20, displayWidth*0.035, displayHeight*0.1)
                #print("X:"+str(soldierX[i-1]*displayWidth/100)+" Y:"+str(soldierY[i-1]*displayWidth/20))
                if soldierX[i] < 76:
                    soldierX[i] = soldierX[i]+0.80
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
        textSize(displayWidth/60)
        fill(0)
        text("Score: "+str(score), displayWidth/40*35,displayHeight/20)
        textSize(displayWidth/60)
        fill(0)
        text("Formation: "+str(formNum+1), displayWidth/3,displayHeight/20)
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

if (dist(soilderX[i-1],soilderY[i-1],archerX[i-1],archerY[i-1]) < screenHeight / 10):
  line(soilderX[i-1],soilderY[i-1],archerX[i-1],archerY[i-1])     
  print("Hit Soldier #"+str(i-1))
  soldierX.pop(i-1)
  soldierY.pop(i-1) 
     
def mouseClicked():
    global gameMode
    #if gameMode == 0:
    if mouseX>displayWidth*0.8:
        archerX.append(mouseX-25)
        archerY.append(mouseY-50)
    else:
        print("Clicked")
        for i in range(len(soldierX)):
            #print("HI, "+str(dist(soldierX[i-1]*displayWidth/100, soldierY[i-1]*displayWidth/20,mouseX, mouseY)))
            print(i)
            if dist((int(soldierX[i-1])*displayWidth/100), (int(soldierY[i-1])*displayHeight/20),mouseX, mouseY)<(displayWidth/19.2):
                print("Hit Soldier #"+str(i))
                soldierX.pop(i-1)
                soldierY.pop(i-1)
             
