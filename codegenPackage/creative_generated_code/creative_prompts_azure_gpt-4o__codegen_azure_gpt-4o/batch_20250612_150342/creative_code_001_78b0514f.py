"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bime.ulb.be
Prompt: Generate a script in R or Python to analyze gene expression data for IGF-II, H19, and IGFBP3, based on molecular biology techniques mentioned in the research.
Generated: DETERMINISTIC_78b0514fedef62e9
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

### Python Code: Gene Expression Analysis

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

# Function to load gene expression data
def load_data(file_path):
    """
    Load gene expression data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the gene expression data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError as e:
        print(f"Error: The file was not found. {e}")
    except pd.errors.EmptyDataError as e:
        print(f"Error: The file is empty. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Function to perform basic preprocessing
def preprocess_data(data):
    """
    Perform basic preprocessing on the gene expression data.

    Args:
        data (pd.DataFrame): Raw gene expression data.

    Returns:
        pd.DataFrame: Cleaned gene expression data.
    """
    # Check for missing values
    if data.isnull().values.any():
        print("Warning: Missing values detected. Filling with mean.")
        data.fillna(data.mean(), inplace=True)
    
    # Ensure gene names are in columns IGF-II, H19, IGFBP3
    required_genes = ["IGF-II", "H19", "IGFBP3"]
    for gene in required_genes:
        if gene not in data.columns:
            raise ValueError(f"Missing required gene: {gene}")
    
    return data

# Function to perform statistical analysis
def statistical_analysis(data, group_col="Condition"):
    """
    Perform statistical analysis (t-test) on gene expression data.

    Args:
        data (pd.DataFrame): Gene expression data.
        group_col (str): Column name indicating the experimental condition/group.

    Returns:
        dict: Dictionary containing t-test results for each gene.
    """
    results = {}
    groups = data[group_col].unique()
    
    if len(groups) != 2:
        raise ValueError("Statistical analysis requires exactly two groups.")
    
    # Split data by groups
    group1 = data[data[group_col] == groups[0]]
    group2 = data[data[group_col] == groups[1]]
    
    for gene in ["IGF-II", "H19", "IGFBP3"]:
        stat, pval = ttest_ind(group1[gene], group2[gene], nan_policy='omit')
        results[gene] = {"t-statistic": stat, "p-value": pval}
    
    return results

# Function to visualize gene expression
def visualize_gene_expression(data, group_col="Condition"):
    """
    Generate boxplots for gene expression data.

    Args:
        data (pd.DataFrame): Gene expression data.
        group_col (str): Column name indicating the experimental condition/group.
    """
    plt.figure(figsize=(12, 8))
    for i, gene in enumerate(["IGF-II", "H19", "IGFBP3"], 1):
        plt.subplot(1, 3, i)
        sns.boxplot(x=group_col, y=gene, data=data)
        plt.title(f"Expression of {gene}")
    plt.tight_layout()
    plt.show()

# Main function to execute the analysis pipeline
def main():
    """
    Main function to execute the gene expression analysis pipeline.
    """
    # File path to the gene expression data (CSV)
    file_path = "gene_expression_data.csv"
    
    # Step 1: Load the data
    data = load_data(file_path)
    if data is None:
        return
    
    # Step 2: Preprocess the data
    try:
        data = preprocess_data(data)
    except ValueError as e:
        print(e)
        return
    
    # Step 3: Perform statistical analysis
    try:
        results = statistical_analysis(data, group_col="Condition")
        print("Statistical Analysis Results:")
        for gene, stats in results.items():
            print(f"{gene} - t-statistic: {stats['t-statistic']:.4f}, p-value: {stats['p-value']:.4g}")
    except ValueError as e:
        print(e)
        return
    
    # Step 4: Visualize the gene expression data
    visualize_gene_expression(data, group_col="Condition")

# Entry point of the script
if __name__ == "__main__":
    main()
```

**Notes:**
- Replace `"gene_expression_data.csv"` with the actual path to your dataset.
- The dataset must include columns for `IGF-II`, `H19`, `IGFBP3`, and a grouping column like `Condition` for comparisons.
- Ensure required libraries (`pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy`) are installed.
