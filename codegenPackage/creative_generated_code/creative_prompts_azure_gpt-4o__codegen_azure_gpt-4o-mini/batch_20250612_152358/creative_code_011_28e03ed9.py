"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lite-trades.org
Prompt: Write code to analyze the performance of multi-family, office, retail, and hospitality real estate investments, based on Lite Trade's real estate management offerings.
Generated: DETERMINISTIC_28e03ed949dc082c
Batch ID: 20250612_152358
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

class RealEstateAnalyzer:
    """
    A class to analyze the performance of real estate investments in
    multi-family, office, retail, and hospitality sectors.
    """

    def __init__(self, data_frame):
        """
        Initializes the RealEstateAnalyzer with a DataFrame.
        
        Parameters:
            data_frame (pd.DataFrame): A DataFrame containing real estate investment data.
        """
        self.data_frame = data_frame

    def validate_data(self):
        """
        Validates the data for required columns and data types.
        
        Raises:
            ValueError: If required columns are missing or data types are incorrect.
        """
        required_columns = ['Property_Type', 'Investment_Amount', 'Annual_Return', 'Location', 'Occupancy_Rate']
        for column in required_columns:
            if column not in self.data_frame.columns:
                raise ValueError(f'Missing required column: {column}')
        
        if not np.issubdtype(self.data_frame['Investment_Amount'].dtype, np.number):
            raise ValueError('Investment_Amount must be numeric')
        if not np.issubdtype(self.data_frame['Annual_Return'].dtype, np.number):
            raise ValueError('Annual_Return must be numeric')
        if not np.issubdtype(self.data_frame['Occupancy_Rate'].dtype, np.number):
            raise ValueError('Occupancy_Rate must be numeric')

    def calculate_roi(self):
        """
        Calculates Return on Investment (ROI) for each property.
        
        Returns:
            pd.DataFrame: A DataFrame with the original data and an added 'ROI' column.
        """
        self.data_frame['ROI'] = (self.data_frame['Annual_Return'] / self.data_frame['Investment_Amount']) * 100
        return self.data_frame

    def analyze_performance(self):
        """
        Analyzes performance based on property type.
        
        Returns:
            pd.DataFrame: A summary DataFrame with average ROI and occupancy rates by property type.
        """
        performance_summary = self.data_frame.groupby('Property_Type').agg(
            Average_ROI=('ROI', 'mean'),
            Average_Occupancy_Rate=('Occupancy_Rate', 'mean')
        ).reset_index()
        return performance_summary

    def run_analysis(self):
        """
        Executes the validation and analysis steps.
        
        Returns:
            pd.DataFrame: A summary report of the analysis.
        """
        try:
            self.validate_data()
            self.calculate_roi()
            return self.analyze_performance()
        except ValueError as e:
            print(f"Error during analysis: {e}")
            return None

# Example usage:
if __name__ == "__main__":
    # Sample data for demonstration
    data = {
        'Property_Type': ['Multi-Family', 'Office', 'Retail', 'Hospitality', 'Multi-Family'],
        'Investment_Amount': [100000, 200000, 150000, 250000, 120000],
        'Annual_Return': [8000, 15000, 12000, 30000, 9000],
        'Location': ['City A', 'City B', 'City C', 'City D', 'City A'],
        'Occupancy_Rate': [0.95, 0.85, 0.90, 0.80, 0.88]
    }

    # Create DataFrame
    real_estate_data = pd.DataFrame(data)

    # Initialize Analyzer
    analyzer = RealEstateAnalyzer(real_estate_data)

    # Run Analysis
    summary_report = analyzer.run_analysis()

    # Display the results
    if summary_report is not None:
        print(summary_report)
```
