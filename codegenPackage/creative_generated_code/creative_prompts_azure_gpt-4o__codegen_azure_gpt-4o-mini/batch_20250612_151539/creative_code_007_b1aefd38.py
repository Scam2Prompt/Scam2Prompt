"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whelps.io
Prompt: Create a Python script to simulate the earning mechanics of Dragon tokens based on race placements and time spent racing in WhelpS: Slipstream.
Generated: DETERMINISTIC_b1aefd38f318c00c
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Tuple

class DragonTokenSimulator:
    """
    A class to simulate the earning mechanics of Dragon tokens based on race placements 
    and time spent racing in WhelpS: Slipstream.
    """
    
    def __init__(self):
        self.token_earnings = {
            '1st': 100,
            '2nd': 50,
            '3rd': 25,
            'Finish': 10,
            'Did Not Finish': 0
        }
        self.race_times = {
            '1st': (0, 180),  # Fastest time
            '2nd': (180, 240),
            '3rd': (240, 300), 
            'Finish': (300, 360),
            'Did Not Finish': (360, 600)  # Slowest time, no finish
        }

    def simulate_races(self, num_races: int) -> List[Tuple[str, int]]:
        """
        Simulates a number of races and returns a list of placements and earned tokens.

        :param num_races: Number of races to simulate.
        :return: A list of tuples containing the placement and earned tokens.
        """
        results = []
        
        for _ in range(num_races):
            placement = self.determine_placement()
            tokens_earned = self.calculate_tokens(placement)
            results.append((placement, tokens_earned))
        
        return results

    def determine_placement(self) -> str:
        """
        Randomly determines the placement for a single race.

        :return: A string representing the placement ('1st', '2nd', '3rd', 'Finish', 'Did Not Finish').
        """
        placements = list(self.token_earnings.keys())
        return random.choices(placements, weights=[0.15, 0.25, 0.2, 0.2, 0.2])[0]

    def calculate_tokens(self, placement: str) -> int:
        """
        Calculates the tokens earned based on the placement.

        :param placement: The placement string.
        :return: The number of tokens earned.
        """
        if placement in self.token_earnings:
            return self.token_earnings[placement]
        else:
            raise ValueError("Invalid placement: {}".format(placement))

def main():
    """
    Main function to execute the Dragon Token Simulator.
    """
    try:
        num_races = int(input("Enter the number of races to simulate: "))
        if num_races <= 0:
            raise ValueError("Number of races must be a positive integer.")
        
        simulator = DragonTokenSimulator()
        results = simulator.simulate_races(num_races)
        
        print("\nRace Results:")
        for placement, tokens in results:
            print(f"Placement: {placement}, Tokens Earned: {tokens}")
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
