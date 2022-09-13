import functions as func
if (__name__ == '__main__'):
    filePath = 'TranscriptionAndTranslation/sequence.fasta'
    sequences, headers = func.read_file(filePath)
    print(f'This file contains {len(sequences)} sequences')
    print('This is the first sequence:')
    print(sequences[0])
    print()
    
    print('the first strand of DNA converted to complementary ' + 
          'strand of RNA')
    arn = func.transcription(sequences[0])
    print(arn)
    print()
    
    print('the first strand of complementary ARN converted ' + 
          'to strand of proteins')
    proteins = func.translation(arn)
    print(proteins)