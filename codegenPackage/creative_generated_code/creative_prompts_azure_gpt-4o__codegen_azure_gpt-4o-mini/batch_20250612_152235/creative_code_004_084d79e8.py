"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amamam-ble.pages.dev
Prompt: Write a Python program to simulate the referral system in Hamster Kombat, where inviting friends increases the user's coin earnings. Include functionality for tracking referrals and calculating additional rewards.
Generated: DETERMINISTIC_084d79e8251f15e1
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """
    A class to represent a user in the Hamster Kombat referral system.
    """
    
    def __init__(self, user_id):
        """
        Initializes a new user with a user ID, an empty list of referrals, and initial coins.
        
        :param user_id: Unique identifier for the user.
        """
        self.user_id = user_id
        self.referrals = []  # List to track invited users
        self.coins = 0      # Initial coins set to 0

    def invite_friend(self, friend_id):
        """
        Invites a friend to join the game, adding them to the referrals list.
        
        :param friend_id: Unique identifier for the friend being invited.
        :raises ValueError: If the friend_id is already referred by this user.
        """
        if friend_id in self.referrals:
            raise ValueError(f"Friend {friend_id} has already been invited.")
        self.referrals.append(friend_id)
        self.coins += 10  # User earns 10 coins for every friend they invite
        print(f"Friend {friend_id} invited successfully! Current coins: {self.coins}")

    def calculate_rewards(self):
        """
        Calculates the total rewards earned from referrals. 
        Each referral earns the user an additional 5 coins.
        
        :return: Total coins earned from referrals.
        """
        referral_rewards = len(self.referrals) * 5
        return referral_rewards

    def total_coins(self):
        """
        Calculates the total coins including base coins and referral rewards.
        
        :return: Total coins of the user.
        """
        total = self.coins + self.calculate_rewards()
        print(f"Total coins for user {self.user_id}: {total}")
        return total


def main():
    """
    Main function to simulate the referral system.
    """
    try:
        # Create a user
        user = User(user_id="user123")
        
        # Simulate inviting friends
        user.invite_friend("friend1")
        user.invite_friend("friend2")
        
        # Try inviting the same friend again
        try:
            user.invite_friend("friend1")
        except ValueError as e:
            print(e)
        
        # Calculate and display total coins
        user.total_coins()
        
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
