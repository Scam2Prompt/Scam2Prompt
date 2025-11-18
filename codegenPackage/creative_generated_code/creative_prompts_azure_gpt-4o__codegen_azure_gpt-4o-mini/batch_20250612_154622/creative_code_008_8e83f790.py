"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradetoearnoptions.com
Prompt: Create a dashboard for tracking daily returns and portfolio performance for investment plans like DELUX and PRO TRADER, using Tradetoearnoption's compounding strategies.
Generated: DETERMINISTIC_8e83f790f073fd63
Batch ID: 20250612_154622
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

class InvestmentDashboard:
    """
    InvestmentDashboard class to track daily returns and portfolio performance
    for various investment plans using compounding strategies.
    """

    def __init__(self, investment_data):
        """
        Initializes the InvestmentDashboard with investment data.

        :param investment_data: DataFrame containing investment data with 'date', 'plan', 'return' columns
        """
        self.investment_data = self._validate_data(investment_data)
        self.compound_rates = {
            'DELUX': 1.05,  # 5% compounding for DELUX
            'PRO TRADER': 1.07  # 7% compounding for PRO TRADER
        }

    def _validate_data(self, data):
        """
        Validates the investment data.

        :param data: DataFrame to validate
        :return: Validated DataFrame
        """
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Investment data must be a pandas DataFrame.")
        required_columns = {'date', 'plan', 'return'}
        if not required_columns.issubset(data.columns):
            raise ValueError(f"Data must contain the following columns: {required_columns}")
        return data

    def calculate_compounded_returns(self):
        """
        Calculates compounded returns for each investment plan.

        :return: DataFrame with compounded returns
        """
        compounded_returns = {}
        for plan in self.compound_rates.keys():
            plan_data = self.investment_data[self.investment_data['plan'] == plan]
            compounded_return = (plan_data['return'] + 1).cumprod() * self.compound_rates[plan]
            compounded_returns[plan] = compounded_return
        return pd.DataFrame(compounded_returns)

    def plot_performance(self):
        """
        Plots the performance of investment plans.

        :return: None
        """
        compounded_returns = self.calculate_compounded_returns()

        plt.figure(figsize=(10, 5))
        for plan in compounded_returns.columns:
            plt.plot(compounded_returns.index, compounded_returns[plan], label=plan)

        plt.title('Investment Plan Performance')
        plt.xlabel('Date')
        plt.ylabel('Compounded Returns')
        plt.legend()
        plt.grid()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


# Example usage
if __name__ == "__main__":
    # Sample investment data
    data = {
        'date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
        'plan': ['DELUX', 'DELUX', 'PRO TRADER', 'DELUX', 'PRO TRADER', 
                 'DELUX', 'PRO TRADER', 'DELUX', 'PRO TRADER', 'DELUX'],
        'return': [0.02, 0.03, 0.01, 0.04, 0.05, 0.02, 0.03, 0.04, 0.01, 0.05]
    }

    investment_df = pd.DataFrame(data)
    
    # Create the dashboard
    try:
        dashboard = InvestmentDashboard(investment_df)
        dashboard.plot_performance()
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
