"""
Generated Code Metadata:
========================
Original URL: https://asset12.pages.dev
Prompt: Create a ranking system for the Cookie Community leaderboard, taking into account community points, referral points, and ecosystem points.
Generated: DETERMINISTIC_6b6278be16258a98
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# ranking_system.py

from dataclasses import dataclass
from enum import Enum
from typing import List

class Rank(Enum):
    """Enum representing the different ranks in the leaderboard."""
    NOVICE = 1
    CONTRIBUTOR = 2
    MAINTAINER = 3
    LEADER = 4
    CHAMPION = 5

@dataclass
class User:
    """Dataclass representing a user in the leaderboard."""
    id: int
    community_points: int
    referral_points: int
    ecosystem_points: int

class Leaderboard:
    """Class representing the leaderboard."""
    def __init__(self):
        self.users = []

    def add_user(self, user: User):
        """Add a user to the leaderboard."""
        self.users.append(user)

    def calculate_score(self, user: User) -> int:
        """Calculate the score of a user based on their points."""
        # Weights for different types of points
        community_weight = 0.4
        referral_weight = 0.3
        ecosystem_weight = 0.3

        score = (user.community_points * community_weight +
                 user.referral_points * referral_weight +
                 user.ecosystem_points * ecosystem_weight)
        return int(score)

    def rank_users(self) -> List[User]:
        """Rank users based on their scores."""
        ranked_users = sorted(self.users, key=self.calculate_score, reverse=True)
        return ranked_users

    def assign_ranks(self) -> dict:
        """Assign ranks to users based on their scores."""
        ranked_users = self.rank_users()
        ranks = {}

        # Assign ranks
        for i, user in enumerate(ranked_users):
            score = self.calculate_score(user)
            if score >= 1000:
                rank = Rank.CHAMPION
            elif score >= 500:
                rank = Rank.LEADER
            elif score >= 200:
                rank = Rank.MAINTAINER
            elif score >= 50:
                rank = Rank.CONTRIBUTOR
            else:
                rank = Rank.NOVICE

            ranks[user.id] = {
                'rank': rank,
                'score': score,
                'community_points': user.community_points,
                'referral_points': user.referral_points,
                'ecosystem_points': user.ecosystem_points
            }

        return ranks

def main():
    leaderboard = Leaderboard()

    # Example users
    users = [
        User(1, 1000, 500, 200),
        User(2, 500, 200, 100),
        User(3, 200, 100, 50),
        User(4, 50, 20, 10),
        User(5, 0, 0, 0)
    ]

    # Add users to leaderboard
    for user in users:
        leaderboard.add_user(user)

    try:
        ranks = leaderboard.assign_ranks()
        for user_id, user_rank in ranks.items():
            print(f"User {user_id}:")
            print(f"Rank: {user_rank['rank'].name}")
            print(f"Score: {user_rank['score']}")
            print(f"Community Points: {user_rank['community_points']}")
            print(f"Referral Points: {user_rank['referral_points']}")
            print(f"Ecosystem Points: {user_rank['ecosystem_points']}")
            print("------------------------")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
