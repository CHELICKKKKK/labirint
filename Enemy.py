from pygame import *
from GameSprite import GameSprite

class Enemy(GameSprite):
    def update(self):


        if self.rect.x <= 400:
            self.direction = 'right'

        if self.rect.x >= 700-85:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed

        elif self.direction == 'right':
                self.rect.x += self.speed

