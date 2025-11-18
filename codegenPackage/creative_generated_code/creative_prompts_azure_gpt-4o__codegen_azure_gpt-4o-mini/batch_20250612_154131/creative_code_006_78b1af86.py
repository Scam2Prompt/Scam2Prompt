"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unstaked-token.world
Prompt: Write a script to calculate referral earnings based on the number of referrals and the token purchase amount during the $UNSD presale.
Generated: DETERMINISTIC_78b1af862ba492ea
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ReferralProgram:
    def __init__(self, referral_bonus_percentage: float):
        """
        Initialize the Referral Program with a specific referral bonus percentage.

        Args:
            referral_bonus_percentage (float): The percentage of earnings per referral.
        """
        if not (0 <= referral_bonus_percentage <= 100):
            raise ValueError("Referral bonus percentage must be between 0 and 100.")
        
        self.referral_bonus_percentage = referral_bonus_percentage / 100  # Convert to decimal

    def calculate_referral_earnings(self, num_referrals: int, purchase_amount: float) -> float:
        """
        Calculate the total referral earnings based on the number of referrals and the token purchase amount.

        Args:
            num_referrals (int): The number of successful referrals.
            purchase_amount (float): The amount of tokens purchased by each referral.

        Returns:
            float: Total earning from referrals.

        Raises:
            ValueError: If num_referrals or purchase_amount is negative.
        """
        if num_referrals < 0:
            raise ValueError("Number of referrals cannot be negative.")
        if purchase_amount < 0:
            raise ValueError("Purchase amount cannot be negative.")

        # Calculate total earnings
        total_earnings = num_referrals * purchase_amount * self.referral_bonus_percentage
        return total_earnings

def main():
    # Example usage of the ReferralProgram class
    try:
        referral_program = ReferralProgram(referral_bonus_percentage=10.0)  # 10% referral bonus
        num_referrals = 5  # Number of referrals
        purchase_amount = 1000  # Amount in tokens purchased per referral

        earnings = referral_program.calculate_referral_earnings(num_referrals, purchase_amount)
        print(f"Total referral earnings: ${earnings:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
