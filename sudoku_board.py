from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        # YOUR CODE HERE
        for i in range(1, 10):
            for j in range(1, 10):
                s += str(self.sudoku.get((i, j), "-"))
                if j % 9 != 0:
                    s += " "
                if j % 3 == 0 and j % 9 != 0:
                    s += " "
            s += "\n"
            if i % 3 == 0 and i % 9 != 0:
                s += "\n"
        # YOUR CODE ENDS HERE
        return s

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        for i, line in enumerate(line for line in s.splitlines() if line.strip() != ""):
            for j, c in enumerate(line.split()):
                if c.isdigit():
                    sudoku[i + 1, j + 1] = int(c)
        # YOUR CODE ENDS HERE
        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        for atom in model.symbols(shown=True):
            if atom.name == "sudoku":
                sudoku[
                    atom.arguments[0].number, atom.arguments[1].number
                ] = atom.arguments[2].number
        # YOUR CODE ENDS HERE
        return cls(sudoku)
