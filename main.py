#!/usr/bin/env python

import pygame
import random
from enemy import Enemy
from attack import Attack
from player import Player
from upgradeBlock import Upgradeblock
pygame.init()

r = [1280, 720]
background = pygame.image.load('1.jpg')
icon = pygame.image.load('enemy2.png')
pygame.display.set_caption("Cactus Invader")
screen = pygame.display.set_mode((r))
pygame.display.set_icon(icon)
fps_clock = pygame.time.Clock()

gunSound = pygame.mixer.Sound('gun.wav')
oof = pygame.mixer.Sound('hurt.wav')
music = pygame.mixer.music.load('cr.wav')
explosion = pygame.mixer.Sound('explosion.wav')
pygame.mixer.music.play(-1)

def redraw():
    if guy.health > 0:
        screen.blit(background, (0,0))
        text = font.render('Wynik: ' + str(score), 1, (255,255,255))
        screen.blit(text,(15,15))
        text2 = font.render('Runda: ' + str(score2),1,(255,255,255))
        screen.blit(text2,(15,60))
        text3 = font.render('Życie  ' + str(guy.health) + '/20',1,(255,255,255))
        screen.blit(text3,(500,15))
        guy.draw(screen)
        for cactus in cactuses:
            cactus.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)
        if not block.picked:
            if score2 == 4:
                block.draw(screen)
                textblock = font3.render('?',1,(255,0,0))
                screen.blit(textblock,(block.x + 6,block.y + 2))
        pygame.display.update()
    else:
        screen.fill((100,0,0))
        text4 = font2.render('GAME OVER',1,(255,0,0))
        screen.blit(text4,(400,320))
        text2 = font.render('Runda: ' + str(score2), 1, (0, 0, 255))
        screen.blit(text2, (400, 400))
        text = font.render('Uzyskany wynik: ' + str(score), 1, (0, 255, 0))
        screen.blit(text, (400, 450))
        pygame.display.update()
        pygame.time.delay(500)

score = 0
cactuses =[]
maximumCactuses = 2
score2 = 1
for i in range(maximumCactuses):
    cactuses.append(Enemy(0-64,(random.randint(125,720 - 64)), 64, 64, (r[0]+64),(random.randint(1,10))))
guy = Player(r[0]//2,r[1]//2,64,64)
block = Upgradeblock(random.randint(0+40,r[0]-40),random.randint(115,r[1]-40),30,30)
bullets = []
bulletCount = 0
running = True
font = pygame.font.SysFont('ariel',50, True, True)
font2 = pygame.font.SysFont('ariel',100,True,True)
font3 = pygame.font.SysFont('comicsans',40,True,True)

while running:
    fps_clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif guy.health < 1:
            pygame.time.delay(500)
            running = False

    for cactus in cactuses:
        if guy.touchable:
            if cactus.isHealth:
                if guy.hitbox[1] < cactus.hitbox[1] + cactus.hitbox[3]-30 and guy.hitbox[1] + guy.hitbox[3] > cactus.hitbox[1]:
                    if guy.hitbox[0] + guy.hitbox[2] > cactus.hitbox[0]+20 and guy.hitbox[0] < cactus.hitbox[0]+20 + cactus.hitbox[2]-30:
                        guy.hit(screen)
                        score -=5
                        explosion.play()
                        guy.touchable = False
        else:
            if guy.touchCount == 100:
                guy.touchable = True
                guy.touchCount =0
            else:
                guy.touchCount += 1

    if bulletCount > 0:
        bulletCount += 1
    if bulletCount > block.upgrade:
        bulletCount = 0

    for bullet in bullets:
        for cactus in cactuses:
            if bullet.y - bullet.rad < cactus.hitbox[1] + cactus.hitbox[3] and bullet.y + bullet.rad > cactus.hitbox[1]:
                if bullet.x + bullet.rad > cactus.hitbox[0] and bullet.x - bullet.rad < cactus.hitbox[0] + cactus.hitbox[2]:
                    if cactus.isHealth:
                        score += 1
                        cactus.hit()
                        oof.play()

        if bullet.x < r[0] and bullet.x > 0:
            bullet.x += bullet.velX
        elif not len(bullets) == 0:
            bullets.pop(bullets.index(bullet))
        else:
            pass

        if bullet.y < r[1] and bullet.y > 0:
            bullet.y -= bullet.velY
        elif not len(bullets) == 0:
            bullets.pop(bullets.index(bullet))
    if not block.picked:
        if guy.hitbox[1] < block.hitbox[1] + block.hitbox[3] and guy.hitbox[1] + guy.hitbox[3] > block.hitbox[1] - 14:
            if guy.hitbox[0] + guy.hitbox[2] > block.hitbox[0] and guy.hitbox[0] < block.hitbox[0] + block.hitbox[2]:
                if score2 == 4:
                    block.picked = True
                    block.upgrade = 3
                    guy.getUpgrade(screen)

    for cactus in cactuses:
        if not cactus.isHealth:
            cactuses.pop(cactuses.index(cactus))
        if len(cactuses) == 0:
            guy.health = 20
            score2 += 1
            maximumCactuses *=1.5
            for i in range(int(maximumCactuses)):
                cactuses.append(Enemy(0 - 64, (random.randint(115, 720-64)), 64, 64, (r[0] + 64), (random.randint(1, 10))))

    press = pygame.key.get_pressed()
    if press[pygame.K_RIGHT] and bulletCount == 0:
        gunSound.play()
        if len(bullets) < 3:
            bullets.append(Attack(round(guy.playerX + guy.width // 2),round(guy.playerY + guy.height // 2),6,(100,255,0),30,0))
        bulletCount = 1
    if press[pygame.K_LEFT] and bulletCount == 0:
        gunSound.play()
        if len(bullets) < 3:
            bullets.append(Attack(round(guy.playerX + guy.width // 2),round(guy.playerY + guy.height // 2),6,(100,255,0),-30,0))
        bulletCount = 1
    if press[pygame.K_UP] and bulletCount == 0:
        gunSound.play()
        if len(bullets) < 3:
            bullets.append(Attack(round(guy.playerX + guy.width // 2),round(guy.playerY + guy.height // 2),6,(100,255,0),0,30))
        bulletCount = 1
    if press[pygame.K_DOWN] and bulletCount == 0:
        gunSound.play()
        if len(bullets) < 3:
            bullets.append(Attack(round(guy.playerX + guy.width // 2),round(guy.playerY + guy.height // 2),6,(100,255,0),0,-30))
        bulletCount = 1

    if press[pygame.K_s]:
        guy.playerY +=guy.vel

    if press[pygame.K_d] and guy.playerX < r[0] - guy.height:
        guy.playerX += guy.vel

    elif press[pygame.K_a] and guy.playerX > 0:
        guy.playerX -= guy.vel

    if press[pygame.K_w]:
        guy.playerY -= guy.vel

    if guy.playerY > r[1] - guy.height:
        guy.playerY = r[1] - guy.height
    if guy.playerY < 115:
        guy.playerY = 115

    redraw()
pygame.quit()


