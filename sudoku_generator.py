# !/usr/bin/python
import json

from Sudoku.Generator import *


def main():
    sudokus: list[str] = []
    needed_length = 10

    # setting difficulties and their cutoffs for each solve method
    difficulties = {
        'easy': (35, 0),
        'medium': (81, 5),
        'hard': (81, 10),
        'extreme': (81, 15)
    }

    # getting desired difficulty from command line
    difficulty = difficulties["extreme"]

    # While length of sudokus is less than needed_length, generate a new puzzle
    while len(sudokus) < needed_length:
        # constructing generator object from puzzle file (space delimited columns, line delimited rows)
        gen = Generator("base.txt")

        # applying 100 random transformations to puzzle
        gen.randomize(100)

        # applying logical reduction with corresponding difficulty cutoff
        gen.reduce_via_logical(difficulty[0])

        # catching zero case
        if difficulty[1] != 0:
            # applying random reduction with corresponding difficulty cutoff
            gen.reduce_via_random(difficulty[1])

        # getting copy after reductions are completed
        final = gen.board.copy()

        str_final = str(final)

        # Replace "_" with "0" in string
        str_final_zeroes = str_final.replace("_", "0")

        numeric_filter = filter(str.isdigit, str_final_zeroes)
        numeric_string = "".join(numeric_filter)
        sudokus.append(numeric_string)
        print(numeric_string)

        # Print how many sudokus have been generated and how many are needed
        print(f"{len(sudokus)}/{needed_length}")

    # Print out the sudokus one by one
    for sudoku in sudokus:
        print(sudoku)

    # Write the sudokus to a json file
    with open('sudokus.json', 'w') as f:
        json.dump(sudokus, f)


if __name__ == "__main__":
    main()
