import game
from ball import *
import random
screen = pygame.display.set_mode((800, 550))
pygame.display.set_caption("Combat")


class Tank(pygame.sprite.Sprite):
    def __init__(self, tank, pos_x, pos_y, current_sprite):
        super().__init__()
        self.score = 0
        self.img_tank = []
        self.ball_list = []
        self.tank = tank
        self.img1 = tank.subsurface((0, 0), (48, 48))
        self.img2 = tank.subsurface((48, 0), (48, 48))
        self.img3 = tank.subsurface((48 * 2, 0), (48, 48))
        self.img4 = tank.subsurface((48 * 3, 0), (48, 48))
        self.img5 = tank.subsurface((0, 48), (48, 48))
        self.img6 = tank.subsurface((48, 48), (48, 48))
        self.img7 = tank.subsurface((48 * 2, 48), (48, 48))
        self.img8 = tank.subsurface((48 * 3, 48), (48, 48))
        self.img9 = tank.subsurface((0, 48 * 2), (48, 48))
        self.img10 = tank.subsurface((48, 48 * 2), (48, 48))
        self.img11 = tank.subsurface((48 * 2, 48 * 2), (48, 48))
        self.img12 = tank.subsurface((48 * 3, 48 * 2), (48, 48))
        self.img13 = tank.subsurface((0, 48 * 3), (48, 48))
        self.img14 = tank.subsurface((48, 48 * 3), (48, 48))
        self.img15 = tank.subsurface((48 * 2, 48 * 3), (48, 48))
        self.img16 = tank.subsurface((48 * 3, 48 * 3), (48, 48))
        self.img_tank.append(self.img1)
        self.img_tank.append(self.img2)
        self.img_tank.append(self.img3)
        self.img_tank.append(self.img4)
        self.img_tank.append(self.img5)
        self.img_tank.append(self.img6)
        self.img_tank.append(self.img7)
        self.img_tank.append(self.img8)
        self.img_tank.append(self.img9)
        self.img_tank.append(self.img10)
        self.img_tank.append(self.img11)
        self.img_tank.append(self.img12)
        self.img_tank.append(self.img13)
        self.img_tank.append(self.img14)
        self.img_tank.append(self.img15)
        self.img_tank.append(self.img16)
        self.current_sprite = current_sprite
        self.cont = 15
        self.image = self.img_tank[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.rot = 0
        self.moveW = False
        self.shoot = False
        self.hit = False
        self.stop = False
        self.shoot_time = 0

    def shoot_(self):
        self.shoot = True

    def no_move_w(self):
        self.moveW = False

    def move_w(self):
        self.moveW = True

    def no_rot(self):
        self.rot = 0

    def rotate(self, rotation):
        self.rot = rotation

    def update(self):
        self.shoot_time = 0
        if (self.stop or self.hit) and game.hit_timer <= 0:
            self.stop = False
            self.hit = False
            choice = random.choice(game.coord)
            game.coord.remove(choice)
            self.rect.x = choice[0]
            self.rect.y = choice[1]
        if self.stop:
            return
        self.shoot_time -= 1
        self.current_sprite -= self.rot
        if self.current_sprite < 0:
            self.current_sprite = self.cont
        if self.current_sprite > self.cont:
            self.current_sprite = 0
        self.image = self.img_tank[int(self.current_sprite)]
        if self.hit:
            self.current_sprite -= 0.8
            return
        if self.moveW:
            if self.image == self.img_tank[0]:
                self.rect.x += 2
            if self.image == self.img_tank[1]:
                self.rect.x += 2
                self.rect.y += 1
            if self.image == self.img_tank[2]:
                self.rect.x += 1
                self.rect.y += 1
            if self.image == self.img_tank[3]:
                self.rect.x += 1
                self.rect.y += 2
            if self.image == self.img_tank[4]:
                self.rect.y += 2
            if self.image == self.img_tank[5]:
                self.rect.x -= 1
                self.rect.y += 2
            if self.image == self.img_tank[6]:
                self.rect.x -= 1
                self.rect.y += 1
            if self.image == self.img_tank[7]:
                self.rect.x -= 2
                self.rect.y += 1
            if self.image == self.img_tank[8]:
                self.rect.x -= 2
            if self.image == self.img_tank[9]:
                self.rect.x -= 2
                self.rect.y -= 1
            if self.image == self.img_tank[10]:
                self.rect.x -= 1
                self.rect.y -= 1
            if self.image == self.img_tank[11]:
                self.rect.x -= 1
                self.rect.y -= 2
            if self.image == self.img_tank[12]:
                self.rect.y -= 2
            if self.image == self.img_tank[13]:
                self.rect.x += 1
                self.rect.y -= 2
            if self.image == self.img_tank[14]:
                self.rect.x += 1
                self.rect.y -= 1
            if self.image == self.img_tank[15]:
                self.rect.x += 2
                self.rect.y -= 1
        if self.shoot and len(self.ball_list) <= 2:
            self.shoot = False
            if self.image == self.img_tank[0]:
                ball1 = Ball(self.rect.x+20, self.rect.y+7, 4, 0)
                self.ball_list.append(ball1)
                game.ball_sprites.add(ball1)

            elif self.image == self.img_tank[1]:
                ball1 = Ball(self.rect.x + 24, self.rect.y + 16, 4, 2)
                self.ball_list.append(ball1)
                game.ball_sprites.add(ball1)

            elif self.image == self.img_tank[2]:
                ball1 = Ball(self.rect.x + 23, self.rect.y + 23, 5, 4)
                self.ball_list.append(ball1)
                game.ball_sprites.add(ball1)

            elif self.image == self.img_tank[3]:
                ball1 = Ball(self.rect.x + 15, self.rect.y + 20, 1, 4)
                self.ball_list.append(ball1)
                game.ball_sprites.add(ball1)

            elif self.image == self.img_tank[4]:
                ball1 = Ball(self.rect.x + 7, self.rect.y + 23, 0, 4)
                self.ball_list.append(ball1)
                game.ball_sprites.add(ball1)

            elif self.image == self.img_tank[5]:
                ball1 = Ball(self.rect.x + 3, self.rect.y + 23, -2, 4)
                self.ball_list.append(ball1)
                game.ball_sprites.add(ball1)

            elif self.image == self.img_tank[6]:
                ball1 = Ball(self.rect.x - 5, self.rect.y + 20, -3, 4)
                self.ball_list.append(ball1)
                game.ball_sprites.add(ball1)

            elif self.image == self.img_tank[7]:
                ball1 = Ball(self.rect.x - 10, self.rect.y + 15, -4, 2)
                self.ball_list.append(ball1)
                game.ball_sprites.add(ball1)

            elif self.image == self.img_tank[8]:
                ball1 = Ball(self.rect.x - 10, self.rect.y + 8, -4, 0)
                self.ball_list.append(ball1)
                game.ball_sprites.add(ball1)

            elif self.image == self.img_tank[9]:
                ball1 = Ball(self.rect.x - 12, self.rect.y, -3, -3)
                self.ball_list.append(ball1)
                game.ball_sprites.add(ball1)

            elif self.image == self.img_tank[10]:
                ball1 = Ball(self.rect.x - 4, self.rect.y - 8, -4, -2)
                self.ball_list.append(ball1)
                game.ball_sprites.add(ball1)

            elif self.image == self.img_tank[11]:
                ball1 = Ball(self.rect.x - 5, self.rect.y - 10, -1, -3)
                self.ball_list.append(ball1)
                game.ball_sprites.add(ball1)

            elif self.image == self.img_tank[12]:
                ball1 = Ball(self.rect.x + 7, self.rect.y - 10, 0, -4)
                self.ball_list.append(ball1)
                game.ball_sprites.add(ball1)

            elif self.image == self.img_tank[13]:
                ball1 = Ball(self.rect.x + 14, self.rect.y - 10, 1, -3)
                self.ball_list.append(ball1)
                game.ball_sprites.add(ball1)

            elif self.image == self.img_tank[14]:
                ball1 = Ball(self.rect.x + 20, self.rect.y - 10, 2, -2)
                self.ball_list.append(ball1)
                game.ball_sprites.add(ball1)

            elif self.image == self.img_tank[15]:
                ball1 = Ball(self.rect.x + 25, self.rect.y, 3, -2)
                self.ball_list.append(ball1)
                game.ball_sprites.add(ball1)


# ball collision with tank
def ball_collision(tank_one, tank_two):
    if tank_two.stop:
        return
    for ball in tank_two.ball_list:
        if pygame.sprite.collide_mask(ball, tank_one):
            tank_two.ball_list.remove(ball)
            game.ball_sprites.remove(ball)
            game.coord = [[400, 275], [40, 120], [730, 120], [730, 400]]
            tank_one.hit = True
            tank_two.stop = True
            tank_two.score += 1


# tank wall collision
def wall_collision(tank01, tank02):
    for wall in game.walls:
        if pygame.sprite.collide_mask(tank01, wall):
            # collision with the left side of the wall
            if abs(wall.rect.left - tank01.rect.right) < 25:
                tank01.rect.x -= 15
            # collision with the right side of the wall
            elif abs(tank01.rect.left - wall.rect.right) < 25:
                tank01.rect.x += 15
            # collision with top side of the wall
            elif abs(tank01.rect.top - wall.rect.bottom) < 25:
                tank01.rect.y += 15
            # collision with bottom side of the wall
            elif abs(wall.rect.top - tank01.rect.bottom) < 25:
                tank01.rect.y -= 15

        if pygame.sprite.collide_mask(tank02, wall):
            # collision with top side of the wall
            if abs(tank02.rect.top - wall.rect.bottom) < 25:
                tank02.rect.y += 15
            # collision with bottom side of the wall
            elif abs(wall.rect.top - tank02.rect.bottom) < 25:
                tank02.rect.y -= 15
            # collision with the left side of the wall
            elif abs(wall.rect.left - tank02.rect.right) < 25:
                tank02.rect.x -= 15
            # collision with the right side of the wall
            elif abs(tank02.rect.left - wall.rect.right) < 25:
                tank02.rect.x += 15
