import time

import pygame
import random

pygame.init()

window_width = 420
window_height = 420
window_game = pygame.display.set_mode((window_width, window_height))
step = 20
score = 0

pygame.display.set_caption('Snake')




class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 20
        self.h = 20

    def draw(self):
        pygame.draw.rect(window_game, 'black', [self.x, self.y, self.w, self.h], 2)


class Apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = 'red'
        self.w = 20
        self.h = 20

    def draw(self):
        pygame.draw.rect(window_game, self.color, [self.x,
                                                   self.y,
                                                   self.w,
                                                   self.h])


def game_over():
    font_game_over = pygame.font.Font('freesansbold.ttf', 30)
    text_game_over = font_game_over.render('Game Over!', True, 'blue', 'yellow')
    text_game_over_rect = text_game_over.get_rect()
    text_game_over_rect.center = ((window_width - 20) // 2, (window_height - 20) // 2)
    window_game.blit(text_game_over, text_game_over_rect)


def show_score():
    font_score = pygame.font.Font('freesansbold.ttf', 15)
    text_score = font_score.render('Score: ' + str(score), True, 'blue', 'yellow')
    text_score_rect = text_score.get_rect()
    text_score_rect.center = (210, 10)
    window_game.blit(text_score, text_score_rect)


def restart_or_quit():
    font_restart = pygame.font.Font('freesansbold.ttf', 20)
    text_restart = font_restart.render('Type R to restart the game', True, 'pink', 'blue')
    text_quit = font_restart.render('or type Q to quit', True, 'pink', 'blue')
    text_restart_rect = text_restart.get_rect()
    text_quit_rect = text_quit.get_rect()
    text_restart_rect.center = ((window_width - 20) // 2, (window_height + 100) // 2)
    text_quit_rect.center = ((window_width - 20) // 2, (window_height + 145) // 2)
    window_game.blit(text_restart, text_restart_rect)
    window_game.blit(text_quit, text_quit_rect)


def init_game():
    global snake_body
    global apple
    global score
    global direction
    global change_dir

    snake_body = [snake_body_element_1, snake_body_element_2, snake_body_element_3]
    apple = Apple(random_apple_x, random_apple_y)
    direction = 'Right'
    change_dir = direction
    score = 0


random_apple_x = random.randrange(20, window_width - 20, step)
random_apple_y = random.randrange(20, window_height - 20, step)
apple = Apple(random_apple_x, random_apple_y)

# init self.min self.max self.step
snake_body_element_1 = Snake(20, 40)
snake_body_element_2 = Snake(40, 40)
snake_body_element_3 = Snake(60, 40)
snake_body = [snake_body_element_1, snake_body_element_2, snake_body_element_3]

clock = pygame.time.Clock()

dx = 20
dy = 0

left_disabled = False
right_disabled = False

game = True
direction = 'Right'
change_dir = direction
running = True
while running:

    clock.tick(5)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                change_dir = 'Right'

            if event.key == pygame.K_LEFT:
                change_dir = 'Left'

            if event.key == pygame.K_UP:
                change_dir = 'Up'

            if event.key == pygame.K_DOWN:
                change_dir = 'Down'

            if event.key == pygame.K_r:
                init_game()

            if event.key == pygame.K_q:
                pygame.quit()

    if change_dir == 'Right' and direction != 'Left':
        direction = 'Right'
    if change_dir == 'Left' and direction != 'Right':
        direction = 'Left'
    if change_dir == 'Up' and direction != 'Down':
        direction = 'Up'
    if change_dir == 'Down' and direction != 'Up':
        direction = 'Down'

    if direction == 'Right':
        dx = 20
        dy = 0
    if direction == 'Left':
        dx = -20
        dy = 0
    if direction == 'Up':
        dy = -20
        dx = 0
    if direction == 'Down':
        dy = 20
        dx = 0

    window_game.fill((255, 255, 255))

    snake_head = Snake(snake_body[-1].x + dx, snake_body[-1].y + dy)

    snake_body.append(snake_head)

    snake_body.pop(0)

    for snake_body_element in snake_body:
        snake_body_element.draw()
        # print(snake_body_element.x, snake_body_element.y)

    apple.draw()

    if direction == 'Right':
        if snake_body[-1].x+20 == apple.x and snake_body[-1].y == apple.y:

            apple.x = random.randrange(20, window_width - 20, step)
            apple.y = random.randrange(20, window_height - 20, step)

            snake_tail = Snake(snake_body[0].x, snake_body[0].y)
            snake_body.insert(0, snake_tail)

            score += 1

    if direction == 'Left':
        if snake_body[-1].x == apple.x+20 and snake_body[-1].y == apple.y:
            apple.x = random.randrange(20, window_width - 20, step)
            apple.y = random.randrange(20, window_height - 20, step)

            snake_tail = Snake(snake_body[0].x, snake_body[0].y)
            snake_body.insert(0, snake_tail)

            score += 1

    if direction == 'Up':
        if snake_body[-1].x == apple.x and snake_body[-1].y == apple.y+20:
            apple.x = random.randrange(20, window_width - 20, step)
            apple.y = random.randrange(20, window_height - 20, step)

            snake_tail = Snake(snake_body[0].x, snake_body[0].y)
            snake_body.insert(0, snake_tail)

            score += 1

    if direction == 'Down':
        if snake_body[-1].x == apple.x and snake_body[-1].y+20 == apple.y:
            apple.x = random.randrange(20, window_width - 20, step)
            apple.y = random.randrange(20, window_height - 20, step)

            snake_tail = Snake(snake_body[0].x, snake_body[0].y)
            snake_body.insert(0, snake_tail)

            score += 1

    if snake_body[-1].x < 0 or snake_body[-1].x > 400 or snake_body[-1].y < 20 or snake_body[-1].y > 400:
        game_over()
        restart_or_quit()
        time.sleep(2)

    for snake_element in range(0, len(snake_body)-1):
        if snake_body[-1].x == snake_body[snake_element].x and snake_body[-1].y == snake_body[snake_element].y:
            game_over()
            restart_or_quit()
            time.sleep(2)
            print('Game Over')

    show_score()

    pygame.display.flip()

pygame.quit()
