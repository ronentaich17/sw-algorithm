import numpy as np
from sequence import Sequence

def find_max_score(matrix: list[list[int]]):
    return np.max(matrix)

def find_max_indices(matrix: list[list[int]]):
    max_indices = np.unravel_index(np.argmax(matrix), matrix.shape)
    return max_indices

def matrix_filling_step(matrix: list[list[int]], len_seq1: int, len_seq2: int, match_score: int, seq1: Sequence, seq2: Sequence, mismatch_penalty: int, gap_penalty: int) -> list[list[int]]:
    """
    Performs the initial matrix filling step:
    Go through the matrix and assign penalities based on whether the step in the loop is a match, mismatch, or gap

    Args:
        matrix (list[list[int]]): the initially empty matrix (filled with zeroes)
        len_seq1 (int): length of the first sequence
        len_seq2 (int): length of the second sequence
        match_score (int): the match score
        seq1 (Sequence): sequence 1
        seq2 (Sequence): sequence 2
        mismatch_penalty (int): mismatch penalty
        gap_penalty (int): gap penalty

    Returns:
        list[list[int]]: the newly filled matrix
    """
    for i in range(1, len_seq1 + 1):
        for j in range(1, len_seq2 + 1):
            match = matrix[i - 1, j - 1] + (match_score if seq1.get_sequence()[i-1] == seq2.get_sequence()[j-1] else mismatch_penalty)
            delete = matrix[i - 1, j] + gap_penalty
            insert = matrix[i, j - 1] + gap_penalty
            matrix[i, j] = max(0, match, delete, insert)
    print(matrix)
    return matrix

def matrix_traceback_step(matrix: list[list[int]], match_score: int, seq1: Sequence, seq2: Sequence, mismatch_penalty: int, gap_penalty: int, i: int, j: int, alignment_seq1: str, alignment_seq2: str):
    """
    Perform the matrix traceback step to find the alignment between the two sequences

    Args:
        matrix (list[int[int]]): matrix that will be used to perform the traceback step on
        match_score (int): match score 
        seq1 (str): sequence 1
        seq2 (str): sequence 2
        mismatch_penalty (int): mismatch penalty
        gap_penalty (int): gap_penalty

    Returns:
        _type_: _description_
    """
    seq1 = seq1.get_sequence()
    seq2 = seq2.get_sequence()
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

    return alignment_seq1, alignment_seq2
