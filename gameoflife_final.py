import pygame
import sys
import time

pygame.init()

block_size = 1
screen_width = 1200
screen_height = 800
zoom = 10
world_center_x = screen_width // 2
world_center_y = screen_height // 2


screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()


# x and y cordinate pairs as tup and then just true, which idk if rudundant could use sets
aliveMap = {}
drawing = True

camera_x = 0
camera_y = 0

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
#i used chatgpt for how to use keydown stuff
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                drawing = False

            if event.key == pygame.K_EQUALS:
                center_x = camera_x + (world_center_x / (block_size * zoom))
                center_y = (world_center_y / (block_size * zoom)) - camera_y

                zoom += 1  

                camera_x = center_x - (world_center_x / (block_size * zoom))
                camera_y = (world_center_y / (block_size * zoom)) - center_y

            if event.key == pygame.K_MINUS and zoom > 1:
                center_x = camera_x + (world_center_x / (block_size * zoom))
                center_y = (world_center_y / (block_size * zoom)) - camera_y

                zoom -= 1

                camera_x = center_x - (world_center_x / (block_size * zoom))
                camera_y = (world_center_y / (block_size * zoom)) - center_y #idkwhy center y is negative

            if event.key == pygame.K_r:
                drawing = True
                aliveMap = {}

                    
    if drawing == True:
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0] or mouse_buttons[2]:
            mx, my = pygame.mouse.get_pos()

            x = camera_x + (mx // (block_size * zoom))
            y = (my // (block_size * zoom)) - camera_y

            if mouse_buttons[0]:
                aliveMap[(x, y)] = True
            elif mouse_buttons[2]:
                if (x, y) in aliveMap:
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
            screen_x = (x - camera_x) *  block_size * zoom
            screen_y = (y + camera_y) *  block_size* zoom #idkwhytheyarenegativeandnotpostivebutthis works

            pygame.draw.rect(
                    screen,
                    (255, 255, 255),
                    (screen_x, screen_y, block_size* zoom, block_size* zoom)
                )  

    
    pygame.display.flip()
    #print(time.time() - starttime)
    if drawing:
        clock.tick(60) #used chat for these lines 1. to have the drawing smoother 2. to have a framerate for the animations
    else:
        clock.tick(9)
    keys = pygame.key.get_pressed()

    move_speed = 1 

    if keys[pygame.K_w]:#i used chatgpt for how event pressdown works 
        camera_y += move_speed
    if keys[pygame.K_s]:
        camera_y -= move_speed
    if keys[pygame.K_a]:
        camera_x -= move_speed
    if keys[pygame.K_d]:
        camera_x += move_speed

