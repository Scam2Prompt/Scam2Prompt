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

# Define a class for analyzing real estate investments
class RealEstateInvestmentAnalysis:
    def __init__(self, data):
        """
        Constructor to initialize the real estate investment data.
        
        :param data: A pandas DataFrame containing real estate performance data.
                     Expected columns: ['Property Type', 'Revenue', 'Expenses', 'Occupancy Rate']
        """
        self.data = data
        self.validate_data()

    def validate_data(self):
        """
        Validates the input data for required columns and data types.
        Raises an exception if validation fails.
        """
        required_columns = ['Property Type', 'Revenue', 'Expenses', 'Occupancy Rate']
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")
        if not all([np.issubdtype(self.data[col].dtype, np.number) for col in ['Revenue', 'Expenses', 'Occupancy Rate']]):
            raise TypeError("Columns 'Revenue', 'Expenses', and 'Occupancy Rate' must be numeric.")

    def calculate_net_income(self):
        """
        Calculates net income (Revenue - Expenses) for each property and adds it as a new column to the data.
        """
        self.data['Net Income'] = self.data['Revenue'] - self.data['Expenses']

    def calculate_roi(self):
        """
        Calculates Return on Investment (ROI) for each property type.
        ROI Formula: (Net Income / Expenses) * 100
        Returns a dictionary of ROI by property type.
        """
        self.calculate_net_income()
        roi_by_type = {}
        grouped_data = self.data.groupby('Property Type')
        for property_type, group in grouped_data:
            total_net_income = group['Net Income'].sum()
            total_expenses = group['Expenses'].sum()
            roi = (total_net_income / total_expenses) * 100 if total_expenses != 0 else 0
            roi_by_type[property_type] = round(roi, 2)
        return roi_by_type

    def average_occupancy_rate(self):
        """
        Calculates the average occupancy rate for each property type.
        Returns a dictionary of average occupancy rates by property type.
        """
        avg_occupancy = self.data.groupby('Property Type')['Occupancy Rate'].mean()
        return avg_occupancy.round(2).to_dict()

    def summarize_performance(self):
        """
        Provides a summary of performance metrics (ROI and average occupancy rate) grouped by property type.
        Returns a summary dictionary.
        """
        roi = self.calculate_roi()
        avg_occupancy = self.average_occupancy_rate()
        summary = {
            property_type: {
                'ROI (%)': roi[property_type],
                'Average Occupancy Rate (%)': avg_occupancy[property_type]
            }
            for property_type in roi.keys()
        }
        return summary


# Example usage
if __name__ == "__main__":
    # Sample data for demonstration
    data = pd.DataFrame({
        'Property Type': ['Multi-Family', 'Office', 'Retail', 'Hospitality', 'Multi-Family', 'Office'],
        'Revenue': [50000, 60000, 40000, 70000, 55000, 62000],
        'Expenses': [20000, 25000, 15000, 30000, 22000, 27000],
        'Occupancy Rate': [95, 88, 92, 80, 96, 89]
    })

    # Create an instance of the analysis class
    analysis = RealEstateInvestmentAnalysis(data)

    # Generate performance summary
    performance_summary = analysis.summarize_performance()

    # Print the summary in a readable format
    print("Real Estate Investment Performance Summary:")
    for property_type, metrics in performance_summary.items():
        print(f"Property Type: {property_type}")
        print(f"  ROI (%): {metrics['ROI (%)']}")
        print(f"  Average Occupancy Rate (%): {metrics['Average Occupancy Rate (%)']}")
        print()
```
