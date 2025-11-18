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

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.formula.api import ols
import statsmodels.api as sm

# Function to read and preprocess gene expression data
def read_and_preprocess_data(file_path):
    """
    Reads gene expression data from a CSV file and preprocesses it.
    
    Parameters:
    file_path (str): Path to the CSV file containing gene expression data.
    
    Returns:
    DataFrame: Preprocessed gene expression data.
    """
    try:
        # Load data into a DataFrame
        data = pd.read_csv(file_path)
        
        # Drop any rows with missing values
        data.dropna(inplace=True)
        
        # Ensure relevant columns are present
        required_columns = ['Sample', 'IGF-II', 'H19', 'IGFBP3']
        if not all(col in data.columns for col in required_columns):
            raise ValueError("Data must contain the following columns: 'Sample', 'IGF-II', 'H19', 'IGFBP3'")
        
        return data
    except Exception as e:
        print(f"Error reading or processing data: {e}")
        raise

# Function to visualize gene expression levels
def plot_gene_expression(data):
    """
    Plots the gene expression levels for IGF-II, H19, and IGFBP3.
    
    Parameters:
    data (DataFrame): DataFrame containing gene expression data.
    """
    try:
        # Set the style for seaborn
        sns.set(style="whitegrid")
        
        # Melt the DataFrame for easier plotting
        melted_data = data.melt(id_vars='Sample', value_vars=['IGF-II', 'H19', 'IGFBP3'],
                                 var_name='Gene', value_name='Expression')
        
        # Create a boxplot for the gene expression data
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='Gene', y='Expression', data=melted_data)
        plt.title('Gene Expression Levels for IGF-II, H19, and IGFBP3')
        plt.xlabel('Gene')
        plt.ylabel('Expression Level')
        plt.show()
    except Exception as e:
        print(f"Error in plotting gene expression: {e}")
        raise

# Function to perform statistical analysis on gene expression data
def perform_statistical_analysis(data):
    """
    Performs ANOVA on gene expression data to compare levels among genes.
    
    Parameters:
    data (DataFrame): DataFrame containing gene expression data.
    
    Returns:
    ANOVA results: ANOVA table from the analysis.
    """
    try:
        # Prepare the data for ANOVA
        melted_data = data.melt(id_vars='Sample', value_vars=['IGF-II', 'H19', 'IGFBP3'],
                                 var_name='Gene', value_name='Expression')
        
        # Fit the model
        model = ols('Expression ~ Gene', data=melted_data).fit()
        
        # Perform ANOVA
        anova_results = sm.stats.anova_lm(model, typ=2)
        
        return anova_results
    except Exception as e:
        print(f"Error in performing statistical analysis: {e}")
        raise

# Main function to execute the analysis workflow
def main(file_path):
    """
    Main function to execute the gene expression analysis workflow.
    
    Parameters:
    file_path (str): Path to the CSV file containing gene expression data.
    """
    try:
        # Read and preprocess the data
        data = read_and_preprocess_data(file_path)
        
        # Visualize gene expression levels
        plot_gene_expression(data)
        
        # Perform statistical analysis
        anova_results = perform_statistical_analysis(data)
        print(anova_results)
    except Exception as e:
        print(f"Error in the main workflow: {e}")

# Example usage (uncomment the line below and provide a valid CSV file path)
# main('gene_expression_data.csv')
```
