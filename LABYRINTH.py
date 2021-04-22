      #####################################################################
      #                             LABYRINTH                             #
      #                    ******************************                 #
      #                           NAME: JENNY WANG                        #
      #                           COURSE: ICS 3UI                         #
      #                        TEACHER: MR. SCHATTMAN                     #
      #####################################################################


from tkinter import *
from math import *
from time import *
from random import *
import winsound

root = Tk()
s = Canvas(root, width = 720, height = 720, background = "black")
#Canvas is black so that the maze isn't visible (the maze is black too)


#SET INITIAL VALUES
def setInitialValues():

    global playAgain, helper, startGame, endGame, monxSpeed, monySpeed, xEye, yEye, r, eyer, scoreCount, score, timeStart, gameTime, clockDisplay, xBall, yBall, ballRadius, ballColour, xMouse, yMouse, xSpeed, ySpeed, maxSpeed, ball, Qpressed, xEnd, yEnd
    global monSpeed, monSpeedEasy, monSpeedNormal, monSpeedHard, eyer, xMon, yMon, xEye, yEye, frame, diff, light, easyTime, normalTime, hardTime, easyLight, normalLight, hardLight, xCircle, yCircle, xCircle2, yCircle2, rad

    #Values for the ball "character" that is controlled by the player
    xBall = 30
    yBall = 30
    xEnd = 630
    yEnd = 690
    ballRadius = 20
    ballColour = "black"
    xMouse = 0
    yMouse = 0
    xSpeed = 0
    ySpeed = 0
    maxSpeed = 5
    ball = 0
    light = 0
     
    #Timer and Scoreboard
    gameTime = 0
    clockDisplay =  s.create_text( 680, 30, text=" ", font="Monaco 15", fill="white")
    scoreCount = s.create_text( 650, 30, text = "0" + "   " , font = "Monaco 15", fill="white")
    score = 0
    timeStart = time()
    
    timeStart = time()        
    clockDisplay = 0
    
    #Boolean values for starting game, difficulty screen, end screen,
    #help screen, and going back to the start screen
    startGame = False
    endGame = False
    diff = False
    helper = False
    playAgain = False

    #Things drawn on the help screen
    xCircle = 220
    yCircle = 310
    xCircle2 = 500
    yCircle2 = 310
    rad = 20
    
    #Different times for each level
    easyTime = 46
    normalTime = 31
    hardTime = 21

    #Different radius of vision for each level
    easyLight = 100
    normalLight = 70
    hardLight = 40

    #Monster initial placement values
    xMon = 360
    yMon = 360
    xEye = 350
    yEye = 350
    eyer = 7
    r = 30
    frame = 50

    #Speed of monster for each level
    monSpeedEasy = 1
    monSpeedNormal = 2
    monSpeedHard = 3
    monSpeed = 0


#Starting Screen
def startScreen():
    global menu, bg, play, playText, title, title2, helpButton, helpText
   
    bg = s.create_rectangle(0, 0, 720, 720, fill = "black")

    #Play Button    
    play = s.create_rectangle(275, 360, 425, 440, fill = "black", activefill = "white", outline = "white")
    playText = s.create_text(350, 400, text = "PLAY", font = "Hev 30", fill = "black", activefill = "white")

    #Title
    title = s.create_text(360, 200, text = "LABYRINTH", font = "Monaco 70 bold", fill = "white", activefill = "red")

    #Help Button
    helpButton = s.create_rectangle(275, 460, 425, 540, fill = "black", activefill = "white", outline = "white")
    helpText = s.create_text(350, 500, text = "HELP", font = "Hev 30", fill = "black", activefill = "white")

    s.update()
    s.delete(bg, play, playText, title, helpButton, helpText)


