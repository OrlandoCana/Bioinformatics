from sys import stdout
from typing import List
import matplotlib.pyplot as plt

'''
Read a fastq file fetching only rows that are multiples of 4

reference: https://es.frwiki.wiki/wiki/FASTQ
'''
def read_file(file_path: str, num_sequences: int = 5) -> None:
    sequences = []
    with open(file_path, 'r') as file:
        sequence = ''
        iterations = 1
        for line in file:
            if (iterations%4 == 0):
                sequences.append(line.rstrip('\n'))
            iterations += 1
            if (iterations > num_sequences):
                break
        if (sequence != ''):
            sequences.append(sequence.rstrip('\n'))
        return sequences

'''
create_matrix: Create array of size(nxm)

show_matrix: Show matrix of size(nxm)
'''
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

'''
matrix quality
refenrence: https://en.wikibooks.org/wiki/Next_Generation_Sequencing_(NGS)/Pre-processing#Sequence_Quality
'''
def quality_matrix(quality_array: List[str]) -> List[List[int]]:
    rows = len(quality_array)
    cols = len(quality_array[0])
    qualityMatrix = create_matrix(rows, cols)
    for r in range(rows):
        for c in range(cols):
            qualityMatrix[r][c] = ord(quality_array[r][c]) - 33

    return qualityMatrix

'''
BoxPlot 
'''
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
