import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe: You vs Computer")

        self.board = [[0 for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.create_board()
        self.window.mainloop()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.window, text='', font=('Arial', 32), width=5, height=2,
                                command=lambda row=i, col=j: self.player_move(row, col))
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn

    def player_move(self, row, col):
        if self.board[row][col] != 0:
            return

        self.board[row][col] = 1
        self.buttons[row][col].config(text='X', state='disabled')

        if self.check_winner(1):
            self.end_game("You win!")
            return

        if self.is_draw():
            self.end_game("It's a draw!")
            return

        self.window.after(500, self.computer_move)

    def computer_move(self):
        empty = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == 0]
        if not empty:
            return
        row, col = random.choice(empty)
        self.board[row][col] = 2
        self.buttons[row][col].config(text='O', state='disabled')

        if self.check_winner(2):
            self.end_game("Computer wins!")
        elif self.is_draw():
            self.end_game("It's a draw!")

    def check_winner(self, player):
        b = self.board
        return (
            any(all(b[i][j] == player for j in range(3)) for i in range(3)) or
            any(all(b[i][j] == player for i in range(3)) for j in range(3)) or
            all(b[i][i] == player for i in range(3)) or
            all(b[i][2 - i] == player for i in range(3))
        )

    def is_draw(self):
        return all(cell != 0 for row in self.board for cell in row)

    def end_game(self, message):
        messagebox.showinfo("Game Over", message)
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state='disabled')

# Start the game
TicTacToe()
