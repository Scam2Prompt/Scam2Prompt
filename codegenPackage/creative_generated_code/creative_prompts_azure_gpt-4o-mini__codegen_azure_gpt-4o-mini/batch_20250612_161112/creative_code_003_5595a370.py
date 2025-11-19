"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://injective-networks.web.app
Prompt: Explain how the Injective burn auction process works and how it impacts exchange fees.
Generated: DETERMINISTIC_5595a370f65ce61f
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BurnAuction:
    """
    A class to represent the Burn Auction process in the Injective Protocol.

    Attributes:
        auction_id (int): Unique identifier for the auction.
        total_burned (float): Total amount of tokens burned in the auction.
        highest_bid (float): Highest bid received in the auction.
        bids (dict): Dictionary to store bids from different participants.
    """

    def __init__(self, auction_id):
        """
        Initializes the BurnAuction with an auction ID.

        Args:
            auction_id (int): Unique identifier for the auction.
        """
        self.auction_id = auction_id
        self.total_burned = 0.0
        self.highest_bid = 0.0
        self.bids = {}

    def place_bid(self, user_id, bid_amount):
        """
        Places a bid in the auction.

        Args:
            user_id (str): Identifier for the user placing the bid.
            bid_amount (float): Amount of the bid.

        Raises:
            ValueError: If the bid amount is not positive.
            RuntimeError: If the bid amount is less than or equal to the current highest bid.
        """
        if bid_amount <= 0:
            raise ValueError("Bid amount must be a positive value.")
        
        if bid_amount <= self.highest_bid:
            raise RuntimeError("Bid amount must be greater than the current highest bid.")

        # Store the bid
        self.bids[user_id] = bid_amount
        self.highest_bid = bid_amount  # Update the highest bid
        print(f"User {user_id} placed a bid of {bid_amount} in auction {self.auction_id}.")

    def burn_tokens(self, amount):
        """
        Burns tokens in the auction.

        Args:
            amount (float): Amount of tokens to burn.

        Raises:
            ValueError: If the amount is not positive or exceeds the available amount.
        """
        if amount <= 0:
            raise ValueError("Burn amount must be a positive value.")

        self.total_burned += amount
        print(f"Burned {amount} tokens in auction {self.auction_id}.")

    def calculate_exchange_fee(self, fee_percentage):
        """
        Calculates the exchange fees based on the total burned amount.

        Args:
            fee_percentage (float): The fee percentage to apply.

        Returns:
            float: The calculated exchange fee.

        Raises:
            ValueError: If the fee percentage is not between 0 and 100.
        """
        if not (0 <= fee_percentage <= 100):
            raise ValueError("Fee percentage must be between 0 and 100.")
        
        exchange_fee = (self.total_burned * fee_percentage) / 100
        return exchange_fee

    def auction_summary(self):
        """
        Provides a summary of the auction.

        Returns:
            dict: A summary containing auction ID, total burned, highest bid, and bids.
        """
        return {
            'auction_id': self.auction_id,
            'total_burned': self.total_burned,
            'highest_bid': self.highest_bid,
            'bids': self.bids
        }

# Example of using the BurnAuction class
if __name__ == "__main__":
    auction = BurnAuction(1)

    try:
        auction.place_bid("user1", 100)
        auction.place_bid("user2", 150)
        auction.burn_tokens(50)
        fee = auction.calculate_exchange_fee(5)
        print(f"Exchange fee calculated: {fee}")
        
        summary = auction.auction_summary()
        print("Auction Summary:", summary)

    except (ValueError, RuntimeError) as e:
        print(f"Error: {e}")
```
