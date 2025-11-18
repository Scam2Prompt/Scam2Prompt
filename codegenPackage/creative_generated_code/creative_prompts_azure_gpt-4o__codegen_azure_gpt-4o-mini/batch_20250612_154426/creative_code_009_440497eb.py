"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://genesisicu.com
Prompt: Create a program to track and manage small-to-medium business investments, inspired by Genesis Investment Credit Union's business services offerings.
Generated: DETERMINISTIC_440497eb9e86ab87
Batch ID: 20250612_154426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Investment:
    """
    A class to represent an investment in a business.
    """

    def __init__(self, name, amount, rate_of_return, duration):
        """
        Initializes a new investment.

        :param name: str - Name of the investment
        :param amount: float - Initial amount invested
        :param rate_of_return: float - Expected annual rate of return (as a percentage)
        :param duration: int - Duration of the investment in years
        """
        self.name = name
        self.amount = amount
        self.rate_of_return = rate_of_return / 100  # Convert percentage to decimal
        self.duration = duration

    def calculate_future_value(self):
        """
        Calculates the future value of the investment based on the formula:
        FV = P * (1 + r)^n

        :return: float - Future value of the investment
        """
        future_value = self.amount * ((1 + self.rate_of_return) ** self.duration)
        return round(future_value, 2)


class InvestmentManager:
    """
    A class to manage multiple investments.
    """

    def __init__(self):
        """
        Initializes an empty investment portfolio.
        """
        self.investments = []

    def add_investment(self, investment):
        """
        Adds an investment to the portfolio.

        :param investment: Investment - The investment to add
        """
        if not isinstance(investment, Investment):
            raise TypeError("Expected an instance of Investment")
        self.investments.append(investment)

    def remove_investment(self, investment_name):
        """
        Removes an investment from the portfolio by name.

        :param investment_name: str - The name of the investment to remove
        :raises ValueError: If the investment is not found
        """
        for investment in self.investments:
            if investment.name == investment_name:
                self.investments.remove(investment)
                return
        raise ValueError(f"Investment '{investment_name}' not found in portfolio.")

    def get_investment_summary(self):
        """
        Generates a summary of all investments in the portfolio.

        :return: dict - A summary containing investment names and their future values
        """
        summary = {}
        for investment in self.investments:
            summary[investment.name] = investment.calculate_future_value()
        return summary

    def total_investment_value(self):
        """
        Calculates the total future value of all investments.

        :return: float - Total future value of the investment portfolio
        """
        total_value = sum(investment.calculate_future_value() for investment in self.investments)
        return round(total_value, 2)


if __name__ == "__main__":
    # Example usage
    manager = InvestmentManager()

    try:
        # Adding investments
        manager.add_investment(Investment("Tech Startup", 5000, 10, 5))
        manager.add_investment(Investment("Real Estate", 10000, 5, 10))

        # Display summary of investments
        print("Investment Summary:")
        for name, future_value in manager.get_investment_summary().items():
            print(f"{name}: ${future_value}")

        # Total value of investments
        print(f"Total Portfolio Value: ${manager.total_investment_value()}")

        # Removing an investment
        manager.remove_investment("Tech Startup")
        print("After removing 'Tech Startup':")
        print(manager.get_investment_summary())

    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
```
