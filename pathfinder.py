import os
import math
from main import *


class Snake(object):
    """Snake class"""
    def __init__(self, field, **kwargs):
        self.field = field
        self.segments = [self.field.get_cell((5,5))]
        self.head.value = C_SNAKE
        self.direction = UP

    @property
    def head(self):
        return self.segments[0]

    def find_path(self, target, current):
        possible = {}
        directions = [UP, RIGHT, DOWN, LEFT]
        movements = []
        n = []

        while target not in n:
            current.value = C_SEARCHED
            
            n = map(lambda x: self.field.get_neighbour(current, x), directions) #gettin' all neighbours
            n = filter(lambda x: x.value in (C_VOID, C_FOOD), n) #filtering obstacles
            
            if n != ():
                for c in n:
                    possible[c] = c.distance(target) #calculating distance from target

            next_cell = min(possible, key=possible.get)
            movements.append(current.get_direction_to(next_cell))
            current = next_cell

        return movements

#################
# START SECTION #
#################

if __name__ == "__main__":
    directory = os.path.dirname(os.path.abspath(__file__))
    f = open(directory+"/map.txt", 'r').read().splitlines()
    field = Field(f)
    snake = Snake(field)
    field.get_cell((5, 3)).value = C_FOOD
    print snake.find_path(field.get_cell((5, 3)), snake.head)