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
from dataclasses import dataclass
from typing import List
import math

@dataclass
class UserStats:
    """Represents a user's statistics for ranking."""
    user_id: str
    community_points: float = 0.0
    referral_points: float = 0.0
    ecosystem_points: float = 0.0

class LeaderboardRanker:
    """Handles ranking users based on multiple point categories."""
    
    # Weight factors for different point categories
    COMMUNITY_WEIGHT = 0.5
    REFERRAL_WEIGHT = 0.3
    ECOSYSTEM_WEIGHT = 0.2
    
    def __init__(self, users: List[UserStats]):
        """Initialize with a list of user statistics."""
        if not users:
            raise ValueError("User list cannot be empty")
        self.users = users
    
    def _calculate_score(self, user: UserStats) -> float:
        """Calculate weighted score for a user."""
        try:
            community_score = user.community_points * self.COMMUNITY_WEIGHT
            referral_score = user.referral_points * self.REFERRAL_WEIGHT
            ecosystem_score = user.ecosystem_points * self.ECOSYSTEM_WEIGHT
            
            # Apply logarithmic scaling to prevent domination by any single metric
            scaled_community = math.log1p(community_score)
            scaled_referral = math.log1p(referral_score)
            scaled_ecosystem = math.log1p(ecosystem_score)
            
            return scaled_community + scaled_referral + scaled_ecosystem
        except (ValueError, TypeError) as e:
            raise ValueError(f"Invalid point values for user {user.user_id}: {e}")
    
    def rank_users(self) -> List[dict]:
        """
        Rank users based on their weighted scores.
        
        Returns:
            List of dictionaries containing user_id and rank, sorted by rank.
        """
        try:
            ranked_users = sorted(
                self.users,
                key=lambda u: self._calculate_score(u),
                reverse=True
            )
            
            return [
                {
                    "user_id": user.user_id,
                    "rank": i + 1,
                    "total_score": self._calculate_score(user),
                    "community_points": user.community_points,
                    "referral_points": user.referral_points,
                    "ecosystem_points": user.ecosystem_points
                }
                for i, user in enumerate(ranked_users)
            ]
        except Exception as e:
            raise RuntimeError(f"Failed to rank users: {e}")

# Example usage
if __name__ == "__main__":
    try:
        users = [
            UserStats("user1", 150, 50, 30),
            UserStats("user2", 100, 75, 20),
            UserStats("user3", 200, 10, 5),
            UserStats("user4", 50, 100, 40)
        ]
        
        ranker = LeaderboardRanker(users)
        rankings = ranker.rank_users()
        
        print("Leaderboard Rankings:")
        for entry in rankings:
            print(f"Rank {entry['rank']}: {entry['user_id']} (Score: {entry['total_score']:.2f})")
    except Exception as e:
        print(f"Error: {e}")
```
