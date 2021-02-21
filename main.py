#************************
#
#
#************************

import pygame
import random
root=pygame
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
        b = random.randint(1, 9)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 100))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / b, HEIGHT / b)

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
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basket")
clock = pygame.time.Clock()
background_image = pygame.image.load('gm_bg.png')
all_sprites = pygame.sprite.Group()
all_sprites1 = pygame.sprite.Group()
player = Player()
all_sprites1.add(player)
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
    # Рендеринг
    all_sprites1.update()
    all_sprites.draw(screen)
    all_sprites1.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()


pygame.quit()