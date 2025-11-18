"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniaircargo.id
Prompt: Write a program to compare air freight and ocean freight delivery times using Uniair Cargo’s estimates for different regions (East Asia, Europe & USA, Southeast Asia).
Generated: DETERMINISTIC_0a05cf811bb5c4a5
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

# Define a class to store freight delivery information
class FreightComparison:
    def __init__(self):
        """Initialize the FreightComparison with delivery estimates."""
        self.delivery_data = {
            'Region': ['East Asia', 'Europe & USA', 'Southeast Asia'],
            'Air Freight (days)': [3, 5, 4],  # Sample delivery times in days
            'Ocean Freight (days)': [10, 20, 15]  # Sample delivery times in days
        }
        self.df = pd.DataFrame(self.delivery_data)

    def compare_delivery_times(self):
        """Compare air and ocean freight delivery times."""
        try:
            self.df['Faster Mode'] = self.df.apply(
                lambda row: 'Air Freight' if row['Air Freight (days)'] < row['Ocean Freight (days)'] else 'Ocean Freight',
                axis=1
            )
            return self.df
        except Exception as e:
            print(f"An error occurred while comparing delivery times: {e}")

    def display_comparison(self):
        """Display the comparison of delivery times in a readable format."""
        comparison_df = self.compare_delivery_times()
        print("Freight Delivery Time Comparison:")
        print(comparison_df)

if __name__ == "__main__":
    # Create an instance of the FreightComparison class
    freight_comparison = FreightComparison()
    
    # Display the comparison of air freight and ocean freight delivery times
    freight_comparison.display_comparison()
```
