import pygame


class SnakeBody:

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h


snake_body = SnakeBody(50, 50, 20, 20)

pygame.init()

window_game = pygame.display.set_mode((400, 400))

clock = pygame.time.Clock()

dx = 10
dy = 0

running = True
while running:

    clock.tick(5)

    snake_body.x += dx
    snake_body.y += dy

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                dx = 10
                dy = 0
                print(snake_body.x, snake_body.y)

            if event.key == pygame.K_LEFT:
                dx = -10
                dy = 0
                print(snake_body.x, snake_body.y)

            if event.key == pygame.K_UP:
                dy = -10
                dx = 0
                print(snake_body.x, snake_body.y)

            if event.key == pygame.K_DOWN:
                dy = 10
                dx = 0
                print(snake_body.x, snake_body.y)

    window_game.fill((255, 255, 255))

    pygame.draw.rect(window_game, 'black', [snake_body.x, snake_body.y, snake_body.w, snake_body.h])

    pygame.display.flip()


pygame.quit()