#Help Screen
def helpScreen():
    global bg2, arrow, ball1, ball2, text1, text2, text3, text4, text5, text6, text7, backButton

    bg2 = s.create_rectangle(0, 0, 720, 720, fill = "black")

    #Intruction Pictures
    ball1 = s.create_oval(xCircle-rad, yCircle-rad, xCircle+rad, yCircle+rad, fill = "black", activefill = "white", outline = "white")
    ball2 = s.create_oval(xCircle2-rad, yCircle2-rad, xCircle2+rad, yCircle2+rad, fill = "white", activefill = "black", outline = "white")
    arrow = s.create_text(360, 310, text = "\u21e8", fill = "white", activefill = "red", font = "Hev 50")

    #Writing Instructions
    text1 = s.create_text(360, 100, text = "HELP", font = "Hev 70", fill = "white", activefill = "red") 
    text2 = s.create_text(360, 200, text = "Using the W A S D or arrow keys, get your ", font = "Hev 20", fill = "white")
    text3 = s.create_text(360, 240, text = "character (the black ball) to the white circle.", font = "Hev 20", fill = "white")
    text4 = s.create_text(360, 380, text = "Watch out for the labyrinth monster!", font = "Hev 20", fill = "white")
    text5 = s.create_text(360, 420, text = "If you touch him it's GAME OVER.", font = "Hev 20", fill = "white", activefill = "red")
    text6 = s.create_text(360, 480, text = "The time limit, amount of the maze visible and labryinth ", font = "Hev 20", fill = "white")
    text7 = s.create_text(360, 520, text = "monster speed varies on which difficulty you choose.", font = "Hev 20", fill = "white")
    text8 = s.create_text(360, 580, text = "If you reach the white circle within the time limit", font = "Hev 20", fill = "white")
    text9 = s.create_text(360, 620, text = "you will gain a point and get your time limit reset.", font = "Hev 20", fill = "white")

    #Back to start screen
    backButton = s.create_text(100, 680, text = "\u2b05", fill = "white", activefill = "red", font = "Hev 80 bold")

    s.update()
    s.delete(bg2, text1, text2, text3, ball1, ball2, arrow, text4, text5, text6, text7, text8, text9, backButton)
    

#Difficulty Screen
def diffScreen():

    bg4 = s.create_rectangle(0, 0, 720, 720, fill = "black")

    #Title    
    difficulty = s.create_text(360, 100, text = "SELECT A DIFFICULTY", font = "Monaco 40 bold", fill = "white", activefill = "red")

    #Easy Button and description
    easy = s.create_rectangle(270, 200, 450, 300, fill = "black", activefill = "white", outline = "white")
    easyText = s.create_text(360, 250, text = "EASY", font = "Hev 30", fill = "black", activefill = "white")
    easyLevel = s.create_text(150, 250, text = "45 seconds", font = "Monaco 20 bold", fill = "dark slate gray", activefill = "white")
    easySee = s.create_text(570, 250, text = "Large Vision", font = "Monaco 20 bold", fill = "dark slate gray", activefill = "white")

    #Normal Button and description
    normal = s.create_rectangle(270, 350, 450, 450, fill = "black", activefill = "white", outline = "white")
    normalText = s.create_text(360, 400, text = "NORMAL", font = "Hev 27", fill = "black", activefill = "white")
    normalLevel = s.create_text(150, 400, text = "30 seconds", font = "Monaco 20 bold", fill = "dark slate gray", activefill = "white")
    normalSee = s.create_text(590, 400, text = "Moderate Vision", font = "Monaco 20 bold", fill = "dark slate gray", activefill = "white")

    #Hard Button and description
    hard = s.create_rectangle(270, 500, 450, 600, fill = "black", activefill = "red", outline = "white")
    hardText = s.create_text(360, 550, text = "HARD", font = "Hev 30", fill = "black", activefill = "white")
    hardLevel = s.create_text(150, 550, text = "20 seconds", font = "Monaco 20 bold", fill = "dark slate gray", activefill = "white")
    hardSee = s.create_text(570, 550, text = "Little Vision", font = "Monaco 20 bold", fill = "dark slate gray", activefill = "white")

    #Back to start screen
    back = s.create_text(70, 670, text = "\u2b05", fill = "white", activefill = "red", font = "Hev 80 bold")

    s.update()
    s.delete(easySee, normalSee, hardSee, easyLevel, normalLevel, hardLevel, bg4, difficulty, easy, easyText, normal, normalText, hard, hardText, back)


