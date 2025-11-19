"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idegensolutionmeme.pages.dev
Prompt: How can I implement a dynamic pricing model for a presale auction similar to iDEGEN's, which adjusts prices based on purchase activity?
Generated: DETERMINISTIC_306fdc8e1b120a22
Batch ID: 20250612_155938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DynamicPricingAuction:
    def __init__(self, base_price, price_increment, decrement_rate, max_price, min_price):
        """
        Initialize the dynamic pricing model for the auction.

        :param base_price: Initial price for the auction.
        :param price_increment: Amount by which the price increases after each purchase.
        :param decrement_rate: Rate at which the price decreases over time (per second).
        :param max_price: Maximum allowable price.
        :param min_price: Minimum allowable price.
        """
        self.current_price = base_price
        self.base_price = base_price
        self.price_increment = price_increment
        self.decrement_rate = decrement_rate
        self.max_price = max_price
        self.min_price = min_price
        self.last_activity_time = time.time()

    def purchase(self):
        """
        Simulates a purchase and adjusts the price dynamically.
        Price is increased after purchase, but capped at max_price.
        """
        self.adjust_price_for_time_decay()
        self.current_price += self.price_increment
        if self.current_price > self.max_price:
            self.current_price = self.max_price

        self.last_activity_time = time.time()
        logging.info(f"Purchase made. New price: ${self.current_price:.2f}")

    def adjust_price_for_time_decay(self):
        """
        Adjusts the price based on time decay since the last purchase.
        Price is decreased over time, but capped at min_price.
        """
        time_since_last_activity = time.time() - self.last_activity_time
        decay_amount = self.decrement_rate * time_since_last_activity
        self.current_price -= decay_amount
        if self.current_price < self.min_price:
            self.current_price = self.min_price
        logging.info(f"Price adjusted for time decay. Current price: ${self.current_price:.2f}")

    def get_current_price(self):
        """
        Returns the current price, adjusting for time decay.
        """
        self.adjust_price_for_time_decay()
        return self.current_price

# Example usage
if __name__ == "__main__":
    # Configure auction parameters
    BASE_PRICE = 10.0
    PRICE_INCREMENT = 2.0
    DECREMENT_RATE = 0.05  # Price decreases by $0.05 every second
    MAX_PRICE = 50.0
    MIN_PRICE = 5.0

    # Start the auction
    auction = DynamicPricingAuction(BASE_PRICE, PRICE_INCREMENT, DECREMENT_RATE, MAX_PRICE, MIN_PRICE)

    # Simulate purchase activity and price decay
    logging.info("Starting auction...")

    # Simulate a purchase
    auction.purchase()
    time.sleep(3)  # Simulate 3 seconds of inactivity

    # Check current price
    current_price = auction.get_current_price()
    logging.info(f"Current price after inactivity: ${current_price:.2f}")

    # Simulate another purchase
    auction.purchase()
    time.sleep(5)  # Simulate 5 seconds of inactivity

    # Check final price
    final_price = auction.get_current_price()
    logging.info(f"Final price after inactivity: ${final_price:.2f}")
```
