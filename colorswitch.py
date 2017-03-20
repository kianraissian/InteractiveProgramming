import pygame
from pygame.locals import*
import os,sys
import random

class Barrier:
    def __init__(self,x,y,width,height,color):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.color=color

class BarrierView(object):
    def __init__(self,models):
        self.models=models

    def draw(self):
        for barrier in self.models:
            models=self.models
            thisbarrier=(barrier.x, barrier.y, barrier.width, barrier.height)
            pygame.draw.rect(screen, barrier.color, thisbarrier, 0)

class Block:
    def __init__(self,x,y,width,height,color):
        self.color = color
        self.x = x
        self.y = y
        self.dy = 0
        self.width = width
        self.height = height

    def step(self):
        self.y += self.dy
        self.dy = 0

class BlockView(object):
    def __init__(self,model):
        self.model=model

    def draw(self):
        model = self.model
        rect=(model.x,model.y,model.width,model.height)
        pygame.draw.rect(screen,model.color,rect,0)

class BlockController(object):
    def __init__ (self, model):
        self.model = model

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.model.dy = 25
            if event.key==pygame.K_UP:
                self.model.dy = -25
            if event.key==pygame.K_r:
                self.model.color = (255,0,0)
            if event.key==pygame.K_b:
                self.model.color = (0,0,255)
            if event.key==pygame.K_g:
                self.model.color = (0,255,0)



if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('PyGame App!')

    RED=(255,0,0)
    BLACK = (0,0,0)
    BLUE = (0,0,255)
    GREEN= (0,255,0)
    colorlist=[RED, BLUE, GREEN]
    barrierlist=[]
    for i in range(3):
        barrier=Barrier(300, 150+150*i, 200, 50, random.choice(colorlist))
        barrierlist.append(barrier)
    barrier_view=BarrierView(barrierlist)

    block = Block(350, 550, 50, 50, BLUE)
    block_view = BlockView(block)

    controller = BlockController(block)

    running = True

    while running:
        for event in pygame.event.get():
            controller.handle_event(event)
            if event.type == pygame.QUIT:
                running = False

        block.step()
        for barrier in barrierlist:
            if (barrier.y+barrier.height)>block.y and block.y>barrier.y:
                if block.color!=barrier.color:
                    pygame.quit()

        screen.fill(BLACK)
        block_view.draw()
        barrier_view.draw()
        pygame.display.update()

    pygame.quit()
