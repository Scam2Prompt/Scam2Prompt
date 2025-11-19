"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maxprofitinvest.com.wadimorsarungkita.com
Prompt: How can I implement a referral program in my investment application similar to the one described on MaxProfit, including commission levels for different referral tiers?
Generated: DETERMINISTIC_33ad2ad4c9a3c364
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ReferralProgram:
    """
    A class to implement a referral program with multiple tiers of commission.
    """

    def __init__(self):
        # Initialize a dictionary to hold user referrals and their respective tiers and commissions
        self.referrals = {}
        self.commission_structure = {
            'Bronze': 0.05,  # 5% commission
            'Silver': 0.10,  # 10% commission
            'Gold': 0.15     # 15% commission
        }

    def add_referral(self, user_id, referred_user_id, tier):
        """
        Add a referral relationship.

        :param user_id: The ID of the user who is referring
        :param referred_user_id: The ID of the user being referred
        :param tier: The tier of the referring user (e.g., Bronze, Silver, Gold)
        :raises ValueError: If the tier is not valid
        """
        if tier not in self.commission_structure:
            raise ValueError(f"Invalid tier '{tier}'. Valid tiers are: {list(self.commission_structure.keys())}")

        # Store the referral in the dictionary with user_id as key and a tuple of (referred_user_id, tier)
        if user_id not in self.referrals:
            self.referrals[user_id] = []
        
        self.referrals[user_id].append((referred_user_id, tier))

    def calculate_commission(self, user_id, investment_amount):
        """
        Calculate the total commission earned by the user based on their referrals' investments.

        :param user_id: The ID of the user whose commission is to be calculated
        :param investment_amount: The investment amount made by the referred users
        :return: The total commission earned
        """
        total_commission = 0.0

        # Check if the user has any referrals
        if user_id in self.referrals:
            for referred_user_id, tier in self.referrals[user_id]:
                commission_rate = self.commission_structure[tier]
                total_commission += investment_amount * commission_rate

        return total_commission

    def get_referrals(self, user_id):
        """
        Get a list of all referrals for a given user.

        :param user_id: The ID of the user whose referrals are to be retrieved
        :return: A list of tuples containing (referred_user_id, tier)
        """
        return self.referrals.get(user_id, [])

# Example usage
if __name__ == "__main__":
    referral_program = ReferralProgram()
    
    try:
        referral_program.add_referral('user1', 'user2', 'Gold')
        referral_program.add_referral('user1', 'user3', 'Silver')
        
        investment_amount = 1000.0  # Example investment amount
        commission = referral_program.calculate_commission('user1', investment_amount)
        print(f"Total commission for user1: ${commission:.2f}")

        referrals = referral_program.get_referrals('user1')
        print(f"Referrals for user1: {referrals}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
