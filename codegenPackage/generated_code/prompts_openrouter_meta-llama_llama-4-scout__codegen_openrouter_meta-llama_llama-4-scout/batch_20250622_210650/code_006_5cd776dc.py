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
from typing import Dict, List
from collections import defaultdict
import heapq

class BidHistory:
    def __init__(self):
        """
        Initialize bid history data structure.
        
        Attributes:
        bid_history (Dict): Mapping of item IDs to their bid histories.
        leaderboard (Dict): Mapping of user IDs to their current scores.
        top_bidders (List): Heap to store top bidders for efficient retrieval.
        """
        self.bid_history = defaultdict(list)
        self.leaderboard = {}
        self.top_bidders = []

    def place_bid(self, item_id: int, user_id: int, bid_amount: float) -> None:
        """
        Place a bid on an item.

        Args:
        item_id (int): ID of the item being bid on.
        user_id (int): ID of the user placing the bid.
        bid_amount (float): Amount of the bid.

        Raises:
        ValueError: If bid amount is non-positive.
        """
        if bid_amount <= 0:
            raise ValueError("Bid amount must be positive")

        # Update bid history
        self.bid_history[item_id].append((user_id, bid_amount))

        # Update leaderboard
        if user_id not in self.leaderboard:
            self.leaderboard[user_id] = 0
        self.leaderboard[user_id] += bid_amount

        # Update top bidders heap
        heapq.heappush(self.top_bidders, (-self.leaderboard[user_id], user_id))

    def get_bid_history(self, item_id: int) -> List:
        """
        Retrieve bid history for an item.

        Args:
        item_id (int): ID of the item.

        Returns:
        List: List of tuples containing user IDs and their corresponding bids.
        """
        return self.bid_history[item_id]

    def get_leaderboard(self, num_top_bidders: int = 10) -> List:
        """
        Retrieve top bidders from the leaderboard.

        Args:
        num_top_bidders (int): Number of top bidders to retrieve.

        Returns:
        List: List of tuples containing user IDs and their current scores.
        """
        top_bidders = []
        heap = self.top_bidders[:]
        for _ in range(min(num_top_bidders, len(heap))):
            score, user_id = heapq.heappop(heap)
            top_bidders.append((user_id, -score))
        return top_bidders

    def get_user_score(self, user_id: int) -> float:
        """
        Retrieve a user's current score.

        Args:
        user_id (int): ID of the user.

        Returns:
        float: User's current score.
        """
        return self.leaderboard.get(user_id, 0)


# Example usage
if __name__ == "__main__":
    bid_history = BidHistory()

    # Place bids
    bid_history.place_bid(1, 1, 100.0)
    bid_history.place_bid(1, 2, 150.0)
    bid_history.place_bid(2, 1, 200.0)
    bid_history.place_bid(2, 3, 250.0)

    # Retrieve bid history
    print("Bid History for Item 1:")
    print(bid_history.get_bid_history(1))

    # Retrieve leaderboard
    print("\nTop 10 Bidders:")
    print(bid_history.get_leaderboard())

    # Retrieve user score
    print("\nUser 1 Score:")
    print(bid_history.get_user_score(1))
```
