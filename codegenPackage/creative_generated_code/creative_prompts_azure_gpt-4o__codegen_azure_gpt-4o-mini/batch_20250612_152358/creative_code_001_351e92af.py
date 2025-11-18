"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://largeoptions.org
Prompt: Generate code to simulate the referral commission system described on largeoptions.org, including tiered percentages (e.g., 6%, 8%, 10%, etc.) and instant payouts.
Generated: DETERMINISTIC_351e92af945d48b5
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ReferralCommissionSystem:
    def __init__(self):
        # Initialize the commission tiers as a list of tuples (min_level, commission_percentage)
        self.commission_tiers = [
            (1, 6),
            (2, 8),
            (3, 10),
            # Add more tiers as necessary
        ]
        self.referrals = {}  # Store referrals and their associated earnings

    def add_referral(self, referrer_id, referral_id):
        """
        Add a referral to the system.
        
        :param referrer_id: ID of the person who referred
        :param referral_id: ID of the newly referred person
        """
        if referrer_id not in self.referrals:
            self.referrals[referrer_id] = {'earnings': 0, 'referrals': []}
        
        self.referrals[referrer_id]['referrals'].append(referral_id)

    def calculate_commission(self, referrer_id, level):
        """
        Calculate the commission based on referral level.
        
        :param referrer_id: ID of the person who referred
        :param level: Level of the referral
        :return: Commission percentage for the given level
        """
        for min_level, commission_percentage in self.commission_tiers:
            if level >= min_level:
                return commission_percentage
        return 0  # Default commission if no tier matches

    def payout_commission(self, referrer_id, amount, referral_level):
        """
        Payout the commission to the referrer based on the referral level.
        
        :param referrer_id: ID of the person who referred
        :param amount: Amount earned by the referral
        :param referral_level: Level of the referral
        :raises ValueError: If referrer_id is not in the system
        """
        if referrer_id not in self.referrals:
            raise ValueError("Referrer ID not found in the system.")
        
        commission_percentage = self.calculate_commission(referrer_id, referral_level)
        commission_earned = (commission_percentage / 100) * amount
        
        # Update earnings for the referrer
        self.referrals[referrer_id]['earnings'] += commission_earned

        # Simulate instant payout
        self.instant_payout(referrer_id, commission_earned)

    def instant_payout(self, referrer_id, commission_earned):
        """
        Process the instant payout for the referrer.
        
        :param referrer_id: ID of the person to receive the payout
        :param commission_earned: Amount to payout
        """
        print(f"Instant payout of ${commission_earned:.2f} made to referrer ID {referrer_id}.")

    def get_referrer_earnings(self, referrer_id):
        """
        Retrieve the total earnings of a referrer.
        
        :param referrer_id: ID of the person whose earnings to retrieve
        :return: Total earnings of the referrer
        :raises ValueError: If referrer_id is not in the system
        """
        if referrer_id not in self.referrals:
            raise ValueError("Referrer ID not found in the system.")
        
        return self.referrals[referrer_id]['earnings']


# Example usage:
if __name__ == "__main__":
    referral_system = ReferralCommissionSystem()
    
    # Add referrals
    referral_system.add_referral("user_1", "referral_1")
    referral_system.add_referral("user_1", "referral_2")

    # Simulate payout for a referral
    referral_system.payout_commission("user_1", 100, 1)  # Level 1 referral
    referral_system.payout_commission("user_1", 200, 2)  # Level 2 referral

    # Get total earnings for referrer
    earnings = referral_system.get_referrer_earnings("user_1")
    print(f"Total earnings for user_1: ${earnings:.2f}")
```
