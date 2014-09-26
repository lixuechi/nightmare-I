# Nightmare interface 1

import pygame, sys
from pygame.locals import *
  
FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()


HORIZON_WIDTH = 3775
SALTICON_WIDTH = 49
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLACK = (  0,   0,   0)
BLACK_OPAQUE = (  0,   0,   0,  125)
LEFT = 'left'
RIGHT = 'right'
ALIVE = 'alive'
DEAD = 'dead'

startX = 100
startY = 200
START_SPEED = 10
FLOW_SPEED = 1
PLAYER_WIDTH = 94
PLAYER_HEIGHT = 100
SALT_WIDTH = 49
SALT_HEIGHT = 56
GSIZE = 1
PMWM = 20 # PAUSE_MENU_WIDTH_MARGIN
PMHM = 25 # PAUSE_MENU_HEIGHT_MARGIN
PMI  = 50 # PAUSE_MENU_ICON_WIDTH_AND_HEIGHT
PM_LEFT = 227 # the left x coordinate of the pause menu
PM_TOP = 200 # the top y coordinate of the pause menu
PM_WIDTH = 300 # the width of the pause menu
PM_HEIGHT = 100 # the height of the pause menu
CAMERASLACK = 200     # how far from the center the player moves before moving the camera
WINWIDTH = 755
WINHEIGHT = 560
HALF_WINWIDTH = 375
HALF_WINHEIGHT = 280
hasSaltNum = 0 # the number of salt that the player currently has
START_SALTNUM = 0
WIN_WIDTH = 755
throwSaltAniX = 200
throwSaltAniY = 200

  
def main():
    global DISPLAYSURF, woman1Obj, woman1X, woman1Y, WOMAN_WIDTH, WOMAN_HEIGHT, womanObjs1, womanLImg, womanRImg, chainX, chainShow, throwSaltAni1, throwSaltAni2, throwSaltAni3, throwSaltAni4, throwSaltAni5, chainImg, FPSCLOCK, STARTSIZE, chainX, chainY, mouseX, mouseY, saltObjs1, saltObjs2, playerObj, saltIconX, saltIconY, lifeX, lifeY, lifeBarX, lifeBarY, playerX, playerY, chainImg, chainX, chainY, chainShow, pauseClicked, mouseClicked, PAUSE_WIDTH, PAUSE_HEIGHT, PAUSE_X, PAUSE_Y, playerObj, playerLImg, playerRImg, saltIconImg, saltImg, pauseImg, bgImg, lifeImg, lifeBarImg, horizon1Img

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((755, 560))
    pygame.display.set_caption('Nightmare interface 1')
    
    playerRImg = pygame.image.load('gr.png')
    playerLImg = pygame.image.load('gl.png')
    STARTSIZE = 100
    chainImg = pygame.image.load('chain2.png')
    chainX = 360

    womanLImg = pygame.image.load('fl.png')
    womanRImg = pygame.image.load('fr.png')
    WOMAN_WIDTH = 89
    WOMAN_HEIGHT = 100
    woman1X = 930
    woman1Y = 390
                                  
    throwSaltAni1 = pygame.image.load('blooddrop1.png')
    throwSaltAni2 = pygame.image.load('blooddrop2.png')
    throwSaltAni3 = pygame.image.load('blooddrop3.png')
    throwSaltAni4 = pygame.image.load('blooddrop4.png')
    throwSaltAni5 = pygame.image.load('blooddrop5.png')
    
    saltImg = pygame.image.load('saltObj.png')
    playerX = 200
    playerY = 400

    saltObjs1 = [] # stores salt1
    saltObjs2 = [] # stores salt2

    #womanObjs1 = [] # stores woman1
    woman1Obj = {'surface': pygame.transform.scale(womanLImg, (woman1X, woman1Y)),
                 'facing': LEFT,
                 'x': woman1X,
                 'y': woman1Y,
                 'width': WOMAN_WIDTH,
                 'height': WOMAN_HEIGHT,
                 'status': ALIVE,
                 'walkCounter': 0}
    
    playerObj = {'surface': pygame.transform.scale(playerRImg, (STARTSIZE, STARTSIZE)),
                 'facing': RIGHT,
                 'x': playerX,
                 'y': playerY,
                 'width': PLAYER_WIDTH,
                 'height': PLAYER_HEIGHT,
                 'saltNum': START_SALTNUM,
                 'thrownSaltNum': 0}
    
    fontObj = pygame.font.Font('freesansbold.ttf', 10)
    textSurfaceObj = fontObj.render('Ghost', True, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (200, 10)
 
    while True:
        runGame()
    
    # showStartScreen()
    # while True:
    #   runGame()
    #   showGameOverScreen()


def runGame():

    moveLeft = False
    moveRight = False
    pauseClicked = False
    salt1Exist = True
    salt2Exist = True

    woman1Alive = True
    womanWalkCounterL = 20 # walk counter of going left
    womanWalkCounterR = 20 # walk counter of going right 

    direction = RIGHT
    mouseX = 0 # used to store x coordinate of mouse event
    mouseY = 0 # used to store y coordinate of mouse event
    
    chainY = -220
    chainShow = False
    saltIconImg = pygame.image.load('saltObj.png')
    dashSaltIconImg = pygame.image.load('dashSaltIcon.png')
    saltIconX = 10
    saltIconY = 25
    pauseImg = pygame.image.load('pause.png')
    PAUSE_X = 680
    PAUSE_Y = 30
    PAUSE_WIDTH = 44
    PAUSE_HEIGHT = 44
    bgImg = pygame.image.load('bg4_3.png')
    lifeImg = pygame.image.load('ghost_right.png')
    lifeX = 400
    lifeY = 25
    lifeBarImg = pygame.image.load('lifebar.png')
    lifeBarX = 450
    lifeBarY = 50
    horizon1Img = pygame.image.load('horizonI.png')
    horizonX = 0
    horizonY = 0
    resumeIconImg = pygame.image.load('play.png')
    resumeIconX = PM_LEFT + PMWM
    resumeIconY = PM_TOP + PMHM
    settingIconImg = pygame.image.load('setting.png')
    settingIconX = PM_LEFT + PMWM + PMI + PMWM
    settingIconY = PM_TOP + PMHM
    replayIconImg = pygame.image.load('replay.png')
    replayIconX = settingIconX + PMI + PMWM
    replayIconY = PM_TOP + PMHM
    mainIconImg = pygame.image.load('main.png')
    mainIconX = replayIconX + PMI + PMWM
    mainIconY = PM_TOP + PMHM
    resumeClicked = False
    settingClicked = False
    replayClicked = False
    mainClicked = False

    # cameraX and cameraY are the top left of where the camera view is
    cameraX = 0
    cameraY = 0

    # salt numbers and boolean toggles
    totalSaltNum = 6 # the total number of salt in this level
    
    mouseSelection = None # stores the (x, y) of the icon clicked

    while True: # main game loop
        mouseClicked = False
        
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(bgImg, (0, 0))

        if playerObj['facing'] == RIGHT:
            throwSaltX = playerObj['x'] + playerObj['width'] - cameraX
        elif playerObj['facing'] == LEFT:
            throwSaltX = playerObj['x'] - 50 - cameraX
        throwSaltY = playerObj['y'] + 20

        
        DISPLAYSURF.blit(pauseImg, (PAUSE_X, PAUSE_Y))
         # DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        DISPLAYSURF.blit(lifeImg, (lifeX, lifeY))
        DISPLAYSURF.blit(lifeBarImg, (lifeBarX, lifeBarY))
        DISPLAYSURF.blit(horizon1Img, (-cameraX, -cameraY))

        # adjust cameraX and cameraY if beyond the "camera slack"
        playerCenterX = playerObj['x'] + int(playerObj['width'] / 2)
        playerCenterY = playerObj['y'] + int(playerObj['height'] / 2)

        if playerCenterX > CAMERASLACK and playerCenterX < (HORIZON_WIDTH - CAMERASLACK):
            if (cameraX + HALF_WINWIDTH) - playerCenterX > CAMERASLACK:
                cameraX = playerCenterX + CAMERASLACK - HALF_WINWIDTH
                
            elif playerCenterX - (cameraX + HALF_WINWIDTH) > CAMERASLACK:
                cameraX = playerCenterX - CAMERASLACK - HALF_WINWIDTH
            if (cameraY + HALF_WINHEIGHT) - playerCenterY > CAMERASLACK:
                cameraY = playerCenterY + CAMERASLACK - HALF_WINHEIGHT
            elif playerCenterY - (cameraY + HALF_WINHEIGHT) > CAMERASLACK:
                cameraY = playerCenterY - CAMERASLACK - HALF_WINHEIGHT



        # draw the player
        playerObj['rect'] = pygame.Rect( (playerObj['x'] - cameraX,
                                          playerObj['y'] - cameraY,
                                          playerObj['width'],
                                          playerObj['height']) )
        DISPLAYSURF.blit(playerObj['surface'], playerObj['rect'])

        if salt1Exist:
            for saltObj in saltObjs1:
                saltObj['width'] = SALT_WIDTH
                saltObj['height'] = SALT_HEIGHT
                saltObj['rect'] = pygame.Rect( (saltObj['x'] - cameraX,
                                                saltObj['y'],
                                                saltObj['width'],
                                                saltObj['height']) )
                DISPLAYSURF.blit(saltImg, saltObj['rect'])
        
        if salt2Exist:
            for saltObj in saltObjs2:
                saltObj['width'] = SALT_WIDTH
                saltObj['height'] = SALT_HEIGHT
                saltObj['rect'] = pygame.Rect( (saltObj['x'] - cameraX,
                                                saltObj['y'],
                                                saltObj['width'],
                                                saltObj['height']) )
                DISPLAYSURF.blit(saltImg, saltObj['rect'])

        if woman1Alive:
            if woman1Obj['facing'] == LEFT:
                if womanWalkCounterL > 0:
                    woman1Obj['x'] -= 5
                    womanWalkCounterL -= 1
                    DISPLAYSURF.blit(womanLImg, (woman1Obj['x'] - cameraX, woman1Obj['y']))
                elif womanWalkCounterL <= 0:
                    woman1Obj['facing'] = RIGHT
                    womanWalkCounterL = 20
            if woman1Obj['facing'] == RIGHT:
                if womanWalkCounterR > 0:
                    woman1Obj['x'] += 5
                    womanWalkCounterR -= 1
                    DISPLAYSURF.blit(womanRImg, (woman1Obj['x'] - cameraX, woman1Obj['y']))
                elif womanWalkCounterR <= 0:
                    woman1Obj['facing'] = LEFT
                    womanWalkCounterR = 20

        # women's direction:
        if woman1Obj['facing'] == LEFT:
            woman1Obj['surface'] = pygame.transform.scale(womanLImg, (woman1Obj['x'], woman1Obj['y']))
        elif woman1Obj['facing'] == RIGHT:
            woman1Obj['surface'] = pygame.transform.scale(womanRImg, (woman1Obj['x'], woman1Obj['y']))
            
            #for womObj in womanObjs1:
            #    womObj['width'] = WOMAN_WIDTH
            #    womObj['height'] = WOMAN_HEIGHT
            #    womObj['rect'] = pygame.Rect( (womObj['x'] - cameraX,
            #                                womObj['y'],
            #                                womObj['width'],
            #                                womObj['height']) )
                
                
            #womObj['x'] -= 10
            #pygame.display.update()
            #DISPLAYSURF.blit(womanLImg, womObj['rect'])
        

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    direction = LEFT
                    playerObj['facing'] = LEFT
                    moveLeft = True
                    moveRight = False
                    
                elif event.key == K_RIGHT:
                    direction = RIGHT
                    playerObj['facing'] = RIGHT
                    moveRight = True
                    moveLeft = False

                elif event.key == K_SPACE:
                    if playerObj['saltNum'] > 0:
                        playerObj['saltNum'] -= 1
                        playerObj['thrownSaltNum'] += 1
                        # test drop salt animation
                        throwSaltAnimation(throwSaltX, throwSaltY)
                    
               
            elif event.type == KEYUP:
                # stop moving the player
                if event.key == K_LEFT:
                    moveLeft = False
                elif event.key == K_RIGHT:
                    moveRight = False

            elif event.type == MOUSEMOTION:
                mouseX, mouseY = event.pos

            elif event.type == MOUSEBUTTONUP:
                mouseX, mouseY = event.pos
                mouseClicked = True

        if moveLeft:
            playerObj['surface'] = pygame.transform.scale(playerLImg, (STARTSIZE, STARTSIZE))
            playerObj['x'] -= START_SPEED
            
            
        if moveRight:
            playerObj['surface'] = pygame.transform.scale(playerRImg, (STARTSIZE, STARTSIZE))
            playerObj['x'] += START_SPEED
            

        if salt1Exist:
            saltObjs1.append(drawNewSalt(40, 430))
        if salt2Exist:
            saltObjs2.append(drawNewSalt(460, 430))

        #if woman1Alive:
            #womanObjs1.append(drawNewWoman(900, 390))

        if salt1Exist:
            # check if the player has collided with salt1
            saObj1 = saltObjs1[0]
            if 'rect' in saObj1 and playerObj['rect'].colliderect(saObj1['rect']):
                # a player/salt collision has occurred
                # the player picks up the salt
                del saltObjs1[0]
                playerObj['saltNum'] += 1
                salt1Exist = False
        
        if salt2Exist:
            # check if the player has collided with salt2
            saObj2 = saltObjs2[0]
            if 'rect' in saObj2 and playerObj['rect'].colliderect(saObj2['rect']):
                # a player/salt collision has occurred
                # the player picks up salt2
                del saltObjs2[0]
                playerObj['saltNum'] += 1
                salt2Exist = False
        

        # the interactive salt panel
        indexS = 0 # the index of the salt icons

        if hasSaltNum <= (totalSaltNum - playerObj['thrownSaltNum']):
            while indexS < playerObj['saltNum'] : # draw the filled salt icons
                DISPLAYSURF.blit(saltIconImg, (saltIconX + indexS * SALTICON_WIDTH, saltIconY))
                indexS += 1

            while indexS < (totalSaltNum - playerObj['thrownSaltNum']): # draw the hollow salt icons
                DISPLAYSURF.blit(dashSaltIconImg, (saltIconX + indexS * SALTICON_WIDTH, saltIconY))
                indexS += 1

        # the functions of the pause icon
        boxRect = pygame.Rect(PAUSE_X, PAUSE_Y, PAUSE_WIDTH, PAUSE_HEIGHT)
        if boxRect.collidepoint(mouseX, mouseY) and mouseClicked:
            pauseClicked = True
            drawMenu = True
        elif boxRect.collidepoint(mouseX, mouseY):
            drawHighlightBox(PAUSE_X, PAUSE_Y, PAUSE_WIDTH, PAUSE_HEIGHT, WHITE)
            # the mouse is currently over a box

        if pauseClicked == True:
            # show the chain:
            chainShow = True
            if chainShow:
                chainAnimation(chainY)
                chainShow = False
            
                
            
            # show the black panel and icons:
            if drawMenu == True:               
                pausePanel = pygame.draw.rect(DISPLAYSURF, BLACK, (PM_LEFT, PM_TOP, PM_WIDTH, PM_HEIGHT))
                DISPLAYSURF.blit(resumeIconImg, (resumeIconX, resumeIconY))
                DISPLAYSURF.blit(settingIconImg, (settingIconX, settingIconY))
                DISPLAYSURF.blit(replayIconImg, (replayIconX, replayIconY))
                DISPLAYSURF.blit(mainIconImg, (mainIconX, mainIconY))
                
                # hovering effects on the 4 icons
                # 1. resumeIcon:
                boxRect2 = pygame.Rect(resumeIconX, resumeIconY, PMI, PMI)
                if boxRect2.collidepoint(mouseX, mouseY) and mouseClicked:
                    resumeClicked = True
                elif boxRect2.collidepoint(mouseX, mouseY):
                    drawHighlightBox(resumeIconX, resumeIconY, PMI, PMI, WHITE)
                    # the mouse is currently over a box
                # 2. settingIcon:
                boxRect3 = pygame.Rect(settingIconX, settingIconY, PMI, PMI)
                #if boxRect3.collidepoint(mouseX, mouseY) and mouseClicked:
                #    settingClicked = True
                if boxRect3.collidepoint(mouseX, mouseY):
                    drawHighlightBox(settingIconX, settingIconY, PMI, PMI, WHITE)
                    # the mouse is currently over a box
                # 3. replayIcon:
                boxRect4 = pygame.Rect(replayIconX, replayIconY, PMI, PMI)
                #if boxRect4.collidepoint(mouseX, mouseY) and mouseClicked:
                #    replayClicked = True
                if boxRect4.collidepoint(mouseX, mouseY):
                    drawHighlightBox(replayIconX, replayIconY, PMI, PMI, WHITE)
                    # the mouse is currently over a box
                # 4. mainIcon:
                boxRect5 = pygame.Rect(mainIconX, mainIconY, PMI, PMI)
                #if boxRect5.collidepoint(mouseX, mouseY) and mouseClicked:
                #    mainClicked = True
                if boxRect5.collidepoint(mouseX, mouseY):
                    drawHighlightBox(mainIconX, mainIconY, PMI, PMI, RED)
                    # the mouse is currently over a box

                if resumeClicked == True:
                    pauseClicked = False
                    resumeClicked = False
                    settingClicked = False
                    replayClicked = False
                    mainClicked = False


        pygame.display.update()
        FPSCLOCK.tick(FPS)


def drawHighlightBox(leftX, topY, boxWidth, boxHeight, color):
    left = leftX
    top = topY
    pygame.draw.rect(DISPLAYSURF, color, (left, top, boxWidth, boxHeight), 2)


def throwSaltAnimation(throwX, throwY):
    DISPLAYSURF.blit(throwSaltAni1, (throwX, throwY))
    pygame.display.update()
    fpsClock.tick(FPS)
    DISPLAYSURF.blit(throwSaltAni2, (throwX, throwY))
    pygame.display.update()
    fpsClock.tick(FPS)
    DISPLAYSURF.blit(throwSaltAni3, (throwX, throwY))
    pygame.display.update()
    fpsClock.tick(FPS)
    DISPLAYSURF.blit(throwSaltAni4, (throwX, throwY))
    pygame.display.update()
    fpsClock.tick(FPS)
    DISPLAYSURF.blit(throwSaltAni5, (throwX, throwY))
    pygame.display.update()
    fpsClock.tick(FPS)


def dyingWomanAnimation():
    pygame.display.update()
    fpsClock.tick(FPS)

def chainAnimation(chainY):    
    while chainY < 0:        
        chainY += 10

    DISPLAYSURF.blit(chainImg, (chainX, chainY))

    

def drawNewSalt(salt_x, salt_y):
    salt_obj = {}
    salt_obj['surface'] = pygame.image.load('saltObj.png')
    salt_obj['x'] = salt_x
    salt_obj['y'] = salt_y
    salt_obj['width'] = SALT_WIDTH
    salt_obj['height'] = SALT_HEIGHT

    return salt_obj



def drawNewWoman(wom_x, wom_y):
    wom_obj = {}
    wom_obj['surface'] = pygame.image.load('fl.png')
    wom_obj['x'] = wom_x
    wom_obj['y'] = wom_y
    wom_obj['width'] = WOMAN_WIDTH
    wom_obj['height'] = WOMAN_HEIGHT
    wom_obj['facing'] = LEFT
    wom_obj['status'] = ALIVE

    return wom_obj
                                 

#def womanWanderAnimation(wom_obj):
    #wom_obj[


if __name__ == '__main__':
    main()
