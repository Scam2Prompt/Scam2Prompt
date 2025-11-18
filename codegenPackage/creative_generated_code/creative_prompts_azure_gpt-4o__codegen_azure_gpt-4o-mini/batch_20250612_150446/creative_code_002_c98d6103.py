"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eunitedcryptofx.com
Prompt: Create a function to simulate the referral bonus system mentioned on eunitedcryptofx.com, where users can earn rewards by referring friends.
Generated: DETERMINISTIC_c98d61035800adf5
Batch ID: 20250612_150446
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
        """
        Initializes the referral system with an empty user database.
        Each user will have a unique ID, a balance, and a list of their referrals.
        """
        self.users = {}  # Dictionary to hold user data
        self.user_id_counter = 1  # Counter for assigning unique IDs to users

    def add_user(self, username):
        """
        Adds a new user to the referral system.

        Parameters:
            username (str): The username of the new user.

        Returns:
            int: The unique ID assigned to the new user.
        """
        if username in self.users:
            raise ValueError("Username already exists.")

        user_id = self.user_id_counter
        self.users[username] = {
            'id': user_id,
            'balance': 0,
            'referrals': []
        }
        self.user_id_counter += 1
        return user_id

    def refer_friend(self, referrer_username, referred_username):
        """
        Simulates a referral where a user refers a friend.

        Parameters:
            referrer_username (str): The username of the user making the referral.
            referred_username (str): The username of the referred friend.

        Returns:
            bool: True if the referral was successful, False otherwise.
        """
        if referrer_username not in self.users:
            raise ValueError("Referrer does not exist.")
        if referred_username in self.users:
            raise ValueError("Referred username already exists.")

        self.users[referrer_username]['referrals'].append(referred_username)
        self.users[referred_username] = {
            'id': self.user_id_counter,
            'balance': 0,
            'referrals': []
        }
        self.user_id_counter += 1
        self.award_bonus(referrer_username)
        return True

    def award_bonus(self, username):
        """
        Awards a referral bonus to the referrer.

        Parameters:
            username (str): The username of the referrer.
        """
        self.users[username]['balance'] += 10  # Example bonus amount

    def get_balance(self, username):
        """
        Retrieves the current balance of a user.

        Parameters:
            username (str): The username of the user.

        Returns:
            int: The balance of the user.

        Raises:
            ValueError: If the user does not exist.
        """
        if username not in self.users:
            raise ValueError("User does not exist.")

        return self.users[username]['balance']

    def get_referrals(self, username):
        """
        Retrieves the list of referrals made by a user.

        Parameters:
            username (str): The username of the user.

        Returns:
            list: A list of referred usernames.

        Raises:
            ValueError: If the user does not exist.
        """
        if username not in self.users:
            raise ValueError("User does not exist.")

        return self.users[username]['referrals']

# Example usage:
if __name__ == "__main__":
    referral_system = ReferralSystem()
    try:
        user_id_1 = referral_system.add_user("Alice")
        user_id_2 = referral_system.add_user("Bob")
        referral_system.refer_friend("Alice", "Charlie")
        
        print(f"Alice's balance: {referral_system.get_balance('Alice')}")
        print(f"Alice's referrals: {referral_system.get_referrals('Alice')}")
    except ValueError as e:
        print(f"Error: {e}")
```
