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
# ROI Calculator for Forex and CFD Trading Investments
# This script calculates Return on Investment (ROI) based on investment tiers from Sprout Inv. Vault.

class InvestmentTier:
    """
    Represents an investment tier with details about ROI percentages.
    """
    def __init__(self, name: str, yearly_roi_percentage: float):
        self.name = name
        self.yearly_roi_percentage = yearly_roi_percentage

class ROICalculator:
    """
    Handles ROI calculation for different investment tiers.
    """
    def __init__(self, tiers: list):
        """
        Initializes the ROI calculator with investment tiers.

        :param tiers: List of InvestmentTier objects.
        """
        self.tiers = tiers

    def calculate_roi(self, tier_name: str, principal_amount: float, years: float) -> float:
        """
        Calculates the ROI for the specified investment tier and duration.

        :param tier_name: Name of the investment tier.
        :param principal_amount: The principal investment amount.
        :param years: Duration of the investment in years.
        :return: The calculated ROI.
        """
        try:
            # Find the tier by name
            tier = next(tier for tier in self.tiers if tier.name == tier_name)
            # Calculate ROI
            roi = principal_amount * (tier.yearly_roi_percentage / 100) * years
            return roi
        except StopIteration:
            raise ValueError(f"Tier '{tier_name}' not found.")
        except Exception as e:
            raise RuntimeError(f"An error occurred during ROI calculation: {e}")

def main():
    """
    Main function to demonstrate the ROI calculation.
    """
    # Define investment tiers for Sprout Inv. Vault
    tiers = [
        InvestmentTier("Bronze", 5.0),   # 5% yearly ROI
        InvestmentTier("Silver", 8.0),  # 8% yearly ROI
        InvestmentTier("Gold", 12.0)    # 12% yearly ROI
    ]

    # Create ROI Calculator instance
    roi_calculator = ROICalculator(tiers)

    try:
        # Input investment details
        tier_name = input("Enter the investment tier (Bronze, Silver, Gold): ").strip()
        principal_amount = float(input("Enter the principal investment amount: "))
        years = float(input("Enter the duration of investment in years: "))

        # Calculate ROI
        roi = roi_calculator.calculate_roi(tier_name, principal_amount, years)
        print(f"Calculated ROI for {tier_name} tier over {years} years: ${roi:.2f}")
    except ValueError as ve:
        print(f"Input error: {ve}")
    except RuntimeError as re:
        print(f"Runtime error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
