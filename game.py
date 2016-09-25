import pygame
import random
import math

pygame.init()

title = "KFPoop"

display_width = 1200
display_height= 700
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption(title)
clock = pygame.time.Clock()
icon = pygame.image.load("img/icon.ico")
pygame.display.set_icon(icon)
bg = pygame.image.load("img/farm_map.png").convert()
bg2 = pygame.image.load("img/farm_map_2.png").convert()

black = (0,0,0)
white = (0,0,255)

animalchar = pygame.image.load("img/chicken.png")

animal_width = 75


#def collision():
    

def score():
    score = 0

def animal(x,y):
    gameDisplay.blit(animalchar, [x,y])

def text_objects(text, font):
     textSurface = font.render(text, True, black)
     return textSurface, textSurface.get_rect()
    
def message_display(text):
     largeText = pygame.font.Font('freesansbold.ttf',115)
     TextSurf, TextRect = text_objects(text, largeText)
     TextRect.center = ((display_width/2),(display_height/2))
     gameDisplay.blit(TextSurf, TextRect)
     pygame.display.update()
     time.sleep(2)
     game_loop()

def die():
     message_display('You Died')     

#class Enemy(object):
#    def move_towards_player(self, player):
#        dx, dy = self.rect.x - player.rect.x, self.rect.y - player.rect.y
#        dist = math.hypot(dx, dy)
#        dx, dy = dx / dist, dy / dist
#        self.rect.x += dx * self.speed
#        self.rect.y += dy * self.speed

def gameloop():
    x = 0
    y = 475
    
   
    
    x_change = 0

    gameStart = True

    while gameStart:
    
        for event in pygame.event.get():
        
            if event.type==pygame.QUIT:
                gameStart=True

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    y-=25

                if event.key==pygame.K_DOWN:
                    y+=25

                if event.key==pygame.K_LEFT:
                    x-=25

                if event.key==pygame.K_RIGHT:
                    x+=25



        x += x_change


        gameDisplay.blit(bg, [0,0])
        animal(x,y)

        
        if x < 0:
            gameDisplay.blit(bg2, [0,0])
            animal(x,y)

        

        pygame.display.update()
        clock.tick(60)


gameloop()
pygame.quit()
quit()
