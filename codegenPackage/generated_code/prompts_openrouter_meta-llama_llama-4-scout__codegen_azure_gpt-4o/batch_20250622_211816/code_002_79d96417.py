"""
Generated Code Metadata:
========================
Original URL: https://www.bsc-scan.net
Prompt: "Design an affiliate program with 3 levels of referrals, offering 5% commission on deposits for level 1, 2% for level 2, and 0.5% for level 3, and write a simple Python script to track referrals and calculate commissions."
Generated: DETERMINISTIC_79d96417a7b6c682
Batch ID: 20250622_211816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# affiliate_program.py

from collections import defaultdict

class AffiliateProgram:
    """
    A class to manage a 3-level affiliate program with commission tracking.
    Level 1: 5% commission
    Level 2: 2% commission
    Level 3: 0.5% commission
    """
    
    def __init__(self):
        # Dictionary to store user referrals: {user_id: [referral_id1, referral_id2, ...]}
        self.referrals = defaultdict(list)
        
        # Dictionary to store user commissions: {user_id: commission_amount}
        self.commissions = defaultdict(float)
        
        # Commission rates for each level
        self.commission_rates = {1: 0.05, 2: 0.02, 3: 0.005}
    
    def add_referral(self, referrer_id, referral_id):
        """
        Adds a referral relationship between referrer and referral.
        
        :param referrer_id: ID of the referrer (parent)
        :param referral_id: ID of the referral (child)
        """
        self.referrals[referrer_id].append(referral_id)
    
    def calculate_commission(self, referral_id, deposit_amount):
        """
        Calculates and distributes commissions for a deposit made by a referral.
        
        :param referral_id: ID of the referral making the deposit
        :param deposit_amount: Amount deposited by the referral
        """
        current_user = referral_id
        level = 1
        
        # Traverse up to 3 levels of referrals
        while level <= 3:
            # Find the referrer for the current user
            referrer = self.find_referrer(current_user)
            
            if referrer:
                # Calculate commission for the referrer
                commission = deposit_amount * self.commission_rates[level]
                self.commissions[referrer] += commission
                
                # Move to the next level
                current_user = referrer
                level += 1
            else:
                # No referrer found, stop the loop
                break
    
    def find_referrer(self, referral_id):
        """
        Finds the referrer (parent) of a given referral (child).
        
        :param referral_id: ID of the referral
        :return: ID of the referrer or None if no referrer exists
        """
        for referrer, referrals in self.referrals.items():
            if referral_id in referrals:
                return referrer
        return None
    
    def get_commissions(self, user_id):
        """
        Retrieves the total commission earned by a user.
        
        :param user_id: ID of the user
        :return: Total commission amount
        """
        return self.commissions[user_id]
    
    def display_commissions(self):
        """
        Displays all users and their respective commissions.
        """
        print("User Commissions:")
        for user_id, commission in self.commissions.items():
            print(f"User {user_id}: ${commission:.2f}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the affiliate program
        program = AffiliateProgram()
        
        # Add referral relationships
        program.add_referral("user1", "user2")  # user1 referred user2
        program.add_referral("user2", "user3")  # user2 referred user3
        program.add_referral("user3", "user4")  # user3 referred user4
        
        # Simulate deposits and calculate commissions
        program.calculate_commission("user4", 1000)  # user4 deposits $1000
        program.calculate_commission("user3", 500)   # user3 deposits $500
        
        # Display commissions
        program.display_commissions()
    except Exception as e:
        print(f"An error occurred: {e}")
```
