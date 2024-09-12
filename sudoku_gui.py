# sudoku_gui.py

import tkinter as tk
from tkinter import messagebox
from sudoku_solver import solve_sudoku

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.grid = [[0] * 9 for _ in range(9)]
        self.entries = [[tk.Entry(root, width=3, font=('Arial', 16), justify='center') for _ in range(9)] for _ in range(9)]
        self.create_widgets()
        
    def create_widgets(self):
        for row in range(9):
            for col in range(9):
                self.entries[row][col].grid(row=row, column=col, padx=5, pady=5)
        
        solve_button = tk.Button(self.root, text="Solve", command=self.solve)
        solve_button.grid(row=9, column=0, columnspan=9)
        
    def solve(self):
        self.get_grid_from_entries()
        if solve_sudoku(self.grid):
            self.update_entries_from_grid()
        else:
            messagebox.showinfo("Solution", "No solution exists")
        
    def get_grid_from_entries(self):
        for row in range(9):
            for col in range(9):
                value = self.entries[row][col].get()
                if value.isdigit():
                    self.grid[row][col] = int(value)
                else:
                    self.grid[row][col] = 0
        
    def update_entries_from_grid(self):
        for row in range(9):
            for col in range(9):
                self.entries[row][col].delete(0, tk.END)
                if self.grid[row][col] != 0:
                    self.entries[row][col].insert(0, str(self.grid[row][col]))

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()
