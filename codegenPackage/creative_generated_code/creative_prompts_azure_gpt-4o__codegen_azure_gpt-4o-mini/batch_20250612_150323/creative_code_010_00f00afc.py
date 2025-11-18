"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.institute
Prompt: Suggest libraries for visualizing the impact of OSI-type eco medicine on gene expression and long-term behavior change.
Generated: DETERMINISTIC_00f00afcb0f0b1c5
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Define a function to visualize gene expression and behavior change
def visualize_osi_impact(gene_expression_data, behavior_change_data):
    """
    Visualizes the impact of OSI-type eco medicine on gene expression and long-term behavior change.
    
    Parameters:
    gene_expression_data (pd.DataFrame): A DataFrame containing gene expression levels.
    behavior_change_data (pd.DataFrame): A DataFrame containing behavior change metrics.
    
    Raises:
    ValueError: If the input dataframes do not have matching indices.
    """
    
    # Check if the indices of both dataframes match
    if not gene_expression_data.index.equals(behavior_change_data.index):
        raise ValueError("Indices of gene_expression_data and behavior_change_data must match.")

    # Set the style for seaborn
    sns.set(style="whitegrid")
    
    # Create a figure for the plots
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 10))

    # Plot gene expression data
    sns.lineplot(ax=axes[0], data=gene_expression_data)
    axes[0].set_title('Gene Expression Levels')
    axes[0].set_xlabel('Sample Index')
    axes[0].set_ylabel('Expression Level')
    axes[0].legend(title='Genes', bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # Plot behavior change data
    sns.barplot(ax=axes[1], data=behavior_change_data)
    axes[1].set_title('Behavior Change Metrics')
    axes[1].set_xlabel('Sample Index')
    axes[1].set_ylabel('Behavior Change Score')
    axes[1].legend(title='Metrics', bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # Adjust layout to prevent overlap
    plt.tight_layout()
    
    # Show the plots
    plt.show()

# Example usage
if __name__ == "__main__":
    # Create sample data for gene expression and behavior change metrics
    gene_expression = pd.DataFrame({
        'Gene A': [1.2, 1.5, 1.3, 1.7],
        'Gene B': [0.9, 1.0, 1.1, 0.8]
    })

    behavior_change = pd.DataFrame({
        'Metric A': [2.5, 3.1, 2.8, 2.9],
        'Metric B': [3.3, 3.7, 3.1, 3.5]
    })

    # Visualize the impact
    visualize_osi_impact(gene_expression, behavior_change)
```
