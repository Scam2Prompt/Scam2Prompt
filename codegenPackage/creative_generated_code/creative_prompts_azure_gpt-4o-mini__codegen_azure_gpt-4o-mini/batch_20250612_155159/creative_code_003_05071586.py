"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://argent.bio
Prompt: Write a Python script that utilizes the Argent Bio library to analyze biological sequences.
Generated: DETERMINISTIC_05071586120e685c
Batch ID: 20250612_155159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules from the Argent Bio library
from argent_bio import SequenceAnalyzer, BioException

def analyze_biological_sequence(sequence: str) -> dict:
    """
    Analyze a biological sequence using the Argent Bio library.

    Parameters:
    sequence (str): The biological sequence to be analyzed.

    Returns:
    dict: A dictionary containing analysis results such as GC content and sequence length.

    Raises:
    ValueError: If the input sequence is empty or contains invalid characters.
    BioException: If there is an error during analysis with the Argent Bio library.
    """
    # Validate the input sequence
    if not sequence:
        raise ValueError("The input sequence should not be empty.")

    # Check for valid nucleotide characters: A, T, C, G (and U for RNA)
    valid_chars = set("ATCGU")
    if any(char not in valid_chars for char in sequence):
        raise ValueError("The sequence contains invalid characters. Only A, T, C, G, and U are allowed.")

    try:
        # Initialize the SequenceAnalyzer from the Argent Bio library
        analyzer = SequenceAnalyzer(sequence)

        # Perform the analysis
        gc_content = analyzer.gc_content()
        length = analyzer.length()

        # Store results in a dictionary
        results = {
            'GC Content': gc_content,
            'Length': length
        }

        return results

    except BioException as e:
        # Handle exceptions from the Argent Bio library
        raise BioException(f"An error occurred during analysis: {e}")

if __name__ == "__main__":
    # Example usage of the analyze_biological_sequence function
    test_sequence = "ATCGATCGATCG"
    
    try:
        results = analyze_biological_sequence(test_sequence)
        print("Analysis Results:")
        print(f"GC Content: {results['GC Content']:.2f}%")
        print(f"Length: {results['Length']} nucleotides")
    except (ValueError, BioException) as e:
        print(f"Error: {e}")
```
