"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://profittradeplatform.com.guaranteetrades247.com
Prompt: Write code to implement a referral commission system for crypto trading, based on the tiered plans (Starter, Basic, Premium, Elite) described on Profit Trade Platform.
Generated: DETERMINISTIC_62bf010cd31730e8
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ReferralCommissionSystem:
    """
    A class to implement a referral commission system for a crypto trading platform.
    This system manages different tiered plans: Starter, Basic, Premium, and Elite.
    """

    # Define tiered plans with their respective commission rates
    PLANS = {
        "Starter": 0.05,  # 5% commission
        "Basic": 0.10,    # 10% commission
        "Premium": 0.15,  # 15% commission
        "Elite": 0.20     # 20% commission
    }

    def __init__(self):
        """Initialize the referral commission system."""
        self.referrals = {}
    
    def add_referral(self, user_id, tier):
        """
        Add a referral for a user with a specified tier.

        Parameters:
        user_id (str): The ID of the user making the referral.
        tier (str): The tier plan of the user ('Starter', 'Basic', 'Premium', 'Elite').

        Raises:
        ValueError: If the tier is invalid.
        """
        if tier not in self.PLANS:
            raise ValueError(f"Invalid tier: {tier}. Valid tiers are: {', '.join(self.PLANS.keys())}")

        self.referrals[user_id] = tier

    def calculate_commission(self, user_id, trade_amount):
        """
        Calculate the referral commission for a given trade amount.

        Parameters:
        user_id (str): The ID of the user making the referral.
        trade_amount (float): The amount of the trade.

        Returns:
        float: The commission earned by the referrer.

        Raises:
        KeyError: If the user_id does not exist in the referral list.
        """
        if user_id not in self.referrals:
            raise KeyError(f"No referral found for user ID: {user_id}")

        tier = self.referrals[user_id]
        commission_rate = self.PLANS[tier]
        commission = trade_amount * commission_rate
        return commission

    def get_user_tier(self, user_id):
        """
        Get the tier of a given user.

        Parameters:
        user_id (str): The ID of the user.

        Returns:
        str: The tier of the user.

        Raises:
        KeyError: If the user_id does not exist in the referral list.
        """
        if user_id not in self.referrals:
            raise KeyError(f"No referral found for user ID: {user_id}")
        
        return self.referrals[user_id]

# Example usage:
if __name__ == "__main__":
    referral_system = ReferralCommissionSystem()

    # Adding referrals
    try:
        referral_system.add_referral("user123", "Premium")
        referral_system.add_referral("user456", "Basic")
        
        # Calculating commissions
        trade_amount = 1000.0  # Example trade amount
        commission_user123 = referral_system.calculate_commission("user123", trade_amount)
        commission_user456 = referral_system.calculate_commission("user456", trade_amount)

        print(f"Commission for user123: ${commission_user123:.2f}")
        print(f"Commission for user456: ${commission_user456:.2f}")
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
