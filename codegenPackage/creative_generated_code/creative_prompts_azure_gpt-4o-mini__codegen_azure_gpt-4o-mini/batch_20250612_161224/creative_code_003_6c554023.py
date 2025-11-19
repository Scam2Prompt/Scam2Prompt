"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld4.pages.dev
Prompt: Describe how to create a referral program for a socialfi platform like Everyworld that encourages users to participate in environmental conservation efforts.
Generated: DETERMINISTIC_6c55402373e662a1
Batch ID: 20250612_161224
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
        # Initialize the referral program with an empty user list and referral counts
        self.users = {}
        self.referral_counts = {}
    
    def register_user(self, username, referrer=None):
        """
        Register a new user in the system.
        
        :param username: str - The username of the new user
        :param referrer: str or None - The username of the referring user (if any)
        :raises ValueError: If the username already exists
        """
        if username in self.users:
            raise ValueError("Username already exists.")
        
        # Add the new user to the users dictionary
        self.users[username] = referrer
        
        # Increment the referral count for the referrer if provided
        if referrer:
            if referrer not in self.referral_counts:
                self.referral_counts[referrer] = 0
            self.referral_counts[referrer] += 1
    
    def get_referral_count(self, username):
        """
        Get the number of referrals for a given user.
        
        :param username: str - The username of the user
        :return: int - The number of referrals made by the user
        :raises KeyError: If the user does not exist
        """
        if username not in self.referral_counts:
            raise KeyError("User not found.")
        
        return self.referral_counts[username]
    
    def reward_users(self):
        """
        Reward users based on their referral counts.
        
        This function can be customized to implement the logic for rewarding users
        based on the number of successful referrals they make.
        """
        for user, count in self.referral_counts.items():
            if count >= 5:
                self._reward(user)
    
    def _reward(self, username):
        """
        Internal method to reward a user.
        
        :param username: str - The username of the user to reward
        """
        # Placeholder for rewarding logic (e.g., points, badges)
        print(f"User {username} has been rewarded for {self.referral_counts[username]} referrals!")

# Example usage:
if __name__ == "__main__":
    referral_program = ReferralProgram()
    
    # Register users
    try:
        referral_program.register_user("Alice")
        referral_program.register_user("Bob", "Alice")
        referral_program.register_user("Charlie", "Alice")
        referral_program.register_user("David", "Bob")
        referral_program.register_user("Eva", "Bob")
        referral_program.register_user("Frank", "Alice")
        
        # Fetch referral counts
        print("Alice's referrals:", referral_program.get_referral_count("Alice"))
        print("Bob's referrals:", referral_program.get_referral_count("Bob"))
        
        # Reward users based on their referrals
        referral_program.reward_users()
        
    except (ValueError, KeyError) as e:
        print(f"An error occurred: {e}")
```
