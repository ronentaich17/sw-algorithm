class Sequence:
    def __init__(self, sequence: str):
        self.sequence = sequence

    def get_length(self):
        """
        Get the length of the sequence

        Returns:
            int: length of the sequence
        """
        return len(self.sequence)
    
    def get_sequence(self):
        """
        Gets the sequence

        Returns:
            str: the string representing the sequence
        """
        return self.sequence