
def read_file(file_path: str) -> None:
    sequences = []
    headers = []
    with open(file_path, 'r') as file:
        sequence = ''
        for line in file:
            if ('>' in line):
                headers.append(line.rstrip('\n'))
                sequences.append(sequence.rstrip('\n'))
                sequence = ''
            else:
                sequence += line.rstrip('\n')
        if (sequence != ''):
            sequences.append(sequence.rstrip('\n'))
        return sequences[1:], headers


def transcription(sequence: str) -> str:
    return sequence.replace('T', 'U')


def reverseTranscription(sequence: str) -> str:
    return sequence.replace('U', 'T')


def translation(sequence: str) -> str:
    genetic_code = {'GGG': 'G', 'GGA': 'G', 'GGC': 'G', 'GGU': 'G',
                    'GAG': 'E', 'GAA': 'E', 'GAC': 'D', 'GAU': 'D',
                    'GCG': 'A', 'GCA': 'A', 'GCC': 'A', 'GCU': 'A',
                    'GUG': 'V', 'GUA': 'V', 'GUC': 'V', 'GUU': 'V',
                    'AGG': 'R', 'AGA': 'R', 'AGC': 'S', 'AGU': 'S',
                    'AAG': 'K', 'AAA': 'K', 'AAC': 'N', 'AAU': 'N',
                    'ACG': 'T', 'ACA': 'T', 'ACC': 'T', 'ACU': 'T',
                    'AUG': 'M', 'AUA': 'I', 'AUC': 'I', 'AUU': 'I',
                    'CGG': 'R', 'CGA': 'R', 'CGC': 'R', 'CGU': 'R',
                    'CAG': 'Q', 'CAA': 'Q', 'CAC': 'H', 'CAU': 'H',
                    'CCG': 'P', 'CCA': 'P', 'CCC': 'P', 'CCU': 'P',
                    'CUG': 'L', 'CUA': 'L', 'CUC': 'L', 'CUU': 'L',
                    'UGG': 'W', 'UGA': '.', 'UGC': 'C', 'UGU': 'C',
                    'UAG': '.', 'UAA': '.', 'UAC': 'Y', 'UAU': 'Y',
                    'UCG': 'S', 'UCA': 'S', 'UCC': 'S', 'UCU': 'S',
                    'UUG': 'L', 'UUA': 'L', 'UUC': 'F', 'UUU': 'F'}

    proteinSequence = ''
    gens = [sequence[i:i+3] for i in range(0, len(sequence), 3)]
    for gen in gens:
        if (len(gen) == 3):
            proteinSequence += genetic_code[gen]

    return proteinSequence


def reverseTranslation(sequence: str) -> str:
    reverse_genetic_code = {'G': 'GGG', 'E': 'GAG', 'D': 'GAC', 'A': 'GCG',
                            'V': 'GUG', 'R': 'AGG', 'S': 'AGC', 'K': 'AAG',
                            'N': 'AAC', 'T': 'ACG', 'M': 'AUG', 'I': 'AUA',
                            'Q': 'CAG', 'H': 'CAC', 'P': 'CCG', 'L': 'CUG',
                            'W': 'UGG', '.': 'UGA', 'C': 'UGC', 'Y': 'UAC',
                            'F': 'UUC'}

    arnmSequence = ''
    for protein in sequence:
        arnmSequence += reverse_genetic_code[protein]

    return arnmSequence
