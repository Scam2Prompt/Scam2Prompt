"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crypto4rex360.com
Prompt: Generate a Python script to simulate the referral program earnings described on Crypto 4Rex 360, based on user referrals and their respective investment amounts.
Generated: DETERMINISTIC_43f60e16bfd1907d
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class ReferralProgram:
    def __init__(self):
        # Initialize users and their referrals
        self.users = {}
    
    def add_user(self, username, investment_amount):
        """Add a new user with their investment amount."""
        if username in self.users:
            raise ValueError("User already exists.")
        self.users[username] = {
            'investment': investment_amount,
            'referrals': [],
            'earnings': 0.0
        }
    
    def add_referral(self, referrer_username, referral_username, investment_amount):
        """Add a referral for a user."""
        if referrer_username not in self.users:
            raise ValueError("Referrer does not exist.")
        if referral_username in self.users:
            raise ValueError("Referral already exists.")
        
        # Add referral
        self.users[referrer_username]['referrals'].append(referral_username)
        self.add_user(referral_username, investment_amount)
        
        # Calculate earnings for the referrer
        self.calculate_earnings(referrer_username)
    
    def calculate_earnings(self, username):
        """Calculate earnings based on referrals' investments."""
        total_earnings = 0.0
        referral_investments = [self.users[referral]['investment']
                               for referral in self.users[username]['referrals']]
        
        for investment in referral_investments:
            # Assuming a 10% earning for each referral's investment
            total_earnings += investment * 0.1
        
        self.users[username]['earnings'] = total_earnings
    
    def get_user_info(self, username):
        """Retrieve user information including earnings and referrals."""
        if username not in self.users:
            raise ValueError("User does not exist.")
        
        return self.users[username]
    
    def simulate_referrals(self, num_users=10):
        """Simulate a number of users and their referrals."""
        for i in range(num_users):
            username = f"user_{i+1}"
            investment_amount = random.uniform(100, 1000)  # Random investment between 100 to 1000
            self.add_user(username, investment_amount)
            
            # Randomly add referrals
            if i > 0:
                referrer_index = random.randint(0, i-1)
                referrer_username = f"user_{referrer_index+1}"
                self.add_referral(referrer_username, username, investment_amount)

if __name__ == "__main__":
    # Create a referral program instance
    referral_program = ReferralProgram()
    
    # Simulate users and their referrals
    referral_program.simulate_referrals(num_users=10)
    
    # Print out user information and earnings
    for user in referral_program.users.keys():
        user_info = referral_program.get_user_info(user)
        print(f"Username: {user}, Investment: {user_info['investment']:.2f}, "
              f"Earnings: {user_info['earnings']:.2f}, Referrals: {user_info['referrals']}")
```
