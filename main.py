import os
import math

###################
# CLASSES SECTION #
###################

class Field(object):
    """Game field class"""
    def __init__(self, map_array):
        self._map = []
        for (y, row) in enumerate(map_array):
            parsed_row = []
            parsed_row = [Cell(x = x, y = y, value = row[x]) for x in range(len(row))]
            self._map.append(parsed_row)

    def get_neighbour(self, position, direction):
        if position.__class__ == Cell:
            position = (position.x, position.y)
        x = y = 0
        if direction == UP:
            y = -1
        elif direction == RIGHT:
            x = 1
        elif direction == DOWN:
            y = 1
        elif direction == LEFT:
            x = -1
        return (self.get_cell((position[0]+x, position[1]+y)))

    def get_cell(self, coords):
        """Returns cell from it's coordinates"""
        x, y = coords
        return self._map[y][x] #y goes before x because while parsing map
                              #rows are processed before columns


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