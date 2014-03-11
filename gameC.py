import random
import time
import sys
import select
import getch
import os
import snake

class Game:
    'Game where snake eats snacks'
    def __init__(self, cell=1, height=24, width=24):
        self.score = 0
        self.speed = 0.5
        self.height = height
        self.width = width
        self.run = True
        self.cell = cell
        self.startSpeed = self.speed
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
    def Loop(self):
        'Loops while self.run = True.'
        thisTime = time.time()
        while self.run:
            char = getch._Getch()
            self.snake.ChangeDirection(char.impl())
            if time.time() - thisTime >= self.speed:
                self.Collision()
                self.snake.Move()
                if self.run:
                    self.DrawField()
                thisTime = time.time()
    def DrawField(self):
        os.system('clear')
        board = []
        for i in range(0,self.width):
            if i == 0 or i == self.width-1:
                board.append(["="] * self.height)
            else:
                board.append([" "] * self.height)

        for k, i in enumerate(board[1]):
            board[k][0] = "="
            board[k][self.width-1] = "="

        board[self.foodx][self.foody] = "F"
        for i in self.snake.positions:
            board[i[0]][i[1]] = "X"
        for i in board:
            print " ".join(i)
        print ''
        currSpeed = (self.startSpeed/self.speed)*100
        print ' SCORE: %s ' % (self.score)
        print ' SPEED: ' + str(int(currSpeed)) + '%'
    def Collision(self):
        if self.snake.x == self.foodx and self.snake.y == self.foody:
            self.score += 1
            self.speed += -0.025
            self.snake.size += 1
            self.CreateNewFoodItem()
        if self.snake.x == self.height-2 or self.snake.y == self.width-2 or self.snake.x == 0 or self.snake.y == 0:
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