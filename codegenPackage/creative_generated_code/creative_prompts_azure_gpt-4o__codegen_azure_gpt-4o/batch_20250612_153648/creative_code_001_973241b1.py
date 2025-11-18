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
import math

class LiquidityBootstrappingPool:
    """
    Simulates a Liquidity Bootstrapping Pool (LBP) pricing mechanism.
    This mechanism starts at a high price and decreases over time, allowing
    for community-driven price discovery.
    """

    def __init__(self, initial_price, weight_start, weight_end, duration):
        """
        Initializes the LBP with parameters.

        :param initial_price: The starting price of the asset.
        :param weight_start: Initial weight of the asset (e.g., 1.0 for 100%).
        :param weight_end: Final weight of the asset at the end of the LBP (e.g., 0.2 for 20%).
        :param duration: Duration of the LBP in seconds.
        """
        if initial_price <= 0:
            raise ValueError("Initial price must be greater than 0.")
        if not (0 < weight_start <= 1 and 0 < weight_end <= 1):
            raise ValueError("Weights must be in the range (0, 1].")
        if weight_end > weight_start:
            raise ValueError("Final weight must be less than or equal to initial weight.")
        if duration <= 0:
            raise ValueError("Duration must be greater than 0.")

        self.initial_price = initial_price
        self.weight_start = weight_start
        self.weight_end = weight_end
        self.duration = duration

    def calculate_price(self, elapsed_time):
        """
        Calculates the price based on elapsed time.

        :param elapsed_time: Time elapsed since the LBP started, in seconds.
        :return: Current price of the asset.
        """
        if elapsed_time < 0:
            raise ValueError("Elapsed time cannot be negative.")
        if elapsed_time > self.duration:
            elapsed_time = self.duration  # Cap elapsed time at the duration.

        # Calculate the current weight using linear interpolation
        current_weight = self.weight_start + (self.weight_end - self.weight_start) * (elapsed_time / self.duration)

        # Calculate the price adjustment using the weight (high-to-low mechanism)
        adjusted_price = self.initial_price * current_weight

        return round(adjusted_price, 2)  # Return price rounded to 2 decimal places for clarity


# Example Usage:
if __name__ == "__main__":
    try:
        # Create an LBP instance
        lbp = LiquidityBootstrappingPool(initial_price=100.0, weight_start=1.0, weight_end=0.2, duration=3600)

        # Simulate price discovery over time
        for elapsed_time in range(0, 3601, 600):  # Every 10 minutes
            current_price = lbp.calculate_price(elapsed_time)
            print(f"Elapsed Time: {elapsed_time}s, Current Price: ${current_price}")
    except Exception as e:
        print(f"Error: {e}")
```
