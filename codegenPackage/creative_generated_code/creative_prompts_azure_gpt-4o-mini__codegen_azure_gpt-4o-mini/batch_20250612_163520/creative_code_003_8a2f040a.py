"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://glencoreminers.net
Prompt: Generate a code snippet that calculates potential profits based on the investment plans offered by Glencoreminers.net.
Generated: DETERMINISTIC_8a2f040a9db9bcf8
Batch ID: 20250612_163520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    """
    A class to represent an investment plan.

    Attributes:
    ----------
    name : str
        The name of the investment plan.
    rate_of_return : float
        The expected rate of return on investment (as a percentage).
    duration : int
        The duration of the investment in months.
    """

    def __init__(self, name: str, rate_of_return: float, duration: int):
        """
        Initializes the InvestmentPlan with the given name, rate of return, and duration.

        Parameters:
        ----------
        name : str
            The name of the investment plan.
        rate_of_return : float
            The expected rate of return on investment (as a percentage).
        duration : int
            The duration of the investment in months.
        """
        self.name = name
        self.rate_of_return = rate_of_return
        self.duration = duration

    def calculate_profit(self, investment_amount: float) -> float:
        """
        Calculates the potential profit from the investment.

        Parameters:
        ----------
        investment_amount : float
            The amount of money invested.

        Returns:
        -------
        float
            The potential profit calculated as investment_amount * rate_of_return / 100 * duration.
        """
        if investment_amount < 0:
            raise ValueError("Investment amount must be non-negative.")
        
        profit = investment_amount * (self.rate_of_return / 100) * self.duration
        return profit


def main():
    """
    Main function that demonstrates the usage of the InvestmentPlan class
    and calculates potential profits based on user input.
    """
    try:
        # Define investment plans offered by Glencoreminers.net
        plans = [
            InvestmentPlan("Basic Plan", 5.0, 12),     # 5% return over 12 months
            InvestmentPlan("Standard Plan", 10.0, 6),  # 10% return over 6 months
            InvestmentPlan("Premium Plan", 15.0, 3)    # 15% return over 3 months
        ]

        # User input for investment amount
        investment_amount = float(input("Enter your investment amount: $"))

        # Calculate and display potential profits for each plan
        for plan in plans:
            profit = plan.calculate_profit(investment_amount)
            print(f"Potential profit for {plan.name}: ${profit:.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
