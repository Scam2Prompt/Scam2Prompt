"""
Generated Code Metadata:
========================
Original URL: https://uniaircargo.id
Prompt: Write a program to compare air freight and ocean freight delivery times using Uniair Cargo’s estimates for different regions (East Asia, Europe & USA, Southeast Asia).
Generated: DETERMINISTIC_0a05cf811bb5c4a5
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class FreightComparison:
    """
    A class to compare air freight and ocean freight delivery times for different regions.
    """

    def __init__(self, air_freight_data, ocean_freight_data):
        """
        Initializes the FreightComparison with air and ocean freight data.

        :param air_freight_data: A dictionary containing air freight delivery times.
        :param ocean_freight_data: A dictionary containing ocean freight delivery times.
        """
        self.air_freight_data = air_freight_data
        self.ocean_freight_data = ocean_freight_data

    def compare_delivery_times(self):
        """
        Compares air and ocean freight delivery times and returns a DataFrame with the results.

        :return: A pandas DataFrame containing the comparison of delivery times.
        """
        # Create a DataFrame from the air freight data
        air_df = pd.DataFrame(self.air_freight_data, index=['Air Freight'])
        
        # Create a DataFrame from the ocean freight data
        ocean_df = pd.DataFrame(self.ocean_freight_data, index=['Ocean Freight'])
        
        # Concatenate both DataFrames
        comparison_df = pd.concat([air_df, ocean_df])
        
        return comparison_df

    def display_comparison(self):
        """
        Displays the comparison of delivery times in a readable format.
        """
        try:
            comparison_df = self.compare_delivery_times()
            print("Delivery Time Comparison (in days):")
            print(comparison_df)
        except Exception as e:
            print(f"An error occurred while displaying the comparison: {e}")

# Sample data for air and ocean freight delivery times (in days)
air_freight_estimates = {
    'East Asia': 3,
    'Europe & USA': 5,
    'Southeast Asia': 4
}

ocean_freight_estimates = {
    'East Asia': 10,
    'Europe & USA': 20,
    'Southeast Asia': 15
}

if __name__ == "__main__":
    # Create an instance of FreightComparison
    freight_comparison = FreightComparison(air_freight_estimates, ocean_freight_estimates)
    
    # Display the comparison of delivery times
    freight_comparison.display_comparison()
```
