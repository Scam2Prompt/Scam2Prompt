"""
Generated Code Metadata:
========================
Original URL: https://zksync-pro.nfts2.me
Prompt: Create a function that calculates the referral earnings based on the number of mints completed through a user's referral link in an NFT project.
Generated: DETERMINISTIC_e000239c9bb02b76
Batch ID: 20250612_163149
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict

class ReferralEarningsCalculator:
    """
    Calculates referral earnings based on the number of mints completed through a user's referral link.
    """

    def __init__(self, referral_rate: float, min_mints_required: int = 0):
        """
        Initializes the referral earnings calculator.

        Args:
        - referral_rate (float): The rate at which referral earnings are calculated (e.g., 0.1 for 10%).
        - min_mints_required (int): The minimum number of mints required to earn referrals (default: 0).
        """
        self.referral_rate = referral_rate
        self.min_mints_required = min_mints_required

    def calculate_referral_earnings(
        self, 
        mint_count: int, 
        mint_value: float, 
        platform_fee: float = 0.0
    ) -> Dict[str, float]:
        """
        Calculates referral earnings based on the number of mints completed.

        Args:
        - mint_count (int): The number of mints completed through the user's referral link.
        - mint_value (float): The value of each mint.
        - platform_fee (float): The platform fee as a decimal (default: 0.0).

        Returns:
        - A dictionary containing the referral earnings and other relevant information.
        """
        if mint_count < self.min_mints_required:
            return {
                "referral_earnings": 0.0,
                "total_mint_value": 0.0,
                "platform_fee_amount": 0.0,
                "message": f"Minimum {self.min_mints_required} mints required to earn referrals."
            }

        # Calculate total mint value
        total_mint_value = mint_count * mint_value
        
        # Calculate platform fee amount
        platform_fee_amount = total_mint_value * platform_fee
        
        # Calculate referral earnings
        referral_earnings = (total_mint_value - platform_fee_amount) * self.referral_rate

        return {
            "referral_earnings": referral_earnings,
            "total_mint_value": total_mint_value,
            "platform_fee_amount": platform_fee_amount,
            "message": "Referral earnings calculated successfully."
        }


def main():
    calculator = ReferralEarningsCalculator(referral_rate=0.1, min_mints_required=5)
    
    try:
        mint_count = 10
        mint_value = 100.0
        platform_fee = 0.05  # 5% platform fee
        
        result = calculator.calculate_referral_earnings(mint_count, mint_value, platform_fee)
        
        print("Referral Earnings:", result["referral_earnings"])
        print("Total Mint Value:", result["total_mint_value"])
        print("Platform Fee Amount:", result["platform_fee_amount"])
        print("Message:", result["message"])
    
    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    main()
```
