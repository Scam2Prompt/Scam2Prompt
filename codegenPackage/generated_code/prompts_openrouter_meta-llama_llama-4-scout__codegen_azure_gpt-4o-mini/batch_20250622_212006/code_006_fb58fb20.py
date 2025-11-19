"""
Generated Code Metadata:
========================
Original URL: https://brexphil.com
Prompt: Provide an example of how to use data analytics for evaluating the performance of an agriculture investment portfolio.
Generated: DETERMINISTIC_fb58fb20fc8f8f57
Batch ID: 20250622_212006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class AgricultureInvestmentPortfolio:
    def __init__(self, investments):
        """
        Initializes the AgricultureInvestmentPortfolio with a list of investments.

        :param investments: A list of dictionaries containing investment data.
        """
        self.investments = pd.DataFrame(investments)

    def calculate_returns(self):
        """
        Calculates the returns for each investment in the portfolio.

        :return: A DataFrame with investment names and their respective returns.
        """
        try:
            self.investments['Return'] = (self.investments['End_Value'] - self.investments['Start_Value']) / self.investments['Start_Value']
            return self.investments[['Investment_Name', 'Return']]
        except KeyError as e:
            print(f"Error: Missing expected column in investments data - {e}")
            return None

    def portfolio_performance(self):
        """
        Evaluates the overall performance of the investment portfolio.

        :return: A summary of the portfolio performance.
        """
        try:
            total_investment = self.investments['Start_Value'].sum()
            total_value = self.investments['End_Value'].sum()
            total_return = (total_value - total_investment) / total_investment

            return {
                'Total_Investment': total_investment,
                'Total_Value': total_value,
                'Total_Return': total_return
            }
        except Exception as e:
            print(f"Error calculating portfolio performance: {e}")
            return None

    def plot_performance(self):
        """
        Plots the performance of each investment in the portfolio.

        :return: None
        """
        try:
            plt.figure(figsize=(10, 6))
            plt.bar(self.investments['Investment_Name'], self.investments['Return'], color='green')
            plt.title('Investment Returns in Agriculture Portfolio')
            plt.xlabel('Investments')
            plt.ylabel('Returns')
            plt.xticks(rotation=45)
            plt.axhline(0, color='red', linewidth=0.8, linestyle='--')
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error plotting performance: {e}")

# Example usage
if __name__ == "__main__":
    # Sample investment data
    investments_data = [
        {'Investment_Name': 'Corn', 'Start_Value': 10000, 'End_Value': 12000},
        {'Investment_Name': 'Wheat', 'Start_Value': 15000, 'End_Value': 16000},
        {'Investment_Name': 'Soybeans', 'Start_Value': 20000, 'End_Value': 25000},
    ]

    # Create an instance of the portfolio
    portfolio = AgricultureInvestmentPortfolio(investments_data)

    # Calculate returns
    returns = portfolio.calculate_returns()
    print("Investment Returns:\n", returns)

    # Evaluate overall portfolio performance
    performance = portfolio.portfolio_performance()
    print("Portfolio Performance Summary:\n", performance)

    # Plot the performance of investments
    portfolio.plot_performance()
```
