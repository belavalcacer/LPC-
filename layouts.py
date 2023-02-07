import wall
from config import *


class Layouts:
    layouts = []

    def __init__(self, layout_type: int):
        self.group = pygame.sprite.Group()
        self.get_screen()
        self.wall_color = "#d4a941"
        self.bg_color = "#861c09"
        self.rectangle()

        for layout in self.layouts[layout_type - 1]:
            self.group.add(wall.Wall(self.wall_color, layout[0], layout[1]))

    def get_group(self):
        return self.group

    def get_bg_color(self):
        return self.bg_color

    def rectangle(self):
        self.group.add(wall.Wall(self.wall_color, (800, 26), (400, 70)))
        self.group.add(wall.Wall(self.wall_color, (800, 26), (400, 537)))
        self.group.add(wall.Wall(self.wall_color, (26, 441), (13, 303)))
        self.group.add(wall.Wall(self.wall_color, (26, 441), (787, 303)))

    def get_screen(self):

        layout_temp = [[RECT_2, (480, 190)], [RECT_1, (500, 210)], [RECT_2, (330, 190)],
                       [RECT_1, (310, 210)], [RECT_2, (330, 390)], [RECT_1, (310, 370)],
                       [RECT_2, (480, 390)], [RECT_1, (500, 370)], [RECT_4, (560, 303)],
                       [RECT_4, (240, 303)], [RECT_5, (650, 303)], [RECT_5, (150, 303)],
                       [RECT_1, (670, 259)], [RECT_1, (670, 347)], [RECT_1, (130, 259)],
                       [RECT_1, (130, 347)], [RECT_8, (400, 90)], [RECT_8, (400, 520)],
                       [RECT_2, (170, 150)], [RECT_2, (170, 420)], [RECT_2, (630, 150)],
                       [RECT_2, (630, 420)]]

        self.layouts.append(layout_temp)
