import random
import time
import sys
import os
import pygame
import snake
from pygame.locals import *

P2 = (171, 240,   0)
P1 = (226, 102, 183)
P3 = (197,   0, 128)
P4 = (226,  59, 167)
BGCOLOR = P1

class Game:
    'Game where snake eats snacks'
    def __init__(self, height=240, width=240, cell=20):
        self.score = 0
        self.speed = 0.3
        self.height = height
        self.width = width
        self.cell = cell
        self.run = True
        self.startSpeed = self.speed

        pygame.init()
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Python Eats Snacks')

        self.Main()

    def CreateNewSnake(self):
        'Creates new Snake object'
        randx = random.randint(5,(self.width/self.cell)-5)
        randy = random.randint(5,(self.height/self.cell)-5)
        return snake.Snake(randx*self.cell, randy*self.cell)
    def CreateNewFoodItem(self):
        'Creates new food item'
        self.foodx = (random.randint(5,(self.width/self.cell)-5))*self.cell
        self.foody = (random.randint(5,(self.height/self.cell)-5))*self.cell
        for i in self.snake.positions:
            if self.foodx == i[0] and self.foody == i[1]:
                self.CreateNewFoodItem()
    def DrawField(self):
        pygame.draw.line(self.display, P4, (self.cell-(self.cell/2)-1, 0), (self.cell-(self.cell/2)-1, self.height), self.cell)
        pygame.draw.line(self.display, P4, (0, (self.cell-(self.cell/2)-1)), (self.width, (self.cell-(self.cell/2)-1)), self.cell)
        pygame.draw.line(self.display, P4, (self.width-self.cell+(self.cell/2)-1, 0), (self.width-self.cell+(self.cell/2)-1, self.height), self.cell)
        pygame.draw.line(self.display, P4, (0, self.height-self.cell+(self.cell/2)-1), (self.width, self.height-self.cell+(self.cell/2)-1), self.cell)
    def DrawSnake(self):
        for i in self.snake.positions:
            x = i[0]
            y = i[1]
            snakeSegmentRect = pygame.Rect(x, y, self.cell, self.cell)
            pygame.draw.rect(self.display, P3, snakeSegmentRect)
            snakeInnerSegmentRect = pygame.Rect(x + 4, y + 4, self.cell - 8, self.cell - 8)
            pygame.draw.rect(self.display, P3, snakeInnerSegmentRect)

    def drawFoodItem(self):
        foodItem = pygame.Rect(self.foodx, self.foody, self.cell, self.cell)
        pygame.draw.rect(self.display, P2, foodItem)

    def Collision(self):
        if self.snake.x == self.foodx and self.snake.y == self.foody:
            self.score += 1
            self.speed += -0.005
            self.snake.size += 1
            self.CreateNewFoodItem()
        if self.snake.x == self.width-(self.cell*2) or self.snake.y == self.height-(self.cell*2) or self.snake.x == self.cell or self.snake.y == self.cell:
            self.run = False
        for k, i in enumerate(self.snake.positions):
            if i[0] == self.snake.x and i[1] == self.snake.y and k != len(self.snake.positions)-1:
                self.run = False
        if self.run == False:
            os.system('clear')
            print ''
            print ' --- SCORE: %s --- ' % (self.score)
            print ' === GAME OVER === '
            print ''
            print ''
            os._exit(1)

    def Main(self):
        'Main function'
        self.snake = self.CreateNewSnake()
        self.CreateNewFoodItem()
        self.Loop()

    def Loop(self):
        thisTime = time.time()
        while self.run:
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                elif event.type == KEYDOWN:
                    self.snake.ChangeDirection(event.key)

            if time.time() - thisTime >= self.speed:
                self.Collision()
                self.snake.Move(self.cell)
                if self.run:
                    self.display.fill(BGCOLOR)
                    self.DrawField()
                    self.drawFoodItem()
                    self.DrawSnake()
                thisTime = time.time()
            pygame.display.update()

game = Game()