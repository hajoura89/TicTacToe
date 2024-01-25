
# Tic Tac Toe Game with AI

## Overview

This Python-based Tic Tac Toe game with AI (Artificial Intelligence) integration allows users to play against each other or challenge the computer. The game features a graphical user interface built using the Tkinter library, providing an interactive and enjoyable experience.

## Table of Contents

-   [Features](#features)
-   [Getting Started](#getting-started)
    -   [Prerequisites](#prerequisites)
    -   [Installation](#installation)
-   [How to Play](#how-to-play)
    -   [Against the Computer](#against-the-computer)
    -   [Two-Player Mode](#two-player-mode)
-   [Code Structure](#code-structure)
-   [Contributing](#contributing)
-   [License](#license)

## Features

-   Single-player mode against an AI opponent
-   Two-player mode for head-to-head matches
-   Intelligent AI using the minimax algorithm for optimal decision-making
-   User-friendly graphical interface with Tkinter

## Getting Started

### Prerequisites

-   Python 3.x
-   Tkinter library (usually included with Python installations)

### Installation

1.  Clone the repository:
    
    bashCopy code
    
    `git clone https://github.com/hajoura89/TicTacToe.git` 
    
2.  Navigate to the project directory:
    
    bashCopy code
    
    `cd TicTacToe` 
    
3.  Run the game:
    
    bashCopy code
    
    `python tictactoe.py` 
    

## How to Play

### Against the Computer

1.  Launch the game.
2.  Select the "Againt AI player" option from the main menu.
3.  Choose whether you want to play as X (first) or O (second).
4.  Enjoy the game and challenge the computer!

### Two-Player Mode

1.  Launch the game.
2.  Select the "Two players" option from the main menu.
3.  Take turns with a friend to make moves on the board.
4.  The game will automatically detect the winner or declare a draw.

## Code Structure

The code is organized into a single Python file, `tictactoe.py`, with a class-based structure. Here's a brief overview of key components:

-   **MyApp Class:** Manages the menus and game functionality.
-   **MainMenu():** Method that opens the main window of the program.
-   **checkWinner():** Determines the winner or if the game is a draw.
-   **makeMove():** Handles player moves and updates the game state.
-   **onePlayer():** Displays the menu with options for the user's game against the computer.
-   **startOnePlayerGame():** Starts the game against the computer
-   **aiMove():** Implements the AI's move using the minimax algorithm.
-   **minimax():** Algorithm for calculating the score from the perspective of the computer or the user.
-   **scorePosition():** To find the optimal move.
-   **twoPlayers():** Initiates a game between two players.
-   **createGame():** Initializes game values.
-   **clearWindow():** Announces the winner of the game in the label created earlier.
-   **announceWinner():** Clears all elements from the Tkinter window.
-   **exit():** Exit the Game.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature: `git checkout -b feature-name`.
3.  Commit your changes: `git commit -m 'Add new feature'`.
4.  Push to the branch: `git push origin feature-name`.
5.  Open a pull request.

## License

This project is licensed under the MIT License.
