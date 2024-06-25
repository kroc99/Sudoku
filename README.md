# Sudoku

# Sudoku Generator

SUDOKU!!

## How to Use

1. Import the `generate_sudoku` function from the `sudoku_generator` module:

```
from sudoku_generator import generate_sudoku
```

2. Generate a Sudoku puzzle by calling the `generate_sudoku` function with two arguments:

   - `size`: The size of the puzzle, which should be 9 for a standard 9x9 Sudoku.
   - `removed`: The number of cells to be removed from the filled Sudoku puzzle to create a playable Sudoku. The higher the `removed` value, the more challenging the puzzle will be.

```
size = 9
removed = 40   # For example, remove 40 cells to create a challenging puzzle
board = generate_sudoku(size, removed)
```


