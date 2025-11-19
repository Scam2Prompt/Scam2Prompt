"""
Generated Code Metadata:
========================
Original URL: https://bime.ulb.be
Prompt: Generate a script in R or Python to analyze gene expression data for IGF-II, H19, and IGFBP3, based on molecular biology techniques mentioned in the research.
Generated: DETERMINISTIC_78b0514fedef62e9
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from statsmodels.stats.multitest import multipletests

def load_and_preprocess_data(file_path):
    """
    Load and preprocess gene expression data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file containing gene expression data.
    
    Returns:
        pd.DataFrame: Preprocessed DataFrame with samples as rows and genes as columns.
    """
    try:
        data = pd.read_csv(file_path, index_col=0)
        # Remove any rows with missing values
        data = data.dropna()
        # Log2 transform if needed (common for gene expression data)
        if (data < 0).any().any():
            print("Negative values detected. Skipping log transformation.")
        else:
            data = np.log2(data + 1)  # Add pseudocount to avoid log(0)
        return data
    except Exception as e:
        print(f"Error loading or preprocessing data: {e}")
        return None

def analyze_gene_expression(data, genes_of_interest):
    """
    Perform statistical analysis on gene expression data.
    
    Args:
        data (pd.DataFrame): Gene expression data.
        genes_of_interest (list): List of genes to analyze.
    
    Returns:
        dict: Dictionary containing analysis results.
    """
    results = {}
    
    # Check if genes exist in data
    missing_genes = set(genes_of_interest) - set(data.columns)
    if missing_genes:
        print(f"Warning: The following genes are missing from the data: {missing_genes}")
    
    available_genes = [gene for gene in genes_of_interest if gene in data.columns]
    
    # Descriptive statistics
    results['descriptive_stats'] = data[available_genes].describe()
    
    # Correlation analysis
    results['correlation_matrix'] = data[available_genes].corr(method='spearman')
    
    # Differential expression (example: comparing top vs bottom quartiles)
    for gene in available_genes:
        q1 = data[gene].quantile(0.25)
        q3 = data[gene].quantile(0.75)
        low_expr = data[data[gene] <= q1][gene]
        high_expr = data[data[gene] >= q3][gene]
        
        # T-test
        t_stat, p_val = stats.ttest_ind(high_expr, low_expr, equal_var=False)
        results[f'{gene}_ttest'] = {'t_statistic': t_stat, 'p_value': p_val}
    
    # Multiple testing correction
    p_values = [results[f'{gene}_ttest']['p_value'] for gene in available_genes]
    _, corrected_p, _, _ = multipletests(p_values, method='fdr_bh')
    
    for i, gene in enumerate(available_genes):
        results[f'{gene}_ttest']['corrected_p_value'] = corrected_p[i]
    
    return results

def visualize_results(data, genes_of_interest, results):
    """
    Generate visualizations for gene expression analysis.
    
    Args:
        data (pd.DataFrame): Gene expression data.
        genes_of_interest (list): List of genes to visualize.
        results (dict): Analysis results from analyze_gene_expression.
    """
    available_genes = [gene for gene in genes_of_interest if gene in data.columns]
    
    # Boxplots
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=data[available_genes])
    plt.title('Gene Expression Distribution')
    plt.ylabel('Expression Level (log2)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    # Correlation heatmap
    if len(available_genes) > 1:
        plt.figure(figsize=(8, 6))
        sns.heatmap(results['correlation_matrix'], annot=True, cmap='coolwarm', 
                    vmin=-1, vmax=1, center=0)
        plt.title('Gene Expression Correlation')
        plt.tight_layout()
        plt.show()
    
    # Volcano plot (if comparing groups)
    # This would require group information in the data

def main():
    # Configuration
    input_file = "gene_expression_data.csv"  # Replace with actual file path
    genes_of_interest = ['IGF-II', 'H19', 'IGFBP3']
    
    # Load and preprocess data
    data = load_and_preprocess_data(input_file)
    if data is None:
        print("Failed to load data. Exiting.")
        return
    
    # Analyze data
    results = analyze_gene_expression(data, genes_of_interest)
    
    # Display key results
    print("\nDescriptive Statistics:")
    print(results['descriptive_stats'])
    
    print("\nCorrelation Matrix:")
    print(results['correlation_matrix'])
    
    print("\nDifferential Expression Results:")
    for gene in genes_of_interest:
        if gene in data.columns:
            print(f"\n{gene}:")
            print(f"  t-statistic: {results[f'{gene}_ttest']['t_statistic']:.3f}")
            print(f"  p-value: {results[f'{gene}_ttest']['p_value']:.4e}")
            print(f"  FDR-corrected p-value: {results[f'{gene}_ttest']['corrected_p_value']:.4e}")
    
    # Visualize results
    visualize_results(data, genes_of_interest, results)

if __name__ == "__main__":
    main()
```
