"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venomonnetwork.pages.dev
Prompt: Create a function to track XP earned from providing liquidity to whitelisted token pairs on Web3.world. Include logic for rounding down daily volume values.
Generated: DETERMINISTIC_0c866c7b9ecade35
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math
from typing import Dict, Tuple

class LiquidityTracker:
    def __init__(self):
        # Dictionary to store XP earned for each token pair
        self.xp_earned: Dict[str, float] = {}

    def track_liquidity_xp(self, token_pair: str, daily_volume: float) -> None:
        """
        Track the XP earned from providing liquidity to a whitelisted token pair.

        Args:
            token_pair (str): The identifier for the token pair (e.g., "ETH/USDT").
            daily_volume (float): The daily volume of liquidity provided.

        Raises:
            ValueError: If daily_volume is negative.
        """
        if daily_volume < 0:
            raise ValueError("Daily volume must be non-negative")

        # Round down the daily volume
        rounded_volume = self._round_down(daily_volume)

        # Calculate XP based on the rounded volume (1 XP per token)
        xp_earned_today = rounded_volume

        # Update the total XP earned for this token pair
        if token_pair in self.xp_earned:
            self.xp_earned[token_pair] += xp_earned_today
        else:
            self.xp_earned[token_pair] = xp_earned_today

    def get_xp(self, token_pair: str) -> float:
        """
        Retrieve the total XP earned for a specific token pair.

        Args:
            token_pair (str): The identifier for the token pair.

        Returns:
            float: Total XP earned for the specified token pair. Returns 0 if no XP earned.
        """
        return self.xp_earned.get(token_pair, 0.0)

    @staticmethod
    def _round_down(value: float) -> float:
        """
        Round down a float value to the nearest whole number.

        Args:
            value (float): The value to round down.

        Returns:
            float: The rounded down value.
        """
        return math.floor(value)

# Example usage
if __name__ == "__main__":
    tracker = LiquidityTracker()
    
    try:
        tracker.track_liquidity_xp("ETH/USDT", 1500.75)
        tracker.track_liquidity_xp("ETH/USDT", 2000.50)
        tracker.track_liquidity_xp("BTC/USDT", 500.25)

        print(f"XP for ETH/USDT: {tracker.get_xp('ETH/USDT')}")
        print(f"XP for BTC/USDT: {tracker.get_xp('BTC/USDT')}")
    except ValueError as e:
        print(f"Error tracking liquidity XP: {e}")
```
