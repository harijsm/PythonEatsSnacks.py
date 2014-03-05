import random
import time
import sys
import select

class Game:
    'Game where snake eats snacks'
    def __init__(self, height=24, width=24):
        self.score = 0
        self.speed = 1
        self.height = height
        self.width = width
        self.run = True
        self.Main()
    def CreateNewSnake(self):
        'Creates new Snake object'
        randx = random.randint(0,self.height)
        randy = random.randint(0,self.width)
        return Snake(randx, randy)
    def CreateNewFoodItem(self):
        'Creates new food item'
        self.foodx = random.randint(0,self.height)
        self.foody = random.randint(0,self.width)
        print "Creating New Food Item"
        if self.foodx == self.snake.x and self.foody == self.snake.y:
            self.CreateNewFoodItem()
    def Loop(self):
        'Loops while self.run = True.'
        thisTime = time.time()
        while self.run:
            while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                char = sys.stdin.readline().rstrip('\n')
                if char:
                    self.snake.ChangeDirection(char)
                else:
                    exit(0)

            if time.time() - thisTime > self.speed*0.7:
                self.snake.Move()
                thisTime = time.time()
                self.DrawField()
    def DrawField(self):
        board = []
        for i in range(0,self.width):
            board.append(["."] * self.height)

        board[self.foodx][self.foody] = "F"
        board[self.snake.x][self.snake.y] = "X"
        print ''
        for i in board:
            print " ".join(i)

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
        self.size = size
        self.direction = direction
    def Move(self):
        'Changes snakes x, y according to its direction'
        if self.direction == 'up':
            self.x = self.x-1
            self.y = self.y
        elif self.direction == 'down':
            self.x = self.x+1
            self.y = self.y
        elif self.direction == 'left':
            self.x = self.x
            self.y = self.y-1
        elif self.direction == 'right':
            self.x = self.x
            self.y = self.y+1
        print "x: %s; y: %s" % (self.x, self.y)
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