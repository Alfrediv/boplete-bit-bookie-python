
import pygame
import math #needed for square root function



pygame.init()#initializes Pygame
pygame.display.set_caption("Boplete bit Bookie")#sets the window title
screen = pygame.display.set_mode((400,400))#creates game screen

print(pygame.font.get_fonts())
#player variables
xpos = 0
ypos = 0
mousePos = (xpos, ypos) #variable mousePos stores TWO numbers
numClicks = 0

#circle variables: circX and circY are the coordinates of the center (where it's drawn), and the radius is how big it is
circX = 200
circY = 199
radius = 100

#gameloop###################################################
while True:
#event queue (bucket that holds stuff that happens in game and passes to one of the sections below)
    event = pygame.event.wait()

    if event.type == pygame.QUIT: #close game window
        break

    if event.type == pygame.MOUSEBUTTONDOWN: #check if clicked
        if math.sqrt()
      print("CLICK")

    if event.type == pygame.MOUSEMOTION: #check if mouse moved
        mousePos = event.pos #refreshes mouse position
        print("mouse position: (",mousePos[0]," , ",mousePos[1], ")")
 
#render section---------------------------------------------
    screen.fill((0, 0, 0)) #wipe screen (without this, things smear)
    
    pygame.draw.circle(screen, (200, 0, 200), (circX,circY), radius)
    #print("clicks:", numClicks) #uncomment this once collision is set up
        
    pygame.display.flip()
    

#end game loop##############################################

pygame.quit()


