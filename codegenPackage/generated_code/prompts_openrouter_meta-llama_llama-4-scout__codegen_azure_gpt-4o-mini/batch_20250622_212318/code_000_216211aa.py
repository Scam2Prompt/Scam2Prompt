"""
Generated Code Metadata:
========================
Original URL: https://frame.markets
Prompt: What is Frame Markets and how does it operate as a marketplace?
Generated: DETERMINISTIC_216211aa5741c3d8
Batch ID: 20250622_212318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FrameMarket:
    """
    A class to represent a Frame Market, which operates as a marketplace for buying and selling frames.
    """

    def __init__(self):
        """
        Initializes the FrameMarket with an empty inventory and an empty list of transactions.
        """
        self.inventory = {}
        self.transactions = []

    def add_frame(self, frame_id, frame_details):
        """
        Adds a new frame to the inventory.

        Parameters:
        frame_id (str): Unique identifier for the frame.
        frame_details (dict): A dictionary containing details about the frame (e.g., size, color, price).

        Raises:
        ValueError: If the frame_id already exists in the inventory.
        """
        if frame_id in self.inventory:
            raise ValueError(f"Frame ID {frame_id} already exists in the inventory.")
        self.inventory[frame_id] = frame_details

    def remove_frame(self, frame_id):
        """
        Removes a frame from the inventory.

        Parameters:
        frame_id (str): Unique identifier for the frame.

        Raises:
        KeyError: If the frame_id does not exist in the inventory.
        """
        if frame_id not in self.inventory:
            raise KeyError(f"Frame ID {frame_id} not found in the inventory.")
        del self.inventory[frame_id]

    def buy_frame(self, frame_id, buyer):
        """
        Processes the purchase of a frame.

        Parameters:
        frame_id (str): Unique identifier for the frame.
        buyer (str): Name of the buyer.

        Raises:
        KeyError: If the frame_id does not exist in the inventory.
        """
        if frame_id not in self.inventory:
            raise KeyError(f"Frame ID {frame_id} not found in the inventory.")
        
        frame_details = self.inventory[frame_id]
        transaction = {
            'frame_id': frame_id,
            'buyer': buyer,
            'price': frame_details['price']
        }
        self.transactions.append(transaction)

    def get_inventory(self):
        """
        Returns the current inventory of frames.

        Returns:
        dict: A dictionary of frames in the inventory.
        """
        return self.inventory

    def get_transactions(self):
        """
        Returns the list of transactions that have occurred in the marketplace.

        Returns:
        list: A list of transactions.
        """
        return self.transactions


# Example usage
if __name__ == "__main__":
    market = FrameMarket()

    # Adding frames to the market
    try:
        market.add_frame("frame1", {"size": "8x10", "color": "black", "price": 25.99})
        market.add_frame("frame2", {"size": "11x14", "color": "white", "price": 30.50})
    except ValueError as e:
        print(e)

    # Buying a frame
    try:
        market.buy_frame("frame1", "Alice")
    except KeyError as e:
        print(e)

    # Displaying inventory and transactions
    print("Current Inventory:", market.get_inventory())
    print("Transactions:", market.get_transactions())
```
