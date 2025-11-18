"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amamam-ble.pages.dev
Prompt: Create a Python program that simulates the auction system for selling Hamster Kombat vouchers, including functionality for setting minimum bid prices and tracking successful sales.
Generated: DETERMINISTIC_1803ff216f5f8e51
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from typing import List, Optional

class Voucher:
    """Class representing a Hamster Kombat voucher."""
    
    def __init__(self, description: str, min_bid: float):
        self.id = uuid.uuid4()  # Unique identifier for each voucher
        self.description = description
        self.min_bid = min_bid  # Minimum bid price for the voucher
        self.current_bid: Optional[float] = None  # Current highest bid
        self.highest_bidder: Optional[str] = None  # Highest bidder's name
        self.is_sold = False  # Status of the voucher

    def place_bid(self, bidder_name: str, bid_amount: float) -> bool:
        """
        Place a bid on the voucher.
        
        :param bidder_name: Name of the bidder
        :param bid_amount: Amount of the bid
        :return: True if the bid is successful, False otherwise
        """
        if self.is_sold:
            print("Error: This voucher has already been sold.")
            return False
        if bid_amount < self.min_bid:
            print(f"Error: Bid must be at least {self.min_bid}.")
            return False
        if self.current_bid is not None and bid_amount <= self.current_bid:
            print(f"Error: Bid must be higher than the current bid of {self.current_bid}.")
            return False
        
        self.current_bid = bid_amount
        self.highest_bidder = bidder_name
        print(f"Bid successful! Current highest bid is now {self.current_bid} by {self.highest_bidder}.")
        return True

    def finalize_sale(self) -> Optional[str]:
        """
        Finalize the sale of the voucher if there's a valid bid.
        
        :return: Confirmation message or None if no sale occurred
        """
        if self.current_bid is not None:
            self.is_sold = True
            confirmation_message = (f"Voucher {self.id} sold to {self.highest_bidder} "
                                    f"for {self.current_bid}.")
            print(confirmation_message)
            return confirmation_message
        else:
            print("Error: No valid bids have been placed.")
            return None


class Auction:
    """Class representing the auction system."""
    
    def __init__(self):
        self.vouchers: List[Voucher] = []  # List to store vouchers

    def add_voucher(self, description: str, min_bid: float) -> Voucher:
        """
        Add a new voucher to the auction.
        
        :param description: Description of the voucher
        :param min_bid: Minimum bid price for the voucher
        :return: The created Voucher object
        """
        voucher = Voucher(description, min_bid)
        self.vouchers.append(voucher)
        print(f"Added voucher: {voucher.id} with minimum bid {min_bid}.")
        return voucher

    def get_voucher(self, voucher_id: str) -> Optional[Voucher]:
        """
        Retrieve a voucher by its ID.
        
        :param voucher_id: ID of the voucher to retrieve
        :return: Voucher object if found, None otherwise
        """
        for voucher in self.vouchers:
            if str(voucher.id) == voucher_id:
                return voucher
        print("Error: Voucher not found.")
        return None

    def list_vouchers(self) -> None:
        """List all vouchers in the auction."""
        if not self.vouchers:
            print("No vouchers available.")
            return
        for voucher in self.vouchers:
            status = "Sold" if voucher.is_sold else "Available"
            print(f"Voucher ID: {voucher.id}, Description: {voucher.description}, "
                  f"Minimum Bid: {voucher.min_bid}, Current Bid: {voucher.current_bid}, "
                  f"Status: {status}")


# Example usage
if __name__ == "__main__":
    auction = Auction()
    
    # Adding vouchers to the auction
    voucher1 = auction.add_voucher("Hamster Kombat Deluxe Voucher", 50.00)
    voucher2 = auction.add_voucher("Hamster Kombat Starter Pack", 20.00)
    
    # Listing vouchers
    auction.list_vouchers()
    
    # Placing bids
    voucher1.place_bid("Alice", 60.00)
    voucher1.place_bid("Bob", 55.00)  # Should fail, not higher than current bid
    voucher1.place_bid("Charlie", 70.00)

    # Finalizing sale
    voucher1.finalize_sale()
    
    auction.list_vouchers()
```
