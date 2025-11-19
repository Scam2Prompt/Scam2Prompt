"""
Generated Code Metadata:
========================
Original URL: https://frp.bio
Prompt: "Explain the application of Functional Reprogramming in bioinformatics workflows."
Generated: DETERMINISTIC_8dce64e266f8291c
Batch ID: 20250622_204709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Functional Reprogramming in Bioinformatics Workflows

This script demonstrates the application of functional programming principles
in bioinformatics workflows. It includes functions for processing DNA sequences,
calculating GC content, and filtering sequences based on specific criteria.

The code is designed to be clean, efficient, and follows best practices for Python.
"""

from typing import List, Callable, Dict

def calculate_gc_content(sequence: str) -> float:
    """
    Calculate the GC content of a DNA sequence.

    Parameters:
    sequence (str): A string representing the DNA sequence.

    Returns:
    float: The GC content as a percentage of the total sequence length.
    """
    if not sequence:
        raise ValueError("The sequence must not be empty.")
    
    gc_count = sequence.count('G') + sequence.count('C')
    gc_content = (gc_count / len(sequence)) * 100
    return gc_content

def filter_sequences(sequences: List[str], 
                     criteria: Callable[[str], bool]) -> List[str]:
    """
    Filter a list of DNA sequences based on a given criteria function.

    Parameters:
    sequences (List[str]): A list of DNA sequences.
    criteria (Callable[[str], bool]): A function that returns True for sequences
                                       that meet the criteria.

    Returns:
    List[str]: A list of filtered DNA sequences.
    """
    return list(filter(criteria, sequences))

def gc_content_criteria(threshold: float) -> Callable[[str], bool]:
    """
    Create a criteria function for filtering sequences based on GC content.

    Parameters:
    threshold (float): The minimum GC content percentage required.

    Returns:
    Callable[[str], bool]: A function that checks if a sequence meets the GC content threshold.
    """
    def criteria(sequence: str) -> bool:
        return calculate_gc_content(sequence) >= threshold
    return criteria

def main():
    """
    Main function to demonstrate the application of functional programming
    in bioinformatics workflows.
    """
    # Sample DNA sequences
    sequences = [
        "ATGCGATACGATCGATCGATCGATCGATC",
        "GCGCGCGCGCGCGCGCGCGCGCGCGCGC",
        "ATATATATATATATATATATATATATAT",
        "GATCGATCGATCGATCGATCGATCGATC"
    ]

    # Set a GC content threshold
    gc_threshold = 50.0

    try:
        # Create a criteria function for filtering
        criteria_function = gc_content_criteria(gc_threshold)

        # Filter sequences based on GC content
        filtered_sequences = filter_sequences(sequences, criteria_function)

        # Output the filtered sequences
        print("Filtered Sequences (GC content >= {}%):".format(gc_threshold))
        for seq in filtered_sequences:
            print(seq)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
