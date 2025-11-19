"""
Generated Code Metadata:
========================
Original URL: https://aspjj.com
Prompt: Write a Python code snippet to simulate a simple slot machine game as described on สล็อตเว็บตรง, considering the RTP rate and potential payouts.
Generated: DETERMINISTIC_2666530b9622cefa
Batch ID: 20250622_212541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Dict, List, Tuple

class SlotMachine:
    """
    A simple slot machine game simulation with configurable RTP and payouts.
    """
    
    def __init__(self, rtp: float = 0.95, symbols: List[str] = None, payouts: Dict[Tuple[str, str, str], float] = None):
        """
        Initialize the slot machine with RTP, symbols, and payout table.
        
        Args:
            rtp: Return to Player percentage (0-1)
            symbols: List of available symbols
            payouts: Dictionary mapping symbol combinations to payout multipliers
        """
        self.rtp = rtp
        self.symbols = symbols or ['🍒', '🍋', '🍊', '🍇', '🔔', '7']
        self.payouts = payouts or {
            ('7', '7', '7'): 10.0,
            ('🔔', '🔔', '🔔'): 5.0,
            ('🍇', '🍇', '🍇'): 3.0,
            ('🍊', '🍊', '🍊'): 2.0,
            ('🍋', '🍋', '🍋'): 1.5,
            ('🍒', '🍒', '🍒'): 1.2,
            ('🍒', '🍒', '*'): 0.5  # Any symbol as wildcard
        }
        
        # Validate RTP
        if not 0 <= self.rtp <= 1:
            raise ValueError("RTP must be between 0 and 1")
            
        # Calculate symbol weights based on RTP
        self._calculate_symbol_weights()
    
    def _calculate_symbol_weights(self) -> None:
        """Calculate symbol weights to achieve the desired RTP."""
        total_payout = sum(self.payouts.values())
        base_weight = 1.0 / len(self.symbols)
        
        # Adjust weights to achieve RTP
        adjustment_factor = self.rtp / (total_payout / len(self.payouts))
        self.symbol_weights = {sym: base_weight * adjustment_factor for sym in self.symbols}
        
        # Normalize weights
        total_weight = sum(self.symbol_weights.values())
        self.symbol_weights = {k: v/total_weight for k, v in self.symbol_weights.items()}
    
    def spin(self, bet_amount: float) -> Tuple[List[str], float, float]:
        """
        Simulate a slot machine spin.
        
        Args:
            bet_amount: The amount bet by the player
            
        Returns:
            Tuple containing:
                - List of symbols spun
                - Payout multiplier
                - Actual payout amount
        """
        if bet_amount <= 0:
            raise ValueError("Bet amount must be positive")
            
        # Generate random symbols based on weights
        symbols = random.choices(
            population=self.symbols,
            weights=[self.symbol_weights[s] for s in self.symbols],
            k=3
        )
        
        # Check for winning combinations
        payout_multiplier = 0.0
        
        # Check exact matches first
        for combo, multiplier in self.payouts.items():
            if len(combo) != 3:
                continue
                
            if (symbols[0] == combo[0] or combo[0] == '*') and \
               (symbols[1] == combo[1] or combo[1] == '*') and \
               (symbols[2] == combo[2] or combo[2] == '*'):
                payout_multiplier = max(payout_multiplier, multiplier)
        
        payout_amount = bet_amount * payout_multiplier
        
        return symbols, payout_multiplier, payout_amount

    def play_round(self, bet_amount: float) -> None:
        """
        Play a round of the slot machine and display results.
        
        Args:
            bet_amount: The amount bet by the player
        """
        try:
            symbols, multiplier, payout = self.spin(bet_amount)
            print(f"Spin result: {' '.join(symbols)}")
            
            if multiplier > 0:
                print(f"Congratulations! You won {payout:.2f} (x{multiplier})")
            else:
                print("No win this time. Try again!")
                
        except ValueError as e:
            print(f"Error: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Create a slot machine with default settings
    slot_machine = SlotMachine(rtp=0.95)
    
    # Simulate playing with a $1 bet
    print("Welcome to the Python Slot Machine!")
    print(f"Available symbols: {' '.join(slot_machine.symbols)}")
    print("Payout examples:")
    for combo, mult in slot_machine.payouts.items():
        print(f"{' '.join(combo)}: x{mult}")
    
    while True:
        try:
            bet = float(input("\nEnter your bet amount (0 to quit): "))
            if bet == 0:
                print("Thanks for playing!")
                break
            slot_machine.play_round(bet)
        except ValueError:
            print("Please enter a valid number")
```
