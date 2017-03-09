import pygame
from pygame.locals import*
import os, sys

class Node:
    def __init__(self,x,y,width,height,next_node=None):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.next_node=next_node

        img = pygame.image.load('snake.png')
        self.img=pygame.transform.scale(img,(self.width,self.height))

    def render(self):
        screen.blit(self.img,(self.x, self.y))
        pygame.display.update()

class LinkedList:
    def __init__(self,head,size):
        self.head=head
        self.size=size
        current = head;
        for i in range(size):
            newnode=Node(current.x-100,current.y,100,100,None)
            current.next_node = newnode;
            current = current.next_node;
    def render(self):
        current = self.head
        for i in range(self.size):
            render(current)
            current = current.next_node

    def movetail(self):
        current=head
        while current.next_node!=None:
            current = current.next_node
        current.next_node=None
        newhead=Node(head.x+100,head.y,100,100,self.head)
        self.head=newhead


class Snake:
    def __init__(self,x,y,width,height):



    def move(self, direction, distance):
        if direction==pygame.K_RIGHT:
            self.x+=distance
        if direction==pygame.K_DOWN:
            self.y+=distance
        if direction==pygame.K_UP:
            self.y-=distance
        if direction==pygame.K_LEFT:
            self.x-=distance

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600)) # window size, as a tuple
    pygame.display.set_caption('PyGame App!')
    # snake = Snake(0, 0, 100, 100)
    # models=[snake]
    head = Node(0, 0, 100, 100, None)
    snakelist = LinkedList(head, 3)
    models=[snakelist]
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # user presses the x-button
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                else:
                    # snake.move(event.key, 3)
                    snakelist.movetail()
        screen.fill((0,0,0))
        snakelist.render()
    pygame.quit()
