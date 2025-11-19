"""
Generated Code Metadata:
========================
Original URL: https://vantardxyz.web.app
Prompt: Generate code to calculate the surge tax for Vantard token redemptions based on the pricing model described, where the tax starts at 0% and increases to a maximum of 50% during high demand.
Generated: DETERMINISTIC_4c7e166ec7f09b44
Batch ID: 20250612_152954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Vantard Token Redemption Surge Tax Calculator

Calculates the surge tax for Vantard token redemptions based on a dynamic pricing model.
The tax starts at 0% and increases to a maximum of 50% during high demand.

Author: [Your Name]
Date: [Today's Date]
"""

class SurgeTaxCalculator:
    def __init__(self, base_tax_rate=0.0, max_tax_rate=0.5, demand_threshold=1000):
        """
        Initializes the SurgeTaxCalculator.

        Args:
            base_tax_rate (float, optional): The base tax rate (default: 0.0).
            max_tax_rate (float, optional): The maximum tax rate (default: 0.5).
            demand_threshold (int, optional): The demand threshold (default: 1000).
        """
        self.base_tax_rate = base_tax_rate
        self.max_tax_rate = max_tax_rate
        self.demand_threshold = demand_threshold

    def calculate_tax(self, redemption_amount, current_demand):
        """
        Calculates the surge tax for a given redemption amount and current demand.

        Args:
            redemption_amount (float): The amount of tokens being redeemed.
            current_demand (int): The current demand.

        Returns:
            float: The surge tax amount.

        Raises:
            ValueError: If redemption_amount or current_demand is negative.
        """
        if redemption_amount < 0 or current_demand < 0:
            raise ValueError("Redemption amount and current demand must be non-negative.")

        # Calculate the tax rate based on the current demand
        tax_rate = self.base_tax_rate + (self.max_tax_rate - self.base_tax_rate) * min(current_demand / self.demand_threshold, 1)

        # Calculate the surge tax amount
        surge_tax_amount = redemption_amount * tax_rate

        return surge_tax_amount

    def calculate_total_redeemed(self, redemption_amount, current_demand):
        """
        Calculates the total amount of tokens redeemed after surge tax.

        Args:
            redemption_amount (float): The amount of tokens being redeemed.
            current_demand (int): The current demand.

        Returns:
            float: The total amount of tokens redeemed after surge tax.

        Raises:
            ValueError: If redemption_amount or current_demand is negative.
        """
        surge_tax_amount = self.calculate_tax(redemption_amount, current_demand)
        total_redeemed = redemption_amount - surge_tax_amount

        return total_redeemed


def main():
    calculator = SurgeTaxCalculator()

    # Example usage:
    redemption_amount = 100.0
    current_demand = 500

    try:
        surge_tax_amount = calculator.calculate_tax(redemption_amount, current_demand)
        total_redeemed = calculator.calculate_total_redeemed(redemption_amount, current_demand)

        print(f"Redemption Amount: {redemption_amount}")
        print(f"Current Demand: {current_demand}")
        print(f"Surge Tax Amount: {surge_tax_amount:.2f}")
        print(f"Total Redeemed: {total_redeemed:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
