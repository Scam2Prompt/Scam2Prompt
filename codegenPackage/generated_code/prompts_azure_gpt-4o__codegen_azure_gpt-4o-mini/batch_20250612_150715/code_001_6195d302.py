"""
Generated Code Metadata:
========================
Original URL: https://moxie.social
Prompt: Generate code for implementing Moxie Batch Auctions to launch Fan Tokens with fair price discovery on the Farcaster network.
Generated: DETERMINISTIC_6195d302ce65996e
Batch ID: 20250612_150715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random
from typing import List, Dict, Any

class FanTokenAuction:
    """
    A class to implement Moxie Batch Auctions for launching Fan Tokens
    with fair price discovery on the Farcaster network.
    """

    def __init__(self, token_name: str, starting_price: float, auction_duration: int):
        """
        Initializes the auction with the token name, starting price, and duration.

        :param token_name: The name of the fan token.
        :param starting_price: The starting price of the token.
        :param auction_duration: The duration of the auction in seconds.
        """
        self.token_name = token_name
        self.starting_price = starting_price
        self.auction_duration = auction_duration
        self.bids: List[Dict[str, Any]] = []
        self.auction_end_time = None

    def start_auction(self):
        """Starts the auction and sets the end time."""
        self.auction_end_time = time.time() + self.auction_duration
        print(f"Auction for {self.token_name} started. It will end at {self.auction_end_time}.")

    def place_bid(self, bidder: str, bid_amount: float):
        """
        Places a bid in the auction.

        :param bidder: The name of the bidder.
        :param bid_amount: The amount of the bid.
        :raises ValueError: If the bid is lower than the starting price or if the auction has ended.
        """
        if self.auction_end_time is None:
            raise ValueError("Auction has not started yet.")
        if time.time() > self.auction_end_time:
            raise ValueError("Auction has already ended.")
        if bid_amount < self.starting_price:
            raise ValueError("Bid amount must be greater than or equal to the starting price.")

        self.bids.append({"bidder": bidder, "amount": bid_amount})
        print(f"Bid placed by {bidder}: ${bid_amount}")

    def end_auction(self) -> Dict[str, Any]:
        """
        Ends the auction and determines the winning bid.

        :return: A dictionary containing the winning bidder and the winning bid amount.
        :raises RuntimeError: If the auction has not ended yet.
        """
        if time.time() < self.auction_end_time:
            raise RuntimeError("Auction is still ongoing.")

        if not self.bids:
            print("No bids were placed.")
            return {"winner": None, "winning_bid": 0}

        # Determine the highest bid
        winning_bid = max(self.bids, key=lambda x: x['amount'])
        print(f"Auction ended. Winner: {winning_bid['bidder']} with a bid of ${winning_bid['amount']}.")
        return {"winner": winning_bid['bidder'], "winning_bid": winning_bid['amount']}

# Example usage
if __name__ == "__main__":
    try:
        auction = FanTokenAuction(token_name="FanTokenX", starting_price=10.0, auction_duration=30)
        auction.start_auction()

        # Simulate bids
        auction.place_bid("Alice", 15.0)
        auction.place_bid("Bob", 20.0)

        # Wait for the auction to end
        time.sleep(30)

        # End the auction and get the results
        results = auction.end_auction()
        print(results)

    except Exception as e:
        print(f"An error occurred: {e}")
```
