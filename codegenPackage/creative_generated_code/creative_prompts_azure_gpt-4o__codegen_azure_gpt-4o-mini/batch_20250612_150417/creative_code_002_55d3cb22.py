"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-idegen.com
Prompt: Generate a script to automate the calculation of rewards on investments based on equity and stock trading, using the features mentioned on Ambro Contables' site.
Generated: DETERMINISTIC_55d3cb222ca44d9f
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class InvestmentRewardCalculator:
    """
    A class to calculate rewards on investments based on equity and stock trading.
    """

    def __init__(self, investments):
        """
        Initializes the calculator with a list of investments.

        :param investments: A DataFrame containing investment data with columns: 
                           ['investment_type', 'amount', 'return_rate', 'duration']
        """
        self.investments = investments

    def validate_investments(self):
        """
        Validates the investment data to ensure all necessary columns are present and correct.

        :raises ValueError: If any required column is missing or contains invalid data.
        """
        required_columns = ['investment_type', 'amount', 'return_rate', 'duration']
        for column in required_columns:
            if column not in self.investments.columns:
                raise ValueError(f"Missing required column: {column}")

        if self.investments['amount'].dtype not in [int, float]:
            raise ValueError("Investment 'amount' must be numeric.")
        if self.investments['return_rate'].dtype not in [int, float]:
            raise ValueError("Investment 'return_rate' must be numeric.")
        if self.investments['duration'].dtype not in [int, float]:
            raise ValueError("Investment 'duration' must be numeric.")

    def calculate_rewards(self):
        """
        Calculates the total rewards for each investment.

        :return: A DataFrame containing the original investment data with an added 'reward' column.
        """
        self.validate_investments()

        # Calculate rewards
        self.investments['reward'] = (
            self.investments['amount'] * (self.investments['return_rate'] / 100) * self.investments['duration']
        )

        return self.investments

def main():
    # Sample investment data
    data = {
        'investment_type': ['stocks', 'bonds', 'mutual funds'],
        'amount': [1000, 1500, 2000],
        'return_rate': [5, 3, 4],
        'duration': [2, 5, 3]
    }

    # Create a DataFrame from sample data
    investments_df = pd.DataFrame(data)

    # Initialize the calculator
    reward_calculator = InvestmentRewardCalculator(investments_df)

    # Calculate rewards and print results
    try:
        rewards_df = reward_calculator.calculate_rewards()
        print(rewards_df)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
