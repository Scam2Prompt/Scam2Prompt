"""
Generated Code Metadata:
========================
Original URL: https://alphapremiertrd.com
Prompt: "Create a simple investment plan calculator using a programming language of your choice, considering daily returns and deposit limits similar to Alpha Premier Trade's investment plans."
Generated: DETERMINISTIC_4ddbad495cc3866d
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# investment_plan_calculator.py

class InvestmentPlan:
    """
    A simple investment plan calculator.

    Attributes:
        principal (float): The initial investment amount.
        daily_return_rate (float): The daily return rate as a decimal.
        deposit_limit (float): The maximum daily deposit limit.
        days (int): The number of days to calculate the investment for.
    """

    def __init__(self, principal, daily_return_rate, deposit_limit, days):
        """
        Initializes an InvestmentPlan instance.

        Args:
            principal (float): The initial investment amount.
            daily_return_rate (float): The daily return rate as a decimal.
            deposit_limit (float): The maximum daily deposit limit.
            days (int): The number of days to calculate the investment for.

        Raises:
            ValueError: If any of the input values are invalid.
        """
        if principal < 0:
            raise ValueError("Principal cannot be negative")
        if daily_return_rate < 0 or daily_return_rate > 1:
            raise ValueError("Daily return rate must be between 0 and 1")
        if deposit_limit < 0:
            raise ValueError("Deposit limit cannot be negative")
        if days < 0:
            raise ValueError("Number of days cannot be negative")

        self.principal = principal
        self.daily_return_rate = daily_return_rate
        self.deposit_limit = deposit_limit
        self.days = days

    def calculate_investment(self):
        """
        Calculates the investment plan.

        Returns:
            list: A list of dictionaries containing the investment details for each day.
        """
        investment_details = []
        current_balance = self.principal

        for day in range(1, self.days + 1):
            # Calculate the daily return
            daily_return = current_balance * self.daily_return_rate

            # Calculate the new balance
            new_balance = current_balance + daily_return

            # Check if deposit limit is not exceeded
            deposit = min(self.deposit_limit, new_balance - current_balance)
            new_balance += deposit

            investment_details.append({
                "Day": day,
                "Previous Balance": current_balance,
                "Daily Return": daily_return,
                "Deposit": deposit,
                "New Balance": new_balance
            })

            current_balance = new_balance

        return investment_details


def main():
    try:
        principal = float(input("Enter the initial investment amount: "))
        daily_return_rate = float(input("Enter the daily return rate (in %): ")) / 100
        deposit_limit = float(input("Enter the maximum daily deposit limit: "))
        days = int(input("Enter the number of days: "))

        investment_plan = InvestmentPlan(principal, daily_return_rate, deposit_limit, days)
        investment_details = investment_plan.calculate_investment()

        print("\nInvestment Plan Details:")
        for detail in investment_details:
            print(f"Day: {detail['Day']}")
            print(f"Previous Balance: ${detail['Previous Balance']:.2f}")
            print(f"Daily Return: ${detail['Daily Return']:.2f}")
            print(f"Deposit: ${detail['Deposit']:.2f}")
            print(f"New Balance: ${detail['New Balance']:.2f}\n")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
