import sys
import clingo

from sudoku_board import Sudoku


class ClingoApp(clingo.application.Application):
    def print_model(self, model, _):
        sudoku = Sudoku.from_model(model)
        sys.stdout.write(str(sudoku))
        sys.stdout.flush()

    def main(self, ctl, files):
        ctl.load("sudoku.lp")
        for file in files:
            ctl.load(file)
        ctl.ground()
        ctl.solve()


if __name__ == "__main__":
    clingo.application.clingo_main(ClingoApp())
