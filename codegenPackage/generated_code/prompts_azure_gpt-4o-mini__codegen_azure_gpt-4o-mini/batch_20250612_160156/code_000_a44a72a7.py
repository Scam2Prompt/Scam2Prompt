"""
Generated Code Metadata:
========================
Original URL: https://safewealthhaven.com.bartercorebase.com
Prompt: Generate a Python script that calculates potential returns based on the investment plans offered by Safe Wealth Haven, including the Silver, Gold, and Platinum plans.
Generated: DETERMINISTIC_a44a72a7fae859a1
Batch ID: 20250612_160156
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
    A class to represent an investment plan.
    """

    def __init__(self, name, principal, rate_of_return, duration):
        """
        Initializes an investment plan with the given parameters.

        :param name: Name of the investment plan
        :param principal: Initial amount invested
        :param rate_of_return: Annual rate of return (as a percentage)
        :param duration: Duration of the investment in years
        """
        self.name = name
        self.principal = principal
        self.rate_of_return = rate_of_return / 100  # Convert percentage to decimal
        self.duration = duration

    def calculate_return(self):
        """
        Calculates the total return on investment after the specified duration.

        :return: Total amount after investment duration
        """
        try:
            total_amount = self.principal * (1 + self.rate_of_return) ** self.duration
            return total_amount
        except Exception as e:
            print(f"Error calculating return for {self.name}: {e}")
            return None


def main():
    """
    Main function to execute the investment return calculations.
    """
    # Define investment plans
    plans = [
        InvestmentPlan("Silver", principal=1000, rate_of_return=5, duration=5),
        InvestmentPlan("Gold", principal=5000, rate_of_return=7, duration=10),
        InvestmentPlan("Platinum", principal=10000, rate_of_return=10, duration=15)
    ]

    # Calculate and display returns for each plan
    for plan in plans:
        total_return = plan.calculate_return()
        if total_return is not None:
            print(f"Total return for {plan.name} plan after {plan.duration} years: ${total_return:.2f}")


if __name__ == "__main__":
    main()
```
