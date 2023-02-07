import pygame.sprite
from config import *
import layouts
from tank import *

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Combat-Atari")

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
for joystick in joysticks:
    joystick.init()

tank_sprites = pygame.sprite.Group()
tank1 = Tank(tank_1, 40, 120, 0)
tank2 = Tank(tank_2, 750, 120, 8)
tank3 = Tank(tank_1, 40, 500, 0)
tank4 = Tank(tank_2, 750, 500, 8)

coord = [[400, 275], [40, 120], [730, 120], [730, 400]]
tank_sprites.add(tank1, tank2, tank3, tank4)
hit_timer = 0


def ball_update(tank):
    for ball in tank.ball_list:
        for i in range(0, ball_speed):
            ball.move()
            ball.wall_collision(walls)
        if ball.cont >= 3:
            tank.ball_list.remove(ball)
            ball_sprites.remove(ball)


class Game:
    def __init__(self):
        pass

    # Check if an event happens
    @staticmethod
    def check_events():
        global hit_timer
        clk.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if hit_timer > 0:
                hit_timer -= 1
                return
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0 or event.button == 1 or event.button == 2 or event.button == 3:
                    if event.joy == 0:
                        tank1.shoot_()
                    if event.joy == 1:
                        tank2.shoot_()
                    if event.joy == 2:
                        tank3.shoot_()
                    if event.joy == 3:
                        tank4.shoot_()

            if event.type == pygame.JOYHATMOTION:
                if event.value == (-1, 0):
                    if event.joy == 0:
                        tank1.rotate(rot_speed)
                    if event.joy == 1:
                        tank2.rotate(rot_speed)
                    if event.joy == 2:
                        tank3.rotate(rot_speed)
                    if event.joy == 3:
                        tank4.rotate(rot_speed)

                if event.value == (1, 0):
                    if event.joy == 0:
                        tank1.rotate(-rot_speed)
                    if event.joy == 1:
                        tank2.rotate(-rot_speed)
                    if event.joy == 2:
                        tank3.rotate(-rot_speed)
                    if event.joy == 3:
                        tank4.rotate(-rot_speed)

                if event.value == (0, 1):
                    if event.joy == 0:
                        tank1.move_w()
                    if event.joy == 1:
                        tank2.move_w()
                    if event.joy == 2:
                        tank3.move_w()
                    if event.joy == 3:
                        tank4.move_w()

                if event.value == (0, 0):
                    if event.joy == 0:
                        tank1.no_rot()
                        tank1.no_move_w()
                    if event.joy == 1:
                        tank2.no_rot()
                        tank2.no_move_w()
                    if event.joy == 2:
                        tank3.no_rot()
                        tank3.no_move_w()
                    if event.joy == 3:
                        tank4.no_rot()
                        tank4.no_move_w()

    # Select Layout
    @staticmethod
    def get_screen(layout_type):
        global background, walls

        layout = layouts.Layouts(layout_type)
        background = layout.get_bg_color()
        walls = layout.get_group()

    # Draws Elements
    @staticmethod
    def draw_sprites():
        global walls, background

        screen.fill(background)
        tank_sprites.draw(screen)
        tank_sprites.update()
        walls.draw(screen)
        ball_sprites.draw(screen)
        ball_sprites.update()

    @staticmethod
    def check_winner(tank_one, tank_two):
        global score_text_1, score_text_2

        if tank_one.score < SCORE_MAX and tank_two.score < SCORE_MAX:
            score_text_1 = score_font.render(str(tank_one.score), True, GREEN)
            score_text_2 = score_font.render(str(tank_two.score), True, BLUE)
            screen.blit(score_text_1, score_text_1_rect)
            screen.blit(score_text_2, score_text_2_rect)

        else:
            if hit_timer > 0:
                score_text_1 = score_font.render(str(tank_one.score), True, GREEN)
                score_text_2 = score_font.render(str(tank_two.score), True, BLUE)
                screen.blit(score_text_1, score_text_1_rect)
                screen.blit(score_text_2, score_text_2_rect)
                return
            if tank_two.score < tank_one.score:
                screen.fill(RED)
                score_text_1 = score_font.render(str(tank_one.score), True, GREEN)
                screen.blit(victory_text1, victory_text_rect)
            elif tank_one.score < tank_two.score:
                screen.fill(RED)
                score_text_2 = score_font.render(str(tank_two.score), True, BLUE)
                screen.blit(victory_text2, victory_text_rect)

    def game_loop(self):

        self.get_screen(1)

        while True:
            ball_collision(tank1, tank2)
            ball_collision(tank2, tank1)
            wall_collision(tank1, tank2)
            ball_update(tank1)
            ball_update(tank2)
            self.check_events()
            self.draw_sprites()
            self.check_winner(tank1, tank2)

            pygame.display.update()

            clk.tick(fps)


# score max
SCORE_MAX = 2

# score text
score_font = pygame.font.Font('font/Gamer.ttf', 90)
score_text_1 = score_font.render(f'{tank1.score}', True, GREEN)
score_text_2 = score_font.render(f'{tank2.score}', True, BLUE)
score_text_1_rect = (180, -15)
score_text_2_rect = (600, -15)

# victory text
victory_font = pygame.font.Font('font/Gamer.ttf', 100)
victory_text1 = victory_font.render('VICTORY PLAYER 1', True, YELLOW)
victory_text2 = victory_font.render('VICTORY PLAYER 2', True, YELLOW)
victory_text_rect = (110, 210)
