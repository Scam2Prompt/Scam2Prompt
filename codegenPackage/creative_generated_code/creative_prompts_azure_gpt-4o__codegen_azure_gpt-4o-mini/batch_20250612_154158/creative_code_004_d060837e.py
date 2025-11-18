"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ff-exchange.in
Prompt: Create a function to track referral rewards for crypto swaps, ensuring accurate reward allocation for each referred user, as described in FF.IO's referral program.
Generated: DETERMINISTIC_d060837e116936da
Batch ID: 20250612_154158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ReferralSystem:
    def __init__(self):
        # Initialize a dictionary to store referral rewards
        self.referrals = {}

    def add_referral(self, referrer: str, referred: str, reward_amount: float) -> None:
        """
        Adds a new referral to the system.

        :param referrer: The user who referred the new user
        :param referred: The user who is being referred
        :param reward_amount: The reward allocated for this referral
        """
        if referrer == referred:
            raise ValueError("Referrer and referred user cannot be the same.")

        if referrer not in self.referrals:
            self.referrals[referrer] = []

        # Store the referral with associated reward
        self.referrals[referrer].append({'user': referred, 'reward': reward_amount})

    def calculate_rewards(self, user: str) -> float:
        """
        Calculates the total rewards for a given user based on their referrals.

        :param user: The user whose total rewards are to be calculated
        :return: The total reward amount for the user
        """
        if user not in self.referrals:
            return 0.0  # No referrals found for the user

        total_rewards = sum(referral['reward'] for referral in self.referrals[user])
        return total_rewards

    def get_referrals(self, user: str):
        """
        Retrieves a list of all referrals made by a given user.

        :param user: The user whose referral list is requested
        :return: A list of referrals for the user
        """
        return self.referrals.get(user, [])

# Example Usage
if __name__ == "__main__":
    referral_system = ReferralSystem()
    
    try:
        # Adding referrals
        referral_system.add_referral("alice", "bob", 10.0)
        referral_system.add_referral("alice", "charlie", 15.0)

        # Calculating rewards for Alice
        alice_rewards = referral_system.calculate_rewards("alice")
        print(f"Alice's total rewards: ${alice_rewards}")

        # Getting referral list for Alice
        alice_referrals = referral_system.get_referrals("alice")
        print("Alice's referrals:", alice_referrals)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
