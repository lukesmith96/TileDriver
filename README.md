# TileDriver

## Purpose

To create the Tile Puzzle game and implement A* pathfinding algorithm to automatically solve instances of the game.

## Game and Implementation

Sliding Tile Puzzles (or N-Puzzles) are games that require one to move tiles around
a grid until the tiles are in a particular order. Since the tiles cannot be lifted, their movement is
made possible by having one tile missing from the grid. Each move thus involves moving a tile
adjacent to this empty space.

Due to the complexity of the solution to this problem as the value of N, the width of the puzzle, 
grows the problems gets harder exponentially due to this, the tile puzzle is classified as NP-hard, which
means it is at least as difficult as other known computation problems that cannot be solved in
polynomial (nx) time; even worse, such a "solution" may not complete in finite time.

The algorithm begins by finding all fringe puzzle states available from the initial state. On each
iteration of a loop, the fringe state with the lowest cost is explored, which requires generating all
possible new puzzle states from it. Once these new states are created, the state that created
them is removed from the list of fringe states and saved to a list of explored states; doing so
ensures that it is not explored again. This process of exploring lowest-cost states and
generating new states continues until the lowest-cost state has a Manhattan distance of 0,
indicating that it is the final state and an optimal path has been found.

## Playing:

For movement, we will use the same navigation keys as in Vim, specifically:
Left: H, Down: J, Up: K, Right: L

Finding the quickest path to solving the puzzle is found using the key command: S

Quit the game with: Q
