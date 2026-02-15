import pygame
import sys
import random

pygame.init()

block_size = 5

screen_width = 600
screen_height = 400

cols = screen_width // block_size   # 120
rows = screen_height // block_size  # 80


screen = pygame.display.set_mode((screen_width, screen_height))

twoD = [[False] * cols for i in range (rows)]

for i in range(1000):
    r = random.randint(0, rows - 1)
    c = random.randint(0, cols - 1)
    twoD[r][c] = True

#turn everything into a comment with comand /

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    #SECTION FOR CHECKING THE BLOCKS AND UPDATING INSIDE OF THE ARRAY
    for i in range(rows):
        for j in range(cols):
            # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

            if twoD[i][j] == False:
                Amount_of_alive = 0
                if 0 < j < cols - 1:
                    if 0 < i < rows - 1:
                        if twoD[i+1][j] == True:
                            Amount_of_alive += 1
                        if twoD[i-1][j] == True:
                            Amount_of_alive += 1
                        if twoD[i][j+1] == True:
                            Amount_of_alive += 1
                        if twoD[i][j-1] == True:
                            Amount_of_alive += 1
                if Amount_of_alive == 3: 
                    twoD[i][j] == True
        

        #SEPRATE SECTION FOR DRAWING 
        for i in range(rows):
            for j in range(cols):
                if twoD[i][j] == True:
                    pygame.draw.rect(
                        screen,
                        (0, 0, 0),
                        (j * block_size, i * block_size, block_size, block_size)
                    )  
                else: 
                    pygame.draw.rect(
                        screen,
                        (255, 255, 255),
                        (j * block_size, i * block_size, block_size, block_size)
                    )  
                            






            



    
    


# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    #this will mean checking for every combo of j+1, j-1, i+1, i-1 tg


# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.


    pygame.display.flip()

