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

bg = pygame.image.load("img/farm_map.png").convert()

black = (0,0,0)
white = (0,0,255)
x = 0
y = 475
animalImg = pygame.image.load("img/chicken.png")


        
animal_speed = 0

gameStart = True

while gameStart == True:
    
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            gameStart=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                y-=25
            if event.key==pygame.K_DOWN:
                y+=25

            if event.key==pygame.K_LEFT:
                x-=25

            if event.key==pygame.K_RIGHT:
                x+=25

    gameDisplay.blit(bg, [0,0])
    animal(x,y)
       
    pygame.display.update()
    clock.tick(30)



pygame.quit()
quit()
