"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connexa.vip
Prompt: Write a Python script to simulate the "smart matching" feature of Connexa, where users are matched based on shared interests, vibe, and goals.
Generated: DETERMINISTIC_231a00bc5851b25e
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict, Tuple

class User:
    """
    Represents a user in the matching system.
    """
    def __init__(self, user_id: int, name: str, interests: List[str], vibe: str, goals: List[str]):
        self.user_id = user_id
        self.name = name
        self.interests = interests
        self.vibe = vibe
        self.goals = goals

    def __repr__(self):
        return f"User({self.name})"


class SmartMatcher:
    """
    Simulates the smart matching feature, matching users based on shared interests, vibe, and goals.
    """
    def __init__(self, users: List[User]):
        self.users = users
    
    def calculate_match_score(self, user1: User, user2: User) -> float:
        """
        Calculates a match score between two users based on shared interests, vibe, and goals.
        """
        # Interest score: Count of shared interests
        interest_score = len(set(user1.interests) & set(user2.interests))
        
        # Vibe score: Exact match results in higher points
        vibe_score = 1 if user1.vibe == user2.vibe else 0
        
        # Goal score: Count of shared goals
        goal_score = len(set(user1.goals) & set(user2.goals))
        
        # Combine scores into a single value (weights can be adjusted)
        total_score = interest_score * 0.5 + vibe_score * 1 + goal_score * 0.5
        return total_score
    
    def find_best_matches(self, user_id: int, top_n: int = 3) -> List[Tuple[User, float]]:
        """
        Finds the top N best matches for the given user ID.
        """
        # Locate the user
        target_user = next((user for user in self.users if user.user_id == user_id), None)
        if not target_user:
            raise ValueError(f"User with ID {user_id} not found.")
        
        # Calculate match scores for all other users
        scores = []
        for user in self.users:
            if user.user_id != user_id:  # Skip the target user
                score = self.calculate_match_score(target_user, user)
                scores.append((user, score))
        
        # Sort users based on match scores in descending order
        scores.sort(key=lambda x: x[1], reverse=True)
        
        # Return the top N matches
        return scores[:top_n]


def main():
    """
    Main function to simulate the smart matching feature.
    """
    # Create a list of sample users
    users = [
        User(1, "Alice", ["music", "coding", "reading"], "introverted", ["career growth", "learning"]),
        User(2, "Bob", ["sports", "coding", "movies"], "extroverted", ["networking", "fun"]),
        User(3, "Charlie", ["reading", "traveling", "music"], "introverted", ["learning", "exploration"]),
        User(4, "Diana", ["coding", "gaming", "traveling"], "ambiverted", ["career growth", "fun"]),
        User(5, "Eve", ["movies", "music", "sports"], "extroverted", ["networking", "exploration"]),
    ]
    
    # Initialize the smart matcher
    matcher = SmartMatcher(users)
    
    # Simulate finding matches for a specific user
    try:
        user_id_to_match = 1  # Match for Alice
        top_matches = matcher.find_best_matches(user_id_to_match)
        
        print(f"Top matches for user {user_id_to_match}:")
        for match, score in top_matches:
            print(f"- {match.name} (Score: {score:.2f})")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
