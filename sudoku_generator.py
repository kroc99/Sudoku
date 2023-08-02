import random

class SudokuGenerator:

    def __init__(self, row_length, removed_cells):   ##Constructs Sudoku Generator
        self.box_length = 3
        self.col_length = row_length
        self.row_length = row_length
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for i in range(row_length)]for j in range(row_length)]
        ##Always 9x9

    def get_board(self):
        return(self.board)

    def print_board(self):
        for row in self.board:
            print(row)



    def valid_in_row(self, row, num):
        for i in range(self.row_length):             ##repeats for just one row
            if self.board[row][i] == num:             ##checks if row is equal to num
                return False
        return True

    def valid_in_col(self, col, num):                ##Does same as above just for col
        for i in range(self.col_length):
            if self.board[i][col] == num:
                return False
        return True

                                                     ##Valid_in_col and Valid_in_row are used later for fill box, not valid_in_box

    def valid_in_box(self, row_start, col_start, num):
        i = 0
        c = 0
        while i < 9:
            i += 1
            if self.board[(row_start)+(c//3)][col_start+(c%3)] == num:    ##should scan each colum moving down by n row
                return False                                             ##returns False if num == to the board,
            c += 1
        return True                                                      ##returns True when all boxes are checked

    def is_valid(self, row, col, num):
        if self.valid_in_row(row, num) and self.valid_in_col(col, num):  ##uses both valid_in_row and valid_in_col,
            return True
        else:
            return False
                                                                         ##USED FOR FILL REMAINING ONLY

    def fill_box(self, row_start, col_start):
        i = 9
        a = 0

        while i > 0:
            var = random.randint(0, 9)
            if self.valid_in_box(row_start,col_start,var):
                self.board[row_start + a%3][col_start + (a//3)] = var
                i -= 1                                                   ##subtracts down from 9
                a += 1                                                   ##adds from 1, should scan first 3 in row then move down a col
            else:
                pass

    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3, 3)                                               ##should always be these for 9x9
        self.fill_box(6, 6)

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        i = 0
        while i < self.removed_cells:
            rng = random.randint(0, 8)
            rng1 = random.randint(0, 8)
            if self.board[rng][rng1] != 0:
                self.board[rng][rng1] = 0
                i += 1
            else:
                pass

                                                ##this should give a random list to be removed, not sure how use with cells


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board

                                        ## board should be 9x9 Array
