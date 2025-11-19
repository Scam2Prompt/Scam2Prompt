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
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Gene Regulation Analysis Tool

This script provides functionalities for analyzing gene regulation data,
including sequence analysis, motif finding, and expression correlation.
"""

import os
import sys
import logging
import argparse
from typing import List, Dict, Tuple, Optional
import pandas as pd
import numpy as np
from Bio import SeqIO, motifs
from Bio.Seq import Seq
from scipy import stats
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class GeneRegulationAnalyzer:
    """Main class for gene regulation analysis."""
    
    def __init__(self, fasta_file: str = None, expression_file: str = None):
        """
        Initialize the analyzer with optional input files.
        
        Args:
            fasta_file: Path to FASTA file containing DNA sequences
            expression_file: Path to gene expression data file (CSV/TSV)
        """
        self.sequences = {}
        self.expression_data = None
        self.motifs = {}
        
        if fasta_file:
            self.load_sequences(fasta_file)
        if expression_file:
            self.load_expression_data(expression_file)
    
    def load_sequences(self, file_path: str) -> None:
        """
        Load DNA sequences from a FASTA file.
        
        Args:
            file_path: Path to the FASTA file
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If file format is invalid
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"FASTA file not found: {file_path}")
            
        try:
            with open(file_path, 'r') as f:
                for record in SeqIO.parse(f, 'fasta'):
                    self.sequences[record.id] = record.seq
            logger.info(f"Loaded {len(self.sequences)} sequences from {file_path}")
        except Exception as e:
            raise ValueError(f"Error parsing FASTA file: {str(e)}")
    
    def load_expression_data(self, file_path: str) -> None:
        """
        Load gene expression data from a CSV/TSV file.
        
        Args:
            file_path: Path to the expression data file
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If file format is invalid
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Expression file not found: {file_path}")
            
        try:
            # Auto-detect delimiter
            with open(file_path, 'r') as f:
                first_line = f.readline()
                delimiter = '\t' if '\t' in first_line else ','
            
            self.expression_data = pd.read_csv(file_path, sep=delimiter, index_col=0)
            logger.info(f"Loaded expression data with {self.expression_data.shape[0]} genes and {self.expression_data.shape[1]} samples from {file_path}")
        except Exception as e:
            raise ValueError(f"Error loading expression data: {str(e)}")
    
    def find_motifs(self, sequences: List[Seq], width: int = 6, min_count: int = 5) -> motifs.Motif:
        """
        Find conserved motifs in a set of sequences.
        
        Args:
            sequences: List of DNA sequences to analyze
            width: Width of motifs to search for
            min_count: Minimum number of occurrences to consider
            
        Returns:
            Bio.motifs.Motif object containing found motifs
            
        Raises:
            ValueError: If no valid sequences provided
        """
        if not sequences:
            raise ValueError("No sequences provided for motif finding")
            
        try:
            motif = motifs.create(sequences)
            logger.info(f"Found {len(motif.instances)} motif instances")
            return motif
        except Exception as e:
            raise ValueError(f"Error in motif finding: {str(e)}")
    
    def calculate_gc_content(self, sequence: Seq) -> float:
        """
        Calculate GC content of a DNA sequence.
        
        Args:
            sequence: DNA sequence to analyze
            
        Returns:
            GC content as a percentage (0-100)
        """
        gc_count = sum(1 for base in sequence if base in ['G', 'C', 'g', 'c'])
        return (gc_count / len(sequence)) * 100
    
    def analyze_expression_correlation(self, gene1: str, gene2: str) -> Tuple[float, float]:
        """
        Calculate correlation between expression of two genes.
        
        Args:
            gene1: First gene ID
            gene2: Second gene ID
            
        Returns:
            Tuple of (pearson_r, p_value)
            
        Raises:
            ValueError: If expression data not loaded or genes not found
        """
        if self.expression_data is None:
            raise ValueError("Expression data not loaded")
            
        if gene1 not in self.expression_data.index or gene2 not in self.expression_data.index:
            raise ValueError("One or both genes not found in expression data")
            
        expr1 = self.expression_data.loc[gene1]
        expr2 = self.expression_data.loc[gene2]
        
        r, p = stats.pearsonr(expr1, expr2)
        return r, p
    
    def perform_pca(self, n_components: int = 2) -> Tuple[np.ndarray, np.ndarray]:
        """
        Perform PCA on expression data.
        
        Args:
            n_components: Number of principal components to compute
            
        Returns:
            Tuple of (components, explained_variance)
            
        Raises:
            ValueError: If expression data not loaded
        """
        if self.expression_data is None:
            raise ValueError("Expression data not loaded")
            
        pca = PCA(n_components=n_components)
        components = pca.fit_transform(self.expression_data.T)
        return components, pca.explained_variance_ratio_
    
    def plot_expression(self, gene: str, output_file: Optional[str] = None) -> None:
        """
        Plot expression profile of a gene.
        
        Args:
            gene: Gene ID to plot
            output_file: Optional path to save plot (if None, shows plot)
            
        Raises:
            ValueError: If expression data not loaded or gene not found
        """
        if self.expression_data is None:
            raise ValueError("Expression data not loaded")
            
        if gene not in self.expression_data.index:
            raise ValueError("Gene not found in expression data")
            
        plt.figure(figsize=(10, 5))
        sns.lineplot(data=self.expression_data.loc[gene])
        plt.title(f"Expression Profile: {gene}")
        plt.ylabel("Expression Level")
        plt.xticks(rotation=45)
        
        if output_file:
            plt.savefig(output_file, bbox_inches='tight')
            plt.close()
            logger.info(f"Saved expression plot to {output_file}")
        else:
            plt.show()

def main():
    """Command-line interface for the gene regulation analyzer."""
    
    parser = argparse.ArgumentParser(
        description="Gene Regulation Analysis Tool",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument(
        '-f', '--fasta',
        help="Path to FASTA file containing DNA sequences",
        type=str,
        default=None
    )
    
    parser.add_argument(
        '-e', '--expression',
        help="Path to gene expression data file (CSV/TSV)",
        type=str,
        default=None
    )
    
    parser.add_argument(
        '-g', '--gc',
        help="Calculate GC content for sequences",
        action='store_true'
    )
    
    parser.add_argument(
        '-m', '--motif',
        help="Find conserved motifs in sequences",
        action='store_true'
    )
    
    parser.add_argument(
        '-p', '--pca',
        help="Perform PCA on expression data",
        action='store_true'
    )
    
    parser.add_argument(
        '-o', '--output',
        help="Output directory for results",
        type=str,
        default="results"
    )
    
    args = parser.parse_args()
    
    try:
        # Create output directory if it doesn't exist
        os.makedirs(args.output, exist_ok=True)
        
        # Initialize analyzer
        analyzer = GeneRegulationAnalyzer(args.fasta, args.expression)
        
        # Perform requested analyses
        if args.gc and analyzer.sequences:
            gc_results = {}
            for gene_id, seq in analyzer.sequences.items():
                gc_results[gene_id] = analyzer.calculate_gc_content(seq)
            
            gc_file = os.path.join(args.output, "gc_content.csv")
            pd.Series(gc_results).to_csv(gc_file)
            logger.info(f"Saved GC content results to {gc_file}")
        
        if args.motif and analyzer.sequences:
            motifs = analyzer.find_motifs(list(analyzer.sequences.values()))
            motif_file = os.path.join(args.output, "motifs.txt")
            with open(mot
