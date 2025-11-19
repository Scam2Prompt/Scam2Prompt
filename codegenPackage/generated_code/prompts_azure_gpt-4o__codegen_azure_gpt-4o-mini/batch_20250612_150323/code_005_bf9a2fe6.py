"""
Generated Code Metadata:
========================
Original URL: https://metamark.lt
Prompt: Write a Python script to analyze e-commerce sales growth trends, inspired by Metamark's insights on the 20% annual growth in online sales.
Generated: DETERMINISTIC_bf9a2fe6802ea7d3
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt

class SalesGrowthAnalyzer:
    """
    A class to analyze e-commerce sales growth trends.
    """

    def __init__(self, sales_data: pd.DataFrame):
        """
        Initializes the SalesGrowthAnalyzer with sales data.

        :param sales_data: A pandas DataFrame containing sales data with 'Year' and 'Sales' columns.
        """
        self.sales_data = sales_data

    def calculate_growth_rate(self) -> pd.Series:
        """
        Calculates the annual growth rate of sales.

        :return: A pandas Series containing the growth rate for each year.
        """
        try:
            self.sales_data['Growth Rate'] = self.sales_data['Sales'].pct_change() * 100
            return self.sales_data['Growth Rate']
        except Exception as e:
            print(f"Error calculating growth rate: {e}")
            return pd.Series(dtype=float)

    def plot_sales_trend(self):
        """
        Plots the sales trend over the years.
        """
        try:
            plt.figure(figsize=(10, 5))
            plt.plot(self.sales_data['Year'], self.sales_data['Sales'], marker='o', linestyle='-')
            plt.title('E-commerce Sales Growth Trend')
            plt.xlabel('Year')
            plt.ylabel('Sales ($)')
            plt.grid()
            plt.xticks(self.sales_data['Year'])
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error plotting sales trend: {e}")

    def plot_growth_rate(self):
        """
        Plots the growth rate over the years.
        """
        try:
            plt.figure(figsize=(10, 5))
            plt.plot(self.sales_data['Year'], self.sales_data['Growth Rate'], marker='o', color='orange', linestyle='-')
            plt.title('E-commerce Sales Growth Rate')
            plt.xlabel('Year')
            plt.ylabel('Growth Rate (%)')
            plt.grid()
            plt.xticks(self.sales_data['Year'])
            plt.axhline(y=20, color='r', linestyle='--', label='20% Growth Target')
            plt.legend()
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error plotting growth rate: {e}")

def main():
    """
    Main function to execute the sales growth analysis.
    """
    # Sample sales data for demonstration
    data = {
        'Year': [2018, 2019, 2020, 2021, 2022],
        'Sales': [100000, 120000, 150000, 180000, 216000]
    }
    
    # Create a DataFrame
    sales_data = pd.DataFrame(data)

    # Initialize the SalesGrowthAnalyzer
    analyzer = SalesGrowthAnalyzer(sales_data)

    # Calculate growth rates
    growth_rates = analyzer.calculate_growth_rate()
    print("Calculated Growth Rates:\n", growth_rates)

    # Plot sales trend
    analyzer.plot_sales_trend()

    # Plot growth rate
    analyzer.plot_growth_rate()

if __name__ == "__main__":
    main()
```
