def smith_waterman(seq1, seq2, match_score, mismatch_penalty, gap_penalty):
    '''
    step 1: initialization
    ----------------------
    create a matrix and initialize it with zeros
    '''
    matrix = []

    for i in range(len(seq2) + 1):
        row = [0] * (len(seq2) + 1)
        matrix.append(row)

    '''
    step 2: matrix filling
    ----------------------
    fill in the matrix based on the match, mismatch, and gap penalty parameters
    '''
    for i in range(1, len(seq1)+1):
        for j in range(1, len(seq2) + 1):
            #conditional to find score for match / mismatch
            if seq1[i - 1] == seq2[j - 1]:
                current_match_score = match_score  
            else: 
                mismatch_penalty

            match = matrix[i - 1][j - 1] + current_match_score
            delete = matrix[i-1][j] + gap_penalty
            insert = matrix[i][j-1] + gap_penalty
            matrix[i][j] = max(0, match, insert, delete)
    
    '''
    step 3: finding in MSP
    ----------------------
    find the maximum scoring pair (the highest scoring segment pair)
    '''
    max_score = 0
    max_idx_i, max_idx_j = 0, 0 #defined in step 3, utilized in step 4
    for i in range (len(seq1)+1):
        for j in range (len(seq2)+1):
            if matrix[i][j] > max_score:
                max_score = matrix[i][j]
                max_idx_i = i
                max_idx_j = j

    '''
    step 4: traceback
    ----------------------
    traceback to find the alignment
    '''        




def main():
    #test strings
    sequence1 = "ACTG"
    sequence2 = "ACTG"

    #implement deafault score if user presses enter
    match = int(input("Enter match score: "))
    mismatch = int(input("Enter mismatch penalty: "))
    gap = int(input("Enter gap penalty: "))

    smith_waterman(sequence1, sequence2, match, mismatch, gap)


if __name__ == "__main__":
    main()


    



    