"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://centraltraderz.com
Prompt: Create a function to simulate the dividend calculation for the Centraltraderz investment plans, incorporating the specific percentages and durations mentioned on the site.
Generated: DETERMINISTIC_73e2e762f1fba3da
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    def __init__(self, principal, duration_months):
        """
        Initializes the InvestmentPlan with a principal amount and duration.

        :param principal: The initial investment amount (float).
        :param duration_months: The duration of the investment in months (int).
        """
        self.principal = principal
        self.duration_months = duration_months

    def calculate_dividend(self):
        """
        Calculates the total dividend based on the investment plan.

        :return: Total dividend earned (float).
        :raises ValueError: If principal or duration_months is negative.
        """
        if self.principal < 0 or self.duration_months < 0:
            raise ValueError("Principal and duration must be non-negative.")

        # Define the dividend rates for different durations
        dividend_rates = {
            6: 0.05,   # 5% for 6 months
            12: 0.10,  # 10% for 12 months
            24: 0.20   # 20% for 24 months
        }

        # Determine the applicable dividend rate
        rate = dividend_rates.get(self.duration_months, 0)

        # Calculate total dividend
        total_dividend = self.principal * rate

        return total_dividend

def main():
    """
    Main function to run the investment plan simulation.
    """
    try:
        # Example usage
        plan = InvestmentPlan(principal=1000.0, duration_months=12)
        dividend = plan.calculate_dividend()
        print(f"Total dividend earned: ${dividend:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
