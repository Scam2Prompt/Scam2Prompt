"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://auction-gomble.pages.dev
Prompt: How can I implement a leaderboard system for an auction using BNB bids similar to GOMBLE's auction?
Generated: DETERMINISTIC_4fb1eb871f70db36
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# auction_leaderboard.py

from typing import List, Dict
from dataclasses import dataclass, field

@dataclass(order=True)
class Bid:
    """Class representing a single bid in the auction."""
    bidder_id: str
    amount: float
    timestamp: float

@dataclass
class Leaderboard:
    """Class to manage the leaderboard for the auction based on BNB bids."""
    bids: List[Bid] = field(default_factory=list)
    
    def add_bid(self, bidder_id: str, amount: float, timestamp: float) -> None:
        """
        Add a new bid to the leaderboard.

        :param bidder_id: Unique identifier for the bidder.
        :param amount: Amount of the bid in BNB.
        :param timestamp: Time of the bid (in seconds since epoch).
        :raises ValueError: If the bid amount is non-positive.
        """
        if amount <= 0:
            raise ValueError("Bid amount must be greater than zero.")
        self.bids.append(Bid(bidder_id, amount, timestamp))

    def get_top_bidders(self, limit: int = 10) -> Dict[str, float]:
        """
        Retrieve the top bidders based on their highest bids.

        :param limit: The number of top bidders to retrieve.
        :return: Dictionary of bidder IDs and their highest bid amounts.
        """
        # Create a dictionary to store the highest bids per bidder
        highest_bids = {}
        for bid in self.bids:
            if bid.bidder_id not in highest_bids or bid.amount > highest_bids[bid.bidder_id]:
                highest_bids[bid.bidder_id] = bid.amount
                
        # Sort bidders by their highest bid amounts in descending order
        top_bidders = dict(sorted(highest_bids.items(), key=lambda item: item[1], reverse=True))
        
        # Return only the top bidders up to the specified limit
        return dict(list(top_bidders.items())[:limit])

def main():
    """Main function to demonstrate the leaderboard functionality."""
    leaderboard = Leaderboard()
    
    # Example bids (Normally, this data would come from the auction system)
    example_bids = [
        ('bidder1', 1.5, 1633017600),
        ('bidder2', 2.0, 1633017700),
        ('bidder1', 2.5, 1633017800),
        ('bidder3', 1.0, 1633017900),
        ('bidder2', 3.0, 1633018000),
    ]
    
    # Adding example bids to the leaderboard
    for bidder_id, amount, timestamp in example_bids:
        try:
            leaderboard.add_bid(bidder_id, amount, timestamp)
        except ValueError as e:
            print(f"Error adding bid: {e}")
    
    # Retrieve and print the top bidders
    top_bidders = leaderboard.get_top_bidders(limit=3)
    print("Top Bidders:")
    for bidder_id, amount in top_bidders.items():
        print(f"{bidder_id}: {amount} BNB")

if __name__ == "__main__":
    main()
```