#Retry Menu after game over
def retryMenu():
    global bg3, quitting, retry, retryText, quittingText, endGame, finalScore    

    bg3 = s.create_rectangle(0, 0, 720, 720, fill = "black")

    #Retry Button
    retry = s.create_rectangle(100, 300, 300, 400, fill = "black", activefill = "white", outline = "white")
    retryText = s.create_text(200, 350, text = "RETRY", font = "Helv 30", fill = "black", activefill = "white")

    #Quit Button
    quitting = s.create_rectangle(400, 300, 600, 400, fill = "black", activefill = "white", outline = "white")
    quittingText = s.create_text(500, 350, text = "QUIT", font = "Helv 30", fill = "black", activefill = "white")

    #GAME OVER Text
    over = s.create_text( 360, 150, text="GAME OVER", anchor=CENTER, font="Helv 60", fill = "red", activefill = "white")

    #Gives player their final score
    finalScore = s.create_text(360, 500, text = "YOUR FINAL SCORE IS: " + str(score), font = "Monaco 30 bold", fill = "white")

    s.update()
    s.delete(bg3, retry, retryText, quitting, quittingText, finalScore, over)

   
#Test if mouse clicks the ball    
def mouseInsideBall():  
    dist = sqrt( (yMouse-yBall)**2 + (xMouse-xBall)**2 )

    if dist < ballRadius:
        return True
    
    else:
        return False
    

#Tests for mouse clicks during certain times
def mouseClickHandler( event ):

    global monSpeed, diff, easyTime, normalTime, hardTime, easyLight, normalLight, hardLight, light, diff, gameTime, initialGameTime, xMouse, yMouse, ballColour, helper, menu, startGame, endGame, playAgain
        
    xMouse = event.x
    yMouse = event.y

    #Click detection for buttons at the help screen
    if helper == True:
        if 50 < event.x < 150 and 670 < event.y < 690:
            helper = False

    #Click detection for buttons at the retry screen
    elif endGame == True:
        if 100 < event.x < 300 and 300 < event.y < 400:
            playAgain = True          
        
        elif 400 < event.x < 600 and 300 < event.y < 400:
            stopGame()

    #Click detection for buttons at the difficulty screen
    elif diff == True:
        
        if 270 < event.x < 450 and 200 < event.y < 300:
            gameTime = easyTime
            initialGameTime = easyTime
            light = easyLight
            monSpeed = monSpeedEasy
            startGame = True
            diff = False
            
        elif 270 < event.x < 450 and 350 < event.y < 450:
            gameTime = normalTime
            initialGameTime = normalTime
            light = normalLight
            monSpeed = monSpeedNormal
            startGame = True
            diff = False

        elif 270 < event.x < 450 and 500 < event.y < 600:
            gameTime = hardTime
            initialGameTime = hardTime
            light = hardLight
            monSpeed = monSpeedHard
            startGame = True
            diff = False

        elif 50 < event.x < 90 and 655 < event.y < 685:
            diff = False

    #Click detection for buttons at the start screen    
    else: 
        if 275 < event.x < 425 and 360 < event.y < 440:
            diff = True
            
        elif 275 < event.x < 425 and 460 < event.y < 540:
            helper = True 
    
    #In game ball changes colour when clicked
    if mouseInsideBall() == True: 
        ballColour = choice( ["red", "cyan", "medium spring green", "black", "hot pink", "orchid", "yellow", "white"] )
    

