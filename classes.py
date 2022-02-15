import math
import random
import sys
from time import time, sleep
import pygame


pygame.font.init()


class Game:
    def __init__(self, name, screen):
        self.name = name
        self.rounds = 0  # number of rounds for a win
        self.curr_player = 0
        self.screen = screen  # pygame screen
        self.screen_size = 700
        self.font = pygame.font.SysFont("arial bold",  50)  # font for pygame
        self.stat = {'wins': 0, 'ties': 0, 'turns': [], 'time': [], 'choosing': []}

    def playGame(self):
        """
        handles the whole game - play each round until winning the desired amount, and present statistics
        :return: None
        """
        curr_round = 0
        while self.stat['wins'] != self.rounds:
            self.drawBoard()
            sleep(1)
            start = time()
            won, turns, tie = self.playOneRound()
            self.resetAll()
            finish = time()
            curr_round += 1
            self.statistics_round(won, turns, finish-start, 0, curr_round, tie)

        self.statistics_game(curr_round)
        return

    def playOneRound(self):
        return 0, 0, 0

    def checkWin(self):
        pass

    def checkTie(self):
        pass

    def drawBoard(self):
        pass

    def resetAll(self):
        pass

    def chooseAmountRounds(self):
        """
        handles the choosing amount of rounds to declare a win
        :return: None
        """
        # present choose amount of rounds
        # present background
        rnd_screen = pygame.image.load(r'photos\rounds.png')
        self.screen.blit(rnd_screen, (0, 0))
        pygame.display.update()

        # present input text rectangle
        input_rect = pygame.Rect(200, 375, 300, 65)
        pygame.draw.rect(self.screen, (34, 177, 36), input_rect)

        # variables for input
        done_to_enter = False
        user_input = ""
        digit = True
        empty = False
        zero = False

        # get the input
        while not done_to_enter:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # if press exit - leave
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:  # if typing record the input if valid
                    error_rect = pygame.Rect(0, 470, 700, 300)
                    pygame.draw.rect(self.screen, (153, 217, 234), error_rect)
                    pygame.display.flip()

                    if event.key == pygame.K_BACKSPACE:  # backspace - delete the last one
                        user_input = user_input[:-1]
                        pygame.draw.rect(self.screen, (34, 177, 36), input_rect)
                        user_txt = self.font.render(user_input, False, (0, 0, 0), (34, 177, 36))
                        self.screen.blit(user_txt, (200, 375))
                        pygame.display.flip()

                    elif event.key == pygame.K_RETURN:  # pressed enter
                        if user_input == "":
                            empty = True
                        else:
                            done_to_enter = True

                    else:  # pressed other key
                        empty = False
                        if event.unicode.isdigit():  # if it is a digit
                            digit = True
                            if int(event.unicode) == 0 and user_input == "":  # input is zero
                                zero = True
                            else:
                                user_input += event.unicode

                                zero = False
                        else:  # not a digit
                            digit = False

            if empty:  # try to enter empty amount
                error_msg = self.font.render("Not valid, enter at least one number.",
                                             False, (255, 0, 0), (153, 217, 234))
                self.screen.blit(error_msg, (52, 475))

            elif zero and digit:  # if it is zero
                error_msg = self.font.render("Not valid, number of rounds", False, (255, 0, 0), (153, 217, 234))
                self.screen.blit(error_msg, (127, 475))
                error_msg = self.font.render("should be bigger than 0.", False, (255, 0, 0), (153, 217, 234))
                self.screen.blit(error_msg, (150, 515))

            elif not digit:  # if we got not digit
                error_msg = self.font.render("Not valid, only numbers.", False, (255, 0, 0), (153, 217, 234))
                self.screen.blit(error_msg, (150, 475))

            else:  # delete the error msg if we have valid input
                error_rect = pygame.Rect(0, 470, 700, 300)
                pygame.draw.rect(self.screen, (153, 217, 234), error_rect)

            # present the input on the screen
            user_txt = self.font.render(user_input, False, (0, 0, 0), (34, 177, 36))
            self.screen.blit(user_txt, (200, 375))
            pygame.display.flip()

        self.rounds = int(user_input)
        return

    def statistics_round(self, won, turns, round_time, choosing, curr_round, tie):
        """
        calculate and present the statistics of each round of the game
        :param won: whether the user won the round, boolean
        :param turns: number of turns this round took, int
        :param round_time: the time the round took, float
        :param choosing: the average time it took the user to choose an action, float
        :param curr_round: number of the current round, int
        :param tie: whether the round ended with a tie, boolean
        :return: the msg of the statistics, string
        """
        self.stat['time'].append(round_time)  # save time
        self.stat['turns'].append(turns)  # save turns
        self.stat['choosing'].append(choosing)
        if won:
            self.stat['wins'] += 1  # remember wins of user
        if tie:
            self.stat['ties'] += 1  # remember ties

        avg_wins = self.stat['wins'] / curr_round  # calc avg wins per round
        avg_turns = sum(self.stat['turns']) / curr_round  # calc avg turns per round

        # make msg after one round
        msg = "Here are the round statistics:\n"
        msg += "You won: " + str(self.stat['wins']) + " times\n"
        msg += "The Computer won: " + str(curr_round - self.stat['ties'] - self.stat['wins']) + " times\n"
        msg += "Amount of turns for this round: " + str(turns) + "\n"
        msg += "This round took you " + str(format(self.stat['time'][curr_round - 1], '.3f')) + " seconds\n"
        # msg += "You chose where to place the token in " + str(format(self.stat['choosing'][curr_round - 1], '.3f'))
        # msg += " seconds in average\n"
        msg += "Average amount of turns per round: " + str(format(avg_turns, '.3f')) + "\n"
        msg += "Average amount of wins per round: " + str(format(avg_wins, '.3f')) + "\n\n"

        # present statistics
        self.screen.fill((173, 216, 230))
        pygame.display.update()
        sleep(0.5)
        stat_msg = pygame.font.SysFont("arial bold", 60).render("Round ended!", False, (0, 0, 0), (173, 216, 230))
        self.screen.blit(stat_msg, (210, 20))

        if won and not tie:
            msg_win = "You won! Congratulations!"
            msg_win_color = (50, 190, 60)
            prefix = 0
        elif tie:
            msg_win = "It is a tie! Try again."
            msg_win_color = (225, 211, 12)
            prefix = 80
        else:
            msg_win = "Computer won! Try again."
            msg_win_color = (255, 37, 37)
            prefix = 10
        stat_msg = pygame.font.SysFont("arial bold", 60).render(msg_win, False, msg_win_color, (173, 216, 230))
        self.screen.blit(stat_msg, (80 + prefix, 65))

        for i in range(len(msg.split('\n')) - 1):
            stat_msg = pygame.font.SysFont("arial", 40).render(msg.split('\n')[i], False, (0, 0, 0), (173, 216, 230))
            k = 10 if i == 0 else 50
            self.screen.blit(stat_msg, (k, i*50 + 150))
        pygame.display.flip()  # display the msg

        while True:  # present until pressed mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    break
            else:
                continue
            break
        print(msg)
        return msg

    def statistics_game(self, rounds):
        """
        calculate and present the statistics of the whole game
        :param rounds: number of rounds the game took, int
        :return: the msg of the statistics, string
        """
        avg_wins = self.stat['wins'] / rounds  # calc avg wins per round
        avg_turns = sum(self.stat['turns']) / rounds  # calc avg turns per round
        avg_time = sum(self.stat['time']) / rounds  # calc avg time per round
        msg = "Here are the game statistics:\n"
        msg += "You won: " + str(self.stat['wins']) + " times\n"
        msg += "The Computer won: " + str(rounds - self.stat['wins']) + " times\n"
        msg += "Average amount of time per round: " + str(format(avg_time, '.3f')) + "s\n"
        # msg += "You choose where to place the token in " + str(format(self.stat['choosing'][rounds - 1], '.3f'))
        # msg += " seconds in average\n"
        msg += "Average amount of turns per round: " + str(format(avg_turns, '.3f')) + "\n"
        msg += "Average amount of wins per round: " + str(format(avg_wins, '.3f')) + "\n\n"

        # present statistics
        self.screen.fill((173, 216, 230))
        pygame.display.update()
        sleep(0.5)
        stat_msg = pygame.font.SysFont("arial bold", 60).render("Game ended!", False, (0, 0, 0), (173, 216, 230))
        self.screen.blit(stat_msg, (210, 20))
        for i in range(len(msg.split('\n')) - 1):
            stat_msg = pygame.font.SysFont("arial", 40).render(msg.split('\n')[i], False, (0, 0, 0), (173, 216, 230))
            k = 10 if i == 0 else 50
            self.screen.blit(stat_msg, (k, i*50 + 95))
        pygame.display.flip()  # display the msg

        while True:  # present until pressed mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    break
            else:
                continue
            break
        print(msg)
        return msg

    def __str__(self):
        return "This is base class for the games"


