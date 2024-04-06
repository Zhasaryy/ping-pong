from pygame import *
from random import randint

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
kick = mixer.Sound('fire.ogg')
window = display.set_mode((700, 500))
display.set_caption('Шутер')
background = transform.scale(image.load('galaxy.jpg'), (700, 500)) 
sprite1 = transform.scale(image.load('rocket.png'), (50, 500))
FPS = 60
game = True
clllock = time.Clock()
speed = 2
finish = False
lost = 0
schet = 0
font.init()
font2 = font.SysFont(None, 40)
font3 = font.SysFont(None, 100)
max_lost = 5
life = 3

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (72, 95))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.image = transform.scale(image.load(player_image), (75, 49))
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
            
        if keys_pressed[K_d] and self.rect.x < 630:
            self.rect.x += self.speed
   
