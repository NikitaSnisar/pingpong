from pygame import *
win_width = 600
win_height = 500
display.set_caption("Ping-Pong до 3")
window = display.set_mode((win_width, win_height))
clock = time.Clock()
FPS= 60
game = True
back = (0,0,135)
window.fill(back

score1 = (0)
score2 = (0)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height)) #вместе 55,55 - параметры
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
 


 

racket1 = Player('raketka.jpg', 30, 200, 5, 50, 150) 
racket2 = Player('raketka.jpg', 520, 200, 5, 50, 150)   
ball = GameSprite('ball.jpg', 200, 200, 10, 40, 40)

finish = False

font.init()
font = font.Font(None, 35)
WIN1 = font.render('Игрок 1 победил!!!', True, (255, 0, 0))
WIN2 = font.render('Игрок 2 выиграл!!', True, (255, 0, 0))

speed_x = 7
speed_y = 7


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
  
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
 
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1
      
    
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if score1 == 3:
            finish = True
            game_over = False

        if score2 == 3:
            finish = True
            game_over = False
            
        text = font2.render("игрок1 " + str(score1), 1, (255, 255, 255))
        window.blit(text, (10, 20))
 
        text_lose = font2.render("игрок2 " + str(score2), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))



        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)