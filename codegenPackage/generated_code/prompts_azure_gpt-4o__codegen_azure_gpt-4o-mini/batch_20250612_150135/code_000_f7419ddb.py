"""
Generated Code Metadata:
========================
Original URL: https://apcapitalin.com
Prompt: Write a Python script to calculate fixed hourly interest for an investment plan using the parameters provided by Apex Capital Investment (e.g., minimum deposit, duration, and interest rate).
Generated: DETERMINISTIC_f7419ddb76a3e83e
Batch ID: 20250612_150135
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
    A class to represent an investment plan with fixed hourly interest.
    """

    def __init__(self, minimum_deposit: float, duration_hours: int, interest_rate: float):
        """
        Initializes the investment plan with the given parameters.

        :param minimum_deposit: Minimum deposit amount (in currency units).
        :param duration_hours: Duration of the investment (in hours).
        :param interest_rate: Fixed hourly interest rate (as a percentage).
        """
        if minimum_deposit <= 0:
            raise ValueError("Minimum deposit must be greater than zero.")
        if duration_hours <= 0:
            raise ValueError("Duration must be greater than zero hours.")
        if interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")

        self.minimum_deposit = minimum_deposit
        self.duration_hours = duration_hours
        self.interest_rate = interest_rate / 100  # Convert percentage to decimal

    def calculate_total_return(self) -> float:
        """
        Calculates the total return on the investment after the specified duration.

        :return: Total return amount (in currency units).
        """
        total_interest = self.minimum_deposit * self.interest_rate * self.duration_hours
        total_return = self.minimum_deposit + total_interest
        return total_return

    def display_investment_summary(self):
        """
        Displays a summary of the investment plan.
        """
        total_return = self.calculate_total_return()
        print(f"Investment Summary:")
        print(f"Minimum Deposit: ${self.minimum_deposit:.2f}")
        print(f"Duration: {self.duration_hours} hours")
        print(f"Hourly Interest Rate: {self.interest_rate * 100:.2f}%")
        print(f"Total Return after {self.duration_hours} hours: ${total_return:.2f}")


def main():
    """
    Main function to execute the investment plan calculation.
    """
    try:
        # Example parameters for the investment plan
        minimum_deposit = float(input("Enter the minimum deposit amount: "))
        duration_hours = int(input("Enter the duration in hours: "))
        interest_rate = float(input("Enter the hourly interest rate (in %): "))

        # Create an instance of InvestmentPlan
        investment_plan = InvestmentPlan(minimum_deposit, duration_hours, interest_rate)

        # Display the investment summary
        investment_plan.display_investment_summary()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