class FourInARow(Game):
    def __init__(self, screen):
        super().__init__("Four In a Row", screen)
        self.cols = 7
        self.rows = 6
        self.game_board = [[0 * x * y for x in range(self.cols)] for y in range(self.rows)]

    def playOneRound(self):
        turn = 0
        user_turn = False
        tie = False
        while not tie:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # if user pressed exit, leave game
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEMOTION and user_turn:  # move with the user
                    pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, self.screen_size, 100))
                    pos_x = event.pos[0]
                    pygame.draw.circle(self.screen, (255, 255, 0), (pos_x, int(100 / 2)), 45)
                pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN and user_turn:  # if pressed place the token if it's user's turn
                    pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, self.screen_size, 100))
                    pos_x = event.pos[0]
                    col = int(math.floor(pos_x / 100))
                    msg = self.findPlaceToDrop(col, 2)  # place the token
                    self.drawBoard()  # print the board

                    if "Full" not in msg:  # if succeed to place
                        turn += 1
                        win_msg = self.checkWin()
                        tie = self.checkTie()
                        if "won" in win_msg:  # check for a win
                            sleep(0.75)
                            return True if "You" in win_msg else False, turn, False
                        elif tie:
                            sleep(0.75)
                            return False, turn, True
                        user_turn = True if not user_turn else False  # switch computer <-> user

                if not user_turn:  # computer's turn
                    sleep_time = random.uniform(0.5, 2)
                    sleep(sleep_time)
                    col = random.randrange(0, 7)
                    msg = self.findPlaceToDrop(col, 1)  # place the token
                    self.drawBoard()  # print the board

                    if "Full" not in msg:  # if succeed to place
                        win_msg = self.checkWin()
                        tie = self.checkTie()
                        if "won" in win_msg:  # check for a win
                            sleep(0.75)
                            return True if "You" in win_msg else False, turn, False
                        elif tie:
                            sleep(0.75)
                            return False, turn, True
                        user_turn = True if not user_turn else False  # switch computer <-> user

        return False, turn, False

    def checkWin(self):
        """
        Check if there is a win and if so, who won - check if there are 4 same symbols in row, column or diagonal
        :return msg - whether there is a win or not:
        """
        # check for win for 4 in row
        for i in range(self.rows):
            curr_player = self.game_board[i][0]
            count_tokens = 1
            for j in range(1, self.cols):
                if curr_player == self.game_board[i][j] and curr_player != 0:  # found token that creates a row
                    count_tokens += 1
                    if count_tokens == 4:  # found 4 tokens in a row
                        msg = "Computer won!\n" if curr_player == 1 else "You won!\n"
                        return msg
                else:  # found different token that breaks the row
                    count_tokens = 1
                    curr_player = self.game_board[i][j]

        # check for win for 4 in column
        for i in range(self.cols):
            curr_player = self.game_board[0][i]
            count_tokens = 1
            for j in range(1, self.rows):
                if curr_player == self.game_board[j][i] and curr_player != 0:  # found token that creates a column
                    count_tokens += 1
                    if count_tokens == 4:  # found 4 tokens in a column
                        msg = "Computer won!\n" if curr_player == 1 else "You won!\n"
                        return msg
                else:  # found different token that breaks the column
                    count_tokens = 1
                    curr_player = self.game_board[j][i]

        # check for win for 4 in diagonal
        for i in range(self.rows):
            for j in range(self.cols):
                try:
                    if self.game_board[i][j] == self.game_board[i + 1][j + 1] == self.game_board[i + 2][j + 2] \
                            == self.game_board[i + 3][j + 3]:  # left->right
                        if self.game_board[i][j] != 0:
                            msg = "Computer won!\n" if self.game_board[i][j] == 1 else "You won!\n"
                            return msg
                except IndexError:
                    break
        for i in range(self.rows):
            for j in range(self.cols):
                try:
                    if self.game_board[i][j] == self.game_board[i - 1][j + 1] == self.game_board[i - 2][j + 2] \
                            == self.game_board[i - 3][j + 3]:  # right->left
                        if self.game_board[i][j] != 0:
                            msg = "Computer won!\n" if self.game_board[i][j] == 1 else "You won!\n"
                            return msg
                except IndexError:
                    break

        return "No win"

    def checkTie(self):
        """
        check if there is a tie - the whole board is full without a winner
        :return True/False - whether there is a tie or not:
        """
        for i in range(self.rows):
            for j in range(self.cols):
                if self.game_board[i][j] == 0:
                    return False
        return True

    def findPlaceToDrop(self, column, player):
        """
        Find the place to put the token to
        :param column: the column to drop in
        :param player: 1 or 2 - the player number
        :return msg with the place in the board or msg that says the column is full:
        """
        msg = ""
        for i in range(self.rows):
            if self.game_board[i][column] == 0:
                self.game_board[i][column] = player
                msg = str(i + 1) + ',' + str(column + 1)
                break  # quit the loop
        if msg == "":
            msg = "Full column"
        return msg

    def drawBoard(self):
        """
        draw the board
        :return: None
        """
        self.screen.fill((0, 0, 0))
        pygame.display.update()

        for c in range(self.cols):
            for r in range(self.rows):
                pygame.draw.rect(self.screen, (0, 0, 255), (c * 100, r * 100 + 100, 100, 100))
                pygame.draw.circle(self.screen, (0, 0, 0), (
                    int(c * 100 + 100 / 2), int(r * 100 + 100 + 100 / 2)), 45)

        for c in range(self.cols):
            for r in range(self.rows):
                if self.game_board[r][c] == 1:
                    pygame.draw.circle(self.screen, (255, 0, 0), (
                        int(c * 100 + 100 / 2), 700 - int(r * 100 + 100 / 2)), 45)
                elif self.game_board[r][c] == 2:
                    pygame.draw.circle(self.screen, (255, 255, 0), (
                        int(c * 100 + 100 / 2), 700 - int(r * 100 + 100 / 2)), 45)
        pygame.display.update()

        print()
        for i in range(self.rows - 1, -1, -1):
            print(self.game_board[i])
        print()
        return

    def resetAll(self):
        """
        reset the game parameters
        :return: None
        """
        self.game_board = [[0 * x * y for x in range(self.cols)] for y in range(self.rows)]
        return

    def __str__(self):
        return "This is class for " + self.name


