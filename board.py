import pygame

import cell
from cell import Cell

BLACK = (0, 0, 0)


class Board:
    def __init__(self, width, height, screen, grid, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.num_font = pygame.font.SysFont('Ariel', 115)
        self.grid = grid
        self.board_cells = Cell(value=None, row=None, col=None, screen=self.screen, grid=self.grid)
        self.cell_index = None
        self.position = None

    def draw(self):

        self.board_cells.draw()

        for i in range(0, 10):
            # makes bold lines every box
            if i % 3 == 0:
                pygame.draw.line(self.screen, (0, 0, 0), (40 + (80 * i), 45), (40 + (80 * i), 765), 4)
                pygame.draw.line(self.screen, (0, 0, 0), (40, 45 + (80 * i)), (760, 45 + (80 * i)), 4)
            # draws the grid
            pygame.draw.line(self.screen, (0, 0, 0), (40 + (80 * i), 45), (40 + (80 * i), 765), 2)
            pygame.draw.line(self.screen, (0, 0, 0), (40, 45 + (80 * i)), (760, 45 + (80 * i)), 2)
        pygame.display.update()

        for i in range(0, len(self.grid[0])):
            for j in range(0, len(self.grid[0])):
                if 0 < self.grid[i][j] < 10:
                    value = self.num_font.render(str(self.grid[i][j]), True, "#003366")
                    self.screen.blit(value, ((80*(j+1) - 25), (i+1)*80 - 30))

    def value(self, row, col):
        pass

    def click(self, position):
        self.position = position
        self.cell_index = self.board_cells.highlight(self.position)
        self.board_cells.draw()
        self.draw()

    def clear(self):
        self.board_cells = Cell(value=None, row=None, col=None, screen=self.screen, grid=self.grid)
        self.draw()

    def sketch(self, value):
        pass

    def reset_to_original(self):
        pass

    def place_number(self, user_input):
        x = self.position[0]
        y = self.position[1]
        row = self.cell_index // 9
        col = self.cell_index % 9
        if self.grid[row][col] != 0:
            pass
        if 0 < (user_input - 48) < 10:
            # get rid of old user_input
            value = self.num_font.render(str(user_input - 48), True, "#003366")
            self.screen.blit(value, (x, y + 5))

    def update_board(self):
        pass

    def find_empty(self):
        pass

    def check_board(self):
        pass
