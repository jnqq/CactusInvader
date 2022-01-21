import pygame
class Enemy(object):

    enemyRight = [pygame.image.load('enemy2.png'), pygame.image.load('enemy3.png'), pygame.image.load('enemy4.png')]
    enemyLeft =  [pygame.image.load('enemy5.png'), pygame.image.load('enemy6.png'), pygame.image.load('enemy7.png')]

    def __init__(self,enemyX,enemyY,widht,height,end,vel):
        self.enemyX = enemyX
        self.enemyY = enemyY
        self.widht = widht
        self.height = height
        self.end = end
        self.walkCount = 0
        self.path = [self.enemyX, self.end]
        self.vel = vel
        self.hitbox = (self.enemyX, self.enemyY, self.widht,self.height)
        self.health = 5
        self.isHealth = True
    def draw(self,screen):
        self.move()
        if self.walkCount >=9:
            self.walkCount = 0
        if self.vel > 0:
            screen.blit(self.enemyRight[self.walkCount // 3], (self.enemyX,self.enemyY))
            self.walkCount +=1
        else:
            screen.blit(self.enemyLeft[self.walkCount // 3], (self.enemyX, self.enemyY))
            self.walkCount += 1
        pygame.draw.rect(screen, (255,0,0), (self.hitbox[0] - 10, self.hitbox[1] - 10, 100, 5))
        pygame.draw.rect(screen, (0, 255, 0), (self.hitbox[0] - 10, self.hitbox[1] - 10, 100 - (20 * (5 - self.health)), 5))
        self.hitbox = (self.enemyX, self.enemyY, self.widht, self.height)

    def move(self):
        if self.vel > 0:
            if self.enemyX + self.vel < self.path[1]:
                self.enemyX += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.enemyX - self.vel > self.path[0]:
                self.enemyX += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 1:
            self.health -= 1
        else:
            self.isHealth = False
