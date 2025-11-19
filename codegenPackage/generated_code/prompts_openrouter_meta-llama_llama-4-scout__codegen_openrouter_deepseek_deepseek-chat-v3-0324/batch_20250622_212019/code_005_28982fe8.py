"""
Generated Code Metadata:
========================
Original URL: https://plf3108.com
Prompt: Create a simple game logic for a slots game, similar to those offered by 868, with multiple reels, bonus rounds, and win multipliers, using a programming language like Python or JavaScript.
Generated: DETERMINISTIC_28982fe8387af46b
Batch ID: 20250622_212019
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
    A simple slot game with multiple reels, bonus rounds, and win multipliers.
    """
    
    def __init__(self, reels: int = 3, symbols: List[str] = None, paytable: Dict[Tuple[str, ...], int] = None):
        """
        Initialize the slot game.
        
        Args:
            reels: Number of reels (default: 3)
            symbols: List of symbols to use (default: ['Cherry', 'Lemon', 'Orange', 'Plum', 'Bell', 'Bar', 'Seven'])
            paytable: Dictionary mapping symbol combinations to payouts
        """
        self.reels = reels
        self.symbols = symbols or ['Cherry', 'Lemon', 'Orange', 'Plum', 'Bell', 'Bar', 'Seven']
        self.paytable = paytable or {
            ('Seven', 'Seven', 'Seven'): 100,
            ('Bar', 'Bar', 'Bar'): 50,
            ('Bell', 'Bell', 'Bell'): 20,
            ('Plum', 'Plum', 'Plum'): 15,
            ('Orange', 'Orange', 'Orange'): 10,
            ('Lemon', 'Lemon', 'Lemon'): 5,
            ('Cherry', 'Cherry', 'Cherry'): 3,
            ('Cherry', 'Cherry', '*'): 2,
            ('Cherry', '*', '*'): 1
        }
        self.bonus_round_active = False
        self.bonus_multiplier = 1
        
    def spin(self, bet_amount: float) -> Tuple[List[str], float, bool]:
        """
        Spin the reels and calculate winnings.
        
        Args:
            bet_amount: Amount bet by the player
            
        Returns:
            Tuple containing:
                - List of symbols displayed on the reels
                - Amount won (0 if no win)
                - Boolean indicating if bonus round was triggered
        """
        if bet_amount <= 0:
            raise ValueError("Bet amount must be positive")
            
        result = [random.choice(self.symbols) for _ in range(self.reels)]
        win_amount = 0.0
        bonus_triggered = False
        
        # Check for wins in paytable
        for combination, payout in self.paytable.items():
            if self._check_combination(result, combination):
                win_amount = payout * bet_amount * self.bonus_multiplier
                break
                
        # Check for bonus trigger (Three Bells)
        if result == ['Bell', 'Bell', 'Bell']:
            bonus_triggered = True
            self.bonus_round_active = True
            self.bonus_multiplier = 3
            
        return result, win_amount, bonus_triggered
        
    def bonus_round(self, bet_amount: float) -> Tuple[List[str], float]:
        """
        Execute bonus round with higher multipliers.
        
        Args:
            bet_amount: Original bet amount
            
        Returns:
            Tuple containing:
                - List of symbols displayed on the reels
                - Amount won (0 if no win)
        """
        if not self.bonus_round_active:
            raise ValueError("Bonus round is not active")
            
        result = [random.choice(self.symbols) for _ in range(self.reels)]
        win_amount = 0.0
        
        # Bonus round has higher payouts
        for combination, payout in self.paytable.items():
            if self._check_combination(result, combination):
                win_amount = payout * bet_amount * self.bonus_multiplier
                break
                
        # End bonus round after one spin
        self.bonus_round_active = False
        self.bonus_multiplier = 1
        
        return result, win_amount
        
    def _check_combination(self, result: List[str], combination: Tuple[str, ...]) -> bool:
        """
        Check if the result matches a paytable combination.
        Wildcard '*' matches any symbol.
        
        Args:
            result: List of symbols from the spin
            combination: Tuple representing a paytable combination
            
        Returns:
            True if the result matches the combination
        """
        if len(result) != len(combination):
            return False
            
        for r, c in zip(result, combination):
            if c != '*' and r != c:
                return False
                
        return True

# Example usage
if __name__ == "__main__":
    game = SlotGame()
    
    # Normal spin
    result, win, bonus = game.spin(1.0)
    print(f"Spin result: {result}")
    print(f"Win amount: {win}")
    print(f"Bonus triggered: {bonus}")
    
    # Bonus round if triggered
    if bonus:
        bonus_result, bonus_win = game.bonus_round(1.0)
        print(f"Bonus round result: {bonus_result}")
        print(f"Bonus win amount: {bonus_win}")
```
