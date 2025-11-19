"""
Generated Code Metadata:
========================
Original URL: https://oasysgames.live
Prompt: Design a system to reward users with VP scores for following and earning on Oasys, similar to the 500 Follow and Earn VP Score campaign.
Generated: DETERMINISTIC_6d31ed9dd87c3f53
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class User:
    """
    Represents a user in the Oasys system.
    Each user has a unique ID, a follow count, and a VP score.
    """
    def __init__(self, user_id):
        self.user_id = user_id
        self.follow_count = 0
        self.vp_score = 0

    def follow(self):
        """
        Increments the follow count for the user.
        """
        self.follow_count += 1
        self.update_vp_score()

    def earn(self, amount):
        """
        Increments the VP score based on the amount earned.
        
        :param amount: The amount earned by the user.
        """
        if amount < 0:
            raise ValueError("Earned amount must be non-negative.")
        self.vp_score += amount

    def update_vp_score(self):
        """
        Updates the VP score based on the number of follows.
        Each follow grants a fixed amount of VP score.
        """
        vp_per_follow = 1  # Define the VP score awarded per follow
        self.vp_score += vp_per_follow


class OasysSystem:
    """
    Represents the Oasys system that manages users and their VP scores.
    """
    def __init__(self):
        self.users = {}

    def add_user(self, user_id):
        """
        Adds a new user to the system.
        
        :param user_id: Unique identifier for the user.
        :raises ValueError: If the user already exists.
        """
        if user_id in self.users:
            raise ValueError("User already exists.")
        self.users[user_id] = User(user_id)

    def follow_user(self, follower_id, followee_id):
        """
        Allows a user to follow another user.
        
        :param follower_id: The ID of the user who is following.
        :param followee_id: The ID of the user being followed.
        :raises ValueError: If either user does not exist.
        """
        if follower_id not in self.users or followee_id not in self.users:
            raise ValueError("Both users must exist to follow.")
        
        self.users[follower_id].follow()

    def earn_vp(self, user_id, amount):
        """
        Allows a user to earn VP based on a specified amount.
        
        :param user_id: The ID of the user earning VP.
        :param amount: The amount to be added to the user's VP score.
        :raises ValueError: If the user does not exist or amount is negative.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist.")
        self.users[user_id].earn(amount)

    def get_user_vp(self, user_id):
        """
        Retrieves the VP score of a user.
        
        :param user_id: The ID of the user.
        :return: The VP score of the user.
        :raises ValueError: If the user does not exist.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist.")
        return self.users[user_id].vp_score


# Example usage
if __name__ == "__main__":
    oasys = OasysSystem()
    
    # Adding users
    oasys.add_user("user1")
    oasys.add_user("user2")

    # User1 follows User2
    oasys.follow_user("user1", "user2")

    # User1 earns VP
    oasys.earn_vp("user1", 10)

    # Retrieve and print User1's VP score
    print(f"User1 VP Score: {oasys.get_user_vp('user1')}")
```
