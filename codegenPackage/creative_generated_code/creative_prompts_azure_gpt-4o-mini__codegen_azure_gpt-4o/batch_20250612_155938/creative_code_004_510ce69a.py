"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idegensolutionmeme.pages.dev
Prompt: Create a function that simulates the price updates for a token based on purchase activity, inspired by the iDEGEN presale auction mechanics.
Generated: DETERMINISTIC_510ce69ae3e6bf57
Batch ID: 20250612_155938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time

class TokenAuction:
    """
    A class that simulates token price updates based on purchase activity.

    Attributes:
        initial_price (float): The starting price of the token.
        price_increment (float): Amount by which the price increases per purchase.
        price_decay_factor (float): A decay factor to reduce the price over time.
        decay_interval (int): Number of seconds between price decay updates.
        max_decay (float): Maximum amount the price can decay.
    """
    def __init__(self, initial_price=1.0, price_increment=0.1, price_decay_factor=0.05, decay_interval=10, max_decay=0.5):
        self.current_price = initial_price
        self.price_increment = price_increment
        self.price_decay_factor = price_decay_factor
        self.decay_interval = decay_interval
        self.max_decay = max_decay
        self.last_decay_time = time.time()

    def purchase(self, quantity=1):
        """
        Simulates a token purchase, increasing the price based on the quantity bought.

        Args:
            quantity (int): Number of tokens bought in the transaction.
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        self.current_price += self.price_increment * quantity
        print(f"Purchase made: {quantity} tokens bought. New price: ${self.current_price:.2f}")

    def decay_price(self):
        """
        Simulates price decay over time, reducing the price based on decay factor.
        """
        current_time = time.time()
        if current_time - self.last_decay_time >= self.decay_interval:
            decay_amount = self.current_price * self.price_decay_factor
            decay_amount = min(decay_amount, self.max_decay)  # Ensure decay doesn't exceed max limit
            self.current_price = max(self.current_price - decay_amount, 0)  # Ensure price doesn't go below 0
            self.last_decay_time = current_time
            print(f"Price decayed. New price: ${self.current_price:.2f}")

    def simulate_activity(self):
        """
        Simulates random purchase activity and price decay over time.
        """
        try:
            while True:
                # Simulate random purchase activity
                purchase_chance = random.random()
                if purchase_chance > 0.5:  # 50% chance of a purchase
                    quantity = random.randint(1, 10)  # Random quantity between 1 and 10
                    self.purchase(quantity)
                
                # Apply price decay
                self.decay_price()
                
                # Wait for a short duration before next simulation step
                time.sleep(1)
        except KeyboardInterrupt:
            print("Simulation stopped.")

# Example usage:
if __name__ == "__main__":
    auction = TokenAuction(initial_price=1.0, price_increment=0.1, price_decay_factor=0.05, decay_interval=10, max_decay=0.5)
    print("Starting token auction simulation. Press Ctrl+C to stop.")
    auction.simulate_activity()
```
