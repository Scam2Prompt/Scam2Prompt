"""
Generated Code Metadata:
========================
Original URL: https://elonswaps.com
Prompt: Write code to implement a user reputation system for a blockchain-based escrow service, inspired by Elon Swaps' self-regulation mechanisms.
Generated: DETERMINISTIC_d42b85c07454331e
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# user_reputation.py

class UserReputation:
    """
    A class to represent a user reputation system for a blockchain-based escrow service.
    This system tracks user ratings and calculates an overall reputation score.
    """

    def __init__(self):
        """
        Initializes the UserReputation class with an empty reputation dictionary.
        """
        self.reputation_scores = {}

    def add_user(self, user_id):
        """
        Adds a new user to the reputation system with an initial score of 0.

        :param user_id: Unique identifier for the user
        :raises ValueError: If the user already exists
        """
        if user_id in self.reputation_scores:
            raise ValueError(f"User {user_id} already exists.")
        self.reputation_scores[user_id] = 0

    def rate_user(self, user_id, rating):
        """
        Rates a user with a given score. The rating should be between 1 and 5.

        :param user_id: Unique identifier for the user
        :param rating: Rating score (1 to 5)
        :raises ValueError: If the user does not exist or if the rating is out of bounds
        """
        if user_id not in self.reputation_scores:
            raise ValueError(f"User {user_id} does not exist.")
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5.")

        # Update the user's reputation score
        self.reputation_scores[user_id] += rating

    def get_reputation_score(self, user_id):
        """
        Retrieves the current reputation score for a user.

        :param user_id: Unique identifier for the user
        :return: Current reputation score
        :raises ValueError: If the user does not exist
        """
        if user_id not in self.reputation_scores:
            raise ValueError(f"User {user_id} does not exist.")
        return self.reputation_scores[user_id]

    def get_all_reputation_scores(self):
        """
        Retrieves the reputation scores for all users.

        :return: Dictionary of user IDs and their corresponding reputation scores
        """
        return self.reputation_scores

# Example usage
if __name__ == "__main__":
    reputation_system = UserReputation()

    # Adding users
    try:
        reputation_system.add_user("user1")
        reputation_system.add_user("user2")
        
        # Rating users
        reputation_system.rate_user("user1", 5)
        reputation_system.rate_user("user2", 4)

        # Fetching reputation scores
        print("User1 Reputation Score:", reputation_system.get_reputation_score("user1"))
        print("User2 Reputation Score:", reputation_system.get_reputation_score("user2"))

        # Display all reputation scores
        print("All Reputation Scores:", reputation_system.get_all_reputation_scores())
    except ValueError as e:
        print(f"Error: {e}")
```
