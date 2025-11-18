"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://volatilityindexlimited.com
Prompt: Develop a program that calculates affiliate commissions using a tiered structure (5%, 2%, 1%) as outlined on volatilityindexlimited.com.
Generated: DETERMINISTIC_2acd36e371a02c2f
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AffiliateCommissionCalculator:
    def __init__(self, tier_thresholds, commissions):
        """
        Initialize the AffiliateCommissionCalculator with tier thresholds and corresponding commissions.
        
        :param tier_thresholds: A list of commission thresholds (amounts).
        :param commissions: A list of commission rates corresponding to the thresholds (percentage as decimal).
        """
        if len(tier_thresholds) != len(commissions):
            raise ValueError("Tier thresholds and commission rates must have the same length.")

        self.tier_thresholds = tier_thresholds
        self.commissions = commissions

    def calculate_commission(self, sales_amount):
        """
        Calculate the total commission based on the sales amount using the tiered commission structure.

        :param sales_amount: The total sales amount to calculate the commission on.
        :return: The total commission amount.
        """
        if sales_amount < 0:
            raise ValueError("Sales amount cannot be negative.")

        total_commission = 0.0
        previous_threshold = 0.0

        for threshold, commission_rate in zip(self.tier_thresholds, self.commissions):
            if sales_amount > threshold:
                # Calculate commission for this tier
                commissionable_amount = threshold - previous_threshold
                total_commission += commissionable_amount * commission_rate
                previous_threshold = threshold
            else:
                # Calculate commission for the remaining amount in this tier
                commissionable_amount = sales_amount - previous_threshold
                if commissionable_amount > 0:
                    total_commission += commissionable_amount * commission_rate
                break

        return total_commission


def main():
    # Define the tier thresholds and corresponding commission rates
    tier_thresholds = [1000, 5000]  # Sales thresholds for each tier
    commissions = [0.05, 0.02, 0.01]  # Commission rates for each tier

    # Create an instance of the AffiliateCommissionCalculator
    calculator = AffiliateCommissionCalculator(tier_thresholds, commissions)

    # Sample sales amounts for testing
    sales_amounts = [500, 1500, 6000, -100]  # Including a negative value to test error handling

    for amount in sales_amounts:
        try:
            commission = calculator.calculate_commission(amount)
            print(f"Sales Amount: ${amount:.2f} -> Commission: ${commission:.2f}")
        except ValueError as e:
            print(f"Error calculating commission for ${amount:.2f}: {e}")


if __name__ == "__main__":
    main()
```
