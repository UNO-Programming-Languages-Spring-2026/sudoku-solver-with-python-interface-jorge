import sys
import clingo

from sudoku_board import Sudoku


class Context:
    def __init__(self, board: Sudoku):
        self.board = []
        for cell, value in board.sudoku.items():
            atom = clingo.Tuple_(
                (clingo.Number(cell[0]), clingo.Number(cell[1]), clingo.Number(value))
            )
            self.board.append(atom)

    def initial(self) -> list[clingo.Symbol]:
        return self.board


def sudoku_from_model(model: clingo.Model) -> Sudoku:
    sudoku = {}
    for atom in model.symbols(shown=True):
        if atom.name == "sudoku":
            sudoku[atom.arguments[0].number, atom.arguments[1].number] = atom.arguments[
                2
            ].number
    return Sudoku(sudoku)


class ClingoApp(clingo.application.Application):
    def print_model(self, model, _):
        sudoku = sudoku_from_model(model)
        # sys.stdout.write(str(sudoku.sudoku))
        # sys.stdout.write('\n')
        sys.stdout.write(str(sudoku))
        sys.stdout.flush()

    def sudoku_from_files(self, files):
        if len(files) != 1:
            sys.stderr.write("Invalid input format: a single file should be provided\n")
            return False
        with open(files[0], "r") as f:
            return Sudoku.from_str(f.read())

    def main(self, ctl, files):
        ctl.load("sudoku.lp")
        ctl.load("sudoku_py.lp")
        sudoku = self.sudoku_from_files(files)
        ctl.ground(context=Context(sudoku))
        ctl.solve()


if __name__ == "__main__":
    clingo.application.clingo_main(ClingoApp())
