"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-evex.io
Prompt: How can I write a Python script to calculate compound interest based on the principles outlined by Arbiquant?
Generated: DETERMINISTIC_ca4d32afa7f0d75a
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CompoundInterestCalculator:
    """
    A class to calculate compound interest based on the principles outlined by Arbiquant.
    """

    def __init__(self, principal: float, rate: float, time: int, compounding_frequency: int):
        """
        Initializes the calculator with the principal, rate of interest, 
        time in years, and compounding frequency.

        :param principal: Initial amount of money (the principal)
        :param rate: Annual interest rate (in percentage)
        :param time: Time the money is invested or borrowed for (in years)
        :param compounding_frequency: Number of times that interest is compounded per year
        """
        if principal < 0:
            raise ValueError("Principal amount cannot be negative.")
        if rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        if time < 0:
            raise ValueError("Time cannot be negative.")
        if compounding_frequency <= 0:
            raise ValueError("Compounding frequency must be a positive integer.")

        self.principal = principal
        self.rate = rate / 100  # Convert percentage to decimal
        self.time = time
        self.compounding_frequency = compounding_frequency

    def calculate_compound_interest(self) -> float:
        """
        Calculates the compound interest.

        :return: The total amount after interest
        """
        try:
            amount = self.principal * (1 + self.rate / self.compounding_frequency) ** (self.compounding_frequency * self.time)
            return amount
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating compound interest: {e}")

    def calculate_interest(self) -> float:
        """
        Calculates the interest earned over the period.

        :return: The interest earned
        """
        total_amount = self.calculate_compound_interest()
        interest = total_amount - self.principal
        return interest


if __name__ == "__main__":
    try:
        # Example parameters for the calculation
        principal_amount = 1000.00  # Principal amount
        annual_rate = 5.0            # Annual interest rate in percentage
        investment_time = 10          # Time in years
        compounding_periods = 4       # Compounding quarterly

        # Create an instance of CompoundInterestCalculator
        calculator = CompoundInterestCalculator(principal_amount, annual_rate, investment_time, compounding_periods)

        # Calculate the total amount and interest earned
        total_amount = calculator.calculate_compound_interest()
        interest_earned = calculator.calculate_interest()

        print(f"Total amount after {investment_time} years: ${total_amount:.2f}")
        print(f"Total interest earned: ${interest_earned:.2f}")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except RuntimeError as re:
        print(f"Calculation error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
