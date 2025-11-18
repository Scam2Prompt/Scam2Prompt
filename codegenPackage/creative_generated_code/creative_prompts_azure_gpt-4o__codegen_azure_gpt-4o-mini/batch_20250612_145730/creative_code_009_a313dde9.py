"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pdma.io
Prompt: Write Python code to implement a brand strategy analysis tool, incorporating frameworks from PDMA's Brand Strategy course.
Generated: DETERMINISTIC_a313dde95ff12c30
Batch ID: 20250612_145730
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

class BrandStrategyAnalysisTool:
    """
    A class to implement brand strategy analysis using frameworks inspired by PDMA's Brand Strategy course.
    """

    def __init__(self, data):
        """
        Initializes the BrandStrategyAnalysisTool with a dataset.

        Parameters:
        data (pd.DataFrame): A DataFrame containing brand data with necessary attributes.
        """
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Input data must be a pandas DataFrame.")
        self.data = data

    def validate_data(self):
        """
        Validates the input data to ensure it meets the required structure.
        Raises ValueError if validation fails.
        """
        required_columns = ['Brand', 'Market Share', 'Customer Satisfaction', 'Brand Loyalty']

        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")
        
        if self.data.isnull().values.any():
            raise ValueError("Data contains null values. Please clean the data before analysis.")

    def calculate_brand_strength(self):
        """
        Calculates a brand strength score based on market share, customer satisfaction, and brand loyalty.
        
        Returns:
        pd.DataFrame: DataFrame with an additional 'Brand Strength' column.
        """
        self.validate_data()

        # Normalizing the values for scoring
        self.data['Market Share'] = self.data['Market Share'] / self.data['Market Share'].max()
        self.data['Customer Satisfaction'] = self.data['Customer Satisfaction'] / self.data['Customer Satisfaction'].max()
        self.data['Brand Loyalty'] = self.data['Brand Loyalty'] / self.data['Brand Loyalty'].max()

        # Calculate brand strength as a weighted sum of normalized scores
        self.data['Brand Strength'] = (
            0.4 * self.data['Market Share'] +
            0.4 * self.data['Customer Satisfaction'] +
            0.2 * self.data['Brand Loyalty']
        )

        return self.data[['Brand', 'Brand Strength']]

    def generate_summary(self):
        """
        Generates a summary of brand analysis including average scores and top brands.
        
        Returns:
        dict: Summary statistics of brand performance.
        """
        summary = {
            'Average Market Share': self.data['Market Share'].mean(),
            'Average Customer Satisfaction': self.data['Customer Satisfaction'].mean(),
            'Average Brand Loyalty': self.data['Brand Loyalty'].mean(),
            'Top Brand': self.data.loc[self.data['Brand Strength'].idxmax(), 'Brand'],
            'Top Brand Strength': self.data['Brand Strength'].max()
        }
        return summary

    def plot_brand_strength(self):
        """
        Plots the brand strength of each brand in the dataset.
        """
        try:
            import matplotlib.pyplot as plt
            
            plt.figure(figsize=(10, 6))
            plt.barh(self.data['Brand'], self.data['Brand Strength'], color='skyblue')
            plt.xlabel('Brand Strength')
            plt.title('Brand Strength Analysis')
            plt.grid(axis='x')
            plt.show()
        except ImportError:
            print("Matplotlib is not installed. Please install it to use this feature.")

# Example usage:
if __name__ == "__main__":
    # Sample data for demonstration
    sample_data = {
        'Brand': ['Brand A', 'Brand B', 'Brand C'],
        'Market Share': [20, 35, 15],
        'Customer Satisfaction': [4.5, 4.0, 3.8],
        'Brand Loyalty': [80, 60, 70]
    }

    # Create DataFrame
    df = pd.DataFrame(sample_data)

    # Initialize the analysis tool
    analysis_tool = BrandStrategyAnalysisTool(df)

    # Perform analysis
    brand_strength_df = analysis_tool.calculate_brand_strength()
    print(brand_strength_df)

    summary = analysis_tool.generate_summary()
    print(summary)

    # Plot the brand strength
    analysis_tool.plot_brand_strength()
```
