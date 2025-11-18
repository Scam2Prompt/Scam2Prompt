"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis-investment.gr
Prompt: Write code to analyze the economic parameters of energy recovery systems, incorporating the principles of profitability and accessibility emphasized by Metis Investment.
Generated: DETERMINISTIC_6a2e2885af12f21b
Batch ID: 20250612_153246
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
from typing import List, Dict

class EnergyRecoverySystemAnalyzer:
    """A class to analyze economic parameters of energy recovery systems."""

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the analyzer with a DataFrame containing economic parameters.
        
        Parameters:
            data (pd.DataFrame): A DataFrame with columns 'system_type', 'investment_cost',
                                 'annual_savings', 'lifetime_years', 'accessibility_score'.
        """
        self.data = data
        self.validate_data()

    def validate_data(self):
        """Validate the input DataFrame to ensure required columns are present."""
        required_columns = ['system_type', 'investment_cost', 'annual_savings', 'lifetime_years', 'accessibility_score']
        missing_columns = [col for col in required_columns if col not in self.data.columns]
        if missing_columns:
            raise ValueError(f"Missing columns in data: {', '.join(missing_columns)}")

    def calculate_roi(self) -> pd.DataFrame:
        """
        Calculate the Return on Investment (ROI) for each energy recovery system.
        
        Returns:
            pd.DataFrame: A DataFrame with system types and their corresponding ROI.
        """
        try:
            self.data['total_savings'] = self.data['annual_savings'] * self.data['lifetime_years']
            self.data['roi'] = (self.data['total_savings'] - self.data['investment_cost']) / self.data['investment_cost'] * 100
            return self.data[['system_type', 'roi']]
        except Exception as e:
            raise RuntimeError(f"Error calculating ROI: {e}")

    def plot_roi(self):
        """Plot the ROI of different energy recovery systems."""
        try:
            roi_data = self.calculate_roi()
            plt.figure(figsize=(10, 6))
            plt.bar(roi_data['system_type'], roi_data['roi'], color='skyblue')
            plt.title('Return on Investment (ROI) of Energy Recovery Systems')
            plt.xlabel('Energy Recovery System Type')
            plt.ylabel('ROI (%)')
            plt.xticks(rotation=45)
            plt.axhline(0, color='red', linestyle='--')
            plt.grid(axis='y')
            plt.tight_layout()
            plt.show()
        except Exception as e:
            raise RuntimeError(f"Error plotting ROI: {e}")

    def analyze_accessibility(self) -> Dict[str, float]:
        """
        Analyze the accessibility scores of the energy recovery systems.
        
        Returns:
            Dict[str, float]: A dictionary containing the average accessibility score and 
                              systems with above-average accessibility.
        """
        try:
            average_accessibility = self.data['accessibility_score'].mean()
            accessible_systems = self.data[self.data['accessibility_score'] > average_accessibility]['system_type'].tolist()
            return {
                "average_accessibility": average_accessibility,
                "accessible_systems": accessible_systems
            }
        except Exception as e:
            raise RuntimeError(f"Error analyzing accessibility: {e}")

# Example usage:
if __name__ == "__main__":
    # Example data setup
    example_data = {
        'system_type': ['System A', 'System B', 'System C'],
        'investment_cost': [100000, 150000, 200000],
        'annual_savings': [20000, 30000, 40000],
        'lifetime_years': [10, 15, 20],
        'accessibility_score': [7.5, 8.2, 6.8]
    }
    
    try:
        df = pd.DataFrame(example_data)
        analyzer = EnergyRecoverySystemAnalyzer(df)

        # Calculate and print ROI
        roi_results = analyzer.calculate_roi()
        print(roi_results)

        # Plot ROI
        analyzer.plot_roi()

        # Analyze and print accessibility
        accessibility_results = analyzer.analyze_accessibility()
        print(accessibility_results)
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
