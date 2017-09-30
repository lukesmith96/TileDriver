from random import randint

#
# Dir [0:UP 1:DOWN 2:LEFT 3:RIGHT]
# @author: Luke Smith
#

# State class holds an instance of the game
# with a specific tile state, this is used when
# trying to discover the most efficient path
class State:
   # @param
   # tiles : matrix of integers representing the board
   # path : String holding all previous moves
   # x,y : integers holding the position of the empty slot (0) on the board
   def __init__(self, tiles, path, x, y):
      self.tiles = tiles
      self.path = path
      self.distance = getManhattanDist(tiles)
      self.cost = len(path) + self.distance
      self.x = x
      self.y = y

def main():
   width = int(input("Width: "))

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
      command = input("Move [H|J|K|L] | [S]olve | [Q]uit: ")
      choices = "kjhl"
      if (command == 's' or command == 'S'):
         start = State(grid, "", x, y)
         final = solve_puzzle(start)
         print("Solution: ", final.path)
      elif command == 'q' or command == 'Q':
         break;
      else:
         try:
            move = choices.index(command.lower())
         except (ValueError):
            print("Invalid Move")
            continue
         if isValidMove(grid, x, y, move):
            newGrid = makeMove(grid, x, y, move)
            grid = newGrid[0]
            x = newGrid[1]
            y = newGrid[2]
         else:
            print("Invalid Move")
         printGrid(grid)
         if (eq(grid, complete)):
            print("Puzzle Complete!")
            break;

# Discovers the most efficient move path
# given a inputted start state. Using an A* algorithm
def solve_puzzle(startState):
   visited = []
   toVisit = createNewStates(startState)
   final = None
   while (final is None):
      minCost = toVisit[0]
      index = 0
      for i in range(len(toVisit)):
         if (toVisit[i].cost < minCost.cost and not isExplored(visited, toVisit[i])):
            minCost = toVisit[i]
            index = i
      # visit min cost option
      del toVisit[index]
      toVisit = toVisit + createNewStates(minCost)
      visited.append(minCost)
      if (minCost.distance == 0):
         final = minCost
   return final

# checks if this state is contained in the explored list
# if so don't add it because we know it won't be as efficient
def isExplored(list, comp):
   for state in list:
      if(eq(state.tiles, comp.tiles)):
         return True
   return False

# Iterates through all possible moves available in a state
# and returns a list of new states with those move made.
def createNewStates(state):
   list = []
   choices = "KJHL"
   for char in choices:
      index = choices.index(char)
      if (not isOpposingMove(state.path[-1:], char) 
          and isValidMove(state.tiles, state.x, state.y, index)):
          move = makeMove(copy(state.tiles), state.x, state.y, index)
          temp = State(move[0], state.path + char, move[1], move[2])
          list.append(temp)
   return list

# No reason to add the opposing move to what was
# just made to our list of possible states. Creates
# a infinite loop, this method returns if the move is
# opposing. Ie. prev = left  and next = right return to same state
def isOpposingMove(prev, next):
   if (prev == ""):
      return False
   if (prev == "H" and next == "L") or (prev == "L" and next == "H"):
      return True
   if (prev == "J" and next == "K") or (prev == "K" and next == "J"):
      return True
   return False;

# Check if two board params are equal to eachother
def eq(grid, comp):
   for i in range(0, len(grid)):
      for j in range(0, len(grid)):
         if grid[i][j] != comp[i][j]:
            return False
   return True

# Shuffles the tiles by starting with a 
# finished grid this gaurentees the solvability
# of the problem
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

# Makes a move on the tiles
# return the new tile positions.
# Keeps track of the empty tile position to make this
# method and isValidMove efficency of O(1)
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

# Returns the Manhattan Distance of the grid
# Used to gaurentee the difficulty of a grid in
# shuffling and in cost analysis.
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

# Preforms deep copy on the tiles in order to
# diferentiate states
def copy(grid):
   width = len(grid)
   newGrid = [[0 for j in range(width)] for i in range(width)]
   for i in range(0, width):
      for j in range(0, width):
         newGrid[i][j] = grid[i][j]
   return newGrid

# Checks if the proposed move is valid. 
# See makeMove() for more details.
def isValidMove(grid, x, y, dir):
   if ((dir == 0 and onGrid(grid, x + 1, y)) 
    or (dir == 1 and onGrid(grid, x - 1, y)) 
    or (dir == 2 and onGrid(grid, x, y + 1)) 
    or (dir == 3 and onGrid(grid, x, y - 1))):
      return True
   return False

# Checks to see if the coordinates exist on the grid
def onGrid(grid, x, y):
   try:
      if x < 0 or y < 0:
         raise IndexError
      grid[x][y]
   except (IndexError, ValueError):
      return False
   return True

# Prints the grid in param
def printGrid(grid):
   for list in grid:
      for number in list:
         if number == 0:
            print("      ", end="")
            continue
         print("[", number, "] ", end="")
      print("\n")

if __name__ == '__main__':
   main()