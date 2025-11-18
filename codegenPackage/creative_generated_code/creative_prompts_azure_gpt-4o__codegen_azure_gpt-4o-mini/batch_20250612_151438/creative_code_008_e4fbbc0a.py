"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elon-crypto.online
Prompt: Write a script to analyze the profitability of OctaFx's VIP plans, comparing the returns across different tiers, and visualize the data using a charting library.
Generated: DETERMINISTIC_e4fbbc0a23cea402
Batch ID: 20250612_151438
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

class OctaFxVIPAnalyzer:
    """
    A class to analyze the profitability of OctaFx's VIP plans by comparing returns across different tiers.
    """

    def __init__(self, data):
        """
        Initializes the OctaFxVIPAnalyzer with given data.

        :param data: A pandas DataFrame containing VIP plan data
        """
        self.data = data

    def calculate_returns(self):
        """
        Calculates the returns for each VIP tier and adds them to the DataFrame.

        :return: A DataFrame with calculated returns
        """
        try:
            self.data['Returns'] = self.data['Investment'] * self.data['Profit_Percent'] / 100
            return self.data
        except KeyError as e:
            print(f"KeyError: {e}. Please ensure the DataFrame contains 'Investment' and 'Profit_Percent' columns.")
            return None

    def visualize_returns(self):
        """
        Visualizes the returns for each VIP tier using a bar chart.
        """
        try:
            plt.figure(figsize=(10, 6))
            plt.bar(self.data['VIP_Tier'], self.data['Returns'], color='skyblue')
            plt.title('Returns by OctaFx VIP Tier')
            plt.xlabel('VIP Tier')
            plt.ylabel('Returns')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"An error occurred while visualizing returns: {e}")

def main():
    # Sample data for OctaFx VIP plans
    data = {
        'VIP_Tier': ['Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond'],
        'Investment': [1000, 5000, 15000, 30000, 50000],
        'Profit_Percent': [5, 7, 10, 12, 15]
    }

    # Create a DataFrame from the sample data
    df = pd.DataFrame(data)

    # Initialize the analyzer with the data
    analyzer = OctaFxVIPAnalyzer(df)

    # Calculate returns
    df_with_returns = analyzer.calculate_returns()
    if df_with_returns is not None:
        print("Calculated Returns:")
        print(df_with_returns[['VIP_Tier', 'Returns']])

        # Visualize the returns
        analyzer.visualize_returns()

if __name__ == "__main__":
    main()
```
