import pygame

pygame.font.init()

# Screen
screen_width = 800
screen_height = 550

# Colors
RED = (134, 28, 9)
YELLOW = (212, 169, 65)
WHITE = (255, 255, 255)
GREEN = (0, 127, 33)
BLUE = (0, 97, 148)

# Rectangles constants
RECT_1 = (20, 20)
RECT_2 = (60, 20)
RECT_3 = (20, 60)
RECT_4 = (30, 30)
RECT_5 = (20, 108)
RECT_6 = (108, 10)
RECT_7 = (60, 30)
RECT_8 = (30, 60)
RECT_9 = (20, 168)
RECT_10 = (168, 10)

# Screen refresh
fps = 30

# Wall group
walls = pygame.sprite.Group()
ball_sprites = pygame.sprite.Group()

TAM_TANK = 36

# Clock
clk = pygame.time.Clock()

# Tanks
tank_1 = pygame.image.load("Sprites/Tank_1.png")
tank_2 = pygame.image.load("Sprites/Tank_2.png")
rot_speed = 0.4
ball_speed = 2
shot_time = 10
defeat_time = 5

# Joystick buttons
button_keys = {
    "up_arrow": 11,
    "left_arrow": 13,
    "right_arrow": 14,
}
