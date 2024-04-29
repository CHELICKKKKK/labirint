from pygame import *
from GameSprite import GameSprite

class Player(GameSprite):
    def update(self):

        keys_pressed = key.get_pressed()

        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 640:
            self.rect.x += self.speed
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 440:
            self.rect.y += self.speed





















