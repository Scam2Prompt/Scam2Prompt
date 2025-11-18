"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zadepositslot.com.mainnetdappschain.top
Prompt: Write code to generate a referral program tracking system that calculates referral income based on Zadepositslot's referral program structure.
Generated: DETERMINISTIC_d2868e2a7cbeefda
Batch ID: 20250612_150345
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
        """
        Initializes a new instance of the ReferralProgram class.
        This class will track referrals and calculate income from them.
        """
        self.referrals = {}  # Dictionary to hold referral data
        self.referral_income_structure = {
            'level_1': 0.10,  # 10% for direct referral
            'level_2': 0.05,  # 5% for second-level referral
            'level_3': 0.02   # 2% for third-level referral
        }

    def add_referral(self, referrer_id, referred_id, deposit_amount):
        """
        Adds a referral to the system.
        
        :param referrer_id: The ID of the referrer.
        :param referred_id: The ID of the referred individual.
        :param deposit_amount: The amount deposited by the referred individual.
        :raises ValueError: If the deposit amount is negative or if IDs are missing.
        """
        if deposit_amount < 0:
            raise ValueError("Deposit amount must be a non-negative value.")
            
        if not referrer_id or not referred_id:
            raise ValueError("Both referrer_id and referred_id must be provided.")

        # Store the referral
        self.referrals[referred_id] = {
            'referrer_id': referrer_id,
            'deposit_amount': deposit_amount
        }

    def calculate_income(self):
        """
        Calculates the total referral income for each referrer based on the referral structure.
        
        :return: A dictionary with referrer_id as keys and their total income as values.
        """
        income_summary = {}

        for referred_id, referral_data in self.referrals.items():
            referrer_id = referral_data['referrer_id']
            deposit_amount = referral_data['deposit_amount']
            
            # Level 1 income
            income_summary[referrer_id] = income_summary.get(referrer_id, 0) + deposit_amount * self.referral_income_structure['level_1']
            
            # Level 2 (check if the referrer has their own referrer)
            if referrer_id in self.referrals:
                level_2_referrer_id = self.referrals[referrer_id]['referrer_id']
                if level_2_referrer_id:
                    income_summary[level_2_referrer_id] = income_summary.get(level_2_referrer_id, 0) + deposit_amount * self.referral_income_structure['level_2']

            # Level 3 (check if the level 2 referrer has their own referrer)
            if level_2_referrer_id in self.referrals:
                level_3_referrer_id = self.referrals[level_2_referrer_id]['referrer_id']
                if level_3_referrer_id:
                    income_summary[level_3_referrer_id] = income_summary.get(level_3_referrer_id, 0) + deposit_amount * self.referral_income_structure['level_3']

        return income_summary

    def get_referrals(self):
        """
        Returns the current list of referrals in the system.
        
        :return: A dictionary of current referrals.
        """
        return self.referrals

# Example use case
if __name__ == "__main__":
    referral_program = ReferralProgram()
    
    try:
        # Adding referrals
        referral_program.add_referral(referrer_id='user1', referred_id='user2', deposit_amount=100)
        referral_program.add_referral(referrer_id='user1', referred_id='user3', deposit_amount=200)
        referral_program.add_referral(referrer_id='user2', referred_id='user4', deposit_amount=150)
        
        # Calculate income for referrers
        income = referral_program.calculate_income()
        print("Referral Income Summary:", income)
        
    except ValueError as e:
        print(f"An error occurred: {e}")
```
