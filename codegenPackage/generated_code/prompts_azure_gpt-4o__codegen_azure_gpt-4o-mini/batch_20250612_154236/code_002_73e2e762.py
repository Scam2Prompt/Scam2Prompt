"""
Generated Code Metadata:
========================
Original URL: https://centraltraderz.com
Prompt: Create a function to simulate the dividend calculation for the Centraltraderz investment plans, incorporating the specific percentages and durations mentioned on the site.
Generated: DETERMINISTIC_73e2e762f1fba3da
Batch ID: 20250612_154236
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
    A class to represent an investment plan for Centraltraderz.
    """

    def __init__(self, principal: float, duration: int, rate: float):
        """
        Initializes the investment plan with principal amount, duration, and rate of return.

        :param principal: The initial amount of money invested.
        :param duration: The duration of the investment in years.
        :param rate: The annual rate of return as a percentage (e.g., 5 for 5%).
        """
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if duration <= 0:
            raise ValueError("Duration must be greater than zero.")
        if rate < 0:
            raise ValueError("Rate must be non-negative.")

        self.principal = principal
        self.duration = duration
        self.rate = rate / 100  # Convert percentage to decimal

    def calculate_dividend(self) -> float:
        """
        Calculates the total dividend earned over the investment duration.

        :return: The total dividend earned.
        """
        total_dividend = self.principal * (1 + self.rate) ** self.duration - self.principal
        return total_dividend

def simulate_investment(principal: float, duration: int, rate: float) -> float:
    """
    Simulates the dividend calculation for a given investment plan.

    :param principal: The initial amount of money invested.
    :param duration: The duration of the investment in years.
    :param rate: The annual rate of return as a percentage.
    :return: The total dividend earned.
    """
    try:
        investment_plan = InvestmentPlan(principal, duration, rate)
        return investment_plan.calculate_dividend()
    except ValueError as e:
        print(f"Error: {e}")
        return 0.0  # Return 0.0 in case of an error

# Example usage:
if __name__ == "__main__":
    principal_amount = 1000.0  # Example principal amount
    investment_duration = 5     # Example duration in years
    annual_rate = 5             # Example annual rate of return in percentage

    dividend = simulate_investment(principal_amount, investment_duration, annual_rate)
    print(f"Total dividend earned: ${dividend:.2f}")
```
