import time

import pygame
import random

pygame.init()

window_width = 420
window_height = 420
window_game = pygame.display.set_mode((window_width, window_height))
step = 20
score = 0
game_over = False

pygame.display.set_caption('Snake')


class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 20
        self.h = 20

    def draw(self):
        return pygame.draw.rect(window_game, '#823FF3', [self.x, self.y, self.w, self.h], 2)


class Apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = '#FF007B'
        self.w = 20
        self.h = 20

    def draw(self):
        pygame.draw.rect(window_game, self.color, [self.x,
                                                   self.y,
                                                   self.w,
                                                   self.h])


class Text:
    def __init__(self, name, size, text, color, bkg_color, coordinates):
        self.name = name
        self.size = size
        self.text = text
        self.color = color
        self.bkg_color = bkg_color
        self.coordinates = coordinates

    def show_score(self):
        font = pygame.font.Font(self.name, self.size)
        text = font.render(self.text + str(score), True, self.color, self.bkg_color)
        rect = text.get_rect()
        rect.center = self.coordinates
        window_game.blit(text, rect)

    def restart_or_quit(self):
        font = pygame.font.Font(self.name, self.size)
        text = font.render(self.text, True, self.color, self.bkg_color)
        rect = text.get_rect()
        rect.center = self.coordinates
        window_game.blit(text, rect)


game_over_text = Text('freesansbold.ttf', 30, 'Game Over!', '#392A46', '#FDF7FF',
                      ((window_width - 20) // 2, (window_height - 20) // 2))

score_text = Text('freesansbold.ttf', 15, 'Score: ', '#392A46', '#FDF7FF', (210, 10))

quit_text = Text('freesansbold.ttf', 20, 'or type Q to quit', '#FDF7FF', '#392A46',
                 ((window_width - 20) // 2, (window_height + 145) // 2))

restart_text = Text('freesansbold.ttf', 20, 'Type R to restart the game', '#FDF7FF', '#392A46',
                    ((window_width - 20) // 2, (window_height + 100) // 2))

def on_game_over():
    global game_over
    game_over = True


def show_score():
    font_score = pygame.font.Font('freesansbold.ttf', 15)
    text_score = font_score.render('Score: ' + str(score), True, '#392A46', '#FDF7FF')
    text_score_rect = text_score.get_rect()
    text_score_rect.center = (210, 10)
    window_game.blit(text_score, text_score_rect)


def restart_or_quit():
    font_game_over = pygame.font.Font('freesansbold.ttf', 30)
    text_game_over = font_game_over.render('Game Over!', True, '#392A46', '#FDF7FF')
    text_game_over_rect = text_game_over.get_rect()
    text_game_over_rect.center = ((window_width - 20) // 2, (window_height - 20) // 2)
    window_game.blit(text_game_over, text_game_over_rect)
    font_restart = pygame.font.Font('freesansbold.ttf', 20)
    text_restart = font_restart.render('Type R to restart the game', True, '#FDF7FF', '#392A46')
    text_quit = font_restart.render('or type Q to quit', True, '#FDF7FF', '#392A46')
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
    global game_over

    snake_body = [snake_body_element_1, snake_body_element_2, snake_body_element_3]
    apple = Apple(random_apple_x, random_apple_y)
    direction = 'Right'
    change_dir = direction
    score = 0
    game_over = False


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

direction = 'Right'
change_dir = direction
running = True
while running:
    clock.tick(20)

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

    if game_over:
        game_over_text.restart_or_quit()
        restart_text.restart_or_quit()
        quit_text.restart_or_quit()
        # restart_or_quit()
    else:
        snake_head = Snake(snake_body[-1].x + dx, snake_body[-1].y + dy)
        snake_body.append(snake_head)
        snake_body.pop(0)

        list(map(lambda snake_body_element: snake_body_element.draw(), snake_body))

        apple_on_snake = list(filter(lambda sbe: sbe.x == apple.x and sbe.y == apple.y, snake_body[:-1]))
        if apple_on_snake:
            apple.x = random.randrange(20, window_width - 20, step)
            apple.y = random.randrange(20, window_height - 20, step)
            print("jabko ktore jest na snejku: " + str(apple.x), str(apple.y))

        else:
            eat_apple = snake_body[-1].x == apple.x and snake_body[-1].y == apple.y
            if eat_apple:
                apple.x = random.randrange(20, window_width - 20, step)
                apple.y = random.randrange(20, window_height - 20, step)
                print("jabko ktore nie jest na snejku: " + str(apple.x), str(apple.y))

                snake_tail = Snake(snake_body[0].x, snake_body[0].y)
                snake_body.insert(0, snake_tail)

                score += 1

            out_of_border = snake_body[-1].x < 0 or snake_body[-1].x > 400 or snake_body[-1].y < 20 or snake_body[-1].y > 400
            if out_of_border:
                on_game_over()

            eat_snake = list(filter(lambda sbe: snake_body[-1].x == sbe.x and snake_body[-1].y == sbe.y, snake_body[:-1]))
            if eat_snake:
                on_game_over()

            apple.draw()

    # show_score()
    score_text.show_score()
    pygame.display.flip()

pygame.quit()
