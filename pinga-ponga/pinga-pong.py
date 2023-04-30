from pygame import *
from random import randint

raketka = 'raketka.png'
ball = 'myachik.png'
bg = 'bg.png'

score1 = 0
score2 = 0
 
win_width = 700
win_height = 500
display.set_caption("PINGA-PONG")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(bg), (win_width, win_height))


class GameSprite(sprite.Sprite):
 #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)

       #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
  #метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    #метод для управления спрайтом стрелками клавиатуры
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed



racket1 = Player(raketka, 15, 250, 50, 125, 5)
racket2 = Player(raketka, 640, 250, 50, 125, 5)
ball = GameSprite(ball, 350, 250, 70, 50, 50)

font.init()
font1 = font.Font(None, 80)
lose1 = font1.render('PLAYER 1 LOSE', True, (0,0,0))
lose2 = font1.render('PLAYER 2 LOSE', True, (0,0,0))

font2 = font.Font(None, 36)

speed_x = 3
speed_y = 3

finish = False
clock = time.Clock()
FPS = 60
#Основной цикл игры:
run = True #флаг сбрасывается кнопкой закрытия окна
while run:
   #событие нажатия на кнопку “Закрыть”
    for e in event.get():
        if e.type == QUIT:
            run = False

    if finish != True:

        window.blit(background,(0,0))

        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > win_height-50 or ball.rect.y < 0:  
            speed_y *= -1

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1.001
            speed_y *= 1.001

        if ball.rect.x < 0:
            score2 = score2 + 1
            ball.rect.x = (350)
            ball.rect.y = (250)

        if ball.rect.x > 700:
            score1 = score1 + 1
            ball.rect.x = (350)
            ball.rect.y = (250)

        if score1 >= 5:
            finish = True
            window.blit(lose2, (200, 200))

        if score2 >= 5:
            finish = True
            window.blit(lose1, (200,200))

        text1 = font2.render(str(score1), 1, (128, 128, 128))
        window.blit(text1, (330, 250))
        text2 = font2.render(str(score2), 1, (128, 128, 128))
        window.blit(text2, (370, 250))


        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)
