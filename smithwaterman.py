def smith_waterman(seq1, seq2, match_score, mismath_score, gap_penalty):
    '''
    step 1: initialization
    ----------------------
    create a matrix and initialize it with zeros
    '''
    matrix = []

    for i in range(len(seq2) + 1):
        row = [0] * (len(seq2) + 1)
        matrix.append(row)

    print(matrix)

def main():
    smith_waterman('ACTG', 'TGGA', 1, -1, 2)

main()

    