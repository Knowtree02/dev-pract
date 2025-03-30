def is_valid_subsequence(array, sequence):
    seq_index = 0
    for item in array:
        if seq_index < len(sequence) and item == sequence[seq_index]:
            seq_index += 1
    return seq_index == len(sequence)

# Example usage
array = [1, 2, 3, 4]
sequence = [1, 3, 4]
print(is_valid_subsequence(array, sequence))  # Output: True
