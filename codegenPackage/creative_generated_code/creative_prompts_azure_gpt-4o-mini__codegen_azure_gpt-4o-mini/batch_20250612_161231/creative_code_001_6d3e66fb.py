"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.rocketpool.club
Prompt: How can I implement a referral program in my application similar to Rocket Pool's affiliate program, including commission structures for direct and indirect referrals?
Generated: DETERMINISTIC_6d3e66fb2cef7692
Batch ID: 20250612_161231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_program.py

class ReferralProgram:
    def __init__(self):
        # Dictionary to hold user referrals and their commissions
        self.referrals = {}
        self.commission_structure = {
            'direct': 0.10,  # 10% commission for direct referrals
            'indirect': 0.05  # 5% commission for indirect referrals
        }

    def add_user(self, user_id, referrer_id=None):
        """Adds a new user to the referral program."""
        if user_id in self.referrals:
            raise ValueError(f"User {user_id} already exists.")
        
        self.referrals[user_id] = {
            'referrer': referrer_id,
            'direct_commission': 0.0,
            'indirect_commission': 0.0
        }
        
        # If there's a referrer, increment their direct commission
        if referrer_id:
            self.referrals[referrer_id]['direct_commission'] += self.commission_structure['direct']
            self._distribute_indirect_commission(referrer_id)

    def _distribute_indirect_commission(self, user_id):
        """Distributes indirect commissions to the user's referrer, if exists."""
        referrer_id = self.referrals[user_id]['referrer']
        if referrer_id:
            # If the user has a referrer, give their referrer an indirect commission
            self.referrals[referrer_id]['indirect_commission'] += self.commission_structure['indirect']
            # Recursively distribute to the next level of referrer
            self._distribute_indirect_commission(referrer_id)

    def get_commissions(self, user_id):
        """Retrieves the commission structure for a given user."""
        if user_id not in self.referrals:
            raise ValueError(f"User {user_id} does not exist.")
        
        return {
            'direct_commission': self.referrals[user_id]['direct_commission'],
            'indirect_commission': self.referrals[user_id]['indirect_commission']
        }

    def summary(self):
        """Prints a summary of all users and their commissions."""
        for user_id, data in self.referrals.items():
            print(f"User {user_id} - Direct Commission: {data['direct_commission']}, Indirect Commission: {data['indirect_commission']}")

if __name__ == '__main__':
    # Example usage of the ReferralProgram class
    referral_program = ReferralProgram()
    
    # Adding users with referrers
    try:
        referral_program.add_user('user1')  # No referrer
        referral_program.add_user('user2', 'user1')  # user2 referred by user1
        referral_program.add_user('user3', 'user2')  # user3 referred by user2

        # Print commission summary
        referral_program.summary()

        # Get specific commission details
        print(referral_program.get_commissions('user1'))
        print(referral_program.get_commissions('user2'))
        print(referral_program.get_commissions('user3'))
    except ValueError as e:
        print(f"Error: {e}")
```
