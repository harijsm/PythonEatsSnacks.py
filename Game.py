import random
import time
import sys
import select
import getch
import os

class Game:
    'Game where snake eats snacks'
    def __init__(self, height=24, width=24):
        self.score = 0
        self.speed = 0.5
        self.height = height
        self.width = width
        self.run = True
        self.startSpeed = self.speed
        self.Main()
    def CreateNewSnake(self):
        'Creates new Snake object'
        randx = random.randint(1,self.height-2)
        randy = random.randint(1,self.width-2)
        return Snake(randx, randy)
    def CreateNewFoodItem(self):
        'Creates new food item'
        self.foodx = random.randint(1,self.height-2)
        self.foody = random.randint(1,self.width-2)
        if self.foodx == self.snake.x and self.foody == self.snake.y:
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
    
class Snake:
    'Very hungry snake'
    def __init__(self, x=0, y=0, size=1, direction='up'):
        self.x = x
        self.y = y
        self.size = size+1
        self.direction = direction
        self.positions = []
    def Move(self):
        'Changes snakes x, y according to its direction'
        if self.direction == 'up':
            self.x = self.x-1
        elif self.direction == 'down':
            self.x = self.x+1
        elif self.direction == 'left':
            self.y = self.y-1
        elif self.direction == 'right':
            self.y = self.y+1

        self.positions.append([self.x, self.y])
        del self.positions[len(self.positions)-self.size:len(self.positions)-self.size+1]

    def ChangeDirection(self, key):
        'Changes direction the snake is moving'
        keys = {
            'a':'left',
            'w':'up',
            'd':'right',
            's':'down'
        }
        if key in keys:
            self.direction = keys[key]

game = Game()