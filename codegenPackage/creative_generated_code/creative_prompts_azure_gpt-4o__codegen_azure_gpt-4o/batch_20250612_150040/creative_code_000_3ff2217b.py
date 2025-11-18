"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://great-alarm-slow.on-fleek.app
Prompt: Write a Python script to simulate the high-to-low pricing mechanism used in Fjord Foundry's Liquidity Bootstrapping Pools (LBPs) for community-driven price discovery.
Generated: DETERMINISTIC_3ff2217bf9e25654
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from datetime import datetime, timedelta

class LiquidityBootstrappingPool:
    """
    A class to simulate the high-to-low pricing mechanism in a Liquidity Bootstrapping Pool (LBP).
    """

    def __init__(self, initial_price, decay_rate, duration_minutes):
        """
        Initialize the LBP simulation.

        Args:
            initial_price (float): Starting price of the asset.
            decay_rate (float): Rate at which the price decreases (percentage per minute, e.g., 0.01 for 1%).
            duration_minutes (int): Total duration of the LBP in minutes.
        """
        if initial_price <= 0 or decay_rate <= 0 or duration_minutes <= 0:
            raise ValueError("Initial price, decay rate, and duration must be positive values.")

        self.initial_price = initial_price
        self.decay_rate = decay_rate
        self.duration = timedelta(minutes=duration_minutes)
        self.start_time = None

    def start_lbp(self):
        """
        Start the LBP simulation.
        """
        self.start_time = datetime.now()
        print(f"LBP started at {self.start_time.strftime('%Y-%m-%d %H:%M:%S')} with initial price {self.initial_price:.2f}")

    def get_current_price(self):
        """
        Get the current price based on elapsed time.

        Returns:
            float: The current price of the asset.
        """
        if self.start_time is None:
            raise RuntimeError("LBP has not started yet. Call start_lbp() to begin.")

        elapsed_time = datetime.now() - self.start_time
        if elapsed_time > self.duration:
            return 0.0  # Price is zero after the LBP duration ends.

        elapsed_minutes = elapsed_time.total_seconds() / 60
        current_price = self.initial_price * (1 - self.decay_rate) ** elapsed_minutes

        return max(current_price, 0.0)  # Ensure price is non-negative.

    def simulate_lbp(self):
        """
        Simulate the LBP pricing over time.

        This method runs until the LBP duration ends, displaying the price at each minute.
        """
        if self.start_time is None:
            raise RuntimeError("LBP has not started yet. Call start_lbp() to begin.")

        end_time = self.start_time + self.duration
        while datetime.now() < end_time:
            current_price = self.get_current_price()
            print(f"Time: {datetime.now().strftime('%H:%M:%S')}, Price: {current_price:.2f}")
            time.sleep(60)  # Wait for one minute.
        
        print("LBP duration has ended. Final price: 0.00")

# Example usage:
if __name__ == "__main__":
    try:
        # Create an LBP with initial price of 100, decay rate of 1% per minute, lasting for 30 minutes.
        lbp = LiquidityBootstrappingPool(initial_price=100.0, decay_rate=0.01, duration_minutes=30)
        
        # Start the LBP.
        lbp.start_lbp()
        
        # Simulate the LBP pricing mechanism.
        lbp.simulate_lbp()
    except Exception as e:
        print(f"Error: {e}")
```