class TicTacToe(Game):
    def __init__(self, screen):
        super().__init__("TicTacToe", screen)
        self.cols = 3
        self.rows = 3
        self.game_board = [[0 * x * y for x in range(self.cols)] for y in range(self.rows)]
        self.x_pic = pygame.image.load(r'photos\x.png')
        self.o_pic = pygame.image.load(r'photos\o.png')

    def playOneRound(self):
        turn = 0
        user_turn = False
        win = False
        tie = False
        while not win or not tie:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # if user pressed exit, leave game
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and user_turn:  # if pressed place the token if it's user's turn
                    (pos_x, pos_y) = pygame.mouse.get_pos()
                    valid = self.isValidPlace(pos_x, pos_y, 2)
                    print(pos_x, pos_y)

                    if valid:
                        self.drawBoard()  # print the board

                        # check for win/tie
                        msg_win = self.checkWin()
                        tie = self.checkTie()
                        if "won" in msg_win:
                            sleep(0.75)
                            return True if "You" in msg_win else False, turn, False
                        elif tie:
                            sleep(0.75)
                            return False, turn, True
                        user_turn = True if not user_turn else False  # switch computer <-> user

                if not user_turn:  # computer's turn
                    turn += 1
                    self.computerChoose()
                    self.drawBoard()  # print the board

                    # check for win/tie
                    msg_win = self.checkWin()
                    tie = self.checkTie()
                    if "won" in msg_win:
                        sleep(0.75)
                        return True if "You" in msg_win else False, turn, False
                    elif tie:
                        sleep(0.75)
                        return False, turn, True
                    user_turn = True if not user_turn else False  # switch computer <-> user

        return True, turn

    def checkWin(self):
        """
        check if there is a win to 'X' or 'O'
        :return: msg who won, string
        """
        players = [1, 2]
        for player in players:
            for i in range(0, 3):  # rows
                if self.game_board[0][i] == self.game_board[1][i] == self.game_board[2][i] == player:
                    return "You won!" if player == 2 else "Computer won!"
            for i in range(0, 3):  # columns
                if self.game_board[i][0] == self.game_board[i][1] == self.game_board[i][2] == player:
                    return "You won!" if player == 2 else "Computer won!"
            # diagonal
            if self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2] == player \
                    or self.game_board[0][2] == self.game_board[1][1] == self.game_board[2][0] == player:
                return "You won!" if player == 2 else "Computer won!"
        return "No win."

    def checkTie(self):
        """
        check if there is a tie
        :return: True/False - boolean
        """
        for row in self.game_board:
            for place in row:
                if place == 0:
                    return False
        return True

    def isValidPlace(self, pos_x, pos_y, token):
        """
        check if the position that chosen is empty and if so place a token there
        :param pos_x: x part of the position
        :param pos_y: y part of the position
        :param token: the token - X or O
        :return: if empty or not - bool
        """
        # get the row and the column
        if pos_y < self.screen_size / 3:
            row = 0
        elif pos_y < self.screen_size * 2 / 3:
            row = 1
        else:
            row = 2
        if pos_x < self.screen_size / 3:
            col = 0
        elif pos_x < self.screen_size * 2 / 3:
            col = 1
        else:
            col = 2

        # check if empty
        print(self.game_board[row][col])
        if self.game_board[row][col] == 0:
            self.game_board[row][col] = token
            return True
        return False

    def computerChoose(self):
        """
        choose the place for the computer X
        :return:
        """
        sleep_time = random.uniform(0.5, 2)
        sleep(sleep_time)

        start_row = random.randrange(0, 3)
        for i in range(start_row, self.rows):
            for j in range(self.cols):
                if self.game_board[i][j] == 0:  # has to happen, if not - tie should already occur
                    self.game_board[i][j] = 1
                    return

        for i in range(start_row):
            for j in range(self.cols):
                if self.game_board[i][j] == 0:  # has to happen, if not - tie should already occur
                    self.game_board[i][j] = 1
                    return

    def drawBoard(self):
        """
        draw the board
        :return: None
        """
        # draw the clean board
        self.screen.fill((255, 255, 255))

        # drawing vertical lines
        pygame.draw.line(self.screen, (0, 0, 0), (self.screen_size / 3, 0), (self.screen_size / 3, self.screen_size), 7)
        pygame.draw.line(self.screen, (0, 0, 0), (self.screen_size / 3 * 2, 0),
                         (self.screen_size / 3 * 2, self.screen_size), 7)

        # drawing horizontal lines
        pygame.draw.line(self.screen, (0, 0, 0), (0, self.screen_size / 3), (self.screen_size, self.screen_size / 3), 7)
        pygame.draw.line(self.screen, (0, 0, 0), (0, self.screen_size / 3 * 2),
                         (self.screen_size, self.screen_size / 3 * 2), 7)

        pygame.display.update()

        # draw the x and o
        for i in range(self.rows):
            for j in range(self.cols):
                if self.game_board[i][j] == 1:
                    pos = (50 + self.screen_size * j / 3, 50 + self.screen_size * i / 3)
                    self.screen.blit(self.x_pic, pos)
                elif self.game_board[i][j] == 2:
                    pos = (50 + self.screen_size * j / 3, 50 + self.screen_size * i / 3)
                    self.screen.blit(self.o_pic, pos)

        pygame.display.update()

        for row in self.game_board:
            print(row)
        return

    def resetAll(self):
        """
        reset the game board
        :return: None
        """
        self.game_board = [[0 * x * y for x in range(self.cols)] for y in range(self.rows)]

    def __str__(self):
        return "This is class for " + self.name


class Hangman(Game):
    def __init__(self, screen):
        super().__init__("Hangman", screen)
        self.list_words = ["Instagram"]
        self.secret_word = None

    def playOneRound(self):
        pass

    def checkWin(self):
        pass

    def checkTie(self):
        pass

    def __str__(self):
        return "This is class for " + self.name
