"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stake-roost.pages.dev
Prompt: Create a function to calculate the presale breakdown of funds, splitting the raise into 50% for liquidity pool and 50% for expenses, development, and distribution, as described in the $ROOST presale breakdown.
Generated: DETERMINISTIC_976eab4567978cc4
Batch ID: 20250612_151057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PresaleBreakdown:
    def __init__(self, total_raised: float):
        """
        Initializes the PresaleBreakdown with the total amount raised.

        :param total_raised: The total funds raised in the presale.
        """
        if total_raised < 0:
            raise ValueError("Total raised amount must be non-negative.")

        self.total_raised = total_raised

    def calculate_breakdown(self):
        """
        Calculates the presale fund breakdown.

        :return: A dictionary containing the breakdown of funds.
        """
        # Split the total raised into two main categories
        liquidity_pool = self.total_raised * 0.50
        expenses_and_development = self.total_raised * 0.50

        # Further breakdown of expenses and development
        expenses_distribution = {
            "expenses": expenses_and_development * 0.40,   # 40% for expenses
            "development": expenses_and_development * 0.30, # 30% for development
            "distribution": expenses_and_development * 0.30  # 30% for distribution
        }

        # Constructing the result
        breakdown = {
            "liquidity_pool": liquidity_pool,
            "expenses_and_development": expenses_distribution
        }

        return breakdown

# Example usage:
if __name__ == "__main__":
    try:
        total_raised_amount = 1000000  # Example total raised amount
        presale = PresaleBreakdown(total_raised_amount)
        breakdown = presale.calculate_breakdown()
        print(breakdown)
    except ValueError as e:
        print(f"Error: {e}")
```
