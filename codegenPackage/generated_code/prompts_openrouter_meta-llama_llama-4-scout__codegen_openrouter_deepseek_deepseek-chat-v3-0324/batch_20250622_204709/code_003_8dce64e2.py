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

This module demonstrates the application of functional programming concepts
in bioinformatics workflows through practical examples.
"""

from typing import Callable, List, Dict, Any, Optional
from functools import partial, reduce
import re
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Type aliases for better readability
DNASequence = str
ProteinSequence = str
SequenceProcessor = Callable[[DNASequence], DNASequence]
Pipeline = List[SequenceProcessor]

def compose(*functions: SequenceProcessor) -> SequenceProcessor:
    """Compose multiple functions into a single function."""
    return reduce(lambda f, g: lambda x: g(f(x)), functions)

def read_fasta(file_path: Path) -> Dict[str, DNASequence]:
    """Read FASTA file and return sequences as a dictionary."""
    try:
        with file_path.open('r') as f:
            content = f.read()
        
        sequences = {}
        for record in content.split('>')[1:]:
            lines = record.split('\n')
            header = lines[0].strip()
            sequence = ''.join(lines[1:]).replace('\n', '')
            sequences[header] = sequence
        
        return sequences
    except Exception as e:
        logger.error(f"Error reading FASTA file: {e}")
        raise

def write_fasta(sequences: Dict[str, DNASequence], output_path: Path) -> None:
    """Write sequences to a FASTA file."""
    try:
        with output_path.open('w') as f:
            for header, sequence in sequences.items():
                f.write(f">{header}\n{sequence}\n")
    except Exception as e:
        logger.error(f"Error writing FASTA file: {e}")
        raise

def filter_sequence(sequence: DNASequence, 
                   min_length: int = 0, 
                   max_length: Optional[int] = None) -> DNASequence:
    """Filter sequence based on length constraints."""
    if len(sequence) < min_length:
        raise ValueError(f"Sequence too short (min {min_length} bp)")
    if max_length and len(sequence) > max_length:
        raise ValueError(f"Sequence too long (max {max_length} bp)")
    return sequence

def reverse_complement(sequence: DNASequence) -> DNASequence:
    """Generate reverse complement of DNA sequence."""
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join([complement[base] for base in sequence[::-1]])

def translate_dna(sequence: DNASequence) -> ProteinSequence:
    """Translate DNA sequence to protein."""
    codon_table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
        'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W'
    }
    
    protein = []
    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i:i+3]
        protein.append(codon_table.get(codon, 'X'))
    
    return ''.join(protein)

def process_sequences(sequences: Dict[str, DNASequence], 
                     pipeline: Pipeline) -> Dict[str, DNASequence]:
    """Apply a processing pipeline to each sequence."""
    return {header: compose(*pipeline)(seq) for header, seq in sequences.items()}

def main():
    """Demonstrate functional bioinformatics workflow."""
    try:
        # Define input/output paths
        input_file = Path("input.fasta")
        output_file = Path("processed.fasta")
        
        # Read sequences
        sequences = read_fasta(input_file)
        
        # Define processing pipeline using functional programming
        pipeline = [
            partial(filter_sequence, min_length=100, max_length=1000),
            reverse_complement,
            translate_dna
        ]
        
        # Process sequences
        processed_seqs = process_sequences(sequences, pipeline)
        
        # Write results
        write_fasta(processed_seqs, output_file)
        logger.info("Processing completed successfully")
        
    except Exception as e:
        logger.error(f"Workflow failed: {e}")
        raise

if __name__ == "__main__":
    main()
```
