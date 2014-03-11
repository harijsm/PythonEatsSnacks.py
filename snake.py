class Snake:
    'Very hungry snake'
    def __init__(self, x=0, y=0, size=1, direction='up'):
        self.x = x
        self.y = y
        self.size = size+1
        self.direction = direction
        self.positions = []
    def Move(self, cell=1):
        'Changes snakes x, y according to its direction'
        if self.direction == 'up':
            self.x = self.x-cell
        elif self.direction == 'down':
            self.x = self.x+cell
        elif self.direction == 'left':
            self.y = self.y-cell
        elif self.direction == 'right':
            self.y = self.y+cell

        self.positions.append([self.x, self.y])
        del self.positions[len(self.positions)-self.size:len(self.positions)-self.size+1]

    def ChangeDirection(self, key):
        'Changes direction the snake is moving'
        keys = {
            'a':'left',
            'w':'up',
            'd':'right',
            's':'down',
            119: 'left',
            97: 'up',
            115: 'right',
            100: 'down'
        }
        if key in keys:
            self.direction = keys[key]