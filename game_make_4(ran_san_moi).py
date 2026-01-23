import pygame,sys
import random

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("ran san moi")

snake_list = []
snake_long = 0

light_blue = (117,248,255)
white = (255,255,255)
grey = (160,160,160)
light_grey = (211,211,211)
dark_grey = (79,79,79)
black = (0,0,0)
red = (255,0,0)

screen.fill(light_blue)

snake_block = 10

x_head = 400
y_head = 300

y_head_change = 0
x_head_change = 0 

def random_foodX():
    ranfoodX = random.randrange(0,800-10)
    spfX = ranfoodX % 10
    return round(ranfoodX-spfX)

def random_foodY():
    ranfoodY = random.randrange(0,600-10)
    spfY = ranfoodY % 10
    return round(ranfoodY-spfY)

random_foodx = random_foodX()
random_foody = random_foodY()

def show_snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(screen,black,[x[0],x[1],snake_block,snake_block])
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_head_change = -snake_block
                y_head_change = 0
            elif event.key == pygame.K_RIGHT:
                x_head_change = +snake_block
                y_head_change = 0
            elif event.key == pygame.K_UP:
                y_head_change = -snake_block
                x_head_change = 0
            elif event.key == pygame.K_DOWN:
                y_head_change = +snake_block
                x_head_change = 0
    screen.fill(light_blue)
    if random_foodx == x_head and random_foody == y_head:
        random_foodx = random_foodX()
        random_foody = random_foodY()
        snake_long += 100
    pygame.draw.rect(screen,red,[random_foodx,random_foody,snake_block,snake_block])

    y_head += y_head_change
    x_head += x_head_change

    snake_head = []
    snake_head.append(x_head)
    snake_head.append(y_head)
    snake_list.append(snake_head)
    show_snake(snake_block,snake_list)
    if len(snake_list) > snake_long:
        del snake_list[0]
    pygame.display.update()
    clock.tick(12)