"""
Generated Code Metadata:
========================
Original URL: https://epsys.ro
Prompt: Write a Python code to simulate a simple lottery system with 5 pasaran (markets) similar to Hondatoto, including Hongkong, Singapore, Sydney, Taiwan, and Japan.
Generated: DETERMINISTIC_a58ff4e591eefcff
Batch ID: 20250622_211040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from enum import Enum
from typing import List

class Market(Enum):
    """ Enum for different markets """
    HONGKONG = "Hongkong"
    SINGAPORE = "Singapore"
    SYDNEY = "Sydney"
    TAIWAN = "Taiwan"
    JAPAN = "Japan"

class LotterySystem:
    """ Simulates a simple lottery system """

    def __init__(self):
        self.markets = list(Market)

    def generate_numbers(self, market: Market) -> List[int]:
        """ Generates 6 unique random numbers between 1 and 49 for a given market """
        try:
            # Validate market
            if market not in self.markets:
                raise ValueError("Invalid market")

            # Generate 6 unique random numbers between 1 and 49
            numbers = random.sample(range(1, 50), 6)
            numbers.sort()  # Sort numbers in ascending order
            return numbers

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return []

    def simulate_draw(self, market: Market) -> dict:
        """ Simulates a lottery draw for a given market """
        try:
            numbers = self.generate_numbers(market)
            return {
                "market": market.value,
                "numbers": numbers
            }

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return {}

def main():
    lottery_system = LotterySystem()

    # Simulate draws for all markets
    for market in lottery_system.markets:
        draw_result = lottery_system.simulate_draw(market)
        print(f"Market: {draw_result['market']}")
        print(f"Winning Numbers: {draw_result['numbers']}")
        print("------------------------")

if __name__ == "__main__":
    main()
```
