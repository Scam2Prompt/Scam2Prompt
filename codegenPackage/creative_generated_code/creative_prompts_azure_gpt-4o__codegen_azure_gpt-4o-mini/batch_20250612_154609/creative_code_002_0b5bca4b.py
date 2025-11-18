"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welforcevestcapital.com
Prompt: Generate Python code for automating the referral bonus calculation based on Welforcevest Capital's multi-level referral program structure. Include logic for tracking referrals and calculating commissions.
Generated: DETERMINISTIC_0b5bca4b06e32a15
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ReferralProgram:
    def __init__(self):
        self.referrals = {}
        self.commission_rate = 0.1  # 10% commission rate
        self.bonus_structure = {  # Define the levels of bonuses
            1: 0.5,  # 50% for level 1 referrals
            2: 0.3,  # 30% for level 2 referrals
            3: 0.2,  # 20% for level 3 referrals
        }

    def add_referral(self, referrer_id, referral_id):
        """
        Add a referral to the system.
        :param referrer_id: ID of the referrer
        :param referral_id: ID of the new referral
        """
        if referrer_id not in self.referrals:
            self.referrals[referrer_id] = []
        self.referrals[referrer_id].append(referral_id)

    def calculate_commission(self, referral_id, amount):
        """
        Calculate total commission for a referral and its referrer(s).
        :param referral_id: ID of the referral
        :param amount: Amount that the referral has transacted
        :return: Dictionary containing commissions for each level
        """
        commissions = {}
        referrer = self.find_referrer(referral_id)

        if referrer:
            level = 1
            while referrer and level <= len(self.bonus_structure):
                commission = amount * self.commission_rate * self.bonus_structure[level]
                commissions[referrer] = commissions.get(referrer, 0) + commission
                referrer = self.find_referrer(referrer)
                level += 1

        return commissions

    def find_referrer(self, referral_id):
        """
        Find the referrer for a given referral ID.
        :param referral_id: ID of the referral
        :return: ID of the referrer or None if not found
        """
        for referrer, referrals in self.referrals.items():
            if referral_id in referrals:
                return referrer
        return None

    def payout_commissions(self, commissions):
        """
        Process the payout for the calculated commissions.
        :param commissions: Dictionary of commissions to be paid out
        """
        for referrer_id, amount in commissions.items():
            if amount > 0:
                # Here you would implement the logic to payout amount to referrer_id
                print(f"Payout of {amount:.2f} to referrer {referrer_id}")

# Example usage
if __name__ == "__main__":
    referral_program = ReferralProgram()

    # Adding referrals
    referral_program.add_referral('user_a', 'user_b')
    referral_program.add_referral('user_a', 'user_c')
    referral_program.add_referral('user_b', 'user_d')

    # Calculate commission for a referral transaction
    transaction_amount = 1000  # Example transaction amount
    commissions = referral_program.calculate_commission('user_d', transaction_amount)

    # Payout calculated commissions
    referral_program.payout_commissions(commissions)
```
