import pygame,sys
import random
pygame.init()
screen_x = 600
screen_y = 800
screen = pygame.display.set_mode(screen_x,screen_y)
live = 3
red = (255,0,0)
blue = (0,255,0)
green = (0,0,255)
black = (0,0,0)
white = (255,255,255)
score = 0
screen.fill(black)
color = [red,blue,green]
pygame.display.update
loc_bas = []
fruit_spawn = []
time = 0
def loc_fruit_spawn():
    for i in range(len(fruit_spawn)):
        random_color = random.randint(0,2)
        pygame.draw.circle(screen,color[random_color],(fruit_spawn[i][0],fruit_spawn[i][1]),30,30,5)
        fruit_spawn[i][1] += 10
        
def check_fruit():
    delete = []
    for i in range(len(fruit_spawn)):
        if i[1] == 800:
            live -= 1
            delete.append(i)
        elif loc_bas[0][0] > i[0] < loc_bas[1][0] and i[1] == 750:
            score += 1
            delete.append(i)
    for i in delete:
        fruit_spawn.remove(fruit_spawn[i])
def reset_game():
    score = 0
    live = 3
    screen.fill(black)
    fruit_spawn = []
clock = pygame.time.Clock()
random_time_spawn = random.randint(48,480)
python.display.update

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_r:
                reset_game()
    if not live == 0:
        if time == random_time_spawn:
            x_random = random.randint(31,569)
            time = 0 
            fruit_spawn.append([x_random,0])
            random_time_spawn = random.randint(48,480)
        loc_fruit_spawn()
        check_fruit()
        clock.tick(12)
        time += 1
        python.display.update