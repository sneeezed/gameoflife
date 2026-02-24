import pygame
import sys
import time

pygame.init()

block_size = 10
screen_width = 1200
screen_height = 800
zoom = 1


screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()


# x and y cordinate pairs as tup and then just true, which idk if rudundant
aliveMap = {}
drawing = True

def CheckAmountAlive(x, y, aliveMap):
    amount_alive = 0
    if (x+1, y) in aliveMap:
        amount_alive +=1
    if (x+1, y+1) in aliveMap:
        amount_alive +=1
    if (x+1, y-1) in aliveMap:
        amount_alive +=1
    if (x, y-1) in aliveMap:
        amount_alive +=1
    if (x, y+1) in aliveMap:
        amount_alive +=1
    if (x-1, y+1) in aliveMap:
        amount_alive +=1
    if (x-1, y-1) in aliveMap:
        amount_alive +=1
    if (x-1, y) in aliveMap:
        amount_alive +=1
    return amount_alive

while True:
    starttime = time.time()

    screen.fill((0, 0, 0))

    newMap = {}
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                drawing = False

            if event.key == pygame.K_1:
                zoom+=1
            if event.key == pygame.K_2:
                if zoom > 1:
                    zoom -= 1
            if event.key == pygame.K_r:
                drawing = True
                aliveMap = {}
                    


            

    if drawing == True:
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0] or mouse_buttons[2]:
            mx, my = pygame.mouse.get_pos()  #lines 47-41 i used chatgpt to understand how drawing works with pygame
            x = mx // block_size 
            y = my // block_size
            if mouse_buttons[0]:      
                aliveMap[(x, y)] = True
            elif mouse_buttons[2]:
                if (x,y) in aliveMap:  
                    aliveMap.pop((x, y))

    else:
        for x, y in aliveMap.keys():
            newMap[(x, y)] = aliveMap[(x, y)]

            amount_alive = CheckAmountAlive(x, y, aliveMap)
            # Any live cell with more than three live neighbours dies, as if by overpopulation.
            if amount_alive > 3:
                newMap.pop((x, y))
            # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
            if amount_alive < 2:
                newMap.pop((x, y))


    # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.   
            amount_around_dead_thats_alive = CheckAmountAlive(x+1, y, aliveMap)
            if amount_around_dead_thats_alive == 3:
                newMap[x+1, y] = True

            amount_around_dead_thats_alive = CheckAmountAlive(x-1, y, aliveMap)
            if amount_around_dead_thats_alive == 3:
                newMap[x-1, y] = True

            amount_around_dead_thats_alive = CheckAmountAlive(x, y-1, aliveMap)
            if amount_around_dead_thats_alive == 3:
                newMap[x, y-1] = True

            amount_around_dead_thats_alive = CheckAmountAlive(x+1, y-1, aliveMap)
            if amount_around_dead_thats_alive == 3:
                newMap[x+1, y-1] = True

            amount_around_dead_thats_alive = CheckAmountAlive(x-1, y-1, aliveMap)
            if amount_around_dead_thats_alive == 3:
                newMap[x-1, y-1] = True

            amount_around_dead_thats_alive = CheckAmountAlive(x, y+1, aliveMap)
            if amount_around_dead_thats_alive == 3:
                newMap[x, y+1] = True

            amount_around_dead_thats_alive = CheckAmountAlive(x+1, y+1, aliveMap)
            if amount_around_dead_thats_alive == 3:
                newMap[x+1, y+1] = True

            amount_around_dead_thats_alive = CheckAmountAlive(x-1, y+1, aliveMap)
            if amount_around_dead_thats_alive == 3:
                newMap[x-1, y+1] = True


    # Any live cell with two or three live neighbours lives on to the next generation.
        #dont really gotta do anything for this condtional
        aliveMap = newMap

    for x, y in aliveMap.keys():
            pygame.draw.rect(
                    screen,
                    (255, 255, 255),
                    (x * block_size * zoom, y * block_size* zoom, block_size* zoom, block_size* zoom)
                )  

    
    pygame.display.flip()
    #print(time.time() - starttime)
    if drawing == False:
        clock.tick(9)

