"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitbullminingpro.com
Prompt: Write code to implement a referral program system with tiered income levels, similar to the one offered by BitBullMiningPro.
Generated: DETERMINISTIC_f2c933653963d0ee
Batch ID: 20250612_150130
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
    A class to represent a referral program with tiered income levels.
    """

    def __init__(self):
        """
        Initializes the referral program with predefined tier levels and earnings.
        """
        self.tiers = {
            1: 0.05,  # Tier 1: 5% commission
            2: 0.07,  # Tier 2: 7% commission
            3: 0.10   # Tier 3: 10% commission
        }
        self.referrals = {}  # To store referrals and their levels

    def add_referral(self, referrer_id, referral_id, tier_level):
        """
        Adds a referral to the program.

        :param referrer_id: The ID of the person who referred.
        :param referral_id: The ID of the new referral.
        :param tier_level: The tier level of the referral.
        :raises ValueError: If the tier level is not valid.
        """
        if tier_level not in self.tiers:
            raise ValueError("Invalid tier level. Valid levels are: {}".format(list(self.tiers.keys())))
        
        # Store the referral and its tier level
        self.referrals[referral_id] = {
            'referrer': referrer_id,
            'tier_level': tier_level
        }

    def calculate_commission(self, referral_id, amount):
        """
        Calculates the commission for a given referral based on the tier level.

        :param referral_id: The ID of the referral for which to calculate commission.
        :param amount: The amount on which the commission is to be calculated.
        :return: Calculated commission amount.
        :raises ValueError: If the referral ID is not found.
        """
        if referral_id not in self.referrals:
            raise ValueError("Referral ID not found: {}".format(referral_id))
        
        tier_level = self.referrals[referral_id]['tier_level']
        commission_rate = self.tiers[tier_level]
        commission = amount * commission_rate
        return commission

    def get_referral_info(self, referral_id):
        """
        Retrieves information about a specific referral.

        :param referral_id: The ID of the referral to retrieve information for.
        :return: A dictionary containing referrer ID and tier level.
        :raises ValueError: If the referral ID is not found.
        """
        if referral_id not in self.referrals:
            raise ValueError("Referral ID not found: {}".format(referral_id))
        
        return self.referrals[referral_id]

# Example usage
if __name__ == "__main__":
    program = ReferralProgram()
    try:
        program.add_referral('user123', 'user456', 1)  # Adding a referral
        commission = program.calculate_commission('user456', 1000)  # Calculate commission for a user
        print("Commission Earned:", commission)  # Output: Commission Earned: 50.0
        referral_info = program.get_referral_info('user456')
        print("Referral Info:", referral_info)  # Output: Referral Info: {'referrer': 'user123', 'tier_level': 1}
    except ValueError as e:
        print("Error:", e)
```
