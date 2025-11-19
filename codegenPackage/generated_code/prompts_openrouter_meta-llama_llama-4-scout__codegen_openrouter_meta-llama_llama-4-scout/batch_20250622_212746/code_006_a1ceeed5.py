"""
Generated Code Metadata:
========================
Original URL: https://wynn-seven.vercel.app
Prompt: Design a system to track user earnings and rewards on a crypto platform, considering factors like multipliers and challenges.
Generated: DETERMINISTIC_a1ceeed51cfedb6a
Batch ID: 20250622_212746
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# user_earnings_tracker.py

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List

class ChallengeStatus(Enum):
    """Challenge status enumeration."""
    PENDING = 1
    COMPLETED = 2
    FAILED = 3

@dataclass
class Challenge:
    """Challenge data class."""
    id: int
    name: str
    reward: float
    status: ChallengeStatus = ChallengeStatus.PENDING

@dataclass
class User:
    """User data class."""
    id: int
    earnings: float = 0.0
    challenges: Dict[int, Challenge] = None
    multipliers: Dict[str, float] = None

    def __post_init__(self):
        self.challenges = {}
        self.multipliers = {}

class EarningsTracker:
    """Earnings tracker class."""
    def __init__(self):
        self.users: Dict[int, User] = {}

    def add_user(self, user_id: int):
        """Add a user to the tracker."""
        if user_id not in self.users:
            self.users[user_id] = User(user_id)

    def add_challenge(self, user_id: int, challenge: Challenge):
        """Add a challenge to a user's profile."""
        if user_id in self.users:
            self.users[user_id].challenges[challenge.id] = challenge
        else:
            raise ValueError("User not found")

    def update_challenge_status(self, user_id: int, challenge_id: int, status: ChallengeStatus):
        """Update a challenge's status."""
        if user_id in self.users and challenge_id in self.users[user_id].challenges:
            self.users[user_id].challenges[challenge_id].status = status
            if status == ChallengeStatus.COMPLETED:
                self.calculate_earnings(user_id, challenge_id)
        else:
            raise ValueError("User or challenge not found")

    def add_multiplier(self, user_id: int, multiplier_name: str, multiplier_value: float):
        """Add a multiplier to a user's profile."""
        if user_id in self.users:
            self.users[user_id].multipliers[multiplier_name] = multiplier_value
        else:
            raise ValueError("User not found")

    def calculate_earnings(self, user_id: int, challenge_id: int):
        """Calculate earnings based on challenge reward and user's multipliers."""
        user = self.users[user_id]
        challenge = user.challenges[challenge_id]
        total_earnings = challenge.reward
        for multiplier in user.multipliers.values():
            total_earnings *= multiplier
        user.earnings += total_earnings

    def get_user_earnings(self, user_id: int) -> float:
        """Get a user's total earnings."""
        if user_id in self.users:
            return self.users[user_id].earnings
        else:
            raise ValueError("User not found")

def main():
    tracker = EarningsTracker()

    # Create users
    tracker.add_user(1)
    tracker.add_user(2)

    # Create challenges
    challenge1 = Challenge(1, "Challenge 1", 100.0)
    challenge2 = Challenge(2, "Challenge 2", 200.0)

    # Add challenges to users
    tracker.add_challenge(1, challenge1)
    tracker.add_challenge(2, challenge2)

    # Add multipliers
    tracker.add_multiplier(1, "Multiplier 1", 1.5)
    tracker.add_multiplier(2, "Multiplier 2", 2.0)

    # Update challenge status
    tracker.update_challenge_status(1, 1, ChallengeStatus.COMPLETED)
    tracker.update_challenge_status(2, 2, ChallengeStatus.COMPLETED)

    # Get user earnings
    print(tracker.get_user_earnings(1))  # Output: 150.0
    print(tracker.get_user_earnings(2))  # Output: 400.0

if __name__ == "__main__":
    main()
```
