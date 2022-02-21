from classes import FourInARow, TicTacToe, Hangman
from time import sleep
import pygame
import sys
import openpyxl

INST_FOURINAROW = pygame.image.load(r'photos\FourInARow\fourinarow_instructions.png')
INST_TICTACTOE = pygame.image.load(r'photos\FourInARow\fourinarow_instructions.png')
INST_HANGMAN = pygame.image.load(r'photos\FourInARow\fourinarow_instructions.png')


def playTheGame(screen, game_name):
    """
    controls the games
    :param screen: the screen of the pygame app
    :param game_name: the name of the game
    :return: None
    """
    # present instructions
    if game_name == 'Four In a Row':
        screen.blit(INST_FOURINAROW, (0, 0))
        game = FourInARow(screen)
    elif game_name == 'Tic Tac Toe':
        screen.blit(INST_TICTACTOE, (0, 0))
        game = TicTacToe(screen)
    else:
        screen.blit(INST_HANGMAN, (0, 0))
        game = Hangman(screen)

    # wait for user to finish read the instructions
    pygame.display.update()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True

    # start game
    screen.fill((0, 0, 0))
    # game.chooseAmountRounds() - play 5 rounds
    game.playGame()
    game.presentRecordTable()
    return


def main():
    # init pygame
    pygame.init()

    # start
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("Game Hall")
    icon = pygame.image.load(r'photos\General\board-game.png')
    pygame.display.set_icon(icon)

    screen.blit(icon, (60, 80))
    pygame.display.update()
    sleep(1.25)

    # set screen, tile and icon
    start_screen = pygame.image.load(r'photos\General\start_screen.png')
    screen.blit(start_screen, (0, 0))
    pygame.display.update()

    # play background music
    pygame.mixer.Sound(r'music\bg_music.mp3').play(-1)

    # create execl(s) for lead boards
    # create the lead board
    game_names = ["FourInARow", "TicTacToe", "Hangman"]
    for name in game_names:
        try:  # check if exists
            openpyxl.load_workbook(r'extras\{0}\lead_board.xlsx'.format(name))
        except FileNotFoundError:  # if not exists
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            sheet['A1'].value = "Names"
            sheet['B1'].value = "Points"
            sheet['C1'].value = "Time(s)"
            workbook.save(r'extras\{0}\lead_board.xlsx'.format(name))

    # start the app
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # leave
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:  # user pressed mouse
                x_pos, y_pos = pygame.mouse.get_pos()
                if 84 < x_pos < 616:  # choose a game
                    if 279 < y_pos < 387:  # four in a row
                        print("Four In a Row")
                        playTheGame(screen, 'Four In a Row')
                        screen.blit(start_screen, (0, 0))
                        pygame.display.update()

                    elif 386 < y_pos < 499:  # tic tac toe
                        print("Tic Tac Toe")
                        playTheGame(screen, 'Tic Tac Toe')
                        screen.blit(start_screen, (0, 0))
                        pygame.display.update()

                    elif 498 < y_pos < 619:  # hangman
                        print("Hangman")
                        playTheGame(screen, 'Hangman')
                        screen.blit(start_screen, (0, 0))
                        pygame.display.update()

                    else:  # pressed out of range
                        print("Out of range")
                else:  # pressed out of range
                    print("Out of range")


if __name__ == '__main__':
    main()
