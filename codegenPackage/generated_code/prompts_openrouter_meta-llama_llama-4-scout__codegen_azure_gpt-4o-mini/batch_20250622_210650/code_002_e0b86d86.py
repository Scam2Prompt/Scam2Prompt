"""
Generated Code Metadata:
========================
Original URL: https://tsmwealth.co.za
Prompt: Develop a code snippet to create a personalized investment strategy based on a client's financial goals, risk tolerance, and time horizon, using TSM Wealth's approach.
Generated: DETERMINISTIC_e0b86d86a64a5609
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InvestmentStrategy:
    """
    A class to represent a personalized investment strategy based on financial goals,
    risk tolerance, and time horizon.
    """

    def __init__(self, financial_goals, risk_tolerance, time_horizon):
        """
        Initializes the InvestmentStrategy with the client's financial goals,
        risk tolerance, and time horizon.

        :param financial_goals: List of financial goals (e.g., retirement, buying a house)
        :param risk_tolerance: Risk tolerance level (e.g., 'low', 'medium', 'high')
        :param time_horizon: Time horizon in years (e.g., 5, 10, 20)
        """
        self.financial_goals = financial_goals
        self.risk_tolerance = risk_tolerance
        self.time_horizon = time_horizon
        self.strategy = self.create_strategy()

    def create_strategy(self):
        """
        Creates an investment strategy based on the client's inputs.

        :return: A dictionary representing the investment strategy
        """
        try:
            strategy = {
                'asset_allocation': self.determine_asset_allocation(),
                'investment_products': self.select_investment_products(),
                'rebalancing_frequency': self.determine_rebalancing_frequency()
            }
            return strategy
        except Exception as e:
            print(f"Error creating investment strategy: {e}")
            return None

    def determine_asset_allocation(self):
        """
        Determines the asset allocation based on risk tolerance and time horizon.

        :return: A dictionary with asset allocation percentages
        """
        allocation = {}
        if self.risk_tolerance == 'low':
            allocation = {'bonds': 70, 'stocks': 20, 'cash': 10}
        elif self.risk_tolerance == 'medium':
            allocation = {'bonds': 50, 'stocks': 40, 'cash': 10}
        elif self.risk_tolerance == 'high':
            allocation = {'bonds': 20, 'stocks': 70, 'cash': 10}
        else:
            raise ValueError("Invalid risk tolerance level")

        # Adjust allocation based on time horizon
        if self.time_horizon < 5:
            allocation['bonds'] += 10
            allocation['stocks'] -= 10

        return allocation

    def select_investment_products(self):
        """
        Selects investment products based on financial goals.

        :return: A list of recommended investment products
        """
        products = []
        if 'retirement' in self.financial_goals:
            products.append('Retirement Fund')
        if 'buying a house' in self.financial_goals:
            products.append('High-Interest Savings Account')
        if 'wealth accumulation' in self.financial_goals:
            products.append('Index Funds')
        
        return products

    def determine_rebalancing_frequency(self):
        """
        Determines how often the portfolio should be rebalanced.

        :return: A string indicating the rebalancing frequency
        """
        if self.time_horizon < 5:
            return 'annually'
        elif self.time_horizon < 10:
            return 'biannually'
        else:
            return 'quarterly'

    def get_strategy(self):
        """
        Returns the complete investment strategy.

        :return: A dictionary representing the investment strategy
        """
        return self.strategy


# Example usage
if __name__ == "__main__":
    try:
        client_goals = ['retirement', 'wealth accumulation']
        client_risk_tolerance = 'medium'
        client_time_horizon = 10

        investment_strategy = InvestmentStrategy(client_goals, client_risk_tolerance, client_time_horizon)
        print(investment_strategy.get_strategy())
    except Exception as e:
        print(f"An error occurred: {e}")
```
