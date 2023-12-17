#Создай собственный Шутер!

from pygame import *

display.set_caption("Shooter")
window = display.set_mode((1920, 1080))
background = transform.scale(image.load('galaxy.jpg'), (1920, 1080))

lost = 0
core = 0


#фоновая музыка
mixer.init()
mixer.music.load('space.mp3')
mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Friend(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        self.rect.y = randint(-100, -70)
        self.rect.x = randint(70, 1200)
        


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[k_LEFT] and self.rect.x >5:
            self.rect.x -= self.speed
        if keys[k_RIGHT] and self.rect.x <1360:
            self.rect.x += self.speed


class Bullet(GameSprite):
    def upgate(self):
         self.rect.y -= self.speed



    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, 10)
        bullets.add(bullet)
        def update(self):           
            self.rect.Bullet += self.speed
            if self.rect.Bullet >= 800:
                Bullet = Bullet.kill 
                self.rect.y = randint(-200, -50)
                self.rect.x = randint(100, 1200)



class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= 800:
            lost += 1
            self.rect.y = randint(-200, -50)
            self.rect.x = randint(100, 1200)

    def update(self):
        self.rect.y += self.speed
        global lost


        if self.rect.y >= 800:
            lost += 1
            self.rect.y = randint(-200, -50)
            self.rect.x = randint(100, 1200)

  
ship = Player('rocket.png', 5, 620 ,80, 100, 10)
ship2 = Player('kosmo_ship.jpg', 5, 520 ,60, 700, 70)

monsters = sprite.Group()
bullets = sprite.Group()
heart = GameSprite('heart.jpg', 1270, 15, 50, 50, 0)


for i in range(7):
    monsters = Enemy('ufo.png', randint(100, 200), randint(-600, -100) )
    monsters.add(monster)

x=0
for i in range(3):
    heart = GameSprite

running= True 
hits = pygame.sprite.spritecollide(Player, mobs, False)
if hits:
    running = False


finish = False
game = True
clock = time.Clock()

font.init()
font_universal = font.Sysfont( 'Arial', 36)

fire_on = False


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_on = True

    if fire_on:
        finish = True
        ship.fire()

    collide = sprite.groupcoloide(monstrers, bullets, True, True)
    for collide in collades:
        score += 1
        monster = Enemy('ufo.png', randint(100, 200), randint(-600, -100) )
        monsters.add(monster)

    if sprite.spritecollide(ship, monsters, False) or lost >= 5:
        finish = True
        print(lose)





    window.blit(background,(0,0))

    text_lost_enemys = font_universal.render('Пропущено:' + str(lost), 1, (255,255,255))
    test_score_enemys = font_universal.render('Пропущено:' + str(lost), 1, (255,255))

    text_lose = font_universal.render('Пропущено:' + str(lost), 1, (255, 255, 255))

    window.blit(background,(0,0))

    if not finish: # пока идет игра
        ship.reset()
        ship.update()
        monsters.draw(window)
        monsters.update()
        window.blit(text_lost_enemys, (10,10))
        window.blit(test_score_enemys, (10,10))


        display.update()
    time.delay(50)


