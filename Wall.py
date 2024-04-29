from pygame import *


class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, height_wall, width_wall, wall_x, wall_y, window ):
        super().__init__()
        self.color1 = color_1
        self.color2 = color_2
        self.color3 = color_3
        self.height = height_wall
        self.width = width_wall
        self.image = Surface((self.width, self.height))
        self.image.fill((self.color1, self.color2, self.color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
        self.window = window
    def draw_wall(self):
        self.window.blit(self.image, (self.rect.x, self.rect.y))
