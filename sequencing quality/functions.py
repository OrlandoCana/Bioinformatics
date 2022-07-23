from sys import stdout
from typing import List
import matplotlib.pyplot as plt


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


def quality_matrix(quality_array: List[str]) -> List[List[int]]:
    rows = len(quality_array)
    cols = len(quality_array[0])
    qualityMatrix = create_matrix(rows, cols)
    for ind_row in range(rows):
        for ind_col in range(cols):
            qualityMatrix[ind_row][ind_col] = ord(
                quality_array[ind_row][ind_col]) - 33

    return qualityMatrix


def box_plot(quality_array: List[str]) -> None:
    rows = len(quality_array)
    cols = len(quality_array[0])
    qualityMatrix = quality_matrix(quality_array)
    data = []
    for ind_col in range(cols):
        items = []
        for ind_row in range(rows):
            items.append(qualityMatrix[ind_row][ind_col])
        data.append(items)

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.boxplot(data)
    plt.show()
