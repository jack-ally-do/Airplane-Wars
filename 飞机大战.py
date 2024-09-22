import sys
import pygame
import time
import random
import os
pygame.mixer.init()
FPS=60
t=(0,255,0)
b=(0,0,0)
wi=(255,255,255)
pygame.mixer.init()
pygame.init()
Width=400
Height=600
c=(255,0,0)
d=(255,255,0)
pygame.display.set_caption("飞机大战")
screen=pygame.display.set_mode((Width,Height))
background_img=pygame.image.load(os.path.join('img','background.png')).convert()
me_img=pygame.image.load(os.path.join('img','me.png')).convert()
e_img=pygame.image.load(os.path.join('img','enemy2.png')).convert()
bu_img=pygame.image.load(os.path.join('img','bullet1.png')).convert()
bomb_img=pygame.image.load(os.path.join('img','bomb5.png')).convert()
w_img=pygame.image.load(os.path.join('img','w.png')).convert()
bombs=pygame.sprite.Group()
player1=pygame.sprite.Group()
a=pygame.sprite.Group()
rocks=pygame.sprite.Group()
bus=pygame.sprite.Group()
bas=pygame.sprite.Group() 
clock=pygame.time.Clock()

pygame.display.flip()
sound=pygame.mixer.Sound(os.path.join('sound','bullet.wav'))
#sound_back=pygame.mixer.Sound(os.path.join('sound','base.ogg'))
class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(me_img,(55,50))
        self.image.set_colorkey(wi)
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(1,400)
        self.rect.y=random.randrange(-100,-40)
        self.speedy=random.randint(2,6)
        self.speedx=random.randint(-1,1)
    def update(self):
        self.rect.y+=self.speedy
        #self.rect.x+=self.speedx
        if self.rect.top>Height:
            self.rect.x=random.randrange(1,400)
            self.rect.y=random.randrange(-100,-40)
            self.speedy=random.randint(1,3)
            #self.speedx=random.randint(-1,1)
#self.rect.left>Width
#self.rect.right<0
for i in range(5):
    rock=Rock()
    a.add(rock)
    rocks.add(rock)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(e_img,(70,80))
        self.image.set_colorkey(wi)
        self.rect=self.image.get_rect()
        self.rect.centerx=Width/2
        self.rect.bottom=Height-10
        self.speedx=8
    def update(self):
        key_pessed=pygame.key.get_pressed()
        if key_pessed[pygame.K_RIGHT]:
           self.rect.x+=self.speedx 
        if key_pessed[pygame.K_LEFT]:
           self.rect.x-=self.speedx 
        if self.rect.left<0:
            self.rect.left=0
        if self.rect.right>Width:
            self.rect.right=Width
    def shoot(self):
        bu=Bu(self.rect.centerx,self.rect.centery) 
        a.add(bu)
        bus.add(bu)
        sound.play()
player=Player()
a.add(player)
player1.add(player)


           
class Bu(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(bu_img,(10,25))
        self.image.set_colorkey(wi)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.speedy=-10
    def update(self):
        self.rect.y+=self.speedy
        if self.rect.bottom<0:
            self.kill()

sore=0    
running=True
while running:
    clock.tick(FPS)
    for event in pygame.event.get(): 
        if event.type  == pygame.QUIT:
            running=False
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                player.shoot()
            

    
    a.update()
    pygame.display.update()
    screen.fill(wi)
    #sound_back.play()  

    screen.blit(background_img,(0,0))
    a.draw(screen)
    H_PandR=pygame.sprite.groupcollide(rocks,player1,True,False)
    H_R_and_B=pygame.sprite.groupcollide(rocks,bus,True,True) 
    
    for n in H_R_and_B:
        r=Rock()
        
        a.add(r)
        rocks.add(r)
    if H_PandR:
        pygame.quit()
        running=False
    
    
    #sound_back.play()
        
            
pygame.quit()
