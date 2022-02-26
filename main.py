import time
import pygame
import random

pygame.init()

window_width = 420
window_height = 420
window_game = pygame.display.set_mode((window_width, window_height))
step = 20
score = 0
speed = 5
game_over = False

pygame.display.set_caption('Snake')

all_coordinates = []
for i in range(0, 401, 20):
    for j in range(0, 401, 20):
        if j == 0:
            pass
        else:
            all_coordinates.append([i, j])


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
        self.color = '#201926'
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

    def show(self):
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


def init_game():
    global snake_body
    global apple
    global score
    global direction
    global change_dir
    global game_over
    global speed

    snake_body = [snake_body_element_1, snake_body_element_2, snake_body_element_3]
    direction = 'Right'
    change_dir = direction
    score = 0
    speed = 5
    game_over = False


apple = Apple(80, 100)

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
    clock.tick(speed)

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
        game_over_text.show()
        restart_text.show()
        quit_text.show()
    else:
        snake_head = Snake(snake_body[-1].x + dx, snake_body[-1].y + dy)
        snake_body.append(snake_head)
        snake_body.pop(0)

        draw_snake = list(map(lambda snake_body_element: snake_body_element.draw(), snake_body))

        eat_apple = snake_body[-1].x == apple.x and snake_body[-1].y == apple.y

        if eat_apple:
            available_apple_coordinates = all_coordinates
            for i in snake_body:
                if [i.x, i.y] in available_apple_coordinates:
                    available_apple_coordinates.remove([i.x, i.y])

            random_apple = random.choice(available_apple_coordinates)
            apple.x, apple.y = random_apple[0], random_apple[1]

            snake_tail = Snake(snake_body[0].x, snake_body[0].y)
            snake_body.insert(0, snake_tail)

            score += 1
            speed += 0.25

        out_of_border = snake_body[-1].x < 0 or snake_body[-1].x > 400 or snake_body[-1].y < 20 or snake_body[-1].y > 400
        if out_of_border:
            on_game_over()

        eat_snake = list(filter(lambda sbe: snake_body[-1].x == sbe.x and snake_body[-1].y == sbe.y, snake_body[:-1]))
        if eat_snake:
            on_game_over()

        apple.draw()

    score_text.show_score()
    pygame.display.flip()

pygame.quit()
