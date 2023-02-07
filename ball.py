import pygame


class Ball(pygame.sprite.Sprite):

    def __init__(self, tank_x, tank_y, vel_x, vel_y):
        pygame.sprite.Sprite.__init__(self)
        self.x = tank_x
        self.y = tank_y
        self.cont = 0
        self.image = pygame.image.load('Sprites/testeball.png')
        self.image = pygame.transform.scale(self.image, (8 * 5, 8 * 5))
        self.group = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]
        self.dx = vel_x
        self.dy = vel_y

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

    def wall_collision(self, walls):
        for wall in walls:
            if pygame.sprite.collide_mask(self, wall):
                # collision with top side of the wall
                if abs(self.rect.top - wall.rect.bottom) < 25 and self.dy < 0:
                    self.dy *= -1
                # collision with bottom side of the wall
                elif abs(wall.rect.top - self.rect.bottom) < 25 and self.dy > 0:
                    self.dy *= -1
                # collision with the left side of the wall
                elif abs(wall.rect.left - self.rect.right) < 25 and self.dx > 0:
                    self.dx *= -1
                # collision with the right side of the wall
                elif abs(self.rect.left - wall.rect.right) < 25 and self.dx < 0:
                    self.dx *= -1
                self.cont += 1
