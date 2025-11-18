"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://publicvibeindia.blogspot.com
Prompt: Develop a script to compare the market share growth of MEXC from 2023 to Q1 2025, using percentage changes provided in the content.
Generated: DETERMINISTIC_394618bc77aecd8d
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt

# Define a class to handle market share calculations
class MarketShareAnalyzer:
    def __init__(self, data):
        """
        Initialize the MarketShareAnalyzer with provided data.

        Parameters:
        data (dict): A dictionary containing market share data.
                     Keys should be '2023' and 'Q1_2025' with respective share values.
        """
        self.data = data
        self.validate_data()

    def validate_data(self):
        """Validate the input data to ensure it contains the necessary keys."""
        required_keys = ['2023', 'Q1_2025']
        for key in required_keys:
            if key not in self.data:
                raise ValueError(f"Missing required data for {key}")

    def calculate_percentage_change(self):
        """
        Calculate the percentage change in market share from 2023 to Q1 2025.

        Returns:
        float: The percentage change in market share.
        """
        initial_value = self.data['2023']
        final_value = self.data['Q1_2025']
        
        if initial_value == 0:
            raise ValueError("Initial market share cannot be zero for percentage calculation.")

        percentage_change = ((final_value - initial_value) / initial_value) * 100
        return percentage_change

    def plot_market_share(self):
        """
        Plot the market share for the years 2023 and Q1 2025.
        """
        years = list(self.data.keys())
        shares = list(self.data.values())

        plt.figure(figsize=(10, 5))
        plt.bar(years, shares, color=['blue', 'orange'])
        plt.title('Market Share Growth of MEXC (2023 to Q1 2025)')
        plt.xlabel('Year')
        plt.ylabel('Market Share (%)')
        plt.ylim(0, max(shares) + 10)
        plt.grid(axis='y')
        plt.show()

# Sample data: market share for 2023 and Q1 2025
market_share_data = {
    '2023': 15.0,   # Example market share in percentage
    'Q1_2025': 25.0 # Example market share in percentage
}

# Execute the analysis
try:
    analyzer = MarketShareAnalyzer(market_share_data)
    percentage_change = analyzer.calculate_percentage_change()
    print(f"Percentage change in market share from 2023 to Q1 2025: {percentage_change:.2f}%")
    analyzer.plot_market_share()
except ValueError as e:
    print(f"Error: {e}")
```
