"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elixinvestmentltd.info
Prompt: Generate a Python script to automate the selection of an investment plan based on user input for deposit amount, using the plan constraints provided by RystonFX Trading (e.g., $100-$500 for Starter Plan, $500-$1,000 for Premium Plan, etc.).
Generated: DETERMINISTIC_6637fb122fe026b6
Batch ID: 20250612_150246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    """Class to represent an investment plan with its constraints."""

    def __init__(self, name, min_amount, max_amount):
        """
        Initialize an investment plan.

        Args:
            name (str): The name of the investment plan.
            min_amount (float): Minimum deposit amount for the plan.
            max_amount (float): Maximum deposit amount for the plan.
        """
        self.name = name
        self.min_amount = min_amount
        self.max_amount = max_amount

    def __str__(self):
        """Return a string representation of the investment plan."""
        return f"{self.name} Plan: ${self.min_amount} - ${self.max_amount}"


class InvestmentSelector:
    """Class to select an investment plan based on user deposit amount."""

    def __init__(self):
        """Initialize available investment plans."""
        self.plans = [
            InvestmentPlan("Starter", 100, 500),
            InvestmentPlan("Premium", 500, 1000),
            InvestmentPlan("Pro", 1000, 5000),
            InvestmentPlan("Elite", 5000, 10000),
        ]

    def select_plan(self, deposit_amount):
        """
        Select an investment plan based on the deposit amount.

        Args:
            deposit_amount (float): The deposit amount from the user.

        Returns:
            str: The name of the selected investment plan or a message indicating
                 no suitable plan was found.
        """
        if deposit_amount <= 0:
            return "Invalid deposit amount. Please enter a positive value."

        for plan in self.plans:
            if plan.min_amount <= deposit_amount <= plan.max_amount:
                return f"Selected Investment Plan: {plan.name} Plan"

        return "No suitable investment plan found for the given deposit amount."


def main():
    """Main function to run the investment plan selection."""
    try:
        # Get user input for deposit amount
        deposit_input = input("Enter your deposit amount: $")
        deposit_amount = float(deposit_input)

        # Create an instance of InvestmentSelector
        selector = InvestmentSelector()

        # Select the investment plan based on user input
        result = selector.select_plan(deposit_amount)

        # Output the result
        print(result)

    except ValueError:
        print("Invalid input. Please enter a numeric value for the deposit amount.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
