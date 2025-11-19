"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.community
Prompt: Explain how to set up a Moxie Batch Auction for fair price discovery of Fan Tokens within the Farcaster economy.
Generated: DETERMINISTIC_46c446eb985915ec
Batch ID: 20250612_162854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is production-ready Python code that outlines how to set up a Moxie Batch Auction for fair price discovery of Fan Tokens within the Farcaster economy. This is a simplified version for educational purposes that implements key auction mechanics.

```python
import random
from decimal import Decimal
from typing import List, Dict, Tuple


class MoxieBatchAuction:
    """
    Class to handle the Moxie Batch Auction for fair price discovery of Fan Tokens.
    """

    def __init__(self, token_name: str, total_tokens: int, auction_duration: int):
        """
        Initialize the auction.

        :param token_name: Name of the Fan Token being auctioned.
        :param total_tokens: Total number of tokens to be auctioned.
        :param auction_duration: Duration of the auction in seconds.
        """
        self.token_name = token_name
        self.total_tokens = total_tokens
        self.auction_duration = auction_duration
        self.bids = []  # Stores all bids as (bidder_id, bid_amount, bid_price)
        self.is_auction_active = False

    def start_auction(self):
        """
        Start the auction.
        """
        if self.is_auction_active:
            raise RuntimeError("Auction is already active.")
        self.is_auction_active = True
        print(f"Auction for {self.token_name} started. Duration: {self.auction_duration} seconds.")

    def place_bid(self, bidder_id: str, bid_amount: int, bid_price: Decimal):
        """
        Place a bid in the auction.

        :param bidder_id: Unique identifier for the bidder.
        :param bid_amount: Number of tokens being bid for.
        :param bid_price: Price per token offered by the bidder.
        """
        if not self.is_auction_active:
            raise RuntimeError("Auction is not active. Cannot place a bid.")
        if bid_amount <= 0 or bid_price <= 0:
            raise ValueError("Bid amount and price must be greater than zero.")
        self.bids.append((bidder_id, bid_amount, bid_price))
        print(f"Bid placed: Bidder {bidder_id} bids {bid_amount} tokens at {bid_price} per token.")

    def end_auction(self):
        """
        End the auction and determine the clearing price.
        """
        if not self.is_auction_active:
            raise RuntimeError("Auction is not active. Cannot end an inactive auction.")
        self.is_auction_active = False

        # Sort bids by bid price in descending order
        self.bids.sort(key=lambda bid: bid[2], reverse=True)

        # Calculate clearing price
        tokens_allocated = 0
        clearing_price = Decimal("0")
        clearing_bidders = []

        for bidder_id, bid_amount, bid_price in self.bids:
            if tokens_allocated + bid_amount <= self.total_tokens:
                tokens_allocated += bid_amount
                clearing_bidders.append((bidder_id, bid_amount, bid_price))
                clearing_price = bid_price
            else:
                remaining_tokens = self.total_tokens - tokens_allocated
                if remaining_tokens > 0:
                    clearing_bidders.append((bidder_id, remaining_tokens, bid_price))
                    clearing_price = bid_price
                    tokens_allocated += remaining_tokens
                break

        print(f"Auction ended. Clearing price: {clearing_price} per token.")
        print("Winning bids:")
        for bidder in clearing_bidders:
            print(f"Bidder {bidder[0]} allocated {bidder[1]} tokens at price {bidder[2]} per token.")

    def get_auction_summary(self) -> Dict[str, any]:
        """
        Retrieve a summary of the auction status.

        :return: A dictionary with auction details.
        """
        return {
            "token_name": self.token_name,
            "total_tokens": self.total_tokens,
            "auction_duration": self.auction_duration,
            "is_auction_active": self.is_auction_active,
            "total_bids": len(self.bids),
        }


# Example usage (this would typically be part of a separate script or system):
if __name__ == "__main__":
    # Initialize the auction
    auction = MoxieBatchAuction(token_name="FanTokenX", total_tokens=1000, auction_duration=3600)

    # Start the auction
    auction.start_auction()

    # Place bids
    auction.place_bid(bidder_id="user1", bid_amount=400, bid_price=Decimal("1.5"))
    auction.place_bid(bidder_id="user2", bid_amount=300, bid_price=Decimal("1.6"))
    auction.place_bid(bidder_id="user3", bid_amount=500, bid_price=Decimal("1.4"))

    # End the auction
    auction.end_auction()

    # Get auction summary
    summary = auction.get_auction_summary()
    print("Auction Summary:", summary)
```

This code is self-contained, handles typical auction workflows, and includes error handling for invalid inputs and auction state transitions. Ensure the `decimal` module is used for accurate financial calculations. If integrating with external systems, additional features such as persistent storage and API endpoints may be required.
