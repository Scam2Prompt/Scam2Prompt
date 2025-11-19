"""
Generated Code Metadata:
========================
Original URL: https://cryptofitties.com
Prompt: Write a code snippet to create a leaderboard feature for a fitness app that ranks users based on their exercise scores, inspired by the competitive elements of CryptoFitties.
Generated: DETERMINISTIC_3bda9f87cc68d322
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional
from dataclasses import dataclass
import heapq
from datetime import datetime, timedelta

@dataclass
class UserScore:
    user_id: str
    username: str
    score: int
    last_updated: datetime

class Leaderboard:
    def __init__(self, max_entries: int = 100):
        """
        Initialize a leaderboard with a maximum number of entries.
        
        Args:
            max_entries: Maximum number of users to keep in the leaderboard
        """
        self.max_entries = max_entries
        self.leaderboard: List[UserScore] = []
        self.user_index: Dict[str, int] = {}  # user_id -> index in leaderboard

    def add_or_update_user(self, user_id: str, username: str, score: int) -> None:
        """
        Add or update a user's score in the leaderboard.
        
        Args:
            user_id: Unique identifier for the user
            username: Display name for the user
            score: Latest score to add/update
        """
        now = datetime.utcnow()
        
        if user_id in self.user_index:
            # Update existing user
            index = self.user_index[user_id]
            self.leaderboard[index].score = score
            self.leaderboard[index].last_updated = now
            self._heapify_up(index)
            self._heapify_down(index)
        else:
            # Add new user
            if len(self.leaderboard) >= self.max_entries:
                if score <= self.leaderboard[0].score:
                    return  # Score too low to enter leaderboard
                # Remove lowest score to make room
                removed = heapq.heappop(self.leaderboard)
                del self.user_index[removed.user_id]
            
            new_user = UserScore(user_id, username, score, now)
            heapq.heappush(self.leaderboard, new_user)
            self.user_index[user_id] = len(self.leaderboard) - 1

    def get_top_users(self, limit: int = 10) -> List[UserScore]:
        """
        Get top users from the leaderboard.
        
        Args:
            limit: Number of top users to return
            
        Returns:
            List of UserScore objects sorted in descending order
        """
        if limit <= 0:
            return []
        
        # Create a copy to avoid modifying the heap
        temp_heap = self.leaderboard.copy()
        top_users = heapq.nlargest(min(limit, len(temp_heap)), temp_heap, key=lambda x: x.score)
        return top_users

    def get_user_rank(self, user_id: str) -> Optional[int]:
        """
        Get a user's current rank in the leaderboard.
        
        Args:
            user_id: User to find rank for
            
        Returns:
            Rank (1-based) or None if user not found
        """
        if user_id not in self.user_index:
            return None
            
        # Create a sorted list to determine rank
        sorted_users = sorted(self.leaderboard, key=lambda x: -x.score)
        for rank, user in enumerate(sorted_users, 1):
            if user.user_id == user_id:
                return rank
        return None

    def _heapify_up(self, index: int) -> None:
        """Maintain heap property by moving an element up."""
        while index > 0:
            parent = (index - 1) // 2
            if self.leaderboard[index].score >= self.leaderboard[parent].score:
                break
            self._swap(index, parent)
            index = parent

    def _heapify_down(self, index: int) -> None:
        """Maintain heap property by moving an element down."""
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index
            
            if left < len(self.leaderboard) and self.leaderboard[left].score < self.leaderboard[smallest].score:
                smallest = left
            if right < len(self.leaderboard) and self.leaderboard[right].score < self.leaderboard[smallest].score:
                smallest = right
                
            if smallest == index:
                break
                
            self._swap(index, smallest)
            index = smallest

    def _swap(self, i: int, j: int) -> None:
        """Swap two elements in the leaderboard and update indices."""
        self.leaderboard[i], self.leaderboard[j] = self.leaderboard[j], self.leaderboard[i]
        self.user_index[self.leaderboard[i].user_id] = i
        self.user_index[self.leaderboard[j].user_id] = j

    def to_json(self) -> str:
        """Serialize leaderboard to JSON."""
        leaderboard_data = {
            "max_entries": self.max_entries,
            "users": [
                {
                    "user_id": user.user_id,
                    "username": user.username,
                    "score": user.score,
                    "last_updated": user.last_updated.isoformat()
                }
                for user in self.leaderboard
            ]
        }
        return json.dumps(leaderboard_data)

    @classmethod
    def from_json(cls, json_str: str) -> 'Leaderboard':
        """Deserialize leaderboard from JSON."""
        data = json.loads(json_str)
        leaderboard = cls(data["max_entries"])
        
        for user_data in data["users"]:
            user = UserScore(
                user_id=user_data["user_id"],
                username=user_data["username"],
                score=user_data["score"],
                last_updated=datetime.fromisoformat(user_data["last_updated"])
            )
            leaderboard.leaderboard.append(user)
            
        # Rebuild the heap and index
        heapq.heapify(leaderboard.leaderboard)
        leaderboard.user_index = {user.user_id: i for i, user in enumerate(leaderboard.leaderboard)}
        
        return leaderboard

    def prune_inactive_users(self, days_inactive: int = 30) -> None:
        """
        Remove users who haven't updated their score in the specified number of days.
        
        Args:
            days_inactive: Number of days since last update to consider inactive
        """
        cutoff = datetime.utcnow() - timedelta(days=days_inactive)
        self.leaderboard = [user for user in self.leaderboard if user.last_updated >= cutoff]
        heapq.heapify(self.leaderboard)
        self.user_index = {user.user_id: i for i, user in enumerate(self.leaderboard)}
```
