import enum


class Status(enum.Enum):
    """
    Enum representing the Status of a position on a goban
    """
    WHITE = 1
    BLACK = 2
    EMPTY = 3
    OUT = 4


class Goban(object):
    def __init__(self, goban):
        self.goban = goban

    def get_status(self, x, y):
        """
        Get the status of a given position
        Args:
            x: the x coordinate
            y: the y coordinate
        Returns:
            a Status
        """
        if not self.goban or x < 0 or y < 0 or y >= len(self.goban) or x >= len(self.goban[0]):
            return Status.OUT
        elif self.goban[y][x] == '.':
            return Status.EMPTY
        elif self.goban[y][x] == 'o':
            return Status.WHITE
        elif self.goban[y][x] == '#':
            return Status.BLACK

    def is_taken(self, x, y):
        neighbours = [(x,y)]
        visited = []
        this_status = self.get_status(x,y)
        while (neighbours):
            cell = neighbours.pop() # берем последний
            #print("x:" + str(cell[0]) +" y:"+str(cell[1]))
            if(cell in visited):
                #print("visited works")
                continue
            else:
                visited.append((cell[0], cell[1]))
            #print("after if")
            if (self.get_status(cell[0], cell[1]) == Status.EMPTY):
                return False
            if(self.get_status(cell[0], cell[1]) != this_status):
                
                continue

            neighbours.append((cell[0],cell[1]-1))
            neighbours.append((cell[0],cell[1]+1))
            neighbours.append((cell[0]+1,cell[1]))
            neighbours.append((cell[0]-1,cell[1]))

        return True

    def get_len(self):
        print(len(self.goban[1]))



