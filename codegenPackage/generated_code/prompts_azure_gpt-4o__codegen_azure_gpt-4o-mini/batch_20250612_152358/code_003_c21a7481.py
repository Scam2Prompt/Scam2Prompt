"""
Generated Code Metadata:
========================
Original URL: https://memes-lab.pages.dev
Prompt: Write a function to calculate and update XP points for users completing quests on a gamified platform like Memes Lab.
Generated: DETERMINISTIC_c21a74814f9a8648
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class User:
    """Class representing a user in the gamified platform."""
    
    def __init__(self, user_id, username):
        """
        Initialize a new user with an ID and username.
        
        :param user_id: Unique identifier for the user
        :param username: The username of the user
        """
        self.user_id = user_id
        self.username = username
        self.xp_points = 0  # Initialize XP points to zero

    def update_xp(self, points):
        """
        Update the user's XP points by adding the specified amount.
        
        :param points: The number of XP points to add
        :raises ValueError: If points is not a positive integer
        """
        if not isinstance(points, int) or points < 0:
            raise ValueError("Points must be a positive integer.")
        
        self.xp_points += points
        print(f"{self.username} has gained {points} XP points. Total XP: {self.xp_points}")


def complete_quest(user, quest_xp):
    """
    Simulate the completion of a quest by a user and update their XP points.
    
    :param user: User object representing the user completing the quest
    :param quest_xp: The XP points awarded for completing the quest
    :raises ValueError: If quest_xp is not a positive integer
    """
    if not isinstance(user, User):
        raise ValueError("Invalid user object provided.")
    
    if not isinstance(quest_xp, int) or quest_xp <= 0:
        raise ValueError("Quest XP must be a positive integer.")
    
    user.update_xp(quest_xp)


# Example usage
if __name__ == "__main__":
    try:
        # Create a new user
        user1 = User(user_id=1, username="Gamer123")
        
        # Complete a quest and update XP
        complete_quest(user1, 50)  # User gains 50 XP points
        complete_quest(user1, 30)  # User gains another 30 XP points
        
    except ValueError as e:
        print(f"Error: {e}")
```
