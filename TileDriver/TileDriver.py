from random import randint

#
# Dir [0:UP 1:DOWN 2:LEFT 3:RIGHT]
# 
#
class State:
   distance = 0
   cost = path + distance
   def __init__(self, tiles, path):
      self.tiles = tiles
      self.path = path
      self.distance = getManhattanDist(tiles)
      self.cost = len(path) + self.distance
   def __eq__(self, other):
      finished(self, other)
   def __repr__(self):
      print(self)


def main():
   width = int(input("Enter Grid Width: "))

   complete = [[0 for j in range(width)] for i in range(width)]
   shuffledTiles = shuffleTiles(width)
   grid = shuffledTiles[0]
   x = shuffledTiles[1]
   y = shuffledTiles[2]

   index = 0
   for i in range(0, width):
      for j in range(0, width):
         complete[i][j] = index
         index += 1

   while True:
      command = input("Next Move: ")
      if (command == 'q' or command == 'Q'):
         break;
      choices = "kjhl"
      try:
         move = choices.index(command.lower())
      except (ValueError):
         print("Incorrect Selection")
         continue
      if isValidMove(grid, x, y, move):
         newGrid = makeMove(grid, x, y, move)
         grid = newGrid[0]
         x = newGrid[1]
         y = newGrid[2]
      printGrid(grid)
      if (finished(grid, complete)):
         print("You Won!")
         break;

def eq(grid, comp):
   for i in range(0, len(grid)):
      for j in range(0, len(grid)):
         if grid[i][j] != comp[i][j]:
            return False
   return True

def shuffleTiles(width):
   grid = [[0 for j in range(width)] for i in range(width)]
   empx = 0
   empy = 0
   
   index = 0
   for i in range(0, width):
      for j in range(0, width):
         grid[i][j] = index
         index += 1

   while(getManhattanDist(grid) < (width * width)):
      dir = randint(0,3)
      if isValidMove(grid, empx, empy, dir):
         move = makeMove(grid, empx, empy, dir)
         grid = move[0]
         empx = move[1]
         empy = move[2]

   #check if the grid is valid
   printGrid(grid)
   return (grid, empx, empy)

def makeMove(grid, x, y, dir):
   adjX = 0
   adjY = 0
   if dir == 0:
      adjX = 1
   if dir == 1:
      adjX = -1
   if dir == 2:
      adjY = 1
   if dir == 3:
      adjY = -1
   grid[x][y] = grid[x + adjX][y + adjY]
   grid[x + adjX][y + adjY] = 0
   return (grid, x + adjX, y + adjY)

def getManhattanDist(grid):
   width = len(grid)
   dist = 0;
   for i in range(0, len(grid)):
      for j in range(0, len(grid)):
         var = grid[i][j]
         if var == 0: 
            continue
         finX = var % width
         finY = int(var/width)
         dist += abs(i - finY) + abs(j - finX)
   return dist

def copy(grid):
   return grid

def isValidMove(grid, x, y, dir):
   if ((dir == 0 and onGrid(grid, x + 1, y)) 
    or (dir == 1 and onGrid(grid, x - 1, y)) 
    or (dir == 2 and onGrid(grid, x, y + 1)) 
    or (dir == 3 and onGrid(grid, x, y - 1))):
      return True
   return False

def onGrid(grid, x, y):
   try:
      if x < 0 or y < 0:
         raise IndexError
      grid[x][y]
   except (IndexError, ValueError):
      return False
   return True

def printGrid(grid):
   for list in grid:
      for number in list:
         print(number, ",", end="")
      print("\n")

if __name__ == '__main__':
   main()