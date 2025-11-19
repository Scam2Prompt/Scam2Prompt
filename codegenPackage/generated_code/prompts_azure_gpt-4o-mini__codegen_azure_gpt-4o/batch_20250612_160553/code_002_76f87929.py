"""
Generated Code Metadata:
========================
Original URL: https://gcbt.com
Prompt: What is the best way to implement a bidding system in Python that complies with the 7-day binding offer rule for domain purchases like gcbt.com?
Generated: DETERMINISTIC_76f879290bb26916
Batch ID: 20250612_160553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class Bid:
    """
    Represents a single bid in the bidding system.
    """
    def __init__(self, bidder_name, bid_amount):
        self.bidder_name = bidder_name
        self.bid_amount = bid_amount
        self.timestamp = datetime.datetime.now()  # Record the time of the bid

    def __str__(self):
        return f"Bidder: {self.bidder_name}, Amount: ${self.bid_amount}, Time: {self.timestamp}"


class BiddingSystem:
    """
    A bidding system for domain purchases that enforces a 7-day binding offer rule.
    """
    def __init__(self, domain_name):
        self.domain_name = domain_name
        self.bids = []  # List to store all bids
        self.start_time = datetime.datetime.now()  # Start time of the bidding system
        self.end_time = self.start_time + datetime.timedelta(days=7)  # 7-day binding offer period
        self.highest_bid = None  # Track the highest bid

    def place_bid(self, bidder_name, bid_amount):
        """
        Places a bid in the system.
        :param bidder_name: Name of the bidder
        :param bid_amount: Amount of the bid
        :return: None
        """
        if datetime.datetime.now() > self.end_time:
            raise Exception("Bidding period has ended. No more bids can be placed.")

        if self.highest_bid and bid_amount <= self.highest_bid.bid_amount:
            raise ValueError("Bid amount must be higher than the current highest bid.")

        new_bid = Bid(bidder_name, bid_amount)
        self.bids.append(new_bid)
        self.highest_bid = new_bid  # Update the highest bid
        print(f"Bid placed successfully: {new_bid}")

    def get_highest_bid(self):
        """
        Returns the highest bid in the system.
        :return: Highest bid object or None if no bids exist
        """
        return self.highest_bid

    def is_bidding_period_active(self):
        """
        Checks if the bidding period is still active.
        :return: True if active, False otherwise
        """
        return datetime.datetime.now() <= self.end_time

    def get_all_bids(self):
        """
        Returns all bids placed in the system.
        :return: List of Bid objects
        """
        return self.bids

    def __str__(self):
        """
        Returns a string representation of the bidding system.
        """
        status = "Active" if self.is_bidding_period_active() else "Closed"
        return f"Domain: {self.domain_name}, Status: {status}, Highest Bid: {self.highest_bid}"


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the bidding system for a domain
        bidding_system = BiddingSystem("gcbt.com")

        # Place bids
        bidding_system.place_bid("Alice", 500)
        bidding_system.place_bid("Bob", 600)
        bidding_system.place_bid("Charlie", 700)

        # Display the highest bid
        print("Highest Bid:", bidding_system.get_highest_bid())

        # Display all bids
        print("All Bids:")
        for bid in bidding_system.get_all_bids():
            print(bid)

        # Check if the bidding period is active
        print("Is bidding period active?", bidding_system.is_bidding_period_active())

    except Exception as e:
        print(f"Error: {e}")
```
