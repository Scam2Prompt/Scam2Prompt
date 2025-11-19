"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fi-dapp-git-rk-featadd-new-badge-dumps-sad-etherfi.vercel.app
Prompt: Generate a function that updates user badges based on their participation in eETH promotions.
Generated: DETERMINISTIC_4dbf957416629ff5
Batch ID: 20250612_135343
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
    Represents a user in the system.

    Attributes:
        user_id (str): Unique identifier for the user.
        badges (list): List of badges awarded to the user.
        participation_count (int): Number of times the user has participated in eETH promotions.
    """

    def __init__(self, user_id: str):
        self.user_id = user_id
        self.badges = []
        self.participation_count = 0

    def participate_in_promotion(self):
        """
        Increment the user's participation count when they participate in a promotion.
        """
        self.participation_count += 1


def update_user_badges(user: User):
    """
    Updates user badges based on their participation in eETH promotions.

    Args:
        user (User): The user object to update badges for.
    
    Raises:
        ValueError: If the user parameter is not an instance of User.
    """
    if not isinstance(user, User):
        raise ValueError("The provided user must be an instance of User.")

    # Define badge requirements based on participation count
    badge_requirements = {
        "Bronze": 1,
        "Silver": 5,
        "Gold": 10,
        "Platinum": 20
    }

    # Check current participation count and assign badges accordingly
    for badge, requirement in badge_requirements.items():
        if user.participation_count >= requirement and badge not in user.badges:
            user.badges.append(badge)
            print(f"Badge '{badge}' awarded to user '{user.user_id}'.")

# Example usage
if __name__ == "__main__":
    # Create a user and simulate participation in promotions
    user = User(user_id="user123")
    
    # Simulating user participation in promotions
    for _ in range(12):
        user.participate_in_promotion()
    
    # Update and print the user's badges
    update_user_badges(user)
    print(f"User badges: {user.badges}")
```
