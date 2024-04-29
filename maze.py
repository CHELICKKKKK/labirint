from pygame import *
from GameSprite import GameSprite
from Player import Player
from Enemy import Enemy
from Wall import Wall

# создай окно игры
window = display.set_mode((700, 500))
display.set_caption("лабиринт")

win = print('YOU WIN')

# задай фон сцены
background = transform.scale(image.load("background.jpg"), (700, 500))

mixer.init()
mixer.music.load('Creedence Clearwater Revival - Fortunate Son.mp3')
mixer.music.play()

#персонажи
wall_1 = Wall(250, 140, 0, 320, 18, 180, 15, window)
wall_2 = Wall(250, 140, 0, 18, 490, 180, 15, window)
hero = Player('hero.png', 100, 350, 10, window)
cyborg = Enemy('cyborg.png', 400, 350, 5, window)
treasure = GameSprite('treasure.png', 625, 425, 10, window)

FPS = 60
clock = time.Clock()
game = True
finish = False
while game:
    # Установка ФПС и обновление экрана
    clock.tick(FPS)







    for e in event.get():
        # обработай событие «клик по кнопке "Закрыть окно"»
        if e.type == QUIT:
            game = False

    while finish is not True:

        window.blit(background, (0, 0))
        wall_1.draw_wall()
        wall_2.draw_wall()
        hero.reset()
        cyborg.reset()
        treasure.reset()
        hero.update()
        wall_1.update()
        wall_2.update()
        cyborg.update()

if finish != True:
    if sprite.collide_rect(hero, treasure):
        window.blit(win, (200, 200))
        finish = True
        treasure.play()

    display.update()

