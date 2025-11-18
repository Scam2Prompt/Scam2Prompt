"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apcapitalin.com
Prompt: Write a Python script to calculate fixed hourly interest for an investment plan using the parameters provided by Apex Capital Investment (e.g., minimum deposit, duration, and interest rate).
Generated: DETERMINISTIC_f7419ddb76a3e83e
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
    def __init__(self, minimum_deposit: float, duration_months: int, interest_rate: float):
        """
        Initializes the InvestmentPlan with the given parameters.

        :param minimum_deposit: Minimum deposit for the investment plan (in currency units).
        :param duration_months: Duration of the investment plan (in months).
        :param interest_rate: Fixed hourly interest rate (as a percentage).
        """
        if minimum_deposit <= 0:
            raise ValueError("Minimum deposit must be greater than zero.")
        if duration_months <= 0:
            raise ValueError("Duration must be greater than zero.")
        if interest_rate <= 0:
            raise ValueError("Interest rate must be greater than zero.")

        self.minimum_deposit = minimum_deposit
        self.duration_months = duration_months
        self.interest_rate = interest_rate / 100  # Convert percentage to decimal for calculations

    def calculate_interest(self) -> float:
        """
        Calculates the total interest earned over the duration of the investment plan.

        :return: Total interest earned (in currency units).
        """
        try:
            # Calculate total hours in the duration
            total_hours = self.duration_months * 30 * 24  # Assuming 30 days in a month
            # Calculate total interest
            total_interest = self.minimum_deposit * self.interest_rate * total_hours
            return total_interest
        except Exception as e:
            raise RuntimeError("An error occurred while calculating interest: " + str(e))

    def total_investment_value(self) -> float:
        """
        Calculates the total value of the investment after the duration, including interest.

        :return: Total investment value (in currency units).
        """
        try:
            total_value = self.minimum_deposit + self.calculate_interest()
            return total_value
        except Exception as e:
            raise RuntimeError("An error occurred while calculating total investment value: " + str(e))


def main():
    """
    Main function to execute the investment calculation.
    """
    try:
        # Example parameters for the investment plan
        minimum_deposit = 1000.0  # Minimum deposit in currency units
        duration_months = 6        # Duration in months
        interest_rate = 5.0        # Fixed hourly interest rate in percentage

        # Create an instance of InvestmentPlan
        investment_plan = InvestmentPlan(minimum_deposit, duration_months, interest_rate)

        # Calculate interest and total investment value
        interest_earned = investment_plan.calculate_interest()
        total_value = investment_plan.total_investment_value()

        # Display results
        print(f"Interest Earned: {interest_earned:.2f}")
        print(f"Total Investment Value: {total_value:.2f}")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except RuntimeError as re:
        print(f"Calculation error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
