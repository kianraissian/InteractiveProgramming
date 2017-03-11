import pygame
from pygame.locals import*
import os,sys

class Barrier:
    def __init__(self,x,y,width,height,color):
        self.x=x
        self.y=y
        self.color=color

    # def render(self,screen):
    #     barrier=(self.x,self.y,self.width,self.height)
    #     pygame.draw.rect(screen,self.color,barrier,0)
    #     pygame.display.update()

class Block:
    def __init__(self,x,y,width,height,color):
        self.color=color
        self.x=x
        self.y=y
        self.width=width
        self.height=height

class BlockView(object):
    def __init__(self,model):
        self.model=model

    def render(self,screen):
        model=self.model
        rect=(model.x,model.y,model.width,model.height)
        pygame.draw.rect(screen,model.color,rect,0)
        pygame.display.update()

class BlockController(object):
    def __init__ (self,model):
        self.model=model

    def move(self,distance):
        model=self.model
        if event.key==pygame.K_DOWN:
            self.model.y-=distance
        if event.key==pygame.K_UP:
            self.model.y+=distance

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('PyGame App!')
    x = 0
    y = 0
    width=200
    height=200
    screen.fill((0,0,0))
    blue=(0,0,255)
    user=Block(x, y, width, height, blue)
    blockview=BlockView(user)
    blockcontroller=BlockController(Block)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type==pygame.KEYDOWN:
                blockcontroller.move(50)
                print(y)
        blockview.render(screen)
    pygame.quit()
