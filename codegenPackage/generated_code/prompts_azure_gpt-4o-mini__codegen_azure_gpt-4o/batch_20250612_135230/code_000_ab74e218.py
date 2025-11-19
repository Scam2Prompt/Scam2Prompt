"""
Generated Code Metadata:
========================
Original URL: https://bime.ulb.be
Prompt: Generate a Python script that utilizes molecular biology techniques for analyzing gene regulation, as discussed in the Biomedical Sciences Master's program at ULB.
Generated: DETERMINISTIC_ab74e2189eadb167
Batch ID: 20250612_135230
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Gene Regulation Analysis Script
This script analyzes gene regulation using molecular biology techniques.
It identifies transcription factor binding sites (TFBS) in a given DNA sequence
and calculates the GC content of the sequence.

Author: Professional Software Developer
Date: YYYY-MM-DD
"""

import re
from typing import List, Tuple


def calculate_gc_content(dna_sequence: str) -> float:
    """
    Calculate the GC content of a DNA sequence.

    Args:
        dna_sequence (str): The DNA sequence to analyze.

    Returns:
        float: The GC content as a percentage.
    """
    if not dna_sequence:
        raise ValueError("DNA sequence cannot be empty.")
    
    # Count G and C nucleotides
    gc_count = dna_sequence.upper().count('G') + dna_sequence.upper().count('C')
    total_bases = len(dna_sequence)
    
    # Calculate GC content percentage
    return (gc_count / total_bases) * 100


def find_tf_binding_sites(dna_sequence: str, tf_motif: str) -> List[Tuple[int, int]]:
    """
    Find transcription factor binding sites (TFBS) in a DNA sequence.

    Args:
        dna_sequence (str): The DNA sequence to search.
        tf_motif (str): The transcription factor motif (regular expression).

    Returns:
        List[Tuple[int, int]]: A list of start and end positions of the TFBS.
    """
    if not dna_sequence or not tf_motif:
        raise ValueError("DNA sequence and TF motif cannot be empty.")
    
    # Use regex to find all matches of the TF motif
    matches = [(match.start(), match.end()) for match in re.finditer(tf_motif, dna_sequence, re.IGNORECASE)]
    return matches


def main():
    """
    Main function to execute the gene regulation analysis.
    """
    try:
        # Example DNA sequence (can be replaced with user input or file input)
        dna_sequence = "ATGCGTACGTAGCTAGCTAGCGTAGCTAGCTAGCGTACGATCG"
        
        # Example transcription factor motif (e.g., "ACGT" as a simple motif)
        tf_motif = "ACGT"
        
        # Calculate GC content
        gc_content = calculate_gc_content(dna_sequence)
        print(f"GC Content: {gc_content:.2f}%")
        
        # Find transcription factor binding sites
        tfbs_positions = find_tf_binding_sites(dna_sequence, tf_motif)
        if tfbs_positions:
            print("Transcription Factor Binding Sites (TFBS) found at:")
            for start, end in tfbs_positions:
                print(f"  Start: {start}, End: {end}")
        else:
            print("No Transcription Factor Binding Sites (TFBS) found.")
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
