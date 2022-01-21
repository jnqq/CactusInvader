import pygame
class Attack(object):

    def __init__(self,x,y,rad,color,VelX,VelY):
        self.x = x
        self.y = y
        self.rad = rad
        self.color = color
        self.velX = VelX
        self.velY = VelY

    def draw(self,screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.rad)
