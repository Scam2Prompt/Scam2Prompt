"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sparkfi.net
Prompt: Describe the process of earning rewards through the Spark Social Media Army and how to participate.
Generated: DETERMINISTIC_37d240cd17b809a1
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SparkSocialMediaArmy:
    """
    This class represents the process of earning rewards through the Spark Social Media Army.
    It includes methods for participating, earning rewards, and managing user accounts.
    """

    def __init__(self):
        """
        Initializes the SparkSocialMediaArmy with an empty user dictionary.
        """
        self.users = {}

    def register_user(self, username: str, email: str) -> None:
        """
        Registers a new user for the Spark Social Media Army.
        
        Args:
            username (str): The username of the user.
            email (str): The email address of the user.
        
        Raises:
            ValueError: If the username or email is already registered.
        """
        if username in self.users:
            raise ValueError("Username already exists. Please choose a different username.")
        if any(user['email'] == email for user in self.users.values()):
            raise ValueError("Email already registered. Please use a different email.")

        self.users[username] = {'email': email, 'rewards': 0}
        print(f"User {username} registered successfully.")

    def participate_in_campaign(self, username: str) -> None:
        """
        Allows a registered user to participate in a social media campaign.
        
        Args:
            username (str): The username of the user.
        
        Raises:
            KeyError: If the user does not exist.
        """
        if username not in self.users:
            raise KeyError("User not found. Please register first.")
        
        # Simulate participation in a campaign
        print(f"{username} is participating in the campaign...")
        self.users[username]['rewards'] += 10  # Earn 10 reward points for participation
        print(f"{username} has earned 10 reward points!")

    def get_rewards(self, username: str) -> int:
        """
        Retrieves the total rewards of a user.
        
        Args:
            username (str): The username of the user.
        
        Returns:
            int: The total rewards of the user.
        
        Raises:
            KeyError: If the user does not exist.
        """
        if username not in self.users:
            raise KeyError("User not found. Please register first.")
        
        return self.users[username]['rewards']

    def redeem_rewards(self, username: str, points: int) -> None:
        """
        Allows a user to redeem their rewards for gifts or benefits.
        
        Args:
            username (str): The username of the user.
            points (int): The number of reward points to redeem.
        
        Raises:
            KeyError: If the user does not exist.
            ValueError: If the user does not have enough rewards.
        """
        if username not in self.users:
            raise KeyError("User not found. Please register first.")
        
        if self.users[username]['rewards'] < points:
            raise ValueError("Insufficient rewards to redeem. Please earn more rewards.")

        self.users[username]['rewards'] -= points
        print(f"{username} redeemed {points} reward points successfully!")

# Example usage:
if __name__ == "__main__":
    army = SparkSocialMediaArmy()
    try:
        army.register_user("john_doe", "john@example.com")
        army.participate_in_campaign("john_doe")
        print(f"John's total rewards: {army.get_rewards('john_doe')}")
        army.redeem_rewards("john_doe", 5)
        print(f"John's total rewards after redemption: {army.get_rewards('john_doe')}")
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
