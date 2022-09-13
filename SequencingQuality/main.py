import functions as func

if (__name__ == '__main__'):
    # Read the first 16 rows of a .fastq file.
    FILEPATH = 'SequencingQuality/sequenceQuality.fastq'
    sequences = func.read_file(FILEPATH, 16)
    
    print(f'This is of sequences number: {len(sequences)}')
    
    # Show box plot
    func.box_plot(sequences)
        
    