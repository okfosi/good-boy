import pygame ,sys

pygame.init()
screen_y = 360
screen_x = 360
screen = pygame.display.set_mode((screen_x,screen_y))
pygame.display.set_caption("x and o")

x_and_o = []
x_rect = 3
y_rect = 3
line_y = screen_y / y_rect
line_x = screen_x / x_rect
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]
space = 10
width = 10
check = [3,0]

red =(255,0,0)
light_blue = (117,248,255)
pink = (255, 156, 247)
white = (255, 255, 255)

player = 1
game_over = False

def draw_line():
    pygame.draw.line(screen,pink,(0,line_x),(screen_y,line_x),10)
    pygame.draw.line(screen,pink,(0,line_x*2),(screen_y,line_x*2),10)
    pygame.draw.line(screen,pink,(line_y,0),(line_y,screen_x),10)
    pygame.draw.line(screen,pink,(line_y*2,0),(line_y*2,screen_x),10)

def draw_x_and_o():
    for row in range(x_rect):
        for col in range(y_rect):
            if board[row][col] == 1:
                pygame.draw.line(screen,red,(col * line_x + space,row * line_x + space),(col * line_x + line_x - space,row * line_x + line_x - space),width)
                pygame.draw.line(screen,red,(col * line_x + line_x - space,row * line_x + space),(col * line_x + space,row * line_x + line_x - space),width)
            elif board[row][col] == 2:
                pygame.draw.circle(screen,light_blue,(int(col * line_x + line_x // 2),int(row * line_x + line_x // 2)),50,width)

def player_sth(row,col,player):
    board[row][col] = player

def check_square(row,col):
    if board[row][col] == 0:
        return True

def check_board():
    for row in range(x_rect):
        if board[row][0] == board[row][1] == board[row][2] == 1:
            return [0,row,red]
        if board[row][0] == board[row][1] == board[row][2] == 2:
            return [0,row,light_blue]
    for col in range(x_rect):
        if board[0][col] == board[1][col] == board[2][col] == 1:
            return [1,col,red]
        if board[0][col] == board[1][col] == board[2][col] == 2:
            return [1,col,light_blue]
    if board[0][0] == board[1][1] == board[2][2] == 1:
        return [2,1,red]
    elif board[0][0] == board[1][1] == board[2][2] == 2:
        return [2,1,light_blue]
    elif board[0][2] == board[1][1] == board[2][0] == 1:
        return [2,2,red]
    elif board[0][2] == board[1][1] == board[2][0] == 2:
        return [2,2,light_blue]
    else:
        return [3,0]

def check_draw_win(dk):
    if dk[0] == 0:
        pygame.draw.line(screen,dk[2],(0 * line_x + line_x // 2,dk[1] * line_x + line_x // 2),(2 * line_x + line_x // 2,dk[1] * line_x + line_x // 2),width)
    if dk[0] == 1:
        pygame.draw.line(screen,dk[2],(dk[1] * line_x + line_x // 2,0 * line_x + line_x // 2),(dk[1] * line_x + line_x // 2,2 * line_x + line_x // 2),width)
    if dk[0] == 2:
        if dk[1] == 0:
            pygame.draw.line(screen,dk[2],(0 * line_x + line_x // 2,0 * line_x + line_x // 2),(2 * line_x + line_x // 2,2 * line_x + line_x // 2),width)
        if dk[1] == 1:
            pygame.draw.line(screen,dk[2],(2 * line_x + line_x // 2,0 * line_x + line_x // 2),(0 * line_x + line_x // 2,2 * line_x + line_x // 2),width)

def play_again():
    screen.fill(white)
    draw_line()
    player = 1
    board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

screen.fill(white)
draw_line()

pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            click_row = int(mouseY // line_y)
            click_col = int(mouseX // line_x)
            if check_square(click_row,click_col):
                player_sth(click_row,click_col,player)
                draw_x_and_o()
                player = player % 2 + 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.Key_r:
                play_again()
                game_over = False
        check = check_board()
        check_draw_win(check)
        pygame.display.update()
    