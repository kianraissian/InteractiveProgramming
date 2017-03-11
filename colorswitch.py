import pygame
from pygame.locals import*
import os,sys

class Barrier:
    def __init__(self,x,y,color):
        self.x=x
        self.y=y
        self.color=color

class Block:
    def __init__(self,x,y,width,height,color):
        self.color=color
        self.x=x
        self.y=y
        self.width=width
        self.height=height

    def render(self,screen):
        rect=(self.x,self.y,self.width,self.height)
        pygame.draw.rect(screen,self.color,rect,0)
        pygame.display.update()

    def move(self,distance):
        if event.key==pygame.K_DOWN:
            self.y-=distance
        if event.key==pygame.K_UP:
            self.y+=distance


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('PyGame App!')

    x = 0
    y = 0
    width=200
    height=200
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type==pygame.KEYDOWN:
                Block.move(50)
        screen.fill((0,0,0))
        blue=(0,0,255)


        block=Block(x, y, width, height, blue)
        block.render(screen)

    pygame.quit()
