"""
Generated Code Metadata:
========================
Original URL: https://tante4dx41.com
Prompt: Write a Python script to simulate a slot game with multiple paylines and reels, similar to those offered on TANTE4D, using a random number generator to determine winning combinations.
Generated: DETERMINISTIC_1bf28c478556f9d7
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Tuple

class SlotGame:
    """
    A class to simulate a slot game with multiple paylines and reels.
    """
    
    def __init__(self, reels: int = 5, rows: int = 3, symbols: List[str] = None, paytable: Dict[str, List[int]] = None):
        """
        Initialize the slot game with reels, rows, symbols, and paytable.
        
        Args:
            reels (int): Number of reels. Default is 5.
            rows (int): Number of rows. Default is 3.
            symbols (List[str]): List of symbols. Default is ['A', 'B', 'C', 'D', 'E', 'F'].
            paytable (Dict[str, List[int]]): Paytable mapping symbols to payouts. Default is provided.
        """
        self.reels = reels
        self.rows = rows
        self.symbols = symbols if symbols else ['A', 'B', 'C', 'D', 'E', 'F']
        
        # Default paytable: key is symbol, value is list of payouts for 3, 4, 5 matches
        self.paytable = paytable if paytable else {
            'A': [10, 20, 50],
            'B': [5, 10, 25],
            'C': [3, 5, 15],
            'D': [2, 4, 10],
            'E': [1, 2, 5],
            'F': [0, 1, 3]
        }
        
        # Define default paylines (each sublist represents a payline's reel positions)
        self.paylines = [
            [0, 0, 0, 0, 0],  # Top horizontal line
            [1, 1, 1, 1, 1],  # Middle horizontal line
            [2, 2, 2, 2, 2],  # Bottom horizontal line
            [0, 1, 2, 1, 0],  # V-shaped line
            [2, 1, 0, 1, 2]   # Inverted V-shaped line
        ]
        
    def spin(self) -> Tuple[List[List[str]], Dict[int, List[str]]]:
        """
        Simulate a spin and return the grid and active paylines.
        
        Returns:
            Tuple[List[List[str]], Dict[int, List[str]]]: 
                - Grid of symbols (reels x rows)
                - Dictionary of paylines with their symbols
        """
        # Generate random symbols for each reel and row
        grid = [
            [random.choice(self.symbols) for _ in range(self.rows)]
            for _ in range(self.reels)
        ]
        
        # Extract symbols for each payline
        active_paylines = {}
        for i, line in enumerate(self.paylines):
            symbols = [grid[reel][row] for reel, row in enumerate(line)]
            active_paylines[i] = symbols
        
        return grid, active_paylines
    
    def calculate_wins(self, active_paylines: Dict[int, List[str]], bet: float = 1.0) -> Dict[int, Dict[str, float]]:
        """
        Calculate wins for each payline based on the active symbols and bet.
        
        Args:
            active_paylines (Dict[int, List[str]]): Dictionary of paylines with their symbols.
            bet (float): Bet amount. Default is 1.0.
            
        Returns:
            Dict[int, Dict[str, float]]: Dictionary with payline index as key and 
                                         a dict of 'symbol', 'count', and 'payout' as value.
        """
        wins = {}
        
        for line_idx, symbols in active_paylines.items():
            # Check for consecutive matching symbols from left to right
            first_symbol = symbols[0]
            count = 1
            
            for symbol in symbols[1:]:
                if symbol == first_symbol:
                    count += 1
                else:
                    break
            
            # Check if the count is enough for a payout
            if count >= 3 and first_symbol in self.paytable:
                payout_multiplier = self.paytable[first_symbol][min(count, 5) - 3]
                payout = bet * payout_multiplier
                wins[line_idx] = {
                    'symbol': first_symbol,
                    'count': count,
                    'payout': payout
                }
        
        return wins
    
    def display_grid(self, grid: List[List[str]]) -> None:
        """
        Display the slot grid in a readable format.
        
        Args:
            grid (List[List[str]]): Grid of symbols (reels x rows).
        """
        for row in range(self.rows):
            line = []
            for reel in range(self.reels):
                line.append(grid[reel][row])
            print(" | ".join(line))
    
    def play(self, bet: float = 1.0) -> None:
        """
        Simulate a single play of the slot game.
        
        Args:
            bet (float): Bet amount. Default is 1.0.
        """
        print(f"Spinning with bet: {bet}")
        grid, active_paylines = self.spin()
        self.display_grid(grid)
        
        wins = self.calculate_wins(active_paylines, bet)
        
        if wins:
            print("\nWinning paylines:")
            total_payout = 0
            for line_idx, win in wins.items():
                print(f"Payline {line_idx + 1}: {win['count']}x {win['symbol']} -> {win['payout']}")
                total_payout += win['payout']
            print(f"\nTotal payout: {total_payout}")
        else:
            print("\nNo winning paylines.")


# Example usage
if __name__ == "__main__":
    game = SlotGame()
    game.play(bet=1.0)
```
