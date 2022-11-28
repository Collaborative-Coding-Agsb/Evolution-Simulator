from Entities import Cell
from Entities import EntityHandler
import pygame
import random

pygame.init()

screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()
averageFps = 60

entities = EntityHandler.EntityHandler()

for index in range(10):
    entities.addEntity( Cell.Cell( (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (0,0), (random.randint(-10,10)/100,random.randint(-10,10)/100), random.uniform(10,15) ) )

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    entities.addEntity( Cell.Cell( (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (0,0), (random.randint(-10,10)/100,random.randint(-10,10)/100), random.uniform(10,15) ) )

    deltaT = clock.tick(60)
    
    entities.update( deltaT )
        
    screen.fill((255, 255, 255))

    entities.draw( screen )

    averageFps = (averageFps+clock.get_fps())/2
    print(int(averageFps), len(entities.entityArray))

    pygame.display.flip()

pygame.quit()