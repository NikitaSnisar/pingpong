from pygame import *
win_width = 700
win_height = 500
display.set_caption("Ping-Pong")
window = display.set_mode((win_width, win_height))
clock = time.Clock()
FPS= 60
game = True
back = (0,0,135)
window.fill(back)
 
class GameSprite(sprite.Sprite):
 #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #вызываем конструктор класса (Sprite):
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
   #метод для управления 2м игрком стрелками клавиатуры
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
 

raketka = Player('raketka.jpg',335, 0, 50,50, 10)
raketka2 = Player('raketka.jpg', -335, 0, 50,50, 10)
ball = Player("ball.jpg", 0, 0,50,50,5)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if sprite.collide_rect(raketka, ball) or sprite.collide_rect(raketka2, ball):
        speed_x *= -1


    display.update()
    clock.tick(FPS)