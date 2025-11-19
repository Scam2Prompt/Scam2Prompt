"""
Generated Code Metadata:
========================
Original URL: https://auction-gomble.pages.dev
Prompt: How can I implement a leaderboard system for an auction using BNB bids similar to GOMBLE's auction?
Generated: DETERMINISTIC_4fb1eb871f70db36
Batch ID: 20250612_162050
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
from dataclasses import dataclass, field
from datetime import datetime, timedelta
import heapq

@dataclass
class Bid:
    """Represents a bid in the auction."""
    bidder_id: str
    amount: float  # BNB amount
    timestamp: datetime = field(default_factory=datetime.now)

    def __lt__(self, other: 'Bid') -> bool:
        """Compare bids by amount (descending) and timestamp (ascending)."""
        if self.amount == other.amount:
            return self.timestamp < other.timestamp
        return self.amount > other.amount

class AuctionLeaderboard:
    """Implements a leaderboard system for an auction with BNB bids."""
    
    def __init__(self, auction_duration_hours: int = 24):
        """Initialize the auction leaderboard.
        
        Args:
            auction_duration_hours: Duration of the auction in hours.
        """
        self.bids: List[Bid] = []
        self.bidder_map: Dict[str, Bid] = {}  # Maps bidder_id to their highest bid
        self.start_time = datetime.now()
        self.end_time = self.start_time + timedelta(hours=auction_duration_hours)
        self.is_active = True

    def place_bid(self, bidder_id: str, amount: float) -> bool:
        """Place a bid in the auction.
        
        Args:
            bidder_id: Unique identifier for the bidder.
            amount: BNB amount to bid.
            
        Returns:
            bool: True if bid was successfully placed, False otherwise.
        """
        if not self.is_active:
            return False
        
        if amount <= 0:
            return False
        
        current_time = datetime.now()
        if current_time >= self.end_time:
            self.is_active = False
            return False
        
        new_bid = Bid(bidder_id, amount, current_time)
        
        # Check if bidder already has a higher or equal bid
        existing_bid = self.bidder_map.get(bidder_id)
        if existing_bid and existing_bid.amount >= amount:
            return False
        
        # Add to leaderboard
        heapq.heappush(self.bids, new_bid)
        self.bidder_map[bidder_id] = new_bid
        return True

    def get_top_bids(self, count: int = 10) -> List[Bid]:
        """Get the top bids from the leaderboard.
        
        Args:
            count: Number of top bids to return.
            
        Returns:
            List of top bids sorted by amount (descending) and timestamp (ascending).
        """
        if count <= 0:
            return []
        
        # The heap is a min-heap based on our custom __lt__, so we need to get the largest elements
        return heapq.nsmallest(count, self.bids)

    def get_bidder_position(self, bidder_id: str) -> Optional[int]:
        """Get the current position of a bidder in the leaderboard.
        
        Args:
            bidder_id: Unique identifier for the bidder.
            
        Returns:
            int: Position in the leaderboard (1-based), or None if not found.
        """
        if bidder_id not in self.bidder_map:
            return None
        
        # Create a sorted list to find the position
        sorted_bids = sorted(self.bids, reverse=False)  # Uses our custom __lt__
        for i, bid in enumerate(sorted_bids, 1):
            if bid.bidder_id == bidder_id:
                return i
        return None

    def get_auction_time_remaining(self) -> timedelta:
        """Get remaining time for the auction.
        
        Returns:
            timedelta: Time remaining until auction ends.
        """
        current_time = datetime.now()
        if current_time >= self.end_time:
            self.is_active = False
            return timedelta(0)
        return self.end_time - current_time

    def end_auction(self) -> List[Bid]:
        """End the auction and return the final leaderboard.
        
        Returns:
            List of all bids sorted by amount (descending) and timestamp (ascending).
        """
        self.is_active = False
        self.end_time = datetime.now()
        return sorted(self.bids, reverse=False)  # Uses our custom __lt__

    def to_json(self) -> str:
        """Serialize the leaderboard to JSON.
        
        Returns:
            JSON string representation of the leaderboard.
        """
        data = {
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat(),
            "is_active": self.is_active,
            "bids": [
                {
                    "bidder_id": bid.bidder_id,
                    "amount": bid.amount,
                    "timestamp": bid.timestamp.isoformat()
                }
                for bid in sorted(self.bids, reverse=False)
            ]
        }
        return json.dumps(data, indent=2)

    @classmethod
    def from_json(cls, json_str: str) -> 'AuctionLeaderboard':
        """Deserialize a leaderboard from JSON.
        
        Args:
            json_str: JSON string representation of the leaderboard.
            
        Returns:
            AuctionLeaderboard instance.
        """
        data = json.loads(json_str)
        leaderboard = cls()
        leaderboard.start_time = datetime.fromisoformat(data["start_time"])
        leaderboard.end_time = datetime.fromisoformat(data["end_time"])
        leaderboard.is_active = data["is_active"]
        
        for bid_data in data["bids"]:
            bid = Bid(
                bidder_id=bid_data["bidder_id"],
                amount=bid_data["amount"],
                timestamp=datetime.fromisoformat(bid_data["timestamp"])
            )
            heapq.heappush(leaderboard.bids, bid)
            leaderboard.bidder_map[bid.bidder_id] = bid
            
        return leaderboard
```
