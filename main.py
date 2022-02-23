import pygame
import random

window_width = 400
window_height = 400
window_game = pygame.display.set_mode((window_width, window_height))
step = 20

good_apple = True


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


random_apple_x = random.randrange(0, window_width, step)
random_apple_y = random.randrange(0, window_height, step)
apple = Apple(random_apple_x, random_apple_y)

# init self.min self.max self.step
snake_body_element_1 = Snake(20, 40)
snake_body_element_2 = Snake(40, 40)
snake_body_element_3 = Snake(60, 40)

snake_body = [snake_body_element_1, snake_body_element_2, snake_body_element_3]

pygame.init()

clock = pygame.time.Clock()

dx = 20
dy = 0

running = True
while running:

    clock.tick(3)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                dx = 20
                dy = 0

            if event.key == pygame.K_LEFT:
                dx = -20
                dy = 0

            if event.key == pygame.K_UP:
                dy = -20
                dx = 0

            if event.key == pygame.K_DOWN:
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

    if snake_body[-1].x == apple.x and snake_body[-1].y == apple.y:

        apple.x = random.randrange(0, window_width, step)
        apple.y = random.randrange(0, window_height, step)

        snake_tail = Snake(snake_body[0].x, snake_body[0].y)
        snake_body.insert(0, snake_tail)

    pygame.display.flip()


pygame.quit()



