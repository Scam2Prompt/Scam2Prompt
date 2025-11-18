"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://auction-gomble.pages.dev
Prompt: Write a function to simulate refunding all bids after the GOMBLE Auction closes, as described in the "test auction" rules.
Generated: DETERMINISTIC_a425fda5bff2efbb
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Auction:
    def __init__(self):
        # Initialize an empty list to store bids
        self.bids = []
        self.auction_closed = False

    def place_bid(self, bidder_id, amount):
        """
        Place a bid in the auction.

        Args:
            bidder_id (str): The ID of the bidder.
            amount (float): The amount of the bid.

        Raises:
            ValueError: If the bid amount is not positive or if the auction is closed.
        """
        if self.auction_closed:
            raise ValueError("Cannot place a bid: The auction is closed.")

        if amount <= 0:
            raise ValueError("Bid amount must be positive.")

        self.bids.append((bidder_id, amount))

    def close_auction(self):
        """Close the auction to prevent further bidding."""
        self.auction_closed = True

    def refund_bids(self):
        """
        Simulate refunding all bids after the auction closes.

        Returns:
            dict: A dictionary containing the bidder IDs and their refunded amounts.

        Raises:
            RuntimeError: If the auction is not closed yet.
        """
        if not self.auction_closed:
            raise RuntimeError("Cannot refund bids: The auction is still open.")

        # Create a dictionary to hold the refunds
        refunds = {}
        for bidder_id, amount in self.bids:
            refunds[bidder_id] = amount  # Refund the full bid amount

        # Clear the bids after refunding
        self.bids.clear()
        return refunds


# Example usage
if __name__ == "__main__":
    auction = Auction()
    
    try:
        auction.place_bid('bidder1', 100)
        auction.place_bid('bidder2', 150)
        
        auction.close_auction()  # Close the auction
        
        refunds = auction.refund_bids()  # Refund all bids
        print("Refunds processed:", refunds)
    except (ValueError, RuntimeError) as e:
        print(f"Error: {e}")
```
