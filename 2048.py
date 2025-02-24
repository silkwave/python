import random
import tkinter as tk
from tkinter import messagebox
from copy import deepcopy

class Game2048GUI:
    def __init__(self, size=4):
        self.size = size
        self.root = tk.Tk()
        self.root.title("2048 Game")
        self.frame = tk.Frame(self.root)
        self.frame.grid()
        self.score_label = tk.Label(self.frame, text="Score: 0")
        self.score_label.grid(row=0, column=0)
        self.board_frame = tk.Frame(self.frame)
        self.board_frame.grid(row=1, column=0)
        self.tiles = [[None] * size for _ in range(size)]
        self.board = [[0]*size for _ in range(size)]
        self.score = 0
        self.add_new_tile()
        self.add_new_tile()
        self.display_board()

    def add_new_tile(self):
        empty_cells = [(i, j) for i in range(self.size) for j in range(self.size) if self.board[i][j] == 0]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.board[row][col] = random.choice([2, 4])

    def display_board(self):
        self.score_label.config(text="Score: " + str(self.score))
        for i in range(self.size):
            for j in range(self.size):
                if self.tiles[i][j] is not None:
                    self.tiles[i][j].destroy()
                self.tiles[i][j] = tk.Label(self.board_frame, text=str(self.board[i][j]) if self.board[i][j] != 0 else "-",
                                             width=5, height=2, font=("Helvetica", 20, "bold"))
                self.tiles[i][j].grid(row=i, column=j)

    def move(self, direction):
        if direction == "left":
            self.board = self.move_left()
        elif direction == "right":
            self.board = self.move_right()
        elif direction == "up":
            self.board = self.move_up()
        elif direction == "down":
            self.board = self.move_down()
        else:
            messagebox.showinfo("Invalid Direction", "Invalid direction! Use left/right/up/down.")
            return

        self.add_new_tile()
        self.display_board()

        if self.is_game_over():
            messagebox.showinfo("Game Over", "Game Over! Final Score: " + str(self.score))
            self.root.destroy()

    def move_left(self):
        new_board = deepcopy(self.board)
        for i in range(self.size):
            new_board[i] = self.compress(new_board[i])
            new_board[i] = self.merge(new_board[i])
            new_board[i] = self.compress(new_board[i])
        return new_board

    def move_right(self):
        new_board = deepcopy(self.board)
        for i in range(self.size):
            new_board[i] = self.reverse(self.compress(self.reverse(new_board[i])))
            new_board[i] = self.reverse(self.merge(self.reverse(new_board[i])))
            new_board[i] = self.reverse(self.compress(self.reverse(new_board[i])))
        return new_board

    def move_up(self):
        new_board = deepcopy(self.board)
        for j in range(self.size):
            col = [new_board[i][j] for i in range(self.size)]
            col = self.compress(col)
            col = self.merge(col)
            col = self.compress(col)
            for i in range(self.size):
                new_board[i][j] = col[i]
        return new_board

    def move_down(self):
        new_board = deepcopy(self.board)
        for j in range(self.size):
            col = [new_board[i][j] for i in range(self.size)]
            col = self.reverse(self.compress(self.reverse(col)))
            col = self.reverse(self.merge(self.reverse(col)))
            col = self.reverse(self.compress(self.reverse(col)))
            for i in range(self.size):
                new_board[i][j] = col[i]
        return new_board

    def compress(self, row):
        new_row = [cell for cell in row if cell != 0]
        new_row += [0] * (len(row) - len(new_row))
        return new_row

    def merge(self, row):
        for i in range(len(row)-1):
            if row[i] == row[i+1] and row[i] != 0:
                row[i] *= 2
                self.score += row[i]
                row[i+1] = 0
        return row

    def reverse(self, row):
        return row[::-1]

    def is_game_over(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return False
                if j < self.size - 1 and self.board[i][j] == self.board[i][j+1]:
                    return False
                if i < self.size - 1 and self.board[i][j] == self.board[i+1][j]:
                    return False
        return True

    def run(self):
        self.root.bind("<Left>", lambda event: self.move("left"))
        self.root.bind("<Right>", lambda event: self.move("right"))
        self.root.bind("<Up>", lambda event: self.move("up"))
        self.root.bind("<Down>", lambda event: self.move("down"))
        self.root.mainloop()

if __name__ == "__main__":
    game = Game2048GUI()
    game.run()
