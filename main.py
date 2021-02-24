"""************************
Эта игра buscet
Автор: johnny-KIV
************************"""

import pygame
import random
import os
import time
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
apple_img = pygame.image.load(os.path.join(img_folder, 'gm_apple.png'))
buscet_img = pygame.image.load(os.path.join(img_folder, 'gm_bowel.png'))
good_img = pygame.image.load(os.path.join(img_folder, 'good.png'))
bad_img = pygame.image.load(os.path.join(img_folder, 'bad.png'))
WIDTH = 1250
HEIGHT = 650
FPS = 30
z = 0
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
z=0

class Apple(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = apple_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
    def update(self):

        a = random.randint(1, 1230)
        self.rect.y += 40
        c=random.randint(1,2)
        if c==1:
            self.rect.x -= 20
        if c==2:
            self.rect.x += 20


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        a1 = random.randint(1, 9)
        self.image = buscet_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / a1, HEIGHT / 1.300 )

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -150
        if keystate[pygame.K_RIGHT]:
            self.speedx = 150
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
class Good(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        a1 = random.randint(1, 9)
        self.image = good_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (50, 50)
class Bad(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        a1 = random.randint(1, 9)
        self.image = bad_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (1200, 50)

def  kasanie():

    xa1=apple.rect.x
    xa2=apple.rect.x-51
    xk1=player.rect.x-76.5
    xk2=player.rect.x+76.5
    ya=apple.rect.y-52
    yk=player.rect.y-47.5
    if ya<=yk and  xa1>=xk1  and xa1<=xk2:
        return True
    else:
        return False
# Создаем игру и окно

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basket")
clock = pygame.time.Clock()
background_image = pygame.image.load('images/gm_bg.png')
all_sprites = pygame.sprite.Group()
apple = Apple()
all_sprites.add(apple)
all_sprites2= pygame.sprite.Group()
player = Player()
all_sprites2.add(player)
all_sprites3= pygame.sprite.Group()
good = Good()
all_sprites3.add(good)
all_sprites4= pygame.sprite.Group()
bad = Bad()
all_sprites4.add(bad)
# Цикл игры
"""music = pygame.mixer.music.load('background_music.mp3')
pygame.mixer.music.play(-1, 0.0)"""
running = True
a2 = 0
fontObj2 = pygame.font.Font('freesansbold.ttf', 26)
textSurfaceObj2 = fontObj2.render("0", True, BLACK, RED)
textRectObj2 = textSurfaceObj2.get_rect()
textRectObj2.center = (1200, 50)
screen.blit(textSurfaceObj2, textRectObj2)
while running:

    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background_image, (0, 0))

    if kasanie():
        a3=random.randint(1, 1230)
        apple.rect.top = 0
        apple.rect.right = a3
        z=z+1
        fontObj = pygame.font.Font('freesansbold.ttf',26)
        textSurfaceObj = fontObj.render(str(z), True, BLACK, GREEN)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (50, 50)
        screen.blit(textSurfaceObj, textRectObj)
    if apple.rect.y>HEIGHT:
        s2= random.randint(1, 1230)
        apple.rect.top = 0
        apple.rect.right = s2
        a2 = a2 + 1
        fontObj = pygame.font.Font('freesansbold.ttf', 26)
        textSurfaceObj = fontObj.render(str(a2),True, BLACK, RED)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (1200, 50)
        screen.blit(textSurfaceObj, textRectObj)

    # Обновление
    all_sprites.update()
    all_sprites2.update()
    # Рендеринг
    all_sprites.draw(screen)
    all_sprites2.draw(screen)
    all_sprites3.draw(screen)
    all_sprites4.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()
pygame.quit()