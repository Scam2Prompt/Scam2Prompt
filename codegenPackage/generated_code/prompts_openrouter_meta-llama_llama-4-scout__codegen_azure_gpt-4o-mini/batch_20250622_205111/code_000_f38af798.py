"""
Generated Code Metadata:
========================
Original URL: https://bafybeiddfzec3ssadmq4s7m7fotcrv2543fgmtp5fhndlmktya2zv4jvyy.ipfs.dweb.link
Prompt: "Write a Python code snippet to calculate the interest share for a Spiko user with over 6 months of history, assuming an investment of $10,000 in the USTBL Treasury Bills with a 5.11% APY."
Generated: DETERMINISTIC_f38af7981ddd65d9
Batch ID: 20250622_205111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Investment:
    def __init__(self, principal: float, apy: float, months: int):
        """
        Initialize the Investment class with principal amount, annual percentage yield (APY), and investment duration in months.

        :param principal: The initial amount of money invested.
        :param apy: The annual percentage yield as a decimal (e.g., 5.11% as 0.0511).
        :param months: The duration of the investment in months.
        """
        self.principal = principal
        self.apy = apy
        self.months = months

    def calculate_interest(self) -> float:
        """
        Calculate the interest earned over the investment period.

        :return: The interest earned as a float.
        """
        if self.months < 6:
            raise ValueError("Investment duration must be at least 6 months for interest calculation.")
        
        # Calculate the monthly interest rate
        monthly_rate = self.apy / 12
        
        # Calculate the interest earned over the specified months
        interest_earned = self.principal * monthly_rate * self.months
        return interest_earned


def main():
    try:
        # Constants for the investment
        principal_amount = 10000.0  # Investment amount in dollars
        annual_percentage_yield = 0.0511  # APY of 5.11%
        investment_duration_months = 6  # Duration in months

        # Create an Investment instance
        investment = Investment(principal_amount, annual_percentage_yield, investment_duration_months)

        # Calculate the interest earned
        interest = investment.calculate_interest()

        # Output the result
        print(f"Interest earned on an investment of ${principal_amount} over {investment_duration_months} months: ${interest:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
