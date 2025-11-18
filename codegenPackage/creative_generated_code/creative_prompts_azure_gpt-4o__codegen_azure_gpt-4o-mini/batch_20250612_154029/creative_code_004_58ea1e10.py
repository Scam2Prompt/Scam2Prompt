"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zksync-pro.nfts2.me
Prompt: Implement a function to calculate referral fees for NFT mints completed via a referral link on the ZKsync Era chain, using the reward structure described on NFTs2Me.com.
Generated: DETERMINISTIC_58ea1e1016db2b43
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from decimal import Decimal, InvalidOperation

class ReferralFeeCalculator:
    def __init__(self, base_fee: Decimal, tier_structure: dict):
        """
        Initializes the ReferralFeeCalculator with a base fee and tier structure.

        :param base_fee: The base fee for calculating referral rewards.
        :param tier_structure: A dictionary defining the tier structure for referral rewards.
        """
        self.base_fee = base_fee
        self.tier_structure = tier_structure

    def calculate_fee(self, mint_amount: Decimal, referrer_tier: str) -> Decimal:
        """
        Calculates the referral fee based on the mint amount and the referrer's tier.

        :param mint_amount: The amount for which the NFT mint fee is calculated.
        :param referrer_tier: The tier of the referrer (e.g., 'bronze', 'silver', 'gold').
        :return: The calculated referral fee as a Decimal.
        :raises ValueError: If the mint amount is negative or the referrer tier is invalid.
        """
        if mint_amount < 0:
            raise ValueError("Mint amount cannot be negative.")

        if referrer_tier not in self.tier_structure:
            raise ValueError(f"Invalid referrer tier: {referrer_tier}")

        # Calculate the referral fee
        tier_percentage = self.tier_structure[referrer_tier]
        referral_fee = mint_amount * (tier_percentage / Decimal('100'))
        return referral_fee

def main():
    """
    Main function to demonstrate the usage of ReferralFeeCalculator.
    """
    # Define the base fee and tier structure
    base_fee = Decimal('0.01')  # Example base fee per mint
    tier_structure = {
        'bronze': Decimal('5'),
        'silver': Decimal('10'),
        'gold': Decimal('15'),
    }

    # Instantiate the ReferralFeeCalculator
    calculator = ReferralFeeCalculator(base_fee, tier_structure)

    # Example mint amount and referrer tier
    mint_amount = Decimal('100')  # Sample mint amount
    referrer_tier = 'silver'       # Sample referrer tier

    try:
        # Calculate the referral fee
        fee = calculator.calculate_fee(mint_amount, referrer_tier)
        print(f"Referral fee for {referrer_tier} tier on mints of {mint_amount}: {fee}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
