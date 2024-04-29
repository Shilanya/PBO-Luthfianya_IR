import tkinter as tk
import random

class SudokuGrid(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()
        self.generate_board()

    def create_widgets(self):
        self.cells = [[tk.Entry(self.master, width=3, font=('Arial', 18, 'bold'))
                       for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                self.cells[i][j].grid(row=i, column=j)
                if (i % 3 == 2 and i != 0) and (j % 3 == 2 and j != 0):
                    self.cells[i][j].grid(padx=(0, 5), pady=(0, 5))
                elif i % 3 == 2 and i != 0:
                    self.cells[i][j].grid(pady=(0, 5))
                elif j % 3 == 2 and j != 0:
                    self.cells[i][j].grid(padx=(0, 5))
                else:
                    self.cells[i][j].grid(padx=(0, 0), pady=(0, 0))

        self.solve_button = tk.Button(self.master, text="Solve", command=self.solve)
        self.solve_button.grid(row=9, columnspan=9)

        self.shuffle_button = tk.Button(self.master, text="Shuffle", command=self.shuffle)
        self.shuffle_button.grid(row=10, columnspan=9)

    def generate_board(self):
        self.board = [[0]*9 for _ in range(9)]
        self.fill_cells()
        self.solve()

    def fill_cells(self):
        for _ in range(17):  # Untuk membuat 17 angka awal
            row, col, num = random.randint(0, 8), random.randint(0, 8), random.randint(1, 9)
            while not self.is_valid(row, col, num) or self.board[row][col] != 0:
                row, col, num = random.randint(0, 8), random.randint(0, 8), random.randint(1, 9)
            self.board[row][col] = num
            self.cells[row][col].insert(0, str(num))
            self.cells[row][col].config(fg="blue")

    def solve(self):
        self.clear_board()
        self._solve_helper(0, 0)

    def _solve_helper(self, row, col):
        if row == 9:
            return True
        next_row, next_col = (row, col + 1) if col < 8 else (row + 1, 0)
        if self.board[row][col] != 0:
            return self._solve_helper(next_row, next_col)
        nums = list(range(1, 10))
        random.shuffle(nums)
        for num in nums:
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self._solve_helper(next_row, next_col):
                    return True
                self.board[row][col] = 0
        return False

    def is_valid(self, row, col, num):
        for i in range(9):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == num:
                    return False
        return True

    def clear_board(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, tk.END)
                self.cells[i][j].config(fg="black")
        self.update()

        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    self.cells[i][j].insert(0, str(self.board[i][j]))

    def shuffle(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, tk.END)
                self.board[i][j] = 0
        self.fill_cells()

def main():
    root = tk.Tk()
    root.title("Sudoku")
    game = SudokuGrid(master=root)
    game.mainloop()

if __name__ == "__main__":
    main()
