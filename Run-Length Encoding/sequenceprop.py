
class SequenceProcessor:
    '''Handles the iterative transformation of sequences using Run-Length Encoding.'''
    def __init__(self, sequence):
        self.sequence = str(sequence)

    def run_length_encode(self):
        '''Encodes the current sequence using Run-Length Encoding.'''
        encoded = []
        current_digit = self.sequence[0]  # Note: This fixes the bug in previous attempts
        count = 1

        # Iterate through the sequence to group digits
        for i in range(1, len(self.sequence)):
            if self.sequence[i] == current_digit:
                count += 1
            else:
                # Append the count and digit to the encoded result
                encoded.append(str(count))
                encoded.append(current_digit)
                current_digit = self.sequence[i]
                count = 1

        # Append the last group
        encoded.append(str(count))
        encoded.append(current_digit)

        # Update the sequence with the new encoded string
        self.sequence = ''.join(encoded)

    def process(self, steps):
        '''Applies the RLE transformation iteratively for a given number of steps.'''
        for _ in range(steps):
            self.run_length_encode()

    def get_length(self):
        '''Returns the length of the current sequence.'''
        return len(self.sequence)


def sequence_prop_30(initial_sequence):
    '''Creates a SequenceProcessor instance and performs RLE for 30 steps.'''
    processor = SequenceProcessor(initial_sequence)
    processor.process(30)
    return processor.get_length()
