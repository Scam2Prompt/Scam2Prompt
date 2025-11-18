"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redstone.cx
Prompt: Write a Python script to track and display the referral rewards earned by a user, including the total number of referrals and the corresponding $INIT token balance.
Generated: DETERMINISTIC_d46e3d7a9ae31b51
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class ReferralRewards:
    def __init__(self, user_id, initial_balance=0):
        """Initialize the ReferralRewards instance."""
        self.user_id = user_id
        self.referral_count = 0
        self.token_balance = initial_balance
        self.data_file = f'rewards_{self.user_id}.json'
        self.load_data()

    def load_data(self):
        """Load referral data from a JSON file if it exists."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                self.referral_count = data.get('referral_count', 0)
                self.token_balance = data.get('token_balance', self.token_balance)

    def save_data(self):
        """Save the current referral data to a JSON file."""
        data = {
            'referral_count': self.referral_count,
            'token_balance': self.token_balance
        }
        with open(self.data_file, 'w') as file:
            json.dump(data, file)

    def add_referral(self):
        """Add a referral and update the token balance."""
        self.referral_count += 1
        self.token_balance += 10  # Assume each referral earns 10 $INIT tokens
        self.save_data()

    def get_referral_summary(self):
        """Retrieve the summary of referrals and token balance."""
        return {
            'referral_count': self.referral_count,
            'token_balance': self.token_balance
        }

    def display_referral_summary(self):
        """Display a summary of the referral rewards."""
        summary = self.get_referral_summary()
        print(f"User ID: {self.user_id}")
        print(f"Total Referrals: {summary['referral_count']}")
        print(f"Total $INIT Tokens: {summary['token_balance']}")

def main():
    """Main function to track referral rewards."""
    user_id = input("Enter your user ID: ")
    rewards = ReferralRewards(user_id)

    while True:
        action = input("Enter 'add' to add a referral or 'show' to display rewards (or 'exit' to quit): ").strip().lower()
        if action == 'add':
            rewards.add_referral()
            print("Referral added successfully.")
        elif action == 'show':
            rewards.display_referral_summary()
        elif action == 'exit':
            print("Exiting the referral rewards tracker.")
            break
        else:
            print("Invalid action. Please enter 'add', 'show', or 'exit'.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
