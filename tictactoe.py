from customtkinter import *
import random
from PIL import Image

class MyApp(CTk):
    # The class that manages the program's menus and game functionality
    def __init__(self):
        super().__init__()
        self.geometry("500x500") # Size of the game window
        self.title("Tic Tac Toe Game") # Window title
        self.mainMenu() # Open the main menu

    def mainMenu(self):
        # Method that opens the main window of the program
        # Displays the title of the game and options for the user to play either against another user or against the computer,
        # or to exit
        
        # Clear the window 
        self.clearWindow() 
        
        # Create a new frame for the main menu
        
        frame = CTkFrame(master=self, fg_color="#4EAC7D", border_color="#FFCC70", border_width=2, width=200, height=50)
        frame.grid(row=1, column=1, sticky="nsew")

        # Add title label and buttons for game options
        label = CTkLabel(master=frame, text="Tic Tac Toe", font=("Arial Bold", 20), justify="left")
        label.pack(anchor="s", expand=True, pady=(30, 15), padx=30)

        onePlayerbtn = CTkButton(master=frame, text="Against AI Player",command=self.onePlayer)
        onePlayerbtn.pack(anchor="s", expand=True, fill="both", pady=(30, 15), padx=30)

        twoPlayersbtn = CTkButton(master=frame, text="Two Players", command=self.twoPlayers)
        twoPlayersbtn.pack(anchor="s", expand=True, fill="both", pady=(30, 15), padx=30)

        # Add an Exit button with an image
        img = Image.open("./icons/exiticon.png")    
        btn = CTkButton(master=frame, text="Exit",command=self.exit, corner_radius=32, fg_color="#4158D0", 
                hover_color="#CD8C67", border_color="#CD8C67", 
                border_width=2, image=CTkImage(dark_image=img, light_image=img))
        btn.pack(anchor="s", expand=True, fill="both", pady=(30, 15), padx=30)

        # Set fonts and styles
        self.font_large = ("Arial", 16)
        self.font_small = ("Arial", 12)
        self.label_style = {"bg": "#A64C62", "fg": "white", "font": self.font_large}
        self.win_label_initial = {"bg": "blue", "fg": "white", "font": self.font_small}
        self.win_label_final = {"bg": "#A64C62"}

        # Configure row and column weights to make the frame expand with the window
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_columnconfigure(1, weight=1)


  
    # Returns the following numbers depending on the result of the ongoing game:
    # 0 -> no winning party, so the game continues
    # 1 -> the player with the character X wins
    # 2 -> the player with the character O wins
    # 3 -> a draw

    def checkWinner(self):
        # The gamePos is a 3x3 array that takes the value 0 in a cell if there is no move in it
        # (neither X nor O). It has a value of 1 if X exists and a value of 2 if O exists.
        # Checks if there is a winner in the horizontal rows in the current game.
        for row in self.gamePos:
            if row[0] == row[1] == row[2] and row[0] != 0:
                return row[0]
        # Checks if there is a winner in the vertical columns in the current game.
        for i in range(3):
            if self.gamePos[0][i] == self.gamePos[1][i] == self.gamePos[2][i] and self.gamePos[0][i] != 0:
                return self.gamePos[0][i]
        # Checks the two diagonals for a winner.
        if self.gamePos[0][0] == self.gamePos[1][1] == self.gamePos[2][2] and self.gamePos[0][0] != 0:
            return self.gamePos[0][0]
        if self.gamePos[0][2] == self.gamePos[1][1] == self.gamePos[2][0] and self.gamePos[0][2] != 0:
            return self.gamePos[0][2]
        # Since all possibilities for a winner have been exhausted, the only possible outcomes are a draw or
        # the game continues (there is at least one cell that the player has not chosen).
        # Checks if there is at least one cell that has not been played.
        for i in range(3):
            for j in range(3):
                if self.gamePos[i][j] == 0:
                    return 0
        # There are no available cells, so the game ends in a draw.
        return 3

    # Plays the move of the player who has the turn in the cell with coordinates (posX, posY)
    def makeMove(self, posX, posY, isAI=False):
        # If the game has already finished, no move should be made
        if self.checkWinner() != 0:
            return
        if self.gamePos[posX][posY] == 0:  # Check if there is no existing move in the corresponding cell
            # Change the value of the cell in the gamePos array to 1 or 2 (X or O respectively)
            self.gamePos[posX][posY] = self.move
            if self.move == 1:
                new_text = "X"
            else:
                new_text = "O"
            # Change the text of the button corresponding to the respective cell in the game (in tkinter) to X or O
            self.buttons[posX][posY].configure(text=new_text)
            winner = self.checkWinner()
            # Check if there is a win or a draw after the respective move
            if winner == 0:  # If not, change the turn to the other player (from O to play X and vice versa)
                if self.move == 1:
                    self.move = 2
                else:
                    self.move = 1
                # If the user is playing with the computer and it was previously the user's turn, the computer plays its move
                if self.isOnePlayer and not isAI:
                    self.aiMove()
            else:  # Announce the result of the game: Winner (X or O) or a draw
                self.announceWinner(winner)

    # Displays the menu with options for the user's game against the computer, as well as the title:
    # Choose your side corresponding to Play as X (first) or Play as O (second) or Return to the main menu
    def onePlayer(self):
        self.clearWindow()
        # Create a new frame and configure its appearance
        new_frame = CTkFrame(master=self, fg_color="#4EAC7D", border_color="#FFCC70", border_width=2)
        new_frame.grid(row=1, column=1, sticky="nsew")  # Use sticky to make the frame expand in all directions

        # Add new widgets to the new frame
        label = CTkLabel(master=new_frame, text="Choose your side", font=("Arial Bold", 20), justify="left")
        label.pack(anchor="s", expand=True, pady=(30, 15), padx=30)

        checkbox_x = CTkCheckBox(master=new_frame, text="X (First)", border_color="#ffffff", fg_color="#ffffff", checkmark_color="#CD8C67")
        checkbox_x.pack(expand=True, pady=20)
        checkbox_x.bind("<Button-1>", lambda event=None: self.startOnePlayerGame(True))

        checkbox_o = CTkCheckBox(master=new_frame, text="O (Second)", border_color="#ffffff", fg_color="#ffffff", checkmark_color="#CD8C67", command=lambda: self.startOnePlayerGame(False))
        checkbox_o.pack(expand=True, pady=20)
        checkbox_o.bind("<Button-1>", lambda event=None: self.startOnePlayerGame(False))

        img = Image.open("goback.png")    
        btn = CTkButton(master=new_frame, text="Return To Main Page", command=self.mainMenu, corner_radius=32, fg_color="#4158D0", 
                        hover_color="#CD8C67", border_color="#CD8C67", 
                        border_width=2, image=CTkImage(dark_image=img, light_image=img))
        btn.pack(anchor="s", expand=True, fill="both", pady=(30, 15), padx=30)
   
        
    # Starts the game against the computer
    def startOnePlayerGame(self, playerFirst):
        self.createGame()  # Initializes game variables
        self.isOnePlayer = True
        self.playerSymbol = 1 if playerFirst else 2
        self.aiSymbol = 2 if playerFirst else 1
        # If the computer plays first, it places its first move in a random box
        if not playerFirst:
            self.aiMove(True)
 
    # Plays the computer's optimal move in the game or a random move if randomMove is True
    def aiMove(self, randomMove=False):
        if randomMove:
            # Places the move in a random cell
            self.makeMove(random.randint(0, 2), random.randint(0, 2), True)
            return

        # The algorithm tries all possible moves in the current game and eventually plays the move
        # with the highest score (Computer wins the game or ends in a draw)
        # Initializes the variables bestScore and bestMove
        bestScore = float('-inf')
        bestMove = None

        # The computer temporarily plays its move for each empty cell
        # Then, the algorithm calculates the score for each of these moves and undoes the corresponding move in the gamePos array
        # Finally, if the score in this variant (sequence of moves) is higher than the scores in previous ones,
        # the bestScore and bestMove variables are updated
        for i in range(3):
            for j in range(3):
                if self.gamePos[i][j] == 0:
                    self.gamePos[i][j] = self.aiSymbol
                    score = self.minimax(False)
                    self.gamePos[i][j] = 0
                    if score > bestScore:
                        bestScore = score
                        bestMove = (i, j)

        # If there is a best move, the computer chooses it against the user
        if bestMove:
            self.makeMove(*bestMove, True)

    # Algorithm for calculating the score from the perspective of the computer or the user (isMaximizing)
    # Positive score means the computer wins, and negative score means the user wins
    def minimax(self, isMaximizing):
        winner = self.checkWinner()
        if winner != 0:
            # Returns 1 if the variant (sequence of moves) wins in favor of the computer or -1 if it wins in favor of the user
            # Otherwise, returns 0 for a draw
            return self.scorePosition(winner)

        if isMaximizing:
            # Similar to aiMove, tries all possible empty cells as the next move for the computer and returns the score of the best move
            bestScore = float('-inf')
            for i in range(3):
                for j in range(3):
                    if self.gamePos[i][j] == 0:
                        self.gamePos[i][j] = self.aiSymbol
                        score = self.minimax(False)
                        self.gamePos[i][j] = 0
                        bestScore = max(score, bestScore)
            return bestScore
        else:
            # Similar to above, returns the score of the best move for the user
            bestScore = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.gamePos[i][j] == 0:
                        self.gamePos[i][j] = self.playerSymbol
                        score = self.minimax(True)
                        self.gamePos[i][j] = 0
                        bestScore = min(score, bestScore)
            return bestScore

    # Part of the algorithm to find the optimal move
    # Returns 1 if the computer wins and -1 if the user wins; otherwise, returns 0
    def scorePosition(self, winner):
        if winner == self.aiSymbol:
            return 1
        elif winner == self.playerSymbol:
            return -1
        return 0

    # Initiates a game between two players
    def twoPlayers(self):
        self.createGame()
        self.isOnePlayer = False
 
    # Method that initializes game values
    def createGame(self):
        # The turn of the player currently playing
        # 1 -> X
        # 2 -> O
        self.move = 1  # X always plays first
        # 3x3 array that stores the moves of the game
        # 0 - no move
        # 1 - X
        # 2 - O
        self.gamePos = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.clearWindow()
        # 3x3 array with the cells of the game (Tkinter)
        self.buttons = [[None, None, None], [None, None, None], [None, None, None]]

        # Creates the empty buttons using Tkinter
        for i in range(3):
            for j in range(3):
                button = CTkButton(master=self, text=" ",command=lambda i=i, j=j: self.makeMove(i, j),fg_color="#4158D0")
                button.grid(row=i, column=j, sticky="nsew", padx=5, pady=5)
                button.configure(width=4, height=2)
                self.grid_rowconfigure(i, weight=1)
                self.grid_columnconfigure(j, weight=1)
                self.buttons[i][j] = button

        
        # Use CTkLabel without 'bg' and 'fg'
        self.label_style = {"bg": "#A64C62", "fg": "white", "font": self.font_large}
        self.win_label_initial = {"bg": "blue", "fg": "white", "font": self.font_small}
        self.win_label_final = {"bg": "#A64C62"}
        self.winner_announcement = CTkLabel(self, text="", font=self.font_small)
        self.winner_announcement.grid(row=3, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)

        # Creates the button to return to the main menu
        img = Image.open("./icons/goback.png")   
        self.return_button = CTkButton(master=self, text="Return To Main Page", command=self.mainMenu, corner_radius=12, fg_color="#4158D0", 
                        hover_color="#CD8C67", border_color="#CD8C67", 
                        border_width=2, image=CTkImage(dark_image=img, light_image=img))
        self.return_button.grid(row=4, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)


    # Announces the winner of the game in the label created earlier
    def announceWinner(self, winner):
        if winner == 1:
            winner_text = "Player X wins!"
        elif winner == 2:
            winner_text = "Player O wins!"
        else:
            winner_text = "It's a draw!"

        # Makes the label not invisible
        self.winner_announcement.configure(self.win_label_final)
        # Changes the text of the label
        self.winner_announcement.configure(text=winner_text)

    # Clears all elements from the Tkinter window
    def clearWindow(self):
        self.geometry("500x500")
        for widget in self.winfo_children():
            widget.destroy()

    # Closes the program
    def exit(self):
        self.destroy()
        

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
