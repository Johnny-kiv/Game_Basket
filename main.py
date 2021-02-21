"""************************
Эта игра buscet
Автор: johnny-KIV
************************"""

import pygame
import random
import os
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
apple_img = pygame.image.load(os.path.join(img_folder, 'images/gm_apple.png'))

WIDTH = 1250
HEIGHT = 650
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (200, 255, 200)
BLUE = (0, 0, 255)

class Apple(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = apple_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
    def update(self):
        a = random.randint(1, 1230)
        self.rect.y += 20
        c=random.randint(1,2)
        if c==1:
            self.rect.x -= 20
        if c==2:
            self.rect.x += 20
        if self.rect.bottom > HEIGHT:
            self.rect.top = 0
            self.rect.right = a

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -30
        if keystate[pygame.K_RIGHT]:
            self.speedx = 30
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
 #       if self.rect.left < 0:
  #          self.rect.left = 0

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
# Цикл игры

running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background_image, (0, 0))
    # Обновление
    all_sprites.update()
    all_sprites2.update()
    # Рендеринг
    all_sprites.draw(screen)
    all_sprites2.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()


pygame.quit()