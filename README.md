
# PRODIGY_SD_04: Sudoku Solver with GUI

This repository contains a Python-based Sudoku Solver that uses the backtracking algorithm. It also provides a simple graphical user interface (GUI) for inputting and solving Sudoku puzzles, built with Tkinter.

## Project Structure

- `sudoku_solver.py`: Contains the core Sudoku solving logic using backtracking.
- `sudoku_gui.py`: Provides a Tkinter-based GUI for inputting Sudoku puzzles and solving them using the logic from `sudoku_solver.py`.

## Features

- **Sudoku Solver**: Solves any valid 9x9 Sudoku puzzle using a backtracking algorithm.
- **Graphical Interface**: Allows users to input puzzles through a user-friendly interface.
- **Real-time Solution**: Once the puzzle is input, the solution is displayed instantly upon pressing the "Solve" button.

## Getting Started

### Prerequisites

Ensure you have Python installed on your system. You also need the Tkinter library for the GUI. Tkinter is generally included in standard Python distributions, but if it's not available, you can install it with the following command:

```bash
pip install tk
```

### Running the Application

1. Clone the repository:

```bash
git clone https://github.com/your-username/PRODIGY_SD_04.git
```

2. Navigate to the project directory:

```bash
cd PRODIGY_SD_04
```

3. Run the GUI:

```bash
python sudoku_gui.py
```

4. Enter the Sudoku puzzle in the GUI. Empty cells should be left blank or set to `0`. Click "Solve" to display the solution.

## Usage

- Input numbers from `1-9` in the appropriate cells of the grid.
- Leave cells empty (or fill with `0`) for unknown values.
- Press the **Solve** button, and the solution will be displayed in the grid. If the puzzle has no valid solution, a message box will inform you.


## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
