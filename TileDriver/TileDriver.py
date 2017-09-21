from random import randint

def main():
	width = int(input("Enter Grid Width: "))
	shuffleTiles(width)

def shuffleTiles(width):
	grid = createPossibleGrid(width)
	#check if the grid is valid
	printGrid(grid)
	return grid

def createPossibleGrid(width):
	grid = [[0 for j in range(width)] for i in range(width)]
	vals = list(range(0, (width * width)))

	for i in range(0, width):
		for j in range(0, width):
			randInt = randint(0, len(vals) - 1)
			val = vals[randInt]
			del vals[randInt]
			grid[i][j] = val
	return grid

def printGrid(grid):
	for list in grid:
		for number in list:
			print(number, ",", end="")
		print("\n")

if __name__ == '__main__':
    main()