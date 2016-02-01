import os
import math

###################
# CLASSES SECTION #
###################

class Field(object):
    """Game field class"""
    def __init__(self, map_array):
        self.map = []
        for (y, row) in enumerate(map_array):
            parsed_row = []
            parsed_row = [Cell(x = x, y = y, value = row[x]) for x in range(len(row))]
            self.map.append(parsed_row)

    def get_neighbour(self, position, direction):
        if position.__class__ == Cell:
            position = (position.x, position.y)
        x = y = 0
        if direction == UP:
            y = 1
        elif direction == RIGHT:
            x = 1
        elif direction == DOWN:
            y = -1
        elif direction == LEFT:
            x = -1
        return (self.map[position[0]+x][position[1]+y])

    def get_cell(self, coords):
        """Returns cell from it's coordinates"""
        x, y = coords
        return self.map[y][x] #y goes before x because while parsing map
                              #rows are processed before columns

    def set_cell_value(self, coords, val):
        """Sets new value to specified cell"""
        if coords.__class__ == Cell:
            coords.value = val
        else:
            x, y = coords
            self.map[y][x].value = val


class Cell(object):
    """Cell of field class"""
    def __init__(self, **kwargs):
        """Sets main attributes of a cell"""
        self.x, self.y, self._value = kwargs["x"], kwargs["y"], kwargs["value"]

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        """Set new value to cell"""
        self._value = val

    def distance(self, to):
        """Distance from cell to target"""
        if to.__class__ == Cell:
            x, y = to.x, to.y
        else:
            x, y = to

        return math.sqrt((self.x - float(x))**2 + (self.y - float(y))**2)

class Snake(object):
    """Snake class"""
    def __init__(self, field, **kwargs):
        self.field = field
        self.segments = [self.field.get_cell((5,5))]
        self.field.set_cell_value(self.head, C_SNAKE)
        self.direction = UP

    @property
    def head(self):
        return self.segments[0]

    def find_path(self, target, current):
        current.value = C_SEARCHED

        directions = [UP, RIGHT, DOWN, LEFT]
        n = tuple(map(lambda x: self.field.get_neighbour(current, x), directions)) #gettin' all neighbours

        if target in n:
            return (True)

        n = filter(lambda x: x.value == C_VOID, n) #filtering obstacles
        if n == ():
            return (False)
        
        n_dirs = tuple(map(current.distance, n)) #calculating distance from target
        
        return directions[n_dirs.index(min(n_dirs))] #returning direction in which distance would be closest

#####################
# CONSTANTS SECTION #
#####################

C_SNAKE    = 's'
C_FOOD     = 'f'
C_VOID     = '0'
C_BORDER   = '#'
C_SEARCHED = '@'

UP    = 'u'
RIGHT = 'r'
DOWN  = 'd'
LEFT  = 'l'

#################
# START SECTION #
#################

if __name__ == "__main__":
    directory = os.path.dirname(os.path.abspath(__file__))
    f = open(directory+"/map.txt", 'r').read().splitlines()
    field = Field(f)
    snake = Snake(field)
    print snake.find_path(field.get_cell((5, 3)), snake.head)