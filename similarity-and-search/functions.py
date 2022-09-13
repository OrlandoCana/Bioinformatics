from sys import stdout
from typing import List


def create_matrix(rows: int, cols: int) -> List[List[int]]:
    array = []
    for ind_row in range(rows):
        row = []
        for ind_col in range(cols):
            row.append(None)
        array.append(row)

    return array


def show_matrix(array: List[List[int]]) -> None:
    for row in array:
        for column in row:
            stdout.write(str(column) + '\t')
        stdout.write('\n')


def levenshtein_algorithm(sequence1: str, sequence2: str) -> None:
    rows = len(sequence1) + 1
    cols = len(sequence2) + 1
    matrix = create_matrix(rows, cols)

    # Put consecutive numbering in the first row and first column
    for ind_row in range(rows):
        matrix[ind_row][0] = ind_row

    for ind_col in range(cols):
        matrix[0][ind_col] = ind_col

    """Compare each character in the row with the corresponding character
    of the intersected column, put the value of 0 if the characters
    are the same, and put 1 if the characters are different."""

    for ind_row in range(1, rows):
        for ind_col in range(1, cols):
            matrix[ind_row][ind_col] = [
                1, 0][sequence1[ind_row-1] == sequence2[ind_col-1]]

    """The value assigned to the cell in process is the minimum
    of:
    ▪ Top cell value + 1
    ▪ Left cell value + 1
    ▪ Upper left diagonal cell value + cell value
    current"""

    for ind_row in range(1, rows):
        for ind_col in range(1, cols):
            matrix[ind_row][ind_col] = min(matrix[ind_row-1][ind_col] + 1,
                                           matrix[ind_row][ind_col-1] + 1, matrix[ind_row-1][ind_col-1] +
                                           matrix[ind_row][ind_col])

    return matrix


def bad_character_rule():
    k = 0
    return k


def sufix_rule():
    k = 0
    return 0


def booyerMoore_algorithm(sequence: str, pattern: str) -> int:
    k = 0
    lenPattern = len(pattern)
    while (k < len(sequence)):
        if (sequence[k: lenPattern] == pattern):
            break
        add_pos = max(bad_character_rule(
            sequence[k:lenPattern]), sufix_rule(sequence[k:lenPattern]))
        k += add_pos
    return k
