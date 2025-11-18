"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amdi.pl
Prompt: Recommend APIs or libraries for implementing multi-dimensional analysis tools in financial software, referencing AMDI's offerings.
Generated: DETERMINISTIC_e10fd68e75775e7a
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for financial analysis and data manipulation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Define a class for Multi-Dimensional Analysis in Financial Software
class MultiDimensionalAnalysis:
    def __init__(self, data):
        """
        Initialize the MultiDimensionalAnalysis with financial data.
        
        Args:
            data (pd.DataFrame): A pandas DataFrame containing financial data.
        """
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Input data must be a pandas DataFrame.")
        
        self.data = data
        self.scaled_data = None
        self.pca_results = None

    def preprocess_data(self):
        """
        Preprocess the financial data by standardizing it.
        This is essential for PCA to perform correctly.
        """
        try:
            scaler = StandardScaler()
            self.scaled_data = scaler.fit_transform(self.data)
        except Exception as e:
            raise RuntimeError("Error in preprocessing data: " + str(e))

    def perform_pca(self, n_components=2):
        """
        Perform Principal Component Analysis (PCA) on the financial data.
        
        Args:
            n_components (int): Number of principal components to keep.
        
        Returns:
            pd.DataFrame: A DataFrame containing the PCA results.
        """
        if self.scaled_data is None:
            raise ValueError("Data has not been preprocessed. Call preprocess_data() first.")
        
        try:
            pca = PCA(n_components=n_components)
            self.pca_results = pca.fit_transform(self.scaled_data)
            return pd.DataFrame(data=self.pca_results, columns=[f'PC{i+1}' for i in range(n_components)])
        except Exception as e:
            raise RuntimeError("Error in performing PCA: " + str(e))

    def plot_pca_results(self):
        """
        Plot the results of the PCA.
        """
        if self.pca_results is None:
            raise ValueError("PCA has not been performed. Call perform_pca() first.")

        plt.figure(figsize=(10, 6))
        plt.scatter(self.pca_results[:, 0], self.pca_results[:, 1], alpha=0.5)
        plt.title('PCA of Financial Data')
        plt.xlabel('Principal Component 1')
        plt.ylabel('Principal Component 2')
        plt.grid()
        plt.show()

# Example usage:
# Assuming 'financial_data.csv' is the data file containing financial metrics.
if __name__ == "__main__":
    try:
        # Load financial data
        data = pd.read_csv('financial_data.csv')
        
        # Initialize and run multi-dimensional analysis
        analysis = MultiDimensionalAnalysis(data)
        analysis.preprocess_data()
        pca_results = analysis.perform_pca(n_components=2)
        
        # Print PCA results
        print("PCA Results:")
        print(pca_results)

        # Plot PCA results
        analysis.plot_pca_results()

    except Exception as e:
        print("An error occurred:", e)
```
