# GameHall
Program for the classic games we all know - Four in a row, Tic Tac Toe, and Hangman.
The program is written in python and uses Pygame for GUI and Python 3.7.  
Each game has five rounds. At the end of each round, the program presents the round statistics, such as the percentage of winning, etc. And at the end of the game (of the five rounds), the program presents the game statistics.  
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
