import pygame #für die ganzen game funktionen
import random #für die rand. zahlen generation

pygame.init() #starte alle pygame module
clock = pygame.time.Clock()

width = 800 
height = 600
window = pygame.display.set_mode((width, height)) #für die Auflösung
pygame.display.set_caption("Snake-Game by sp11xy") #für den Titel

#for i in range(1,10):
#   print(i)
    
snakeStartPosX = random.randint(1,500)
snakeStartPosY = random.randint(1,500)

pygame.draw.rect(window, (255,0,0), (snakeStartPosX, snakeStartPosY, 30,10)) #width: (x,y,w,h)

snake_speed = 2.5

dir_x = 1
dir_y = 0

while True:
    for event in pygame.event.get(): #für die events die im window passieren
        if event.type == pygame.QUIT:
            pygame.quit() #damit sich das fenster selbst schließt 
            exit() #für einen richtig exit code (return 0)

        if event.type == pygame.KEYDOWN:
           # print("Key pressed") #wird aktiviert bei jeder pfeiltaste
            if event.key == pygame.K_RIGHT:
                print("rechts")
                dir_x = 1
                dir_y = 0
            elif event.key == pygame.K_DOWN:
                print("unten")
                dir_y = -1
                dir_x = 0
            elif  event.key == pygame.K_LEFT:
                print("links")
                dir_x = -1
                dir_y = 0
            elif  event.key == pygame.K_UP:
                print("oben")
                dir_y = 1
                dir_x = 0
            
                      
    window.fill((50,50,50))
    pygame.draw.rect(window, (255,0,0), (snakeStartPosX, snakeStartPosY, 30, 10))
    pygame.display.update()
        
    snakeStartPosX += dir_x * snake_speed
    snakeStartPosY -= dir_y * snake_speed
    
    clock.tick(60) #60 frame cap damit der speed auch effektiver wird 

    
