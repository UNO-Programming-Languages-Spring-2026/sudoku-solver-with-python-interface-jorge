import sys
import clingo


class ClingoApp(clingo.application.Application):
    def print_model(self, model, _):
        print(" ".join(sorted(str(s) for s in model.symbols(shown=True))))
        sys.stdout.write("\n")
        # sys.stdout.flush()

    def main(self, ctl, files):
        if len(files) != 1:
            sys.stderr.write("Invalid input format: a single file should be provided\n")
            return False
        ctl.load("sudoku.lp")
        ctl.load(files[0])
        ctl.ground()
        ctl.solve()


if __name__ == "__main__":
    clingo.application.clingo_main(ClingoApp())