#Controls for how the ball is moved
def keyDownHandler( event ):
    global xSpeed, ySpeed, Qpressed  
    
    if event.keysym == "a" or event.keysym == "A" or event.keysym == "Left": 
        xSpeed = -maxSpeed
        
    elif event.keysym == "d" or event.keysym == "D" or event.keysym == "Right":  
        xSpeed = maxSpeed

    elif event.keysym == "w" or event.keysym == "W" or event.keysym == "Up":
        ySpeed = -maxSpeed

    elif event.keysym == "s" or event.keysym == "S" or event.keysym == "Down":
        ySpeed = maxSpeed


#When keys are not pushed ball is not moving
def keyUpHandler( event ):
    global xSpeed, ySpeed

    xSpeed = 0
    ySpeed = 0


#Hit detection for if you hit a monster (game over)
def monsterHit():
    global xBall, yBall, xMon, yMon, endGame, startGame

    monDist = getDist(xBall, yBall, xMon, yMon)

    if monDist <= 50:
        startGame = False
        endGame = True


#Draws the Monster and makes its movements
def drawMonster():
    global body, eye1, eye2, frame, move, xMon, yMon, xEye, yEye, monSpeed

    x = []   

    #Hit detection so that the monster doesn't go off the screen
    if xMon-r > 50*monSpeed:
        x.append("left")

    if yMon-r > 50*monSpeed:
        x.append("up")

    if xMon+r < 710 - 50*monSpeed:
        x.append("right")

    if yMon+r < 710 - 50*monSpeed:
        x.append("down")

    #Random movement of he monster    
    if frame >= 50:
        frame = 0
        move = choice(x)
        
    elif move == "up":
        frame = frame + monSpeed
        yMon = yMon - monSpeed
        yEye = yEye - monSpeed

    elif move == "down":
        frame = frame + monSpeed
        yMon = yMon + monSpeed
        yEye = yEye + monSpeed

    elif move == "right":
        frame = frame + monSpeed
        xMon = xMon + monSpeed
        xEye = xEye + monSpeed

    elif move == "left":
        frame = frame + monSpeed
        xMon = xMon - monSpeed
        xEye = xEye - monSpeed


    #Drawing the monster
    body = s.create_oval(xMon-r, yMon-r, xMon+r, yMon+r, fill = "black")
    eye1 = s.create_oval(xEye-eyer, yEye-eyer, xEye+eyer, yEye+eyer, fill = "yellow")
    eye2 = s.create_oval(xEye+20-eyer, yEye-eyer, xEye+20+eyer, yEye+eyer, fill = "yellow")
    

#Detects if the ball being controled reached its goal (the white ball)
def endMaze():
    distEnd = getDist(xBall, yBall, xEnd, yEnd)
        
    if distEnd <= 40:
        return True
    
    else:
        return False
    

#Creates Scorboard and counts the score
def drawScore():
    global scoreCount

    s.delete(scoreCount)    
    scoreCount = s.create_text( 570, 30, text = str(score) + "   " , font = "Monaco 15", fill="white")
    s.update()    


#Detects if the white circle is reached. Resets timer and increases score. Puts new white circle randomly on the map
def finishMaze():
    global xEnd, yEnd, ended, gameTime, score, initialGameTime

    ended = 0

    if endMaze() == True:
        xEnd = randint(30, 690)
        yEnd = randint(30, 690)       
        ended = s.create_oval(xEnd-ballRadius, yEnd-ballRadius, xEnd+ballRadius, yEnd+ballRadius, fill = "white", outline = "white")
        gameTime = initialGameTime
        score = score + 1


#Finds distance between 2 points
def getDist( x1, y1, x2, y2 ):
    return sqrt( (x2-x1)**2 + (y2-y1)**2 )


#Hit detection for sides of the screen, updates ball position
def updateBallPosition():
    global xBall, yBall, xSpeed, ySpeed

    if xBall-ballRadius <= 0: 
       xBall = 20 

    if yBall-ballRadius <= 0: 
       yBall = 20

    if xBall+ballRadius > 720: 
       xBall = 700 

    if yBall+ballRadius > 720:
       yBall = 700

                
    xBall = xBall + xSpeed
    yBall = yBall + ySpeed
      

