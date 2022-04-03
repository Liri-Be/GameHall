# GameHall
Program for the classic games we all know - Four in a row, Tic Tac Toe, and Hangman.  
The program is written in python and uses Pygame for GUI and Python 3.7.  
Each game has five rounds. At the end of each round, the program presents the round statistics, such as the percentage of winning, etc., and at the end of the game (of the five rounds), the program presents the game statistics.  
Also, the user may choose to enter the lead board and see the other users in the lead board who were in the top five.  
The user plays against the computer in Four in a row and Tic Tac Toe.  
Each game starts with instructions of the game.

## How to run?
There are a few steps -
1. Install the required libraries using pip - 
    ```
    pip install pygame
    pip install pandas
    pip install openpyxl
    ```
2. Clone into the project using git bush with this commend -  
    ```
    git clone https://github.com/Liri-Be/GameHall.git
    ```  
3. Open the command line in the directory of the code (which you cloned the code into)
4. Run the program - 
    ```
    python main.py
    ```

## The games
### Four in a row   
Each player (in their turn) chooses a column to drop their token.  
The first player to complete four tokens in a row, column, or diagonal, win the game!  
The computer starts. The user uses the yellow token, and the computer uses the red.

### Tic Tac Toe
Each player (in their turn) chooses a place to put X or O (their symbol).
The first player to complete three symbols in a row, column, or diagonal, win the game!  
The computer starts. The user uses the O, and the computer uses the X.

### Hangman
The computer selects randomly each round a secret word. The goal of the user is to guess the secret word.  
At the start of the game, the computer draws bars for each letter in the secret word.  
The user guesses the letters of the secret word. If they are wrong, the computer will add body parts for the hangman and present the wrong guesses. After six wrong guesses, the user loses, but if the user guesses the secret word before that, they win!

## Files
### main.py
The shellcode - 
1. handles the choosing game part - the user chooses the game they want to play.
2. runs the functions of each game while the user play - 
    - starts the game
    - present and update lead board

### classes.py
Contains all the code of the games and their classes.  
Handles the game itself - the functionality and important features of each game.
#### classes
There are four classes - 
1. Game -  
    This class is the shell of each game. Has only base functions.
2. FourInARow -  
    This class handles the four in a row game.
3. TicTacToe -  
    This class handles the tic tac toe game.
4. Hangman -  
    This class handles the hangman game.

### files directory
This directory has three more directories in it (one for each game) and in each one there are two xlsx files.  
The first one includes the users and their points and the time the game took them.  
The second one is the same as the first one but sorted first by points (most points at the top) and secondly by time (shortest time at the top).

### music directory
This directory has the music files of the game.

### Photos directory
In this directory, there are four more directories -  
1. General - has photos for the program itself (not for a specific game).  
2. FourInARow, TicTacToe, and Hangman - have photos related to each game - instructions, etc.

## Attributions
1. <a href="https://www.flaticon.com/free-icons/board-game" title="board game icons">Board game icon for start screen and app icon was created by Good Ware - Flaticon</a>  
2. <a href="https://www.flaticon.com/free-icons/x" title="x icons">X icon for tic tac toe was created by Stockio - Flaticon</a>  
3. <a href="https://www.flaticon.com/free-icons/o" title="o icons">O icon for tic tac toe was created by Freepik - Flaticon</a>  
4. <a href="https://www.flaticon.com/free-icons/hangman" title="hangman icons">Wood icon for hangman was created by surang - Flaticon</a>  
5. <a href="https://www.flaticon.com/free-icons/sad" title="sad icons">Head icon for hangman was created by Freepik - Flaticon</a>
