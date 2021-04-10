import math
import pygame
import random

pygame.init()

# Create window
game_window = pygame.display.set_mode((500, 600))
pygame.display.set_caption('Ping Pong')

background_image = pygame.image.load('fields.png')
computer_pong = pygame.image.load('002-ping-pong-1.png')
computer_x_position = 220
computer_y_position = 50
computer_x_change = 0
computer_y_change = 0

player_pong = pygame.image.load('001-ping-pong.png')
player_x_position = 220
player_y_position = 370
player_x_change = 0
player_y_change = 0

pong_ball = pygame.image.load('001-medicine-ball.png')
pong_ball_x_position = 240
pong_ball_y_position = 235
pong_ball_x_position_change = 0
pong_ball_y_position_change = .1


def player(x, y):
    game_window.blit(player_pong,(x, y))


def computer(x, y):
    game_window.blit(computer_pong,(x, y))


def ball(x, y):
    game_window.blit(pong_ball, (x, y))


def collision(player_x, player_y, ball_position_x, ball_position_y):
    distance = math.sqrt(math.pow(player_x - ball_position_x, 2) + math.pow(player_y - ball_position_y, 2))

    if distance < 40:
        return True
    else:
        return  False


game_running = True

while game_running:
    game_window.fill((255, 255, 255))
    game_window.blit(background_image, (0, 0))
    player(player_x_position, player_y_position)
    computer(computer_x_position, computer_y_position)
    ball(pong_ball_x_position, pong_ball_y_position)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change += - .3
            if event.key == pygame.K_RIGHT:
                player_x_change += .3
            if event.key == pygame.K_a:
                computer_x_change += -.3
            if event.key == pygame.K_d:
                computer_x_change += .3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
            if event.key == pygame.K_a or event.key == pygame.K_d:
                computer_x_change = 0

    if player_x_position <= 0:
        player_x_position = 0
    elif player_x_position >= 436:
        player_x_position = 435

    if computer_x_position <= 0:
        computer_x_position = 0
    elif computer_x_position >= 436:
        computer_x_position = 435

    if pong_ball_x_position <= 0:
        pong_ball_x_position = 0
        pong_ball_x_position_change = random.choice([.211, .234, .2, .134, .232])
    elif pong_ball_x_position >= 468:
        pong_ball_x_position = 468
        pong_ball_x_position_change = random.choice([-.211, -.210, -.2, -.134, -.182])

    player_has_collided = collision(player_x_position, player_y_position, pong_ball_x_position, pong_ball_y_position)
    computer_has_collided = collision(computer_x_position, computer_y_position, pong_ball_x_position, pong_ball_y_position)

    if player_has_collided or computer_has_collided:
        if pong_ball_y_position > 240:
            pong_ball_y_position_change = -.2
            pong_ball_x_position_change = random.randint(-1, 2) / 10
        if pong_ball_y_position < 100:
            pong_ball_y_position_change = .2
            pong_ball_x_position_change = random.randint(-1, 2) / 10

    player_x_position += player_x_change
    computer_x_position += computer_x_change
    pong_ball_y_position += pong_ball_y_position_change
    pong_ball_x_position += pong_ball_x_position_change
    pygame.display.update()

