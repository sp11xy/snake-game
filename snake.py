import pygame
import random

pygame.init() #starte alle pygame module

width = 800
height = 600
window = pygame.display.set_mode((width, height)) #für die Auflösung
pygame.display.set_caption("Snake-Game") #für den Titel

#for i in range(1,10):
#   print(i)
    
snakeStartPosX = random.randint(1,500)
snakeStartPosY = random.randint(1,500)

snakeSpeed = 100
pygame.draw.rect(window, (255,0,0), (snakeStartPosX, snakeStartPosY, 10,10)) #width: x,y,w,h

snake_speed = 0.05

dir_x = 1
dir_y = 0

while True:
    for evnt in pygame.event.get(): #für die events die im fenster passieren
        if evnt.type == pygame.QUIT:
            pygame.quit()
                
    window.fill((50,50,50))
   
    pygame.draw.rect(window, (255,0,0), (snakeStartPosX, snakeStartPosY, 10, 10))

    if evnt.type == pygame.KEYDOWN:
       # print("Key pressed") #wird aktiviert bei jeder pfeiltaste
        if evnt.key == pygame.K_RIGHT:
           print("rechts")
           pygame.draw.rect(window, (255,0,0), (snakeStartPosX, snakeStartPosY, 10,10))
           #snakeStartPosX+=snake_speed
           dir_x = 1
        elif evnt.key == pygame.K_DOWN:
            print("unten")
            pygame.draw.rect(window, (255,0,0), (snakeStartPosX, snakeStartPosY, 10,10))
            #snakeStartPosY += snake_speed
            dir_y = -1
        elif  evnt.key == pygame.K_LEFT:
            print("links")
            pygame.draw.rect(window, (255,0,0), (snakeStartPosX, snakeStartPosY, 10,10))
            #snakeStartPosX -= snake_speed
            dir_x = -1
        elif  evnt.key == pygame.K_UP:
            print("oben")
            pygame.draw.rect(window, (255,0,0), (snakeStartPosX, snakeStartPosY, 10,10))
            #snakeStartPosY -= snake_speed
            dir_y = 1
        
    pygame.display.update()
    
    snakeStartPosX += dir_x * snake_speed
    snakeStartPosY -= dir_y * snake_speed

    
