"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://futurespaceinvestment.com
Prompt: Write a Python script that automates the referral commission calculation for FutureSpaceInvestments, including support for 3.5%, 5%, and 7% commission tiers based on the first capital invested by referred users.
Generated: DETERMINISTIC_ee3b4e1546fec15b
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_commission_calculator.py

class ReferralCommissionCalculator:
    """
    A class to calculate referral commissions based on the first capital invested by referred users.
    
    Attributes:
        commission_tiers (dict): A dictionary mapping investment thresholds to commission rates.
    """

    def __init__(self):
        # Define commission tiers: investment threshold (in currency) to commission rate (in percentage)
        self.commission_tiers = {
            1000: 0.035,  # 3.5% for investments of at least $1000
            5000: 0.05,   # 5% for investments of at least $5000
            10000: 0.07   # 7% for investments of at least $10000
        }

    def calculate_commission(self, investment):
        """
        Calculate the commission based on the investment amount.
        
        Parameters:
            investment (float): The amount of capital invested by the referred user.
        
        Returns:
            float: The calculated commission, or raises ValueError if investment is negative.
        """
        if investment < 0:
            raise ValueError("Investment cannot be negative.")

        commission_rate = 0
        # Determine the applicable commission rate based on the investment amount
        for threshold, rate in sorted(self.commission_tiers.items(), reverse=True):
            if investment >= threshold:
                commission_rate = rate
                break
        
        # Calculate the commission
        commission = investment * commission_rate
        return commission

    def display_commission(self, investment):
        """
        Display the calculated commission for the given investment.
        
        Parameters:
            investment (float): The amount of capital invested by the referred user.
        """
        try:
            commission = self.calculate_commission(investment)
            print(f"Investment: ${investment:.2f}, Commission: ${commission:.2f} at rate {commission * 100 / investment:.2f}%")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    # Example usage of the ReferralCommissionCalculator
    calculator = ReferralCommissionCalculator()
    
    # List of example investments to calculate commissions for
    example_investments = [500, 1500, 5500, 12000, -300]

    for investment in example_investments:
        calculator.display_commission(investment)
```
