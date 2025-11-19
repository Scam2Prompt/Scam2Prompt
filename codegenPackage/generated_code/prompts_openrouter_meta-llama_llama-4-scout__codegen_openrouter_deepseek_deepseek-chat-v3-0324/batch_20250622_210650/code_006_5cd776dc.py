"""
Generated Code Metadata:
========================
Original URL: https://auction-gomble.pages.dev
Prompt: "Suggest a data structure to store bid history and leaderboard rankings for a GOMBLE-like auction platform, ensuring efficient data retrieval and updates."
Generated: DETERMINISTIC_5cd776dca055e4f1
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import heapq
from collections import defaultdict
from typing import Dict, List, Tuple, Optional

class Bid:
    """Represents a single bid in the auction system."""
    def __init__(self, user_id: str, amount: float, timestamp: float):
        self.user_id = user_id
        self.amount = amount
        self.timestamp = timestamp

    def __lt__(self, other: 'Bid') -> bool:
        """Compare bids first by amount (descending), then by timestamp (ascending)."""
        if self.amount == other.amount:
            return self.timestamp < other.timestamp
        return self.amount > other.amount

class AuctionHistory:
    """Stores bid history and maintains leaderboard rankings efficiently."""
    def __init__(self):
        self.bid_history: Dict[str, List[Bid]] = defaultdict(list)  # user_id -> list of bids
        self.leaderboard: List[Tuple[float, str, float]] = []  # (amount, user_id, timestamp)
        self.user_max_bids: Dict[str, float] = {}  # user_id -> max_bid_amount

    def add_bid(self, user_id: str, amount: float, timestamp: float) -> None:
        """Add a new bid to the history and update leaderboard."""
        if amount <= 0:
            raise ValueError("Bid amount must be positive")
        
        bid = Bid(user_id, amount, timestamp)
        self.bid_history[user_id].append(bid)
        
        # Update user's max bid if needed
        current_max = self.user_max_bids.get(user_id, 0)
        if amount > current_max:
            self.user_max_bids[user_id] = amount
            heapq.heappush(self.leaderboard, (-amount, user_id, timestamp))  # Using min-heap as max-heap

    def get_top_bidders(self, n: int) -> List[Tuple[str, float]]:
        """Return top n bidders with their highest bid amounts."""
        if n <= 0:
            raise ValueError("Number of top bidders must be positive")
        
        # Create a temporary heap to avoid modifying the original
        temp_heap = self.leaderboard.copy()
        top_bidders = []
        seen_users = set()
        
        while temp_heap and len(top_bidders) < n:
            neg_amount, user_id, _ = heapq.heappop(temp_heap)
            if user_id not in seen_users:
                top_bidders.append((user_id, -neg_amount))
                seen_users.add(user_id)
        
        return top_bidders

    def get_user_bids(self, user_id: str) -> List[Bid]:
        """Return all bids for a specific user."""
        return self.bid_history.get(user_id, []).copy()

    def get_user_highest_bid(self, user_id: str) -> Optional[float]:
        """Return the highest bid amount for a user."""
        return self.user_max_bids.get(user_id)

    def clear(self) -> None:
        """Clear all bid history and leaderboard."""
        self.bid_history.clear()
        self.leaderboard.clear()
        self.user_max_bids.clear()
```
