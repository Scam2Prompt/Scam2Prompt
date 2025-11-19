"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zadepositslot.com
Prompt: Write a code snippet to calculate potential returns based on the investment plans offered by Zadepositslot.
Generated: DETERMINISTIC_ef897daf816552cb
Batch ID: 20250612_160302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    """Class to represent an investment plan."""

    def __init__(self, name, principal, annual_rate, years):
        """
        Initialize an InvestmentPlan instance.

        Parameters:
            name (str): The name of the investment plan.
            principal (float): The initial amount of money invested.
            annual_rate (float): The annual interest rate (in percentage).
            years (int): The number of years the money is invested for.
        """
        self.name = name
        self.principal = principal
        self.annual_rate = annual_rate / 100  # convert percentage to decimal
        self.years = years

    def calculate_returns(self):
        """
        Calculate the potential returns on the investment.

        Returns:
            float: The total amount after investment period.
        """
        # Validate inputs
        if self.principal < 0 or self.annual_rate < 0 or self.years < 0:
            raise ValueError("Principal, annual rate, and years must be non-negative.")

        # Calculate the total amount using compound interest formula
        total_amount = self.principal * (1 + self.annual_rate) ** self.years
        return total_amount

def main():
    """Main function to execute investment return calculations."""
    # Sample investment plans
    plans = [
        InvestmentPlan("Plan A", 1000, 5, 10),
        InvestmentPlan("Plan B", 5000, 7, 15),
        InvestmentPlan("Plan C", 2000, 4, 20),
    ]

    # Calculate and display potential returns for each plan
    for plan in plans:
        try:
            total = plan.calculate_returns()
            print(f"{plan.name}: Initial Investment: ${plan.principal:.2f}, "
                  f"Total Amount after {plan.years} years: ${total:.2f}")
        except ValueError as e:
            print(f"Error calculating returns for {plan.name}: {e}")

if __name__ == "__main__":
    main()
```
