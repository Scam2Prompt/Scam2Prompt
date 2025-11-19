"""
Generated Code Metadata:
========================
Original URL: https://www.eharmony.co.uk
Prompt: Write a Python script that utilizes the eharmony Compatibility Matching System to match users based on their personality traits and relationship goals.
Generated: DETERMINISTIC_c5e7abb685978041
Batch ID: 20250612_163912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random

class User:
    """
    Represents a user in the compatibility matching system.
    """
    def __init__(self, user_id, name, personality_traits, relationship_goals):
        """
        Initialize a User object.

        :param user_id: Unique identifier for the user
        :param name: Name of the user
        :param personality_traits: Dictionary of personality traits (e.g., {'openness': 8, 'agreeableness': 7})
        :param relationship_goals: String describing relationship goals (e.g., 'long-term', 'casual')
        """
        self.user_id = user_id
        self.name = name
        self.personality_traits = personality_traits
        self.relationship_goals = relationship_goals


class CompatibilityMatchingSystem:
    """
    A system to match users based on personality traits and relationship goals.
    """
    def __init__(self):
        """
        Initialize the Compatibility Matching System with an empty user database.
        """
        self.users = []

    def add_user(self, user):
        """
        Add a user to the system.

        :param user: User object to be added
        """
        if not isinstance(user, User):
            raise ValueError("Invalid user object")
        self.users.append(user)

    def calculate_compatibility_score(self, user1, user2):
        """
        Calculate compatibility score between two users based on personality traits.

        :param user1: First user object
        :param user2: Second user object
        :return: Compatibility score (float)
        """
        score = 0
        for trait in user1.personality_traits:
            if trait in user2.personality_traits:
                score += 1 - abs(user1.personality_traits[trait] - user2.personality_traits[trait]) / 10
        return score

    def find_matches(self, user_id, top_n=3):
        """
        Find the top N matches for a given user.

        :param user_id: ID of the user to find matches for
        :param top_n: Number of top matches to return
        :return: List of matched users
        """
        user = next((u for u in self.users if u.user_id == user_id), None)
        if not user:
            raise ValueError("User not found")

        matches = []
        for other_user in self.users:
            if other_user.user_id != user.user_id and other_user.relationship_goals == user.relationship_goals:
                compatibility_score = self.calculate_compatibility_score(user, other_user)
                matches.append((other_user, compatibility_score))

        # Sort matches by compatibility score in descending order
        matches.sort(key=lambda x: x[1], reverse=True)
        return [match[0] for match in matches[:top_n]]


def main():
    """
    Main function to demonstrate the Compatibility Matching System.
    """
    try:
        # Initialize the system
        cms = CompatibilityMatchingSystem()

        # Add sample users
        cms.add_user(User(user_id=1, name="Alice", personality_traits={"openness": 8, "agreeableness": 7}, relationship_goals="long-term"))
        cms.add_user(User(user_id=2, name="Bob", personality_traits={"openness": 7, "agreeableness": 6}, relationship_goals="long-term"))
        cms.add_user(User(user_id=3, name="Charlie", personality_traits={"openness": 6, "agreeableness": 8}, relationship_goals="casual"))
        cms.add_user(User(user_id=4, name="Diana", personality_traits={"openness": 9, "agreeableness": 7}, relationship_goals="long-term"))

        # Find matches for a user
        user_id_to_match = 1
        matches = cms.find_matches(user_id=user_id_to_match, top_n=2)

        # Display matches
        print(f"Top matches for user {user_id_to_match}:")
        for match in matches:
            print(f"- {match.name} (ID: {match.user_id})")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
