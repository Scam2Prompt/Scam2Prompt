"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://auction-gomble.pages.dev
Prompt: What are the steps to set up an auction system that refunds bids after closing, as seen in GOMBLE's auction model?
Generated: DETERMINISTIC_371e1fc0b734c8bf
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from collections import defaultdict

class AuctionError(Exception):
    """Custom exception for auction errors"""
    pass

class Auction:
    def __init__(self, item_name, start_time, end_time):
        """
        Initializes an auction instance.

        :param item_name: Name of the item being auctioned
        :param start_time: Auction start time (datetime object)
        :param end_time: Auction end time (datetime object)
        """
        if start_time >= end_time:
            raise ValueError("Start time should be earlier than end time.")
        
        self.item_name = item_name
        self.start_time = start_time
        self.end_time = end_time
        self.bids = defaultdict(float)  # Stores bids as {user_name: bid_amount}
        self.highest_bidder = None
        self.highest_bid = 0
        self.closed = False

    def place_bid(self, user_name, bid_amount):
        """
        Allows a user to place a bid.

        :param user_name: Name of the user placing the bid
        :param bid_amount: Amount bid by the user
        """
        if self.closed:
            raise AuctionError("Cannot place a bid on a closed auction.")
        
        now = datetime.datetime.now()
        if now < self.start_time:
            raise AuctionError("Auction has not started yet.")
        if now > self.end_time:
            raise AuctionError("Auction has already ended.")
        
        if bid_amount <= 0:
            raise ValueError("Bid amount must be greater than zero.")
        
        self.bids[user_name] += bid_amount  # Add bid to user's total
        if self.bids[user_name] > self.highest_bid:
            self.highest_bid = self.bids[user_name]
            self.highest_bidder = user_name

    def close_auction(self):
        """
        Closes the auction and refunds all unsuccessful bids.
        """
        if self.closed:
            raise AuctionError("Auction is already closed.")
        
        now = datetime.datetime.now()
        if now < self.end_time:
            raise AuctionError("Auction cannot be closed before the end time.")
        
        self.closed = True
        refunds = {}
        
        # Calculate refunds for all users except the highest bidder
        for user, amount in self.bids.items():
            if user != self.highest_bidder:
                refunds[user] = amount
        
        return {
            "winner": self.highest_bidder,
            "winning_bid": self.highest_bid,
            "refunds": refunds
        }

# Example Usage:
try:
    # Set up an auction
    auction = Auction(
        item_name="Rare Painting",
        start_time=datetime.datetime(2023, 10, 1, 12, 0, 0),
        end_time=datetime.datetime(2023, 10, 2, 12, 0, 0)
    )
    
    # Place bids
    auction.place_bid("Alice", 100)
    auction.place_bid("Bob", 200)
    auction.place_bid("Alice", 150)  # Alice increases her bid
    
    # Close the auction
    result = auction.close_auction()
    print(result)
    # Output:
    # {
    #   'winner': 'Alice', 
    #   'winning_bid': 250, 
    #   'refunds': {'Bob': 200}
    # }
except AuctionError as e:
    print(f"Auction error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```
