# import pygame module
import pygame as pg
#import from random library module randrange, this gives you the ability generate random number and allows room for steps
from random import randrange
# decides the size of the window for the game
WINDOW = 1000
#
TILE_SIZE = 50
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
get_random_position = lambda: [randrange(*RANGE), randrange(*RANGE)]
#pygame.Rect is a class whose instances represent rectangular areas.
#pygame.draw.rect is a function that draws rectangles. One of its arguments is a pygame.Rect instance representing the rectangle to draw.
# Remember rect vs Rect there is a big difference on their functions.
# 
snake = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
snake.center = get_random_position()
lenght = 1
segments = [snake.copy()]
snake_dir = (0, 0)
time, time_step = 0, 110
food = snake.copy()
food.center = get_random_position()
screen = pg.display.set_mode([WINDOW] * 2)
clock = pg.time.Clock()
# dictionary, prohibition of movement
dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_d: 1}

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w and dirs[pg.K_w]:
                snake_dir = (0, -TILE_SIZE)
                dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_d: 1}
            if event.key == pg.K_s:
                snake_dir = (0, TILE_SIZE)
                dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_d: 1}
            if event.key == pg.K_a:
                snake_dir = (-TILE_SIZE, 0)
                dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_d: 1}
            if event.key == pg.K_d:
                snake_dir = (TILE_SIZE, 0)
                dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_d: 1}  
    screen.fill('black')
    # check borders adn selfeating
    self_eating = pg.Rect.collidelist(snake, segments[:-1]) != -1
    if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or self_eating:
        snake.center, food.center = get_random_position(), get_random_position()
        lenght, snake_dir = 1, (0, 0)
        segments = [snake.copy()]
    # check food
    if snake.center == food.center:
        food.center = get_random_position()
        lenght += 1
    # draw food
    pg.draw.rect(screen, 'red', food)
    # draw snake
    [pg.draw.rect(screen, 'green', segment) for segment in segments]
    # move snake
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-lenght:]
    pg.display.flip()
    clock.tick(60)