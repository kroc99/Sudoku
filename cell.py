import pygame
import sys


class Cell:
    def __init__(self, value, row, col, screen, grid):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.cell = []
        self.grid = grid
        self.click = False
        self.highlighted_cell = None
        self.highlight_count = 0

    def set_cell_value(self, value):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.K_BACKSPACE:
                pass

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(80):
                    if self.cell[i].collidepoint(event.pos):
                        row_pressed = i // 9
                        col_pressed = i % 9
                        self.grid[row_pressed][col_pressed] = 1

    def set_sketched_value(self, value):
        pass

    def draw(self):

        if not self.click or self.highlight_count >= 1:
            for i in range(0, 81):
                row = i // 9
                col = i % 9
                self.cell.append(pygame.draw.rect(self.screen, "White",
                                                  pygame.Rect(42 + (col * 80), 47 + (row * 80), 78, 78)))
                self.highlight_count = 0
        if self.highlight_count <= 1 and self.click:
            self.cell[self.highlighted_cell] = \
                pygame.draw.rect(self.screen, "#ADD8E6", pygame.Rect(42 + (self.col * 80), 47 + (self.row * 80), 78, 78))

    def highlight(self, position):
        self.highlight_count += 1
        for i in range(80):
            self.col = i % 9
            self.row = i // 9
            if self.cell[i].collidepoint(position):
                self.click = True
                self.highlighted_cell = i
                return self.highlighted_cell

    def place_num(self, value):
        pass
