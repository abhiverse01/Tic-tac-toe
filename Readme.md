Tic-Tac-Toe Game
This is a simple implementation of the Tic-Tac-Toe game using the tkinter library in Python. The game provides a graphical user interface where two players can take turns marking X and O symbols on a 3x3 grid. The objective of the game is to get three of your own symbols (X or O) in a row, column, or diagonal.

How to Play
Run the program.
The game window will appear, displaying the title "Tic-Tac-Toe" and two buttons: "Play" and game statistics.
Click the "Play" button to start a new game.
The game board will appear with a 3x3 grid of empty buttons.
Player X starts the game.
Each player takes turns clicking on an empty cell to mark their symbol (X or O).
The game will automatically determine if a player wins or if it's a draw.
A message box will appear to indicate the game result (draw or player X/O wins).
Click "OK" on the message box to close it.
The game statistics will update with the number of wins for player X and player O.
To play again, click the "Play" button.
Customization
The color of the X and O symbols can be changed by modifying the fg (foreground) parameter of the tk.Button objects. In this code, the color is set to white (fg="white").
The game window size can be adjusted by modifying the self.window.geometry() line in the constructor (__init__) of the TicTacToe class.
Development Information
This game was developed by Abhishek Shah in 2023.
The developer's name and year are displayed in the footer of the game window.
Enjoy playing Tic-Tac-Toe!