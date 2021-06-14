
import pygame
import random
import sys


pygame.init()

screenColor = (0, 0, 0)
screenDimension = (600, 600)
fontColor = (255, 255, 255)
font = pygame.font.SysFont("hack", 35)
clock = pygame.time.Clock()

# Configs Cobra
snakeColor = (34, 139, 34)
x = screenDimension[0] / 2
y = screenDimension[1] / 2
d = 20
snakeBody = [[x, y]]
dx = 0
dy = 0

# Configs Comida
appleX = round(random.randrange(0 + d, 550 - d) / 20) * 20
appleY = round(random.randrange(0 + d, 550 - d) / 20) * 20
appleColor = [(255, 255, 0), (255, 255, 0), (255, 255, 0)]
color = 0

# Tela
screen = pygame.display.set_mode((screenDimension))
pygame.display.set_caption('Python.io')

screen.fill(screenColor)

# Função Desenhar Cobra
def drawSnake(snakeBody):
    screen.fill(screenColor)
    for unit in snakeBody:
        pygame.draw.rect(screen, snakeColor, [unit[0], unit[1], d, d])

# Função Mover Cobra
def moveSnake(dx, dy, snakeBody):
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                dx = -d
                dy = 0
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                dx = d
                dy = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                dx = 0
                dy = -d
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                dx = 0
                dy = d

    newX = snakeBody[-1][0] + dx
    newY = snakeBody[-1][1] + dy

    snakeBody.append([newX, newY])
    del snakeBody[0]

    return dx, dy, snakeBody

# Função Checar Comida
def checkApples(dx, dy, appleX, appleY, snakeBody, color):

    head = snakeBody[-1]
    newX = head[0] + dx
    newY = head[1] + dy

    if head[0] == appleX and head[1] == appleY:
        snakeBody.append([newX, newY])
        appleX = round(random.randrange(0 + d, 550 - d) / 20) * 20
        appleY = round(random.randrange(0 + d, 550 - d) / 20) * 20
        color = round(random.randrange(0, 3))

    pygame.draw.rect(screen, appleColor[color], [appleX, appleY, d, d])

    return appleX, appleY, snakeBody, color

# Função de checar colisão com as paredes
def checkWalls(snakeBody):
    head = snakeBody[-1]
    x = head[0]
    y = head[1]

    if x not in range(650) or y not in range(650):
        raise Exception

# Função do que acontece com a cobra depois de comer
def checkBitTail(snakeBody):
    head = snakeBody[-1]
    body = snakeBody.copy()
    del body[-1]

    for x, y in body:
        if x == head[0] and y == head[1]:
            raise Exception


# Loop do jogo
while True:
    pygame.display.update()
    drawSnake(snakeBody)
    dx, dy, snakeBody = moveSnake(dx, dy, snakeBody)
    appleX, appleY, snakeBody, color = checkApples(dx, dy, appleX, appleY, snakeBody, color)
    checkWalls(snakeBody)
    checkBitTail(snakeBody)
    clock.tick(10)