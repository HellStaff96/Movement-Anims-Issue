from pygame import *
'''Игровая сцена'''

scr_W = 1280
scr_H = 720

fps = 60

screen = display.set_mode((scr_W, scr_H)) #Настраиваем размер окна
display.set_caption('Shadows of the past') # называем нашу игру!
display.set_icon(image.load('PH_Icon.png'))

background = transform.scale(image.load('Placeholders/PH_Locations/PH_NightSky.jpg'), (scr_W, scr_H)) #добавление фона и настраиваем его
clock = time.Clock()

#hero = transform.scale(image.load("Placeholders/PH_Anims/PH_RightAnim/PHR_1.png"),(90, 90)) # я с этим говном мучалась долго ибо ему всё не то
# Крч, тут мы даем герою спарйт(1)
'''Анимация персонажей'''

# walk_left = [
#     image.load('images/hero/left/PHL_1.png'),
#     image.load('images/hero/left/PHL_2.png'),
#     image.load('images/hero/left/PHL_3.png'),
#     image.load('images/hero/left/PHL_4.png')
# ]

# walk_right = [
#     image.load('images/hero/right/PHR_1.png'),
#     image.load('images/hero/right/PHR_2.png'),
#     image.load('images/hero/right/PHR_3.png'),
#     image.load('images/hero/right/PHR_4.png')
# ]
walk_left = [
    image.load('Placeholders/PH_Left.png'),
    image.load('Placeholders/PH_Left.png'),
    image.load('Placeholders/PH_Left.png'),
    image.load('Placeholders/PH_Left.png')
]

walk_right = [
    image.load('Placeholders/PH_Right.png'),
    image.load('Placeholders/PH_Right.png'),
    image.load('Placeholders/PH_Right.png'),
    image.load('Placeholders/PH_Right.png')
]

walk_up = [
    image.load("Placeholders/PH_Foward.png"),
    image.load("Placeholders/PH_Foward.png"),
    image.load("Placeholders/PH_Foward.png"),
    image.load("Placeholders/PH_Foward.png")
]

walk_down = [
    image.load("Placeholders/PH_Down.png"),
    image.load("Placeholders/PH_Down.png"),
    image.load("Placeholders/PH_Down.png"),
    image.load("Placeholders/PH_Down.png")
]

'''Шаблон пресонажей!'''
class MainHero(sprite.Sprite):
    def __init__(self, player_img, x, y, w, h, speed):
        sprite.Sprite.__init__(self) #говорим что наследуем sprite.Sprite
        self.w = w
        self.h = h
        self.image = transform.scale(image.load(player_img), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.count = 0 #количество проиграных анимаций, изначально оно будет приравниватся 0


class Player(MainHero):
    def update(self):
        keys = key.get_pressed()

        if keys[K_d] and self.rect.x < scr_W - self.w:
            self.rect.x += self.speed
            self.left = False
            self.right = True
            self.up = False
            self.down = False

        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
            self.left = True
            self.right = False
            self.up = False
            self.down = False
            
            
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
            self.left = False
            self.right = False
            self.up = True
            self.down = False
            
        if keys[K_s] and self.rect.y < scr_H - self.h:
            self.rect.y += self.speed
            self.left = False
            self.right = False
            self.up = False
            self.down = True
            
        else:
            self.up = False
            self.down = False
            self.left = False
            self.right = False
            self.count = 0

    def animation(self):
        if self.count + 1 >= fps:
            self.count = 0
        if self.left:
            screen.blit(transform.scale(walk_left[self.count // 10], (self.w, self.h)), (self.rect.x, self.rect.y))
            self.count += 1

        elif self.right:
            screen.blit(transform.scale(walk_right[self.count // 10], (self.w, self.h)), (self.rect.x, self.rect.y))
            self.count += 1
        elif self.up:
            screen.blit(transform.scale(walk_up[self.count // 10], (self.w, self.h)), (self.rect.x, self.rect.y))
            self.count += 1

        elif self.down:
            screen.blit(transform.scale(walk_down[self.count // 10], (self.w, self.h)), (self.rect.x, self.rect.y))
            self.count += 1

        else:
            screen.blit(self.image, (self.rect.x, self.rect.y))
            self.count = 0

    

'''Персонажи'''

#hero = Player('images/hero/right/PHR_1.png', 100, 300, 90, 90, 8)
hero = Player('Placeholders/PH_Left.png', 100, 30, 90, 90, 5)

'''Игровой цикл'''
game = True

x = 100
y = 300
speed = 10

while game: # Цикл игры
    screen.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False

    hero.update()
    hero.animation()

    display.update()
    clock.tick(fps)
