"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apcapitalin.com
Prompt: Generate code to model and calculate hourly interest payments for multiple investment plans, ensuring instant withdrawal functionality as described by Apex Capital Investment.
Generated: DETERMINISTIC_3118c14f6d491665
Batch ID: 20250612_150135
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
    A class to represent an investment plan for calculating hourly interest payments.
    """

    def __init__(self, principal: float, annual_interest_rate: float, withdrawal_limit: float):
        """
        Initializes a new investment plan.

        :param principal: The initial amount of money invested (float).
        :param annual_interest_rate: The annual interest rate as a percentage (float).
        :param withdrawal_limit: The maximum amount that can be withdrawn instantly (float).
        """
        if principal < 0 or annual_interest_rate < 0 or withdrawal_limit < 0:
            raise ValueError("Principal, interest rate, and withdrawal limit must be non-negative.")

        self.principal = principal
        self.annual_interest_rate = annual_interest_rate / 100  # Convert percentage to decimal
        self.withdrawal_limit = withdrawal_limit

    def calculate_hourly_interest(self) -> float:
        """
        Calculates the hourly interest payment based on the investment plan.

        :return: Hourly interest payment (float).
        """
        hourly_interest_rate = self.annual_interest_rate / 365 / 24  # Annual rate to hourly rate
        hourly_payment = self.principal * hourly_interest_rate
        return hourly_payment

    def withdraw(self, amount: float) -> float:
        """
        Allows the user to withdraw an amount from the investment plan.

        :param amount: The amount to withdraw (float).
        :return: The actual amount withdrawn (float).
        :raises ValueError: If the withdrawal amount exceeds the withdrawal limit or the available principal.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount must be non-negative.")
        if amount > self.withdrawal_limit:
            raise ValueError("Withdrawal amount exceeds the withdrawal limit.")
        if amount > self.principal:
            raise ValueError("Withdrawal amount exceeds available principal.")

        self.principal -= amount
        return amount

def main():
    """
    Main function to demonstrate the usage of the InvestmentPlan class.
    """
    try:
        # Example of creating an investment plan
        plan = InvestmentPlan(principal=10000, annual_interest_rate=5, withdrawal_limit=500)

        # Calculate hourly interest
        hourly_interest = plan.calculate_hourly_interest()
        print(f"Hourly Interest Payment: ${hourly_interest:.2f}")

        # Withdraw funds
        withdrawn_amount = plan.withdraw(300)
        print(f"Amount withdrawn: ${withdrawn_amount:.2f}")
        print(f"Remaining principal: ${plan.principal:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
