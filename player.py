import pygame
move = [pygame.image.load('1.png'), pygame.image.load('2.png')]
godmode = [pygame.image.load('fire1.png'),pygame.image.load('fire2.png')]
class Player(object):

    def __init__(self, playerX, playerY, width, height):
        self.playerX = playerX
        self.playerY = playerY
        self.width = width
        self.height = height
        self.hitbox = (self.playerX, self.playerY, width, height)
        self.vel = 6
        self.walkCount = 0
        self.touchable = True
        self.touchCount = 0
        self.health = 20

    def draw(self,screen):
        if self.walkCount >= 16:
            self.walkCount = 0
        if not (self.touchable):
            screen.blit(godmode[self.walkCount//8], (self.playerX, self.playerY))
            self.walkCount +=1
        else:
            screen.blit(move[self.walkCount//8], (self.playerX, self.playerY))
            self.walkCount +=1


        self.hitbox = (self.playerX, self.playerY, self.width, self.height)
        pygame.draw.rect(screen, (255, 0, 0), (500, 60, 500, 10))
        pygame.draw.rect(screen, (0, 255, 0), (500, 60, 500 - (26 * (20 - self.health)), 10))
        pygame.draw.rect(screen, (100,30,255),(0,100,1280,10))

    def hit(self,screen):
        if self.touchable:
            if self.health > 0:
                self.health -= 1
        inf1 = pygame.font.SysFont('ariel', 60)
        text = inf1.render('-5!', 1, (255,0,0))
        screen.blit(text, (self.playerX + self.width, self.playerY))
        pygame.display.update()

    def getUpgrade(self,screen):
        inf2 = pygame.font.SysFont('comicsans',200)
        upgradeMessange = inf2.render('LASER UPGRADE', 1, (100, 255, 0))
        screen.blit(upgradeMessange, (20, 320))
        pygame.display.update()
        pygame.time.delay(500)
