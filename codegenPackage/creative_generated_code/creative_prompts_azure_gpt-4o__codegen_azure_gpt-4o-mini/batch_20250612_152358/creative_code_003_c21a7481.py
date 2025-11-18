"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memes-lab.pages.dev
Prompt: Write a function to calculate and update XP points for users completing quests on a gamified platform like Memes Lab.
Generated: DETERMINISTIC_c21a74814f9a8648
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """Represents a user in the gamified platform."""
    
    def __init__(self, username, xp=0):
        """Initializes a User with a username and starting XP."""
        self.username = username
        self.xp = xp

    def __str__(self):
        """Returns a string representation of the user."""
        return f"User: {self.username}, XP: {self.xp}"


def update_xp(user, quest_xp):
    """
    Updates the XP points of a user after completing a quest.
    
    Args:
        user (User): The user whose XP needs to be updated.
        quest_xp (int): The amount of XP to add.

    Raises:
        ValueError: If quest_xp is not a positive integer.
    """
    if not isinstance(user, User):
        raise TypeError("The user must be an instance of User class.")
    
    if not isinstance(quest_xp, int) or quest_xp <= 0:
        raise ValueError("Quest XP must be a positive integer.")
    
    # Update the user's XP
    user.xp += quest_xp
    print(f"{user.username} has completed a quest and gained {quest_xp} XP! Total XP: {user.xp}")


# Example usage:
if __name__ == "__main__":
    # Create a user instance
    user1 = User("AdventureSeeker")

    # Update user XP after completing a quest
    try:
        update_xp(user1, 50)  # user gains 50 XP
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
```
