import pygame
class Upgradeblock (object):
    def __init__(self,x,y,widht,height):
        self.x = x
        self.y = y
        self.widht = widht
        self. height = height
        self.hitbox = (self.x, self.y, self.widht, self. height)
        self.picked = False
        self.upgrade = 40
    def draw(self,screen):
        pygame.draw.rect(screen,(255,222,0),self.hitbox)

