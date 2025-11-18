"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatepeak.io
Prompt: Develop a Python program to calculate the potential risks and rewards of different investment types, as categorized by Immediate Peak.
Generated: DETERMINISTIC_841ef0dc195024f3
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class Investment:
    """
    A class to represent an investment.

    Attributes:
        name (str): The name of the investment.
        initial_amount (float): The initial amount of money invested.
        expected_return_rate (float): The expected return rate of the investment as a percentage.
        risk_factor (float): The risk factor of the investment as a percentage.
    """

    def __init__(self, name, initial_amount, expected_return_rate, risk_factor):
        """
        Constructs all the necessary attributes for the Investment object.

        Args:
            name (str): The name of the investment.
            initial_amount (float): The initial amount of money invested.
            expected_return_rate (float): The expected return rate of the investment.
            risk_factor (float): The risk factor of the investment.
        """
        self.name = name
        self.initial_amount = initial_amount
        self.expected_return_rate = expected_return_rate
        self.risk_factor = risk_factor

    def calculate_return(self):
        """
        Calculate the expected return on the investment.

        Returns:
            float: The expected return amount.
        """
        return self.initial_amount * (self.expected_return_rate / 100)

    def calculate_risk(self):
        """
        Calculate the potential monetary loss considering the risk factor.

        Returns:
            float: The potential loss amount.
        """
        return self.initial_amount * (self.risk_factor / 100)

    def risk_reward_profile(self):
        """
        Generate the risk-reward profile for the investment.

        Returns:
            dict: A dictionary containing the potential return and risk.
        """
        return {
            'Investment Name': self.name,
            'Expected Return': self.calculate_return(),
            'Potential Risk': self.calculate_risk()
        }


def main():
    """
    Main function to execute the investment risk and reward calculation.
    """
    investments = []
    investment_data = [
        {'name': 'Stocks', 'amount': 10000, 'return_rate': 7, 'risk': 15},
        {'name': 'Bonds', 'amount': 10000, 'return_rate': 3, 'risk': 5},
        {'name': 'Real Estate', 'amount': 10000, 'return_rate': 5, 'risk': 10},
        {'name': 'Cryptocurrency', 'amount': 10000, 'return_rate': 20, 'risk': 50},
    ]

    # Create Investment objects
    for data in investment_data:
        try:
            investment = Investment(
                name=data['name'],
                initial_amount=data['amount'],
                expected_return_rate=data['return_rate'],
                risk_factor=data['risk']
            )
            investments.append(investment.risk_reward_profile())
        except Exception as e:
            print(f"Error creating investment {data['name']}: {e}")

    # Convert the results into a DataFrame for better visualization
    df_investments = pd.DataFrame(investments)

    # Display the risk-reward profile
    print("\nInvestment Risk and Reward Profiles:")
    print(df_investments)


if __name__ == "__main__":
    main()
```
