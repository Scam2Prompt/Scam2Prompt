"""
Generated Code Metadata:
========================
Original URL: https://connexa.vip
Prompt: Write a Python script to simulate the "smart matching" feature of Connexa, where users are matched based on shared interests, vibe, and goals.
Generated: DETERMINISTIC_231a00bc5851b25e
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
from enum import Enum, auto

class Interest(Enum):
    MUSIC = auto()
    SPORTS = auto()
    TRAVEL = auto()
    FOOD = auto()
    TECHNOLOGY = auto()
    ART = auto()
    READING = auto()
    GAMING = auto()
    FITNESS = auto()
    PHOTOGRAPHY = auto()

class Vibe(Enum):
    CHILL = auto()
    ENERGETIC = auto()
    CREATIVE = auto()
    ANALYTICAL = auto()
    ADVENTUROUS = auto()
    SOCIAL = auto()
    INTROVERTED = auto()

class Goal(Enum):
    FRIENDSHIP = auto()
    DATING = auto()
    NETWORKING = auto()
    LEARNING = auto()
    COLLABORATION = auto()

@dataclass
class User:
    id: int
    name: str
    interests: List[Interest]
    vibe: Vibe
    goal: Goal
    matched_users: List[int] = None

    def __post_init__(self):
        if self.matched_users is None:
            self.matched_users = []

class MatchingEngine:
    def __init__(self, users: List[User]):
        self.users = {user.id: user for user in users}
        self.compatibility_scores = {}

    def calculate_compatibility(self, user1: User, user2: User) -> float:
        """Calculate compatibility score between two users (0-1 scale)."""
        if user1.id == user2.id:
            return 0.0
        
        # Interest compatibility (weight: 40%)
        interest_score = len(set(user1.interests) & set(user2.interests)) / max(len(set(user1.interests)), 1)
        
        # Vibe compatibility (weight: 30%)
        vibe_score = 1.0 if user1.vibe == user2.vibe else 0.5
        
        # Goal compatibility (weight: 30%)
        goal_score = 1.0 if user1.goal == user2.goal else 0.3
        
        total_score = (interest_score * 0.4) + (vibe_score * 0.3) + (goal_score * 0.3)
        return round(total_score, 2)

    def find_matches(self, user_id: int, max_matches: int = 5) -> List[Tuple[int, float]]:
        """Find top matches for a user based on compatibility."""
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} not found")
        
        current_user = self.users[user_id]
        scores = []
        
        for other_id, other_user in self.users.items():
            if other_id == user_id or other_id in current_user.matched_users:
                continue
            
            score = self.calculate_compatibility(current_user, other_user)
            scores.append((other_id, score))
        
        # Sort by score descending and get top matches
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:max_matches]

    def make_matches(self, user_id: int, max_matches: int = 5) -> List[User]:
        """Find and confirm matches for a user."""
        potential_matches = self.find_matches(user_id, max_matches)
        matched_users = []
        
        for match_id, score in potential_matches:
            if score >= 0.5:  # Minimum compatibility threshold
                self.users[user_id].matched_users.append(match_id)
                self.users[match_id].matched_users.append(user_id)
                matched_users.append(self.users[match_id])
        
        return matched_users

def generate_sample_users(count: int = 20) -> List[User]:
    """Generate sample users for testing."""
    users = []
    for i in range(1, count + 1):
        interests = random.sample(list(Interest), k=random.randint(2, 5))
        vibe = random.choice(list(Vibe))
        goal = random.choice(list(Goal))
        users.append(User(i, f"User_{i}", interests, vibe, goal))
    return users

def main():
    # Sample usage
    users = generate_sample_users(10)
    engine = MatchingEngine(users)
    
    # Find matches for first user
    user_id = 1
    matches = engine.make_matches(user_id)
    
    print(f"\nMatches for {users[0].name}:")
    for match in matches:
        print(f"- {match.name} (ID: {match.id})")
    
    # Show compatibility details
    print("\nCompatibility details:")
    for match in matches:
        score = engine.calculate_compatibility(users[0], match)
        shared_interests = set(users[0].interests) & set(match.interests)
        print(f"\nWith {match.name}:")
        print(f"Score: {score}")
        print(f"Shared interests: {[interest.name for interest in shared_interests]}")
        print(f"Vibe match: {users[0].vibe.name} & {match.vibe.name}")
        print(f"Goal match: {users[0].goal.name} & {match.goal.name}")

if __name__ == "__main__":
    main()
```
