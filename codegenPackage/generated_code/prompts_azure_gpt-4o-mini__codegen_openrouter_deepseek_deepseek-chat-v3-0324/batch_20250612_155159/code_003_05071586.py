"""
Generated Code Metadata:
========================
Original URL: https://argent.bio
Prompt: Write a Python script that utilizes the Argent Bio library to analyze biological sequences.
Generated: DETERMINISTIC_05071586120e685c
Batch ID: 20250612_155159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Biological Sequence Analysis Script using Argent Bio library.

This script demonstrates how to use the Argent Bio library to analyze
biological sequences (DNA, RNA, protein) with various operations.
"""

import argparse
from argento_bio import Sequence, SequenceAnalyzer
from typing import Optional, List, Dict


def analyze_sequence(
    sequence: str,
    sequence_type: str,
    operations: List[str],
    output_file: Optional[str] = None
) -> Dict[str, str]:
    """
    Perform specified analysis operations on a biological sequence.

    Args:
        sequence: Input biological sequence
        sequence_type: Type of sequence ('dna', 'rna', or 'protein')
        operations: List of operations to perform
        output_file: Optional file path to save results

    Returns:
        Dictionary containing analysis results

    Raises:
        ValueError: If invalid sequence type or operation is provided
    """
    # Validate sequence type
    if sequence_type.lower() not in ['dna', 'rna', 'protein']:
        raise ValueError(f"Invalid sequence type: {sequence_type}")

    # Create sequence object
    seq_obj = Sequence(sequence, sequence_type)

    # Initialize analyzer
    analyzer = SequenceAnalyzer(seq_obj)

    # Perform requested operations
    results = {}
    for op in operations:
        op_lower = op.lower()
        if op_lower == 'reverse_complement':
            if sequence_type != 'dna':
                raise ValueError("Reverse complement only valid for DNA sequences")
            results[op] = analyzer.reverse_complement()
        elif op_lower == 'transcribe':
            if sequence_type != 'dna':
                raise ValueError("Transcription only valid for DNA sequences")
            results[op] = analyzer.transcribe()
        elif op_lower == 'translate':
            if sequence_type not in ['dna', 'rna']:
                raise ValueError("Translation only valid for DNA/RNA sequences")
            results[op] = analyzer.translate()
        elif op_lower == 'gc_content':
            if sequence_type not in ['dna', 'rna']:
                raise ValueError("GC content only valid for DNA/RNA sequences")
            results[op] = str(analyzer.gc_content())
        elif op_lower == 'molecular_weight':
            results[op] = str(analyzer.molecular_weight())
        elif op_lower == 'amino_acid_composition':
            if sequence_type != 'protein':
                raise ValueError("Amino acid composition only valid for protein sequences")
            results[op] = analyzer.amino_acid_composition()
        else:
            raise ValueError(f"Unknown operation: {op}")

    # Save results to file if specified
    if output_file:
        with open(output_file, 'w') as f:
            for op, result in results.items():
                f.write(f"{op}:\n{result}\n\n")

    return results


def main():
    """Main function to handle command line interface."""
    parser = argparse.ArgumentParser(
        description="Biological Sequence Analysis Tool using Argent Bio library"
    )
    parser.add_argument(
        'sequence',
        type=str,
        help="Biological sequence to analyze"
    )
    parser.add_argument(
        '--type',
        type=str,
        choices=['dna', 'rna', 'protein'],
        required=True,
        help="Type of biological sequence (dna, rna, protein)"
    )
    parser.add_argument(
        '--operations',
        type=str,
        nargs='+',
        required=True,
        choices=[
            'reverse_complement',
            'transcribe',
            'translate',
            'gc_content',
            'molecular_weight',
            'amino_acid_composition'
        ],
        help="Analysis operations to perform"
    )
    parser.add_argument(
        '--output',
        type=str,
        help="Output file to save results"
    )

    args = parser.parse_args()

    try:
        results = analyze_sequence(
            sequence=args.sequence,
            sequence_type=args.type,
            operations=args.operations,
            output_file=args.output
        )

        # Print results to console
        print("\nAnalysis Results:")
        for operation, result in results.items():
            print(f"\n{operation}:")
            print(result)

    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