#Draws the ball and "circle of light" around it
def drawBall():
    global ball, ballLight, light

    ballLight = s.create_oval(xBall-ballRadius-light, yBall-ballRadius-light, xBall+ballRadius+light, yBall+ballRadius+light, fill = "white")    
    ball = s.create_oval(xBall-ballRadius, yBall-ballRadius, xBall + ballRadius, yBall+ballRadius, fill = ballColour)


#Draws the timer and updates the time
def redrawGameClock():
      global clockDisplay, gameTime
      
      s.delete( clockDisplay )

      if gameTime > 10:
          clockDisplay = s.create_text( 700, 30, text=str( gameTime ) + "   " , font="Monaco 15", fill="white")

      else:
          clockDisplay = s.create_text( 700, 30, text=str( gameTime ) + "   " , font="Monaco 15", fill="red")
          

#Stops the game, quits program
def stopGame():
    sleep(1)
    root.destroy()


#Draws the maze
def drawEasyMaze():
    global maze, x1, y1, x2, y2, end, scoreBoard, timeBoard

    #Each wall coordinate is organized in rows so that it's easy to keep track of
    maze = []
    x1 = [0, 60, 120, 240, 480, 540, 660  , 120, 240, 600, 300, 0,   360, 600, 360, 420, 600, 60,  660, 120, 300,  60, 180, 360, 480, 180, 300, 540, 0,   180, 540, 0,   180, 300, 600, 360, 420, 660, 0,   120, 600, 60,  240, 600, 120, 240, 660, 480, 660, 60,  480, 360, 300, 0,   300, 420, 60,  180, 120, 240, 420, 480, 600, 660, 240, 360, 540, 180, 300, 480, 180, 540]
    y1 = [0,  0,   0,   0,   60,  0,   0  ,  60,  60,  60,  60, 120, 120, 120, 120, 120, 120, 180, 180, 180, 180, 240, 240, 240, 240, 240, 240, 240, 300, 300, 300, 300, 300, 360, 300, 240, 240, 180, 360, 360, 360, 360, 360, 360, 420, 420, 420, 420, 420, 480, 480, 420, 480, 540, 540, 540, 540, 540, 600, 600, 600, 600, 600, 600, 600, 600, 600, 660, 660, 660, 660, 660]
    x2 = [0, 60, 120, 240, 480, 540, 660  , 180, 420, 660, 300, 240, 420, 720, 360, 420, 600, 360, 720, 120, 300,  60, 240, 420, 540, 180, 300, 540, 60,  300, 660, 60,  240, 480, 660, 360, 420, 660, 60,  240, 660, 60,  240, 600, 180, 360, 720, 480, 660, 180, 540, 360, 300, 180, 360, 660, 60,  180, 120, 240, 420, 480, 600, 660, 300, 420, 600, 240, 360, 600, 180, 540]
    y2 = [720, 60, 60, 60, 300, 180, 60   ,  60,   60,  60, 120, 120, 120, 120, 180, 180, 240, 180, 180, 420, 360, 300, 240, 240, 240, 300, 300, 480, 300, 300, 300, 300, 300, 360, 300, 300, 540, 240, 360, 360, 360, 480, 540, 540, 420, 420, 420, 480, 480, 480, 480, 480, 660, 540, 540, 540, 660, 600, 720, 660, 720, 660, 660, 720, 600, 600, 600, 660, 660, 660, 720, 720]


    for i in range(len(x1)):
        maze.append(0)
        maze[i] = s.create_line(x1[i], y1[i], x2[i], y2[i], fill = "black", width = 5)

    #Creates initial white circle endpoint, scoreboard and timeboard
    end = s.create_oval(xEnd-ballRadius, yEnd-ballRadius, xEnd+ballRadius, yEnd+ballRadius, fill = "white", outline = "white")
    scoreBoard = s.create_text( 520, 30, text = "Score:" + "   " , font = "Monaco 15", fill="white")
    timeBoard = s.create_text( 640, 30, text = "Time:" + "   " , font = "Monaco 15", fill="white")


