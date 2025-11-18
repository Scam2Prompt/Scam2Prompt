"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://camp-dmb.pages.dev
Prompt: Write a Python script to simulate the profit distribution for the "Achievers Plan," which offers a 15% return after 8 days, based on the deposit amount.
Generated: DETERMINISTIC_ef89c12d24ab2dac
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class AchieversPlan:
    """
    A class to simulate the profit distribution for the Achievers Plan.
    """

    def __init__(self, deposit_amount: float):
        """
        Initializes the Achievers Plan with a deposit amount.

        :param deposit_amount: The amount deposited by the user.
        :raises ValueError: If the deposit amount is not positive.
        """
        if deposit_amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.deposit_amount = deposit_amount
        self.profit_percentage = 15  # Return percentage after 8 days
        self.plan_duration_days = 8  # Plan duration in days

    def calculate_profit(self) -> float:
        """
        Calculates the profit based on the deposit amount and percentage.

        :return: The profit amount.
        """
        return self.deposit_amount * (self.profit_percentage / 100)

    def get_maturity_date(self) -> datetime.date:
        """
        Calculates the date when the plan matures.

        :return: The maturity date (current date + 8 days).
        """
        return datetime.date.today() + datetime.timedelta(days=self.plan_duration_days)

    def simulate_profit_distribution(self):
        """
        Simulates the profit distribution by displaying the deposit amount, profit,
        and maturity date in a user-friendly format.

        :return: None
        """
        profit = self.calculate_profit()
        maturity_date = self.get_maturity_date()

        print("=== Achievers Plan Profit Simulation ===")
        print(f"Deposit Amount: ${self.deposit_amount:.2f}")
        print(f"Profit Percentage: {self.profit_percentage}%")
        print(f"Profit Amount (after {self.plan_duration_days} days): ${profit:.2f}")
        print(f"Maturity Date: {maturity_date}")
        print("========================================")


def main():
    """
    The main function to execute the Achievers Plan simulation.
    """
    try:
        # Prompt the user for deposit amount
        deposit_amount = float(input("Enter deposit amount: $"))
        
        # Create an AchieversPlan instance and simulate profit distribution
        achievers_plan = AchieversPlan(deposit_amount)
        achievers_plan.simulate_profit_distribution()
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point for the script
    main()
```
