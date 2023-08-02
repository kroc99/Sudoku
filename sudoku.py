# from sudoku_generator import *

import pygame
import sys

import sudoku_generator
from button import Button
from board import Board
pygame.init()

SCREEN = pygame.display.set_mode((800, 950))
pygame.display.set_caption("Menu")
sudoku = None
grid = [[0 for i in range(9)] for j in range(9)]

BG = pygame.image.load("assets/sudoku/background.jpeg")


def get_font(size):
    return pygame.font.Font("assets/sudoku/REFUSETR.TTF", size)


def game_win():

    SCREEN.fill("White")

    SCREEN.blit(BG, (0, 0))

    win_mouse_position = pygame.mouse.get_pos()
    win_text = get_font(150).render("GAME WON", True, "#003366")
    win_rect = win_text.get_rect(center=(400, 300))

    win_exit_button = Button(image=pygame.image.load("assets/sudoku/Play Rect.png"), pos=(400, 500),
                         text_input="EXIT", font=get_font(90), base_color="#003366", hovering_color="White")

    SCREEN.blit(win_text, win_rect)

    win_exit_button.change_color(win_mouse_position)
    win_exit_button.update(SCREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if win_exit_button.check_for_input(win_mouse_position):
                pygame.quit()
                sys.exit()


def game_over():

    SCREEN.fill("White")

    SCREEN.blit(BG, (0, 0))

    lose_mouse_position = pygame.mouse.get_pos()
    lose_text = get_font(145).render("GAME OVER", True, "#003366")
    lose_rect = lose_text.get_rect(center=(400, 300))

    lose_restart_button = Button(image=pygame.image.load("assets/sudoku/Play Rect.png"), pos=(400, 500),
                         text_input="RESTART", font=get_font(90), base_color="#003366", hovering_color="White")

    SCREEN.blit(lose_text, lose_rect)

    lose_restart_button.change_color(lose_mouse_position)
    lose_restart_button.update(SCREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if lose_restart_button.check_for_input(lose_mouse_position):
                main_menu()


def play(difficulty):

    SCREEN.fill("White")

    # FIXME: changes the gameplay according to difficulty
    if difficulty == 'easy':
        sudoku = sudoku_generator.SudokuGenerator(9, 30)
        sudoku.fill_values()
        completed_grid = sudoku.get_board()
        game_grid = sudoku_generator.generate_sudoku(9, 30)

    elif difficulty == 'medium':
        sudoku = sudoku_generator.SudokuGenerator(9, 40)
        sudoku.fill_values()
        completed_grid = sudoku.get_board()
        game_grid = sudoku_generator.generate_sudoku(9, 30)

    elif difficulty == 'hard':
        sudoku = sudoku_generator.SudokuGenerator(9, 50)
        sudoku.fill_values()
        completed_grid = sudoku.get_board()
        game_grid = sudoku_generator.generate_sudoku(9, 30)

    game_board = Board(width=800, height=800, screen=SCREEN, grid=game_grid, difficulty=difficulty)
    game_board.draw()

    game_winner = False
    game_loser = False

    while True:

        play_mouse_position = pygame.mouse.get_pos()

        play_restart = Button(image=None, pos=(410, 850),
                              text_input="RESTART", font=get_font(50), base_color="Black", hovering_color="Green")

        play_reset = Button(image=None, pos=(105, 850),
                            text_input="RESET", font=get_font(50), base_color="Black", hovering_color="Green")

        play_exit = Button(image=None, pos=(705, 850),
                           text_input="EXIT", font=get_font(50), base_color="Black", hovering_color="Green")

        for button in [play_restart, play_reset, play_exit]:
            button.change_color(play_mouse_position)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # checks events for buttons
                if play_exit.check_for_input(play_mouse_position):
                    pygame.quit()
                    sys.exit()
                if play_reset.check_for_input(play_mouse_position):
                    game_board.clear()
                if play_restart.check_for_input(play_mouse_position):
                    main_menu()
                # checks if a cell is clicked
                game_board.click(play_mouse_position)
            if event.type == pygame.KEYDOWN:
                print(event.key - 48)
                game_board.place_number(event.key)

        if game_winner:
            game_win()

        if game_loser:
            game_over()

        pygame.display.update()


def main_menu():

    while True:

        SCREEN.blit(BG, (0, 0))

        menu_mouse_position = pygame.mouse.get_pos()

        menu_text = get_font(225).render("SUDOKU", True, "#003366")
        menu_rect = menu_text.get_rect(center=(410, 200))

        easy_button = Button(image=pygame.image.load("assets/sudoku/Play Rect.png"), pos=(400, 430),
                             text_input="EASY", font=get_font(90), base_color="#003366", hovering_color="White")
        medium_button = Button(image=pygame.image.load("assets/sudoku/Play Rect.png"), pos=(400, 580),
                               text_input="MEDIUM", font=get_font(90), base_color="#003366", hovering_color="White")
        hard_button = Button(image=pygame.image.load("assets/sudoku/Play Rect.png"), pos=(400, 730),
                             text_input="HARD", font=get_font(90), base_color="#003366", hovering_color="White")

        SCREEN.blit(menu_text, menu_rect)

        for button in [easy_button, medium_button, hard_button]:
            button.change_color(menu_mouse_position)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.check_for_input(menu_mouse_position):
                    play('easy')
                if medium_button.check_for_input(menu_mouse_position):
                    play('medium')
                if hard_button.check_for_input(menu_mouse_position):
                    play('hard')

        pygame.display.update()


def main():
    main_menu()


if __name__ == '__main__':
    main()
