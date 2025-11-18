"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.uhcstepup.com
Prompt: Write code to simulate the "wild scatter" feature in a slot game, as described in Slot Thailand on Slot138, including random multipliers and bonus triggers.
Generated: DETERMINISTIC_fc7f293959717580
Batch ID: 20250612_145319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class WildScatterSlot:
    def __init__(self, num_reels=5, num_symbols=10, scatter_symbol='W', wild_symbol='S'):
        """
        Initialize the WildScatterSlot game.
        
        :param num_reels: Number of reels in the slot machine.
        :param num_symbols: Number of different symbols on the reels.
        :param scatter_symbol: Symbol representing the scatter in the game.
        :param wild_symbol: Symbol representing the wild in the game.
        """
        self.num_reels = num_reels
        self.num_symbols = num_symbols
        self.scatter_symbol = scatter_symbol
        self.wild_symbol = wild_symbol
        self.reels = self._initialize_reels()

    def _initialize_reels(self):
        """
        Initialize the reels with random symbols.
        
        :return: A list of lists representing the reels.
        """
        return [[random.randint(1, self.num_symbols) for _ in range(3)] for _ in range(self.num_reels)]

    def spin(self):
        """
        Spin the reels and check for wild scatter and multipliers.
        
        :return: Result of the spin with potential multipliers and bonuses.
        """
        self.reels = self._initialize_reels()
        results = self._check_wild_scatter()
        return results

    def _check_wild_scatter(self):
        """
        Check for wild and scatter symbols and determine outcome.
        
        :return: A dictionary with the spin result, multipliers, and bonus information.
        """
        wild_count = sum(symbol == self.wild_symbol for reel in self.reels for symbol in reel)
        scatter_count = sum(symbol == self.scatter_symbol for reel in self.reels for symbol in reel)

        # Basic multiplier logic
        multiplier = 1
        if wild_count > 0:
            multiplier *= wild_count * 2  # Example: each wild symbol doubles the payout
        
        if scatter_count > 0:
            multiplier *= scatter_count * 3  # Example: each scatter symbol triples the payout

        bonus_triggered = scatter_count >= 3  # Trigger bonus game if 3 or more scatters

        return {
            'reels': self.reels,
            'wild_count': wild_count,
            'scatter_count': scatter_count,
            'multiplier': multiplier,
            'bonus_triggered': bonus_triggered
        }

    def display_results(self, results):
        """
        Display the results of the spin in a user-friendly format.

        :param results: Results dictionary from a spin.
        """
        print("Reels: ", results['reels'])
        print(f"Wild Symbols Count: {results['wild_count']}")
        print(f"Scatter Symbols Count: {results['scatter_count']}")
        print(f"Multiplier: x{results['multiplier']}")
        if results['bonus_triggered']:
            print("Bonus game triggered!")
        else:
            print("No bonus game this time.")

def main():
    """
    Main function to run the WildScatterSlot game simulation.
    """
    try:
        game = WildScatterSlot()
        results = game.spin()
        game.display_results(results)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
