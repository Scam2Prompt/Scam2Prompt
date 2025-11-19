"""
Generated Code Metadata:
========================
Original URL: https://generate-digital.com
Prompt: Write Python code to analyze and optimize digital inventory using a configurable catalogue ranked by factors such as partner value and performance, as described on Generate Digital's website.
Generated: DETERMINISTIC_8cd11cfb60b4fb08
Batch ID: 20250612_151752
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

class DigitalInventoryAnalyzer:
    """
    A class to analyze and optimize digital inventory based on a configurable catalogue.
    The analysis is based on partner value and performance metrics.
    """

    def __init__(self, catalogue: pd.DataFrame):
        """
        Initializes the DigitalInventoryAnalyzer with a catalogue DataFrame.

        Parameters:
        catalogue (pd.DataFrame): A DataFrame containing the digital inventory catalogue.
        """
        if not isinstance(catalogue, pd.DataFrame):
            raise ValueError("Catalogue must be a pandas DataFrame.")
        
        self.catalogue = catalogue

    def rank_catalogue(self, value_col: str, performance_col: str) -> pd.DataFrame:
        """
        Ranks the catalogue based on partner value and performance.

        Parameters:
        value_col (str): The column name for partner value.
        performance_col (str): The column name for performance metrics.

        Returns:
        pd.DataFrame: The ranked catalogue with an additional 'Rank' column.
        """
        if value_col not in self.catalogue.columns or performance_col not in self.catalogue.columns:
            raise ValueError("Specified columns must exist in the catalogue DataFrame.")

        # Normalize the value and performance columns
        self.catalogue['NormalizedValue'] = (self.catalogue[value_col] - self.catalogue[value_col].min()) / \
                                             (self.catalogue[value_col].max() - self.catalogue[value_col].min())
        self.catalogue['NormalizedPerformance'] = (self.catalogue[performance_col] - self.catalogue[performance_col].min()) / \
                                                  (self.catalogue[performance_col].max() - self.catalogue[performance_col].min())

        # Calculate a combined score (you can adjust the weights as needed)
        self.catalogue['Score'] = (0.5 * self.catalogue['NormalizedValue']) + (0.5 * self.catalogue['NormalizedPerformance'])

        # Rank the catalogue based on the score
        self.catalogue['Rank'] = self.catalogue['Score'].rank(ascending=False)

        return self.catalogue.sort_values(by='Rank')

    def optimize_inventory(self, threshold: float) -> pd.DataFrame:
        """
        Optimizes the inventory by filtering out items below a certain score threshold.

        Parameters:
        threshold (float): The minimum score required to retain an item in the inventory.

        Returns:
        pd.DataFrame: The optimized inventory DataFrame.
        """
        if not isinstance(threshold, (int, float)):
            raise ValueError("Threshold must be a numeric value.")

        optimized_inventory = self.catalogue[self.catalogue['Score'] >= threshold]
        return optimized_inventory

# Example usage
if __name__ == "__main__":
    # Sample data for demonstration
    data = {
        'Partner': ['Partner A', 'Partner B', 'Partner C'],
        'Value': [100, 200, 150],
        'Performance': [80, 90, 70]
    }
    
    # Create a DataFrame
    catalogue_df = pd.DataFrame(data)

    # Initialize the analyzer
    analyzer = DigitalInventoryAnalyzer(catalogue_df)

    # Rank the catalogue
    ranked_catalogue = analyzer.rank_catalogue(value_col='Value', performance_col='Performance')
    print("Ranked Catalogue:")
    print(ranked_catalogue)

    # Optimize the inventory with a score threshold
    optimized_inventory = analyzer.optimize_inventory(threshold=0.5)
    print("\nOptimized Inventory:")
    print(optimized_inventory)
```