#Wall hit detection for your character ball    
def hitWall():
    global xBall, yBall

    #In range of number of walls there are
    for i in range(len(x1)):
        
        #If side of ball touches wall, it's position is set back 5 pixels (takes wall values from array in drawEasyMaze())
        #Detection for left side of ball
        if xBall - ballRadius == x1[i] and y1[i]-ballRadius <= yBall <= y2[i]+ballRadius:
            xBall = x1[i] + ballRadius + 5
        elif xBall - ballRadius == x2[i] and y1[i]-ballRadius <= yBall <= y2[i]+ballRadius:
            xBall = x2[i] + ballRadius + 5

        #Detection for right side of ball
        if xBall + ballRadius == x1[i] and y1[i]-ballRadius <= yBall <= y2[i]+ballRadius:
            xBall = x1[i] - ballRadius - 5
        elif xBall + ballRadius == x2[i] and y1[i]-ballRadius <= yBall <= y2[i]+ballRadius:
            xBall = x2[i] - ballRadius - 5

        #Detection for top side of ball
        if yBall - ballRadius == y1[i] and x1[i]-ballRadius <= xBall <= x2[i]+ballRadius:
            yBall = y1[i] + ballRadius + 5
        elif yBall - ballRadius == y2[i] and x1[i]-ballRadius <= xBall <= x2[i]+ballRadius:
            yBall = y2[i] + ballRadius + 5

        #Detection for bottom side of ball
        if yBall + ballRadius == y1[i] and x1[i]-ballRadius <= xBall <= x2[i]+ballRadius:
            yBall = y1[i] - ballRadius - 5
        elif yBall + ballRadius == y2[i] and x1[i]-ballRadius <= xBall <= x2[i]+ballRadius:
            yBall = y2[i] - ballRadius - 5


#Runs the game
def runGame():
    global gameTime, timeStart, clockDisplay, playAgain, endGame, startGame, diff

    #playAgain detects whether the game is running or not    
    playAgain = True
    
    while playAgain == True:
        setInitialValues()

        #Start menu button paths
        while startGame == False:

            if helper == True:
                helpScreen()

            elif diff == True:
                diffScreen()
                
            else:
                startScreen()
            
        #When your timer hasn't reached 0 and the game is still running                
        while startGame == True and gameTime > 0:
            updateBallPosition() 
            drawBall()
            drawEasyMaze()
            hitWall()
            endMaze()
            drawMonster()
            drawScore()
            monsterHit()
            finishMaze()
            s.update()
            sleep(0.01)
            s.delete(ball, ballLight, end, ended, scoreBoard, timeBoard, eye1, eye2, body)

            #Deletes maze every frame (prevents lag)            
            for i in range(len(x1)):
                s.delete(maze[i])

            #Timer                
            timeNow = time()
            timeElapsedSinceLastCheck = timeNow - timeStart

            if timeElapsedSinceLastCheck >= 1:  
                gameTime = gameTime - 1

                if gameTime < 0:
                      endGame = True

                else:
                    redrawGameClock()
                                
                timeStart = time()        

        s.delete(all)
        s.delete(clockDisplay, scoreCount)

        #When retry button is clicked, restarts the game to the start screen
        #playAgain is set to false when game is lost
        while playAgain == False:
            endGame = True
            retryMenu()


#After 0 seconds, runs the game   
root.after(0, runGame)

s.bind( "<Button-1>", mouseClickHandler)

s.bind( "<Key>", keyDownHandler)

s.bind( "<KeyRelease>", keyUpHandler)

s.pack()
s.focus_set()
root.mainloop()
