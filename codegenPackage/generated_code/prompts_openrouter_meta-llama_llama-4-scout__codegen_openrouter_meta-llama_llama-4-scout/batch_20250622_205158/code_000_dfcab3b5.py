"""
Generated Code Metadata:
========================
Original URL: https://alphagrowth.fund
Prompt: What are the key factors to consider when investing in a fund for alpha growth?
Generated: DETERMINISTIC_dfcab3b5ec189c06
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd

class InvestmentAnalyzer:
    """
    Analyzes key factors for alpha growth when investing in a fund.
    """

    def __init__(self, fund_data):
        """
        Initializes the InvestmentAnalyzer with fund data.

        Args:
            fund_data (pd.DataFrame): A DataFrame containing fund data.
                Expected columns: ['name', 'alpha', 'beta', 'sharpe_ratio', 'expense_ratio']
        """
        self.fund_data = fund_data

    def evaluate_alpha_growth(self):
        """
        Evaluates key factors for alpha growth.

        Returns:
            dict: A dictionary containing key factors for alpha growth.
        """
        try:
            # Filter funds with positive alpha
            positive_alpha_funds = self.fund_data[self.fund_data['alpha'] > 0]

            # Calculate average alpha, beta, and Sharpe ratio for positive alpha funds
            avg_alpha = positive_alpha_funds['alpha'].mean()
            avg_beta = positive_alpha_funds['beta'].mean()
            avg_sharpe_ratio = positive_alpha_funds['sharpe_ratio'].mean()

            # Identify funds with low expense ratio (< 0.5%)
            low_expense_ratio_funds = positive_alpha_funds[positive_alpha_funds['expense_ratio'] < 0.005]

            key_factors = {
                'average_alpha': avg_alpha,
                'average_beta': avg_beta,
                'average_sharpe_ratio': avg_sharpe_ratio,
                'low_expense_ratio_funds': low_expense_ratio_funds['name'].tolist()
            }

            return key_factors

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None


def main():
    # Sample fund data
    fund_data = pd.DataFrame({
        'name': ['Fund A', 'Fund B', 'Fund C', 'Fund D'],
        'alpha': [0.05, -0.02, 0.08, 0.03],
        'beta': [1.2, 0.8, 1.1, 1.0],
        'sharpe_ratio': [1.5, 0.8, 1.8, 1.2],
        'expense_ratio': [0.004, 0.007, 0.003, 0.006]
    })

    analyzer = InvestmentAnalyzer(fund_data)
    key_factors = analyzer.evaluate_alpha_growth()

    if key_factors:
        print("Key Factors for Alpha Growth:")
        print(f"Average Alpha: {key_factors['average_alpha']:.4f}")
        print(f"Average Beta: {key_factors['average_beta']:.4f}")
        print(f"Average Sharpe Ratio: {key_factors['average_sharpe_ratio']:.4f}")
        print("Funds with Low Expense Ratio:")
        for fund in key_factors['low_expense_ratio_funds']:
            print(fund)


if __name__ == "__main__":
    main()
```
