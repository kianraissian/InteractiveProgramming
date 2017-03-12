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

    def draw(self, surface):
        model = self.model
        rect=(model.x,model.y,model.width,model.height)
        pygame.draw.rect(screen,model.color,rect,0)

class BlockController(object):
    def __init__ (self, model):
        self.model = model

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.model.dy = 10
            if event.key==pygame.K_UP:
                self.model.dy = -10


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('PyGame App!')

    x = 0
    y = 0
    width=200
    height=200
    BLACK = (0,0,0)
    BLUE = (0,0,255)


    block = Block(x, y, width, height, BLUE)
    block_view = BlockView(block)

    controller = BlockController(block)

    running = True

    while running:
        for event in pygame.event.get():
            controller.handle_event(event)
            if event.type == pygame.QUIT:
                running = False

        block.step()

        screen.fill(BLACK)
        block_view.draw(screen)

        pygame.display.update()

    pygame.quit()
