"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://generate-digital.com
Prompt: Write Python code to analyze and optimize digital inventory using a configurable catalogue ranked by factors such as partner value and performance, as described on Generate Digital's website.
Generated: DETERMINISTIC_8cd11cfb60b4fb08
Batch ID: 20250612_151752
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

class DigitalInventoryAnalyzer:
    """
    A class to analyze and optimize digital inventory based on partner value and performance.
    """

    def __init__(self, catalogue_df):
        """
        Initializes the DigitalInventoryAnalyzer with a catalogue DataFrame.

        Parameters:
        catalogue_df (pd.DataFrame): A DataFrame containing digital inventory data with 
                                      'partner', 'value', and 'performance' columns.
        """
        self.catalogue_df = catalogue_df
        self.validate_data()

    def validate_data(self):
        """
        Validates the input DataFrame to ensure it contains the necessary columns.
        Raises ValueError if any required column is missing.
        """
        required_columns = ['partner', 'value', 'performance']
        for column in required_columns:
            if column not in self.catalogue_df.columns:
                raise ValueError(f'Missing required column: {column}')

    def rank_catalogue(self):
        """
        Ranks the catalogue based on partner value and performance scores, 
        and returns a sorted DataFrame.

        Returns:
        pd.DataFrame: A DataFrame sorted by the optimization score.
        """
        try:
            # Normalize the 'value' and 'performance' columns
            self.catalogue_df['normalized_value'] = (
                self.catalogue_df['value'] - self.catalogue_df['value'].min()
            ) / (self.catalogue_df['value'].max() - self.catalogue_df['value'].min())
            self.catalogue_df['normalized_performance'] = (
                self.catalogue_df['performance'] - self.catalogue_df['performance'].min()
            ) / (self.catalogue_df['performance'].max() - self.catalogue_df['performance'].min())

            # Calculate an optimization score
            self.catalogue_df['optimization_score'] = (
                self.catalogue_df['normalized_value'] + self.catalogue_df['normalized_performance']
            ) / 2

            # Sort by the optimization score in descending order
            ranked_catalogue = self.catalogue_df.sort_values(
                by='optimization_score', ascending=False
            )

            return ranked_catalogue[['partner', 'value', 'performance', 'optimization_score']]

        except Exception as e:
            raise RuntimeError(f"Error in ranking catalogue: {e}")

    def optimize_inventory(self, threshold=0.5):
        """
        Filters the ranked catalogue to include only those entries above a specified optimization score threshold.

        Parameters:
        threshold (float): The optimization score threshold for filtering.

        Returns:
        pd.DataFrame: A DataFrame containing optimized inventory.
        """
        ranked_catalogue = self.rank_catalogue()
        optimized_inventory = ranked_catalogue[
            ranked_catalogue['optimization_score'] >= threshold
        ]
        return optimized_inventory.reset_index(drop=True)

# Example usage:
if __name__ == "__main__":
    # Sample data to demonstrate functionality
    sample_data = {
        'partner': ['Partner A', 'Partner B', 'Partner C'],
        'value': [100, 200, 150],
        'performance': [80, 90, 85]
    }

    # Create a DataFrame
    catalogue_df = pd.DataFrame(sample_data)
    
    try:
        # Initialize the analyzer
        analyzer = DigitalInventoryAnalyzer(catalogue_df)

        # Get the optimized inventory
        optimized_inventory = analyzer.optimize_inventory(threshold=0.6)

        # Display the optimized inventory
        print(optimized_inventory)

    except Exception as e:
        print(f"An error occurred: {e}")
```
