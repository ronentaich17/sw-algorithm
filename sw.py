import numpy as np
import pandas as pd
from sw_helper_methods import *

def sw(seq1, seq2, match_score=2, mismatch_penalty=-1, gap_penalty=-1):
    
    #initialization step: create the matrix with appropriate dimensions
    len_seq1, len_seq2 = len(seq1), len(seq2)
    matrix = np.zeros((len_seq1 + 1, len_seq2 + 1))

    matrix = matrix_filling_step(matrix=matrix, len_seq1=len_seq1, len_seq2=len_seq2, match_score=match_score, seq1=seq1, seq2=seq2, mismatch_penalty=mismatch_penalty, gap_penalty=gap_penalty)

    max_score = find_max_score(matrix)
    max_indices = find_max_indices(matrix)

    # traceback to find the alignment
    i, j = max_indices

    alignment_seq1, alignment_seq2 = matrix_traceback_step(matrix=matrix, match_score=match_score, seq1=seq1, seq2=seq2, mismatch_penalty=mismatch_penalty, gap_penalty=gap_penalty, i=i, j=j, alignment_seq1= '', alignment_seq2= '')

    return alignment_seq1, alignment_seq2, max_score

# read sequences from a CSV file using Pandas
sequences_df = pd.read_csv('sequences.csv')

# loop through each row in the DataFrame
for index, row in sequences_df.iterrows():
    seq1 = row['Sequence1']
    seq2 = row['Sequence2']

    # perform sequence alignment
    alignment1, alignment2, score = sw(seq1, seq2)

    # present alignment results using Pandas DataFrame
    alignment_df = pd.DataFrame({'Alignment1': list(alignment1),
                                 'Alignment2': list(alignment2)})
    print("Pair:", index + 1)
    print(alignment_df)
    print("Alignment Score:", score)
    print()
    