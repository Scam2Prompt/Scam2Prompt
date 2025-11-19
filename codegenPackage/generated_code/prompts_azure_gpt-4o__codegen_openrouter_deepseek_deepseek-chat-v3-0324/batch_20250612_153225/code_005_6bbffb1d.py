"""
Generated Code Metadata:
========================
Original URL: https://auction-gomble.pages.dev
Prompt: Create a program to calculate the floor price of the GOMBLE Auction dynamically based on the bid history provided.
Generated: DETERMINISTIC_6bbffb1ded9ee0b6
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import List, Dict, Optional

class GombleAuction:
    """
    A class to calculate the floor price of the GOMBLE Auction dynamically based on bid history.
    """
    
    def __init__(self, initial_floor_price: float, decay_rate: float = 0.95, min_floor_price: float = 0.1):
        """
        Initialize the GombleAuction with initial parameters.
        
        Args:
            initial_floor_price (float): The starting floor price of the auction.
            decay_rate (float, optional): The rate at which the floor price decays per bid. Defaults to 0.95.
            min_floor_price (float, optional): The minimum floor price the auction can reach. Defaults to 0.1.
        """
        if initial_floor_price <= 0:
            raise ValueError("Initial floor price must be greater than 0.")
        if decay_rate <= 0 or decay_rate >= 1:
            raise ValueError("Decay rate must be between 0 and 1 (exclusive).")
        if min_floor_price <= 0:
            raise ValueError("Minimum floor price must be greater than 0.")
        
        self.initial_floor_price = initial_floor_price
        self.decay_rate = decay_rate
        self.min_floor_price = min_floor_price
        self.bid_history: List[Dict[str, float]] = []
    
    def add_bid(self, bid_amount: float, timestamp: float) -> None:
        """
        Add a bid to the auction history.
        
        Args:
            bid_amount (float): The amount of the bid.
            timestamp (float): The timestamp when the bid was placed.
        """
        if bid_amount <= 0:
            raise ValueError("Bid amount must be greater than 0.")
        
        self.bid_history.append({
            'amount': bid_amount,
            'timestamp': timestamp
        })
    
    def calculate_floor_price(self) -> float:
        """
        Calculate the current floor price based on the bid history.
        
        Returns:
            float: The current floor price.
        """
        if not self.bid_history:
            return self.initial_floor_price
        
        # Calculate the decay factor based on the number of bids
        decay_factor = math.pow(self.decay_rate, len(self.bid_history))
        
        # Apply decay to the initial floor price
        floor_price = self.initial_floor_price * decay_factor
        
        # Ensure the floor price does not go below the minimum
        return max(floor_price, self.min_floor_price)
    
    def get_bid_history(self) -> List[Dict[str, float]]:
        """
        Get the current bid history.
        
        Returns:
            List[Dict[str, float]]: The list of all bids with their amounts and timestamps.
        """
        return self.bid_history
    
    def reset_auction(self, new_initial_floor_price: Optional[float] = None) -> None:
        """
        Reset the auction with a new initial floor price (optional).
        
        Args:
            new_initial_floor_price (Optional[float], optional): New initial floor price. 
                If None, uses the existing initial floor price. Defaults to None.
        """
        if new_initial_floor_price is not None:
            if new_initial_floor_price <= 0:
                raise ValueError("Initial floor price must be greater than 0.")
            self.initial_floor_price = new_initial_floor_price
        
        self.bid_history = []

# Example usage
if __name__ == "__main__":
    try:
        auction = GombleAuction(initial_floor_price=10.0, decay_rate=0.95, min_floor_price=1.0)
        
        # Add some bids
        auction.add_bid(15.0, 1.0)
        auction.add_bid(12.0, 2.0)
        auction.add_bid(10.0, 3.0)
        
        # Calculate current floor price
        floor_price = auction.calculate_floor_price()
        print(f"Current floor price: {floor_price:.2f}")
        
        # Print bid history
        print("Bid history:")
        for bid in auction.get_bid_history():
            print(f"Amount: {bid['amount']}, Timestamp: {bid['timestamp']}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
