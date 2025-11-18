"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cosmicrewards.com
Prompt: Write a script to analyze monthly install growth (e.g., 300%+ MoM growth) for a rewards-based gaming app like Cosmic Rewards.
Generated: DETERMINISTIC_481ebd493b039738
Batch ID: 20250612_151445
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

class InstallGrowthAnalyzer:
    def __init__(self, data):
        """
        Initializes the InstallGrowthAnalyzer with monthly install data.

        :param data: A dictionary containing month and install counts.
                     e.g., {'January': 100, 'February': 400, ...}
        """
        self.data = pd.Series(data)
        self.monthly_growth = None

    def calculate_growth(self):
        """
        Calculates the month-over-month growth percentages.

        :returns: A pandas Series containing the growth rates.
        """
        try:
            # Calculate the percentage change to get growth rates
            self.monthly_growth = self.data.pct_change() * 100
            return self.monthly_growth
        except Exception as e:
            print(f"Error calculating growth: {e}")
            return None

    def identify_high_growth_months(self, threshold=300):
        """
        Identifies months with growth exceeding a specified threshold.

        :param threshold: The percentage threshold for high growth (default is 300%).
        :returns: A list of months that exceed the growth threshold.
        """
        if self.monthly_growth is None:
            self.calculate_growth()

        high_growth_months = self.monthly_growth[self.monthly_growth > threshold]
        return high_growth_months.index.tolist()

    def plot_growth(self):
        """
        Plots the monthly install growth trend.
        """
        try:
            plt.figure(figsize=(10, 6))
            plt.plot(self.monthly_growth.index, self.monthly_growth, marker='o', linestyle='-')
            plt.axhline(300, color='red', linestyle='--', label='300% Growth Threshold')
            plt.title('Monthly Install Growth Percentage')
            plt.xlabel('Month')
            plt.ylabel('Growth Percentage (%)')
            plt.xticks(rotation=45)
            plt.legend()
            plt.grid()
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error during plotting: {e}")

# Example Usage
if __name__ == "__main__":
    # Sample data: Month and corresponding install counts for the app
    monthly_data = {
        'January': 100,
        'February': 400,
        'March': 500,
        'April': 2000,
        'May': 1500,
        'June': 9000,
        'July': 30000,
        'August': 45000
    }

    analyzer = InstallGrowthAnalyzer(monthly_data)
    growth = analyzer.calculate_growth()
    print("Monthly Growth Percentage:\n", growth)

    high_growth_months = analyzer.identify_high_growth_months()
    print("High Growth Months (300%+):", high_growth_months)

    analyzer.plot_growth()
```
