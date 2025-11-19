"""
Generated Code Metadata:
========================
Original URL: https://alltecskateparks.com
Prompt: Write code to simulate free spin mechanics in a slot game, ensuring multipliers (x2 to x20) are applied correctly, as described for Lucky Neko on INDOXSLOT.
Generated: DETERMINISTIC_ff1b2893ca57ed99
Batch ID: 20250612_152827
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

class FreeSpinSimulator:
    """
    Simulates free spin mechanics for a slot game with multipliers.
    """
    
    def __init__(self, base_spins: int = 10, multiplier_range: Tuple[int, int] = (2, 20)):
        """
        Initialize the free spin simulator.
        
        Args:
            base_spins: Number of base free spins awarded.
            multiplier_range: Tuple representing min and max multiplier values (inclusive).
        """
        self.base_spins = base_spins
        self.min_multiplier, self.max_multiplier = multiplier_range
        self.current_spins = base_spins
        self.total_wins = 0
        self.multiplier = 1
        self.spin_history = []
        
    def _generate_multiplier(self) -> int:
        """Generate a random multiplier within the specified range."""
        return random.randint(self.min_multiplier, self.max_multiplier)
    
    def _calculate_win(self, base_win: float) -> float:
        """Calculate the win amount after applying the current multiplier."""
        return base_win * self.multiplier
    
    def spin(self, base_win: float) -> Dict[str, float]:
        """
        Execute a free spin with the given base win amount.
        
        Args:
            base_win: The base win amount before multiplier is applied.
            
        Returns:
            Dictionary containing spin results including:
            - win_amount: Total win after multiplier
            - multiplier: Current multiplier applied
            - spins_remaining: Free spins left
        """
        if self.current_spins <= 0:
            raise ValueError("No free spins remaining")
            
        # Apply multiplier to win
        win_amount = self._calculate_win(base_win)
        self.total_wins += win_amount
        
        # Generate new random multiplier for next spin
        self.multiplier = self._generate_multiplier()
        
        # Record spin history
        spin_result = {
            "spin_number": self.base_spins - self.current_spins + 1,
            "base_win": base_win,
            "win_amount": win_amount,
            "multiplier": self.multiplier,
            "spins_remaining": self.current_spins - 1
        }
        self.spin_history.append(spin_result)
        
        # Decrement remaining spins
        self.current_spins -= 1
        
        return spin_result
    
    def get_summary(self) -> Dict[str, float]:
        """
        Get summary of all free spins.
        
        Returns:
            Dictionary containing:
            - total_wins: Sum of all wins during free spins
            - total_spins: Total free spins executed
            - average_multiplier: Average multiplier across all spins
        """
        if not self.spin_history:
            return {
                "total_wins": 0,
                "total_spins": 0,
                "average_multiplier": 0
            }
            
        multipliers = [spin["multiplier"] for spin in self.spin_history]
        return {
            "total_wins": self.total_wins,
            "total_spins": len(self.spin_history),
            "average_multiplier": sum(multipliers) / len(multipliers)
        }

# Example usage
if __name__ == "__main__":
    # Initialize with 10 free spins and multipliers between 2x and 20x
    simulator = FreeSpinSimulator(base_spins=10, multiplier_range=(2, 20))
    
    # Simulate spins with random base wins between 1 and 100
    for _ in range(simulator.base_spins):
        base_win = random.uniform(1, 100)
        result = simulator.spin(base_win)
        print(f"Spin {result['spin_number']}: Base Win: {base_win:.2f}, "
              f"Multiplier: {result['multiplier']}x, "
              f"Win: {result['win_amount']:.2f}, "
              f"Spins Left: {result['spins_remaining']}")
    
    # Print summary
    summary = simulator.get_summary()
    print("\nFree Spins Summary:")
    print(f"Total Wins: {summary['total_wins']:.2f}")
    print(f"Total Spins: {summary['total_spins']}")
    print(f"Average Multiplier: {summary['average_multiplier']:.2f}x")
```
