"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zenixglobaltrade.com.veritafinancebank.com
Prompt: Generate code to simulate investment plans with different ROI tiers (e.g., Starter, Classic, Professional, Premium) and instant withdrawal functionality, as outlined on ZenixGlobaltrade.
Generated: DETERMINISTIC_41fbd7854760d604
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from enum import Enum
from typing import List, Dict

# Enum to define different investment tiers
class InvestmentTier(Enum):
    STARTER = ("Starter", 0.05)
    CLASSIC = ("Classic", 0.1)
    PROFESSIONAL = ("Professional", 0.15)
    PREMIUM = ("Premium", 0.2)

    def __init__(self, name: str, roi: float):
        self.name = name
        self.roi = roi

# Class to represent an investment plan
class InvestmentPlan:
    def __init__(self, tier: InvestmentTier, initial_investment: float):
        self.tier = tier
        self.initial_investment = initial_investment
        self.current_value = initial_investment
        self.withdrawn_amount = 0.0

    def calculate_roi(self):
        """Calculate the return on investment based on the tier's ROI."""
        return self.current_value * self.tier.value[1]

    def apply_roi(self):
        """Apply the ROI to the current investment value."""
        roi = self.calculate_roi()
        self.current_value += roi

    def withdraw(self, amount: float):
        """Withdraw a specified amount from the investment plan."""
        if amount > self.current_value:
            raise ValueError("Withdrawal amount exceeds current investment value.")
        self.current_value -= amount
        self.withdrawn_amount += amount
        return amount

    def get_summary(self) -> Dict[str, float]:
        """Get a summary of the investment details."""
        return {
            'Tier': self.tier.name,
            'Initial Investment': self.initial_investment,
            'Current Value': self.current_value,
            'Withdrawn Amount': self.withdrawn_amount
        }

# Function to simulate investment over a period
def simulate_investment(tier: InvestmentTier, initial_investment: float, periods: int) -> List[Dict[str, float]]:
    """Simulate the investment growth and allow withdrawals over a specified number of periods."""
    investment_plan = InvestmentPlan(tier, initial_investment)
    results = []

    for period in range(periods):
        investment_plan.apply_roi()
        
        # Randomly decide to withdraw an amount (up to 50% of current value)
        if random.choice([True, False]):
            withdraw_amount = min(investment_plan.current_value * 0.5, 1000)  # Limit max withdrawal
            try:
                investment_plan.withdraw(withdraw_amount)
            except ValueError as e:
                print(f"Error during withdrawal: {e}")

        # Save the current state
        results.append(investment_plan.get_summary())

    return results

# Example usage
if __name__ == "__main__":
    tier = InvestmentTier.CLASSIC
    initial_investment = 5000.0
    investment_periods = 12  # Simulating for 12 periods (e.g., months)

    investment_results = simulate_investment(tier, initial_investment, investment_periods)

    # Print the investment summaries
    for month, summary in enumerate(investment_results, start=1):
        print(f"Month {month}: {summary}")
```
