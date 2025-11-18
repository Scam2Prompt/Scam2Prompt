"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lanimal443331.github.io
Prompt: Generate code to simulate the high-to-low pricing mechanism used in Fjord Foundry's LBPs for community-driven price discovery.
Generated: DETERMINISTIC_973241b1f0c69876
Batch ID: 20250612_153648
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
from typing import List, Tuple

class LBP:
    """
    This class simulates a Liquidity Bootstrapping Pool (LBP) for community-driven price discovery.
    It allows for the management of token pricing from high to low over a specified duration.
    """

    def __init__(self, start_price: float, end_price: float, duration: int):
        """
        Initializes the LBP with the starting price, ending price, and duration for the price change.

        :param start_price: Initial price of the token.
        :param end_price: Final price of the token after the duration.
        :param duration: Total time (in seconds) over which the price will decrease.
        """
        if start_price <= end_price:
            raise ValueError("Start price must be greater than end price.")
        if duration <= 0:
            raise ValueError("Duration must be a positive integer.")

        self.start_price = start_price
        self.end_price = end_price
        self.duration = duration
        self.current_price = start_price
        self.start_time = time.time()

    def calculate_price(self) -> float:
        """
        Calculates the current price based on elapsed time since the start.

        :return: Current price of the token.
        """
        elapsed_time = time.time() - self.start_time
        if elapsed_time >= self.duration:
            return self.end_price
        
        # Linear price decay calculation
        price_decay = (self.start_price - self.end_price) * (elapsed_time / self.duration)
        self.current_price = self.start_price - price_decay
        return round(self.current_price, 2)

    def simulate_price_changes(self, intervals: int) -> List[Tuple[int, float]]:
        """
        Simulates the price changes at specified intervals.

        :param intervals: The number of intervals at which to capture the price.
        :return: A list of tuples containing (time elapsed, current price).
        """
        if intervals <= 0:
            raise ValueError("Intervals must be a positive integer.")
        
        price_history = []
        for i in range(intervals):
            time.sleep(self.duration / intervals)  # Wait for the time interval
            current_price = self.calculate_price()
            price_history.append((i * (self.duration / intervals), current_price))
            print(f"Time: {i * (self.duration / intervals)}s, Price: {current_price}")

        return price_history

# Example usage
if __name__ == "__main__":
    try:
        lbp = LBP(start_price=10.0, end_price=1.0, duration=60)  # 10 to 1 over 60 seconds
        lbp.simulate_price_changes(intervals=10)  # Capture price 10 times
    except ValueError as e:
        print(f"Error: {e}")
```
