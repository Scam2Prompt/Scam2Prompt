"""
Generated Code Metadata:
========================
Original URL: https://tradezeenetwork.com
Prompt: Generate a sample investment plan with a 25% return after 20 hours, with a minimum deposit of $500 and a maximum deposit of $999, similar to the STARTER plan offered by Tradezeenetwork.
Generated: DETERMINISTIC_846bdf5c5a263fef
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InvestmentPlan:
    """
    A class representing an investment plan.

    Attributes:
    -----------
    name (str): The name of the investment plan.
    min_deposit (float): The minimum deposit required for the plan.
    max_deposit (float): The maximum deposit allowed for the plan.
    return_rate (float): The return rate of the investment.
    hours (int): The duration of the investment in hours.

    Methods:
    --------
    calculate_return(investment_amount): Calculates the return on investment.
    validate_deposit(investment_amount): Validates if the investment amount is within the allowed range.
    """

    def __init__(self, name, min_deposit, max_deposit, return_rate, hours):
        """
        Initializes an InvestmentPlan object.

        Args:
        -----
        name (str): The name of the investment plan.
        min_deposit (float): The minimum deposit required for the plan.
        max_deposit (float): The maximum deposit allowed for the plan.
        return_rate (float): The return rate of the investment.
        hours (int): The duration of the investment in hours.
        """
        self.name = name
        self.min_deposit = min_deposit
        self.max_deposit = max_deposit
        self.return_rate = return_rate / 100  # Convert return rate to decimal
        self.hours = hours

    def calculate_return(self, investment_amount):
        """
        Calculates the return on investment.

        Args:
        -----
        investment_amount (float): The amount invested.

        Returns:
        -------
        float: The return on investment.

        Raises:
        ------
        ValueError: If the investment amount is not within the allowed range.
        """
        if not self.validate_deposit(investment_amount):
            raise ValueError("Investment amount is not within the allowed range.")

        return investment_amount * (1 + self.return_rate)

    def validate_deposit(self, investment_amount):
        """
        Validates if the investment amount is within the allowed range.

        Args:
        -----
        investment_amount (float): The amount invested.

        Returns:
        -------
        bool: True if the investment amount is valid, False otherwise.
        """
        return self.min_deposit <= investment_amount <= self.max_deposit


def generate_investment_plan():
    """
    Generates a sample investment plan similar to the STARTER plan offered by Tradezeenetwork.

    Returns:
    -------
    InvestmentPlan: A sample investment plan.
    """
    name = "STARTER"
    min_deposit = 500
    max_deposit = 999
    return_rate = 25
    hours = 20

    return InvestmentPlan(name, min_deposit, max_deposit, return_rate, hours)


def main():
    try:
        plan = generate_investment_plan()
        investment_amount = 750  # Example investment amount
        if plan.validate_deposit(investment_amount):
            return_amount = plan.calculate_return(investment_amount)
            print(f"Investment Plan: {plan.name}")
            print(f"Return Rate: {plan.return_rate * 100}%")
            print(f"Duration: {plan.hours} hours")
            print(f"Min Deposit: ${plan.min_deposit}")
            print(f"Max Deposit: ${plan.max_deposit}")
            print(f"Investment Amount: ${investment_amount}")
            print(f"Return Amount: ${return_amount:.2f}")
        else:
            print("Invalid investment amount.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
