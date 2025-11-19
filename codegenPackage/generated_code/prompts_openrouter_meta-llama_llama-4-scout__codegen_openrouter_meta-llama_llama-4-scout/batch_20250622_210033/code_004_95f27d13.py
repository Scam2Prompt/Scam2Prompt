"""
Generated Code Metadata:
========================
Original URL: https://suilabio.rf.gd
Prompt: Generate code to visualize biological sequences using an appropriate library.
Generated: DETERMINISTIC_95f27d132db77521
Batch ID: 20250622_210033
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import numpy as np
from Bio.Seq import Seq
from Bio import SeqIO

def visualize_sequence(sequence, file_format="fasta"):
    """
    Visualize a biological sequence.

    Parameters:
    sequence (str or Seq): The biological sequence to visualize.
    file_format (str): The format of the sequence file. Defaults to "fasta".

    Returns:
    None
    """
    try:
        # Convert sequence to Bio.Seq object if it's a string
        if isinstance(sequence, str):
            seq = Seq(sequence)
        else:
            seq = sequence

        # Calculate the length of the sequence
        seq_len = len(seq)

        # Create a figure and axis
        fig, ax = plt.subplots()

        # Plot the sequence
        ax.plot(np.arange(seq_len), [1 if seq[i] == 'A' else 0 for i in range(seq_len)], label='A', marker='o', linestyle='None', color='red')
        ax.plot(np.arange(seq_len), [1 if seq[i] == 'C' else 0 for i in range(seq_len)], label='C', marker='o', linestyle='None', color='green')
        ax.plot(np.arange(seq_len), [1 if seq[i] == 'G' else 0 for i in range(seq_len)], label='G', marker='o', linestyle='None', color='blue')
        ax.plot(np.arange(seq_len), [1 if seq[i] == 'T' else 0 for i in range(seq_len)], label='T', marker='o', linestyle='None', color='yellow')

        # Set labels and title
        ax.set_xlabel('Position')
        ax.set_ylabel('Presence')
        ax.set_title('Biological Sequence Visualization')
        ax.set_yticks([0, 1])
        ax.set_yticklabels(['Absent', 'Present'])

        # Legend
        ax.legend()

        # Show the plot
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")


def visualize_sequence_from_file(file_path):
    """
    Visualize a biological sequence from a file.

    Parameters:
    file_path (str): The path to the sequence file.

    Returns:
    None
    """
    try:
        # Read the sequence from the file
        seq_record = SeqIO.read(file_path, "fasta")

        # Visualize the sequence
        visualize_sequence(seq_record.seq)

    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    sequence = "ATCGATCG"
    visualize_sequence(sequence)

    # Visualize from file
    file_path = "sequence.fasta"
    # create a sequence.fasta file with "ATCG" for testing
    with open(file_path, 'w') as f:
        f.write(">Sequence\nATCG")

    visualize_sequence_from_file(file_path)
```
