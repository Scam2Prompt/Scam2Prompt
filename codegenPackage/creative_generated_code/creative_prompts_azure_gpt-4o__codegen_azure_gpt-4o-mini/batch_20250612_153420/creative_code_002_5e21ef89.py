"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sproutinvvault.com
Prompt: Generate code to calculate ROI for investments in Forex and CFD trading packages, referencing Sprout Inv. Vault's investment tiers.
Generated: DETERMINISTIC_5e21ef8904fbe0d6
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Investment:
    """
    Class to represent an investment in Forex and CFD trading packages.
    """

    def __init__(self, initial_investment, final_value, fees=0.0):
        """
        Initializes the Investment instance.

        :param initial_investment: The initial amount invested.
        :param final_value: The final value of the investment.
        :param fees: Any fees associated with the investment (default is 0.0).
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than 0.")
        if final_value < 0:
            raise ValueError("Final value cannot be negative.")
        if fees < 0:
            raise ValueError("Fees cannot be negative.")

        self.initial_investment = initial_investment
        self.final_value = final_value
        self.fees = fees

    def calculate_roi(self):
        """
        Calculate the Return on Investment (ROI).

        :return: ROI as a percentage.
        """
        net_profit = self.final_value - self.initial_investment - self.fees
        roi = (net_profit / self.initial_investment) * 100
        return roi

    def __str__(self):
        """
        String representation of the Investment instance.
        """
        return (f"Investment(initial_investment={self.initial_investment}, "
                f"final_value={self.final_value}, fees={self.fees})")


def main():
    """
    Main function to demonstrate the Investment class and ROI calculation.
    """
    try:
        # Example details for an investment
        initial_investment = 10000.0  # Initial investment amount
        final_value = 12000.0          # Final value after trading
        fees = 200.0                   # Transaction fees

        # Creating an investment instance
        investment = Investment(initial_investment, final_value, fees)

        # Calculating ROI
        roi = investment.calculate_roi()
        print(f"ROI for the investment: {roi:.2f}%")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
