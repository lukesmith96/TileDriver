from random import randint

#
# Dir [0:UP 1:DOWN 2:LEFT 3:RIGHT]
# 
#

def main():
   width = int(input("Enter Grid Width: "))
   shuffleTiles(width)
   while ((var = input("")) != 'Q'):


def shuffleTiles(width):
   grid = [[0 for j in range(width)] for i in range(width)]
   vals = list(range(0, (width * width)))
   empx = 0
   empy = 0
   for i in range(0, width):
      for j in range(0, width):
         randInt = randint(0, len(vals) - 1)
         val = vals[randInt]
         if (val == 0):
            empx = i
            empy = j
         del vals[randInt]
         grid[i][j] = val
   
   while(getManhattanDist(grid) < (width * width)):
      dir = randint(0,3)
      if isValidMove(grid, empx, empy, dir):
         move = makeMove(grid, empx, empy, dir)
         grid = move[0]
         empx = move[1]
         empy = move[2]

   #check if the grid is valid
   printGrid(grid)
   return grid

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
         finX = var % width
         finY = int(var/width)
         dist += abs(i - finX) + abs(j - finY)
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