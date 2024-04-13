import numpy as np
import pandas as pd

def smith_waterman(seq1, seq2, match_score=2, mismatch_penalty=-1, gap_penalty=-1):
    
    #initialization step: create the matrix with appropriate dimensions
    len_seq1, len_seq2 = len(seq1), len(seq2)
    matrix = np.zeros((len_seq1 + 1, len_seq2 + 1))

    #matrix filling step: go through the matrix and assign penalities based on whether the step in the loop is a match, mismatch, or gap
    for i in range(1, len_seq1 + 1):
        for j in range(1, len_seq2 + 1):
            match = matrix[i - 1, j - 1] + (match_score if seq1[i - 1] == seq2[j - 1] else mismatch_penalty)
            delete = matrix[i - 1, j] + gap_penalty
            insert = matrix[i, j - 1] + gap_penalty
            matrix[i, j] = max(0, match, delete, insert)
    print(matrix)

    max_score = np.max(matrix)
    max_indices = np.unravel_index(np.argmax(matrix), matrix.shape)

    # traceback to find the alignment
    alignment_seq1, alignment_seq2 = '', ''
    i, j = max_indices
    while i > 0 and j > 0 and matrix[i, j] > 0:
        if matrix[i, j] == matrix[i - 1, j - 1] + (match_score if seq1[i - 1] == seq2[j - 1] else mismatch_penalty):
            alignment_seq1 = seq1[i - 1] + alignment_seq1
            alignment_seq2 = seq2[j - 1] + alignment_seq2
            i -= 1
            j -= 1
        elif matrix[i, j] == matrix[i - 1, j] + gap_penalty:
            alignment_seq1 = seq1[i - 1] + alignment_seq1
            alignment_seq2 = '-' + alignment_seq2
            i -= 1
        else:
            alignment_seq1 = '-' + alignment_seq1
            alignment_seq2 = seq2[j - 1] + alignment_seq2
            j -= 1

    return alignment_seq1, alignment_seq2, max_score

# read sequences from a CSV file using Pandas
sequences_df = pd.read_csv('sequences.csv')

# loop through each row in the DataFrame
for index, row in sequences_df.iterrows():
    seq1 = row['Sequence1']
    seq2 = row['Sequence2']

    # perform sequence alignment
    alignment1, alignment2, score = smith_waterman(seq1, seq2)

    # present alignment results using Pandas DataFrame
    alignment_df = pd.DataFrame({'Alignment1': list(alignment1),
                                 'Alignment2': list(alignment2)})
    print("Pair:", index + 1)
    print(alignment_df)
    print("Alignment Score:", score)
    print()