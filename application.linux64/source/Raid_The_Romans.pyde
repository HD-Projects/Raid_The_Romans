import random        

soldierX = []
soldierY = []
archerX = []
archerY = []
hp = 100
waveNum = 1
gameMode = 0
frames = 0
score = 0
archerCooldown = 1
framesStopped = 0

formNum = random.randint(0, 4)
if formNum == 0:
    soldierX = [1,1,1,1,1,1,-4,-4]
    soldierY = [1, 3, 6,8, 11,13,6,8]
elif formNum == 1:
    soldierX = [1,1,1,1-5,-5,-5,-5]
    soldierY = [3,5,7,9,2,4,6,8]
elif formNum == 2:
    soldierX = [1,1,-1,-1, -5,-5]
    soldierY = [10, 12, 2, 4, 14,16,10,12]
elif formNum == 3:
    soldierX = [2, -2,-2,-2,-2,-2,-2, -7,-7]
    soldierY = [10,2,4,6,8,10,12, 6,8]
elif formNum == 4:
    soldierX = [1,1,1,-5,-5,3,3]
    soldierY = [2,4,6,5,7,10,12]

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
     reload = 1
     archerTowerX = 0 
     archerTowerY = 0
     
def draw():
    global soldierX, soldierY, soldierAlive, gameMode,hp,waveNum, frames, score, formNum,framesStopped
    if gameMode == 0:
        frames += 1
        background(255)
        if frames/150 == waveNum:
            formNum = random.randint(0, 4)
            if formNum == 0:
                soldierX = [1,1,1,1,1,1,-4,-4]
                soldierY = [1, 3, 6,8, 11,13,6,8]
            elif formNum == 1:
                soldierX = [1,1,1,1-5,-5,-5,-5]
                soldierY = [3,5,7,9,2,4,6,8]
            elif formNum == 2:
                soldierX = [1,1,-1,-1, -5,-5]
                soldierY = [10, 12, 2, 4, 14,16,10,12]
            elif formNum == 3:
                soldierX = [2, -2,-2,-2,-2,-2,-2, -7,-7]
                soldierY = [10,2,4,6,8,10,12, 6,8]
            elif formNum == 4:
                soldierX = [1,1,1,-5,-5,3,3]
                soldierY = [2,4,6,5,7,10,12]
            waveNum +=1
        if soldierX:
            for i in range(len(soldierY)-1):
                img = loadImage("soldier.png")
                image(img, soldierX[i-1]*displayWidth/100, soldierY[i-1]*displayHeight/20, displayWidth*0.035, displayHeight*0.1)
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
        strokeWeight(displayWidth/70)
        fill(113, 79, 26)
        line(displayWidth*0.82, 0, displayWidth*0.82, displayHeight)
        fill(113, 79, 26)
        fill(10)
        strokeWeight(1)
        rect(displayWidth*0.865, displayHeight*0.2, displayWidth/10 ,displayHeight/30)
        fill(255) 
        rect(displayWidth*0.867, displayHeight*0.2+2, displayWidth/10.5*hp/100,displayHeight/35) 
        textSize(displayWidth/60)
        fill(0)
        text("Wave: "+str(waveNum), displayWidth/40,displayHeight/20)
        textSize(displayWidth/60)
        fill(0)
        text("Score: "+str(frames*waveNum), displayWidth/40*35,displayHeight/20)
        textSize(displayWidth/60)
        fill(0)
        text("Formation: "+str(formNum+1), displayWidth/3,displayHeight/20)
        if archerX and soldierX:
            for i in range(len(archerX)):
                if (dist(soldierX[i-1],soldierY[i-1],archerX[i-1],archerY[i-1]) < displayWidth / 5):
                    line(soldierX[i-1],soldierY[i-1],archerX[i-1],archerY[i-1])     
                    print("Hit Soldier #"+str(i-1))
                    soldierX.pop(i-1)
                    soldierY.pop(i-1) 
    elif gameMode == 1:
        framesStopped += 1
        if framesStopped == 60:
            gameMode = 0
            hp = 100
            framesStopped = 0
            frames = 0
            waveNum = 0
        background(0)
        textSize(displayWidth/15)
        fill(255)
        text("  Game\n   Over\n\nScore: "+str(waveNum*frames), displayWidth/3, displayHeight/3)
    else:
        background(0)
        textSize(64)
        fill(255)
        text("Error x00001, gameMode var out of range", displayWidth/10, displayHeight/2)
     
def mouseClicked():
    global gameMode, frames
    print("Clicked")
    if mouseX>displayWidth*0.8:
        if frames >100:
            archerX.append(mouseX-25)
            archerY.append(mouseY-50)
            frames += -100
    else:
        #print("Clicked")
        for i in range(len(soldierX)-1):
            #print("HI, "+str(dist(soldierX[i-1]*displayWidth/100, soldierY[i-1]*displayWidth/20,mouseX, mouseY)))
            print(i)
            if dist((int(soldierX[i-1])*displayWidth/100), (int(soldierY[i-1])*displayHeight/20),mouseX, mouseY)<(displayWidth/19.2):
                print("Hit Soldier #"+str(i))
                soldierX.pop(i-1)
                soldierY.pop(i-1)
             
