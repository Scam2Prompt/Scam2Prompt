"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.espglobal.co
Prompt: Provide a code example for integrating ESP Global's auction optimization techniques into a real estate platform, ensuring agents can manage auctions effectively.
Generated: DETERMINISTIC_1054c41b6bd2705a
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Auction:
    """
    Represents an auction for a real estate property.
    """

    def __init__(self, property_id, starting_price, start_time, end_time):
        """
        Initialize auction details.

        :param property_id: Unique ID of the property
        :param starting_price: Starting price for the auction
        :param start_time: Start time of the auction (datetime object)
        :param end_time: End time of the auction (datetime object)
        """
        self.property_id = property_id
        self.starting_price = starting_price
        self.start_time = start_time
        self.end_time = end_time
        self.bids = []
        self.is_active = False

    def start_auction(self):
        """
        Activates the auction if the start time is valid.
        """
        if datetime.datetime.now() >= self.start_time:
            self.is_active = True
            logging.info(f"Auction for property ID {self.property_id} has started.")
        else:
            logging.error("Cannot start auction before the scheduled start time.")

    def place_bid(self, bidder_name, bid_amount):
        """
        Allows a bidder to place a bid if the auction is active.

        :param bidder_name: Name of the bidder
        :param bid_amount: Amount of the bid
        :raises ValueError: If the bid amount is less than the starting price
        """
        if not self.is_active:
            logging.error("Attempt to place bid on an inactive auction.")
            raise RuntimeError("Auction is not active.")

        if bid_amount < self.starting_price:
            logging.error("Bid amount is lower than the starting price.")
            raise ValueError("Bid amount must be at least the starting price.")

        self.bids.append({"bidder_name": bidder_name, "bid_amount": bid_amount})
        logging.info(f"Bid placed by {bidder_name} for amount ${bid_amount}.")

    def end_auction(self):
        """
        Ends the auction and selects the winner.
        """
        if not self.is_active:
            logging.error("Attempt to end an inactive auction.")
            raise RuntimeError("Auction is not active.")

        self.is_active = False
        if self.bids:
            winning_bid = max(self.bids, key=lambda x: x["bid_amount"])
            logging.info(
                f"Auction for property ID {self.property_id} has ended. "
                f"Winner: {winning_bid['bidder_name']} with bid amount ${winning_bid['bid_amount']}."
            )
        else:
            logging.info(f"Auction for property ID {self.property_id} ended with no bids.")

class AgentPortal:
    """
    Represents a portal for real estate agents to manage auctions.
    """

    def __init__(self):
        # A dictionary to store auctions with property_id as key
        self.auctions = {}

    def create_auction(self, property_id, starting_price, start_time, end_time):
        """
        Allows agents to create a new auction.

        :param property_id: ID of the property
        :param starting_price: Starting price for the auction
        :param start_time: Start time of the auction
        :param end_time: End time of the auction
        :raises ValueError: If the end time is earlier than the start time
        """
        if end_time <= start_time:
            logging.error("End time cannot be earlier than the start time.")
            raise ValueError("End time must be later than start time.")

        auction = Auction(property_id, starting_price, start_time, end_time)
        self.auctions[property_id] = auction
        logging.info(f"Auction created for property ID {property_id}.")

    def start_auction(self, property_id):
        """
        Starts an auction for a given property.

        :param property_id: ID of the property
        """
        auction = self.auctions.get(property_id)
        if not auction:
            logging.error(f"No auction found for property ID {property_id}.")
            raise KeyError(f"No auction found for property ID {property_id}.")

        auction.start_auction()

    def end_auction(self, property_id):
        """
        Ends an auction for a given property.

        :param property_id: ID of the property
        """
        auction = self.auctions.get(property_id)
        if not auction:
            logging.error(f"No auction found for property ID {property_id}.")
            raise KeyError(f"No auction found for property ID {property_id}.")

        auction.end_auction()

    def place_bid(self, property_id, bidder_name, bid_amount):
        """
        Places a bid on a specific auction.

        :param property_id: ID of the property
        :param bidder_name: Name of the bidder
        :param bid_amount: Amount of the bid
        """
        auction = self.auctions.get(property_id)
        if not auction:
            logging.error(f"No auction found for property ID {property_id}.")
            raise KeyError(f"No auction found for property ID {property_id}.")

        auction.place_bid(bidder_name, bid_amount)


# Example Usage
if __name__ == "__main__":
    agent_portal = AgentPortal()

    # Create an auction
    try:
        agent_portal.create_auction(
            property_id="12345",
            starting_price=100000,
            start_time=datetime.datetime(2023, 10, 1, 9, 0),
            end_time=datetime.datetime(2023, 10, 1, 17, 0),
        )
    except ValueError as e:
        logging.error(f"Error while creating auction: {e}")

    # Start the auction
    try:
        agent_portal.start_auction(property_id="12345")
    except KeyError as e:
        logging.error(f"Error while starting auction: {e}")

    # Place bids
    try:
        agent_portal.place_bid(property_id="12345", bidder_name="Alice", bid_amount=120000)
        agent_portal.place_bid(property_id="12345", bidder_name="Bob", bid_amount=125000)
        agent_portal.place_bid(property_id="12345", bidder_name="Charlie", bid_amount=130000)
    except (KeyError, ValueError, RuntimeError) as e:
        logging.error(f"Error while placing bid: {e}")

    # End the auction
    try:
        agent_portal.end_auction(property_id="12345")
    except KeyError as e:
        logging.error(f"Error while ending auction: {e}")
```
