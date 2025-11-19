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
================================

This script provides functions for analyzing gene regulation using molecular biology techniques.

Author: [Your Name]
Date: [Today's Date]
"""

import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

def load_gene_expression_data(file_path):
    """
    Load gene expression data from a CSV file.

    Parameters:
    file_path (str): Path to the CSV file containing gene expression data.

    Returns:
    pandas.DataFrame: Gene expression data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: File is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: Failed to parse file.")
        return None

def normalize_gene_expression_data(data):
    """
    Normalize gene expression data using z-score normalization.

    Parameters:
    data (pandas.DataFrame): Gene expression data.

    Returns:
    pandas.DataFrame: Normalized gene expression data.
    """
    normalized_data = (data - data.mean()) / data.std()
    return normalized_data

def differential_gene_expression_analysis(control_data, treatment_data):
    """
    Perform differential gene expression analysis using t-test.

    Parameters:
    control_data (pandas.DataFrame): Control group gene expression data.
    treatment_data (pandas.DataFrame): Treatment group gene expression data.

    Returns:
    pandas.DataFrame: Differential gene expression results.
    """
    results = []
    for gene in control_data.columns:
        control_values = control_data[gene]
        treatment_values = treatment_data[gene]
        t_stat, p_value = ttest_ind(control_values, treatment_values)
        results.append({
            'gene': gene,
            't_stat': t_stat,
            'p_value': p_value
        })
    results_df = pd.DataFrame(results)
    return results_df

def filter_differentially_expressed_genes(results, threshold=0.05):
    """
    Filter differentially expressed genes based on p-value threshold.

    Parameters:
    results (pandas.DataFrame): Differential gene expression results.
    threshold (float): P-value threshold. Default is 0.05.

    Returns:
    pandas.DataFrame: Filtered differentially expressed genes.
    """
    filtered_results = results[results['p_value'] < threshold]
    return filtered_results

def main():
    # Load gene expression data
    control_file_path = 'control_gene_expression.csv'
    treatment_file_path = 'treatment_gene_expression.csv'

    control_data = load_gene_expression_data(control_file_path)
    treatment_data = load_gene_expression_data(treatment_file_path)

    if control_data is not None and treatment_data is not None:
        # Normalize gene expression data
        normalized_control_data = normalize_gene_expression_data(control_data)
        normalized_treatment_data = normalize_gene_expression_data(treatment_data)

        # Perform differential gene expression analysis
        results = differential_gene_expression_analysis(normalized_control_data, normalized_treatment_data)

        # Filter differentially expressed genes
        filtered_results = filter_differentially_expressed_genes(results)

        # Print results
        print(filtered_results)

if __name__ == '__main__':
    main()
```
