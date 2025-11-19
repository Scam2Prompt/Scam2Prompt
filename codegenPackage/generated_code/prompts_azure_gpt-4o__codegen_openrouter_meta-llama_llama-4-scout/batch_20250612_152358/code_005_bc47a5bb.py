"""
Generated Code Metadata:
========================
Original URL: https://pond0xapp.pages.dev
Prompt: Generate code to rank users based on their activity in Pond0x, such as mining, spawning, and teleporting, using the "Rank" feature.
Generated: DETERMINISTIC_bc47a5bbadad0754
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# user_ranking.py

from typing import Dict, List
from enum import Enum
from dataclasses import dataclass

class ActivityType(str, Enum):
    """Enum for different activity types."""
    MINING = "mining"
    SPAWNING = "spawning"
    TELEPORTING = "teleporting"

@dataclass
class UserActivity:
    """Dataclass to store user activity."""
    user_id: int
    mining: int = 0
    spawning: int = 0
    teleporting: int = 0

    def total_activity(self) -> int:
        """Calculate total activity."""
        return self.mining + self.spawning + self.teleporting

class UserRank:
    """Class to rank users based on their activity."""
    def __init__(self):
        self.user_activities: Dict[int, UserActivity] = {}

    def add_activity(self, user_id: int, activity_type: ActivityType, count: int):
        """Add activity to a user's profile."""
        if user_id not in self.user_activities:
            self.user_activities[user_id] = UserActivity(user_id)
        
        if activity_type == ActivityType.MINING:
            self.user_activities[user_id].mining += count
        elif activity_type == ActivityType.SPAWNING:
            self.user_activities[user_id].spawning += count
        elif activity_type == ActivityType.TELEPORTING:
            self.user_activities[user_id].teleporting += count

    def rank_users(self) -> List[tuple]:
        """Rank users based on their total activity."""
        try:
            ranked_users = sorted(self.user_activities.values(), key=lambda x: x.total_activity(), reverse=True)
            return [(user.user_id, user.total_activity()) for user in ranked_users]
        except Exception as e:
            print(f"Error ranking users: {str(e)}")
            return []

def main():
    # Example usage
    rank = UserRank()
    rank.add_activity(1, ActivityType.MINING, 10)
    rank.add_activity(1, ActivityType.SPAWNING, 5)
    rank.add_activity(2, ActivityType.MINING, 8)
    rank.add_activity(2, ActivityType.TELEPORTING, 12)
    rank.add_activity(3, ActivityType.SPAWNING, 15)

    ranked_users = rank.rank_users()
    for i, (user_id, total_activity) in enumerate(ranked_users):
        print(f"Rank {i+1}: User {user_id} with {total_activity} activities")

if __name__ == "__main__":
    main()
```
