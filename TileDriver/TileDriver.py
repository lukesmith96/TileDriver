from random import randint

#
# Dir [0:UP 1:DOWN 2:LEFT 3:RIGHT]
# 
#

def main():
   width = int(input("Enter Grid Width: "))
   shuffleTiles(width)

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
   #check if the grid is valid
   isValidMove(grid, empx, empy, dir)
   dist = getManhattanDist(grid)
   printGrid(grid)
   return grid

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
   if ((dir == 0 and grid[x - 1, y] is not None) 
    or (dir == 1 and grid[x + 1, y] is not None) 
    or (dir == 2 and grid[x, y - 1] is not None) 
    or (dir == 3 and grid[x, y + 1] is not None)):
      return True
   return False

def printGrid(grid):
   for list in grid:
      for number in list:
         print(number, ",", end="")
      print("\n")

if __name__ == '__main__':
   main()