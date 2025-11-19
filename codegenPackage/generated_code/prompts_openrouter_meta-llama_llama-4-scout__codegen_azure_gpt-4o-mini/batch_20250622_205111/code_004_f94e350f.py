"""
Generated Code Metadata:
========================
Original URL: https://ahmetiwealth.com
Prompt: "Design a charitable legacy plan for a high-net-worth individual, incorporating wealth management strategies and investment advice from a registered investment adviser."
Generated: DETERMINISTIC_f94e350f1f4d1d26
Batch ID: 20250622_205111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CharitableLegacyPlan:
    """
    A class to represent a charitable legacy plan for high-net-worth individuals.
    This plan incorporates wealth management strategies and investment advice.
    """

    def __init__(self, individual_name, net_worth):
        """
        Initializes the CharitableLegacyPlan with the individual's name and net worth.

        :param individual_name: str - The name of the high-net-worth individual.
        :param net_worth: float - The net worth of the individual.
        """
        self.individual_name = individual_name
        self.net_worth = net_worth
        self.charitable_donations = []
        self.investment_strategies = []

    def add_charitable_donation(self, charity_name, amount):
        """
        Adds a charitable donation to the plan.

        :param charity_name: str - The name of the charity.
        :param amount: float - The amount to be donated.
        :raises ValueError: If the donation amount is negative or exceeds net worth.
        """
        if amount < 0:
            raise ValueError("Donation amount cannot be negative.")
        if amount > self.net_worth:
            raise ValueError("Donation amount exceeds net worth.")

        self.charitable_donations.append({'charity': charity_name, 'amount': amount})
        self.net_worth -= amount  # Deduct the donation from net worth

    def add_investment_strategy(self, strategy_name, expected_return):
        """
        Adds an investment strategy to the plan.

        :param strategy_name: str - The name of the investment strategy.
        :param expected_return: float - The expected return on investment.
        :raises ValueError: If the expected return is negative.
        """
        if expected_return < 0:
            raise ValueError("Expected return cannot be negative.")

        self.investment_strategies.append({'strategy': strategy_name, 'expected_return': expected_return})

    def generate_plan_summary(self):
        """
        Generates a summary of the charitable legacy plan.

        :return: str - A summary of the plan including donations and investment strategies.
        """
        summary = f"Charitable Legacy Plan for {self.individual_name}:\n"
        summary += f"Net Worth: ${self.net_worth:,.2f}\n"
        summary += "Charitable Donations:\n"
        for donation in self.charitable_donations:
            summary += f"  - {donation['charity']}: ${donation['amount']:,.2f}\n"
        summary += "Investment Strategies:\n"
        for strategy in self.investment_strategies:
            summary += f"  - {strategy['strategy']}: Expected Return {strategy['expected_return']}%\n"
        return summary

# Example usage
if __name__ == "__main__":
    try:
        legacy_plan = CharitableLegacyPlan("John Doe", 5000000)
        legacy_plan.add_charitable_donation("Local Food Bank", 100000)
        legacy_plan.add_investment_strategy("Real Estate", 8.5)
        legacy_plan.add_investment_strategy("Stock Market", 10.0)
        
        print(legacy_plan.generate_plan_summary())
    except ValueError as e:
        print(f"Error: {e}")
```
