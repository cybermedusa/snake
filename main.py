import pygame
import random

window_game = pygame.display.set_mode((400, 400))

apple = pygame.image.load('apple.png')

class SnakeBody:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw_snake(self):
        pygame.draw.rect(window_game, 'black', [self.x, self.y, self.w, self.h], 2)

class Apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw_apple(self):
        window_game.blit(apple, (self.x, self.y))


snake_body_element_1 = SnakeBody(10, 50, 20, 20)
snake_body_element_2 = SnakeBody(30, 50, 20, 20)
snake_body_element_3 = SnakeBody(50, 50, 20, 20)

snake_body = [snake_body_element_1, snake_body_element_2, snake_body_element_3]

apple_1 = Apple(random.randint(24, 400), random.randint(24, 400))

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

    apple_1.draw_apple()

    new_element = SnakeBody(snake_body[-1].x+dx, snake_body[-1].y+dy, snake_body[-1].w, snake_body[-1].h)

    snake_body.append(new_element)

    snake_body.pop(0)

    for snake_body_element in snake_body:

        snake_body_element.draw_snake()

    # if snake_body[-1].x in range(apple_1.x, apple_1.x+24) or snake_body[-1].y in range(apple_1.y, apple_1.y+24):
    # if snake_body[-1].x >= apple_1.x and snake_body[-1].x <=
    #     print(snake_body[-1].x, snake_body[-1].y)
    #     print(apple_1.x, apple_1.y)
    #     print('Collision')

    pygame.display.flip()


pygame.quit()



