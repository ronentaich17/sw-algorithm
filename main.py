from sw import sw
from sequence import Sequence
import pandas as pd

def main():
    # read sequences from a CSV
    sequences_df = pd.read_csv('sequences.csv')
    
    # loop through each row in the DataFrame
    for index, row in sequences_df.iterrows():
        seq1 = Sequence(row['Sequence1'])
        seq2 = Sequence(row['Sequence2'])

        # perform sequence alignment
        alignment1, alignment2, score = sw(seq1, seq2)

        # present alignment results using Pandas DataFrame
        alignment_df = pd.DataFrame({'Alignment1': list(alignment1),
                                    'Alignment2': list(alignment2)})
        print("Pair:", index + 1)
        print(alignment_df)
        print("Alignment Score:", score)
        print()

if __name__ == '__main__':
    main()
