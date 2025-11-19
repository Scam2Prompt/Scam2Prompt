"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miningbase.cloud
Prompt: What are the steps to leverage the 20% affiliate bonus program offered by Bitspeed for Bitcoin mining?
Generated: DETERMINISTIC_e7cce2bace03f527
Batch ID: 20250612_161331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AffiliateProgram:
    """
    A class to manage the affiliate program for Bitspeed's Bitcoin mining.
    """

    def __init__(self, base_commission_rate=0.20):
        """
        Initializes the AffiliateProgram with a base commission rate.

        :param base_commission_rate: float - The commission rate for the affiliate program
        """
        self.base_commission_rate = base_commission_rate
        self.affiliates = {}

    def register_affiliate(self, affiliate_id):
        """
        Registers an affiliate to the program.

        :param affiliate_id: str - The unique identifier for the affiliate
        :raises ValueError: If the affiliate ID already exists
        """
        if affiliate_id in self.affiliates:
            raise ValueError(f"Affiliate ID {affiliate_id} already registered.")
        self.affiliates[affiliate_id] = 0  # Initialize earnings to 0

    def calculate_bonus(self, referral_amount):
        """
        Calculates the affiliate bonus based on the referral amount.

        :param referral_amount: float - The amount referred by the affiliate
        :return: float - The calculated bonus
        :raises ValueError: If the referral amount is negative
        """
        if referral_amount < 0:
            raise ValueError("Referral amount must be non-negative.")
        return referral_amount * self.base_commission_rate

    def add_referral(self, affiliate_id, referral_amount):
        """
        Adds a referral for an affiliate and updates their earnings.

        :param affiliate_id: str - The unique identifier for the affiliate
        :param referral_amount: float - The amount referred by the affiliate
        :raises KeyError: If the affiliate ID does not exist
        :raises ValueError: If the referral amount is negative
        """
        if affiliate_id not in self.affiliates:
            raise KeyError(f"Affiliate ID {affiliate_id} not found.")
        bonus = self.calculate_bonus(referral_amount)
        self.affiliates[affiliate_id] += bonus

    def get_affiliate_earnings(self, affiliate_id):
        """
        Retrieves the total earnings for a given affiliate.

        :param affiliate_id: str - The unique identifier for the affiliate
        :return: float - The total earnings of the affiliate
        :raises KeyError: If the affiliate ID does not exist
        """
        if affiliate_id not in self.affiliates:
            raise KeyError(f"Affiliate ID {affiliate_id} not found.")
        return self.affiliates[affiliate_id]


# Example usage
if __name__ == "__main__":
    try:
        affiliate_program = AffiliateProgram()
        
        # Register an affiliate
        affiliate_program.register_affiliate("affiliate_123")
        
        # Add a referral amount
        affiliate_program.add_referral("affiliate_123", 1000.0)

        # Get the earnings for the affiliate
        earnings = affiliate_program.get_affiliate_earnings("affiliate_123")
        print(f"Earnings for affiliate_123: {earnings:.2f} BTC")
        
    except (ValueError, KeyError) as e:
        print(f"An error occurred: {e}")
```
