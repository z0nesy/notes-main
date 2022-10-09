from pygame import *

#створи вікно гри
window = display.set_mode((700, 500))
display.set_caption("Maze")
#задай фон сцени
background = transform.scale(
    image.load("background.jpg"),    
        (700, 500)
    )
window.blit(background,(0, 0))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player (GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"
        
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2  
        self.color_3 = color_3  
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


x1 = 100
y1 = 300

win_width = 700
win_height = 500

player = Player('hero.png', 5, 420, 4)
monster = Enemy('cyborg.png', 620, 280, 2)
final = GameSprite("treasure.png", 630, 420, 0)

w1 = Wall(0, 250, 0, 100, 10, 450, 10)
w2 = Wall(0, 255, 0, 100, 480, 350, 10)
w3 = Wall(0, 255, 0, 100, 20, 10, 380)
w4 = Wall(0, 255, 0, 200, 100, 10, 380)
w5 = Wall(0, 255, 0, 300, 10, 10, 380)
w6 = Wall(0, 255, 0, 440, 100, 10, 380)
w7 = Wall(0, 255, 0, 400, 100, 100, 10)

speed = 10

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

font.init()
font = font.Font(None, 70)
win = font.render('you win!', True, (255, 215, 0))
lose = font.render('YOU lOSE!', True, (180, 215, 0))

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')


run = True
finish = False
clock = time.Clock()

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if final != True:
        window.blit(background,(0, 0))
        player.update()
        monster.update()

        player.reset()
        monster.reset()
        final.reset()

        w1.draw_wall()   
        w2.draw_wall() 
        w3.draw_wall()  
        w4.draw_wall() 
        w5.draw_wall() 
        w6.draw_wall() 
        w7.draw_wall() 

        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) \
            or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) \
            or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) \
            or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7):
            finish = True
            window.blit(lose, (200, 200))
            kick = mixer.Sound('kick.ogg')

        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (200, 200))
            money.play()

    display.update()
    clock.tick(60)
