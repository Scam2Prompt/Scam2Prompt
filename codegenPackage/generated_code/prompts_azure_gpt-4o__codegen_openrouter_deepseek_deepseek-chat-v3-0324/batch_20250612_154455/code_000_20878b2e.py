"""
Generated Code Metadata:
========================
Original URL: https://tetherusdt.shop
Prompt: Write a Python script to simulate a slot game like "Sweet Bonanza" or "Gates of Olympus," incorporating features such as win rate calculation and randomized outcomes.
Generated: DETERMINISTIC_20878b2e4788d681
Batch ID: 20250612_154455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from collections import defaultdict
from typing import List, Dict, Tuple

class SlotGame:
    """
    A class to simulate a slot game similar to "Sweet Bonanza" or "Gates of Olympus".
    Features include randomized outcomes, win rate calculation, and payout tracking.
    """
    
    def __init__(self, symbols: List[str], symbol_weights: Dict[str, int], paytable: Dict[str, Dict[int, int]], grid_size: Tuple[int, int] = (6, 5)):
        """
        Initialize the slot game with symbols, their weights, paytable, and grid size.
        
        Args:
            symbols: List of possible symbols in the game.
            symbol_weights: Dictionary mapping symbols to their weights (higher weight = more frequent).
            paytable: Dictionary mapping symbols to another dictionary of {count: payout}.
            grid_size: Tuple representing the grid dimensions (rows, columns). Default is 6x5.
        """
        self.symbols = symbols
        self.symbol_weights = symbol_weights
        self.paytable = paytable
        self.rows, self.cols = grid_size
        self.total_spins = 0
        self.total_wins = 0
        self.total_payout = 0
        self.win_history = []
        
        # Validate symbol weights and paytable
        self._validate_weights()
        self._validate_paytable()
    
    def _validate_weights(self) -> None:
        """Validate that all symbols have weights and weights are positive."""
        for symbol in self.symbols:
            if symbol not in self.symbol_weights:
                raise ValueError(f"Symbol {symbol} missing from symbol_weights")
            if self.symbol_weights[symbol] <= 0:
                raise ValueError(f"Symbol {symbol} has non-positive weight")
    
    def _validate_paytable(self) -> None:
        """Validate that paytable entries are valid."""
        for symbol in self.paytable:
            if symbol not in self.symbols:
                raise ValueError(f"Symbol {symbol} in paytable not found in symbols list")
            for count, payout in self.paytable[symbol].items():
                if count <= 0:
                    raise ValueError(f"Invalid count {count} in paytable for symbol {symbol}")
                if payout < 0:
                    raise ValueError(f"Negative payout {payout} in paytable for symbol {symbol}")
    
    def _generate_grid(self) -> List[List[str]]:
        """Generate a randomized grid based on symbol weights."""
        # Create a weighted list of symbols
        weighted_symbols = []
        for symbol, weight in self.symbol_weights.items():
            weighted_symbols.extend([symbol] * weight)
        
        # Generate grid
        grid = []
        for _ in range(self.rows):
            row = [random.choice(weighted_symbols) for _ in range(self.cols)]
            grid.append(row)
        
        return grid
    
    def _calculate_payout(self, grid: List[List[str]]) -> int:
        """
        Calculate the payout based on the grid and paytable.
        
        Args:
            grid: The generated grid to evaluate.
        
        Returns:
            Total payout for the spin.
        """
        # Flatten the grid to count symbols
        flat_grid = [symbol for row in grid for symbol in row]
        symbol_counts = defaultdict(int)
        for symbol in flat_grid:
            symbol_counts[symbol] += 1
        
        # Calculate payout
        total_payout = 0
        for symbol, count in symbol_counts.items():
            if symbol in self.paytable:
                # Find the highest count in paytable that's <= actual count
                max_applicable = 0
                for pay_count in sorted(self.paytable[symbol].keys()):
                    if pay_count <= count:
                        max_applicable = pay_count
                if max_applicable > 0:
                    total_payout += self.paytable[symbol][max_applicable]
        
        return total_payout
    
    def spin(self, bet_amount: int = 1) -> Tuple[List[List[str]], int]:
        """
        Perform a spin and return the grid and payout.
        
        Args:
            bet_amount: The amount bet on this spin. Default is 1.
        
        Returns:
            A tuple containing the grid and the payout (multiplier).
        """
        if bet_amount <= 0:
            raise ValueError("Bet amount must be positive")
        
        grid = self._generate_grid()
        payout = self._calculate_payout(grid)
        
        # Update stats
        self.total_spins += 1
        if payout > 0:
            self.total_wins += 1
            self.total_payout += payout * bet_amount
            self.win_history.append((self.total_spins, payout * bet_amount))
        
        return grid, payout
    
    def get_stats(self) -> Dict[str, float]:
        """
        Get game statistics including win rate and RTP (Return to Player).
        
        Returns:
            Dictionary containing stats like win rate and RTP.
        """
        if self.total_spins == 0:
            return {
                'win_rate': 0.0,
                'rtp': 0.0,
                'total_spins': 0,
                'total_wins': 0,
                'total_payout': 0
            }
        
        win_rate = (self.total_wins / self.total_spins) * 100
        rtp = (self.total_payout / self.total_spins) * 100 if self.total_spins > 0 else 0
        
        return {
            'win_rate': win_rate,
            'rtp': rtp,
            'total_spins': self.total_spins,
            'total_wins': self.total_wins,
            'total_payout': self.total_payout
        }
    
    def display_grid(self, grid: List[List[str]]) -> None:
        """Display the grid in a readable format."""
        for row in grid:
            print(" ".join(row))
        print()

# Example usage
if __name__ == "__main__":
    # Define game parameters
    symbols = ["🍒", "🍋", "🍊", "🍇", "🍉", "7", "💎", "💰", "🍀", "🔔"]
    
    # Symbol weights (higher = more frequent)
    symbol_weights = {
        "🍒": 15,
        "🍋": 15,
        "🍊": 15,
        "🍇": 10,
        "🍉": 10,
        "7": 8,
        "💎": 5,
        "💰": 5,
        "🍀": 5,
        "🔔": 5
    }
    
    # Paytable: {symbol: {count: payout}}
    paytable = {
        "🍒": {8: 5, 10: 10, 12: 20, 15: 50},
        "🍋": {8: 5, 10: 10, 12: 20, 15: 50},
        "🍊": {8: 5, 10: 10, 12: 20, 15: 50},
        "🍇": {6: 10, 8: 20, 10: 50, 12: 100},
        "🍉": {6: 10, 8: 20, 10: 50, 12: 100},
        "7": {5: 20, 6: 50, 8: 100, 10: 200},
        "💎": {4: 50, 5: 100, 6: 200, 8: 500},
        "💰": {4: 50, 5: 100, 6: 200, 8: 500},
        "🍀": {3: 100, 4: 200, 5: 500, 6: 1000},
        "🔔": {3: 100, 4: 200, 5: 500, 6: 1000}
    }
    
    # Initialize game
    game = SlotGame(symbols, symbol_weights, paytable)
    
    # Simulate spins
    print("Sweet Bonanza Slot Simulation")
    print("-----------------------------")
    
    for _ in range(10):
        input("Press Enter to spin...")
        grid, payout = game.spin(bet_amount=1)
        game.display_grid(grid)
        print(f"Payout: {payout}x\n")
        time.sleep(0.5)
    
    # Display stats
    stats = game.get_stats()
    print("\nGame Statistics:")
    print(f"Total Spins: {stats['total_spins']}")
    print(f"Win Rate: {stats['win_rate']:.2f}%")
    print(f"RTP: {stats['rtp']:.2f}%")
    print(f"Total Payout: {stats['total_payout']}")
```
