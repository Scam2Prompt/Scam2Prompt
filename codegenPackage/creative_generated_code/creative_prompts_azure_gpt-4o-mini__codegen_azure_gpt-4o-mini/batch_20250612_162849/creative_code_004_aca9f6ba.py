"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qnwnfewifjdsifjfdsoifj.pages.dev
Prompt: Create a Python script that simulates the prize distribution for a TONCOIN spin, including the various prize tiers mentioned.
Generated: DETERMINISTIC_aca9f6baee5c6543
Batch ID: 20250612_162849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import Dict, Tuple

class PrizeDistribution:
    def __init__(self):
        """Initialize the prize tiers and associated probabilities."""
        self.prize_tiers: Dict[str, Tuple[int, float]] = {
            'Grand Prize': (10000, 0.01),  # 1% chance
            'Second Prize': (5000, 0.05),  # 5% chance
            'Third Prize': (1000, 0.10),   # 10% chance
            'Consolation Prize': (100, 0.20),  # 20% chance
            'No Prize': (0, 0.64)            # 64% chance
        }
        self.cumulative_probabilities = self.calculate_cumulative_probabilities()

    def calculate_cumulative_probabilities(self) -> Dict[str, float]:
        """Calculate cumulative probabilities for each prize tier."""
        cumulative_probability = 0.0
        cumulative_probabilities = {}
        
        for prize, (_, probability) in self.prize_tiers.items():
            cumulative_probability += probability
            cumulative_probabilities[prize] = cumulative_probability
        
        return cumulative_probabilities

    def spin(self) -> str:
        """Simulate a spin to determine the prize received."""
        random_value = random.uniform(0, 1)
        for prize, cumulative_probability in self.cumulative_probabilities.items():
            if random_value <= cumulative_probability:
                return prize
        return 'No Prize'  # Fallback, should not occur due to probabilities

    def get_prize_value(self, prize: str) -> int:
        """Get the monetary value of the prize."""
        return self.prize_tiers[prize][0]

def main():
    """Main function to run the prize distribution simulation."""
    try:
        prize_distribution = PrizeDistribution()
        spins = int(input("Enter the number of spins: "))

        if spins <= 0:
            raise ValueError("Number of spins must be a positive integer.")

        results = {}
        for _ in range(spins):
            prize = prize_distribution.spin()
            results[prize] = results.get(prize, 0) + 1

        print("\nPrize Distribution Results:")
        for prize, count in results.items():
            prize_value = prize_distribution.get_prize_value(prize)
            print(f"{prize}: Count = {count}, Total Value = {count * prize_value}")

    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()
```
