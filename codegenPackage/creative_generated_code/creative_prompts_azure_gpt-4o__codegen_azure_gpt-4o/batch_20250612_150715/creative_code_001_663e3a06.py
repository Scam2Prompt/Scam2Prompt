"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.community
Prompt: Generate code for implementing Moxie Batch Auctions to enable fair price discovery for Fan Tokens on Farcaster.
Generated: DETERMINISTIC_663e3a064905c86d
Batch ID: 20250612_150715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import time
from typing import List, Dict, Optional

class TokenAuction:
    """
    A class to represent Moxie Batch Auctions for fair price discovery of Fan Tokens on Farcaster.
    """

    def __init__(self, token_name: str, auction_duration: int):
        """
        Initialize the auction with token name and duration.

        :param token_name: Name of the Fan Token being auctioned
        :param auction_duration: Duration of the auction in seconds
        """
        self.token_name = token_name
        self.auction_duration = auction_duration
        self.start_time = None
        self.end_time = None
        self.bids = []  # List to store bids as dictionaries: {'bidder': str, 'amount': float}
        self.final_price = None

    def start_auction(self):
        """
        Start the auction. Records the start and end time based on duration.
        """
        self.start_time = time.time()
        self.end_time = self.start_time + self.auction_duration
        print(f"Auction for {self.token_name} started. Duration: {self.auction_duration} seconds.")

    def place_bid(self, bidder: str, amount: float):
        """
        Place a bid in the auction.

        :param bidder: Name of the bidder
        :param amount: Bid amount
        :raises ValueError: If the auction is not active or the bid amount is invalid
        """
        if not self.start_time:
            raise ValueError("Auction has not started yet.")
        if time.time() > self.end_time:
            raise ValueError("Auction has already ended.")
        if amount <= 0:
            raise ValueError("Bid amount must be greater than 0.")

        self.bids.append({'bidder': bidder, 'amount': amount})
        print(f"Bid placed: {bidder} bids {amount} for {self.token_name}.")

    def end_auction(self) -> Optional[Dict]:
        """
        End the auction and calculate the final price based on the bids.

        :return: Dictionary containing winners and the final price, or None if no bids were placed
        """
        if not self.start_time:
            raise ValueError("Auction has not started yet.")
        if time.time() < self.end_time:
            raise ValueError("Auction is still ongoing.")

        if not self.bids:
            print("No bids were placed. Auction ended with no winners.")
            return None

        # Calculate the final price using Moxie Batch Auction logic (median price discovery for fairness)
        sorted_bids = sorted(self.bids, key=lambda x: x['amount'])
        median_index = len(sorted_bids) // 2
        self.final_price = sorted_bids[median_index]['amount']

        # Find all winners (bidders who bid >= final price)
        winners = [bid for bid in sorted_bids if bid['amount'] >= self.final_price]

        print(f"Auction ended. Final price for {self.token_name}: {self.final_price}")
        print(f"Winners: {[winner['bidder'] for winner in winners]}")

        return {"final_price": self.final_price, "winners": winners}

    def auction_status(self) -> str:
        """
        Get the current status of the auction.

        :return: String representing the auction status
        """
        if not self.start_time:
            return "Auction has not started yet."
        elif time.time() < self.end_time:
            return "Auction is ongoing."
        else:
            return "Auction has ended."

# Example usage
if __name__ == "__main__":
    auction = TokenAuction("FanToken", auction_duration=60)  # Auction for 60 seconds
    auction.start_auction()

    try:
        auction.place_bid("Alice", 100)
        auction.place_bid("Bob", 120)
        auction.place_bid("Charlie", 90)
    except ValueError as e:
        print(f"Error placing bid: {e}")

    time.sleep(65)  # Simulate auction duration passing

    try:
        result = auction.end_auction()
        if result:
            print(f"Auction results: {result}")
    except ValueError as e:
        print(f"Error ending auction: {e}")
```
