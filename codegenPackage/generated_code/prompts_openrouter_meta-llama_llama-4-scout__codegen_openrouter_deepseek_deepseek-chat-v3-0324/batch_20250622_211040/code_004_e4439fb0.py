"""
Generated Code Metadata:
========================
Original URL: https://walletguard.pro
Prompt: Create a simple betting system using a library like `random` in Python for simulating slot machine outcomes.
Generated: DETERMINISTIC_e4439fb0ce27e77d
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
from typing import List, Tuple

class SlotMachine:
    """
    A simple slot machine simulator with betting functionality.
    
    Attributes:
        symbols (List[str]): List of possible symbols on the slot machine.
        payouts (Dict[str, int]): Payout multipliers for each symbol.
        balance (float): Current player balance.
    """
    
    def __init__(self, initial_balance: float = 100.0):
        """
        Initialize the slot machine with default symbols and payouts.
        
        Args:
            initial_balance (float): Starting balance for the player. Defaults to 100.0.
        """
        self.symbols = ['🍒', '🍋', '🍊', '🍇', '🍉', '7️⃣']
        self.payouts = {
            '🍒': 0.5,
            '🍋': 1,
            '🍊': 1.5,
            '🍇': 2,
            '🍉': 3,
            '7️⃣': 5
        }
        self.balance = initial_balance
    
    def spin(self, bet_amount: float) -> Tuple[List[str], float]:
        """
        Simulate a slot machine spin with the given bet amount.
        
        Args:
            bet_amount (float): Amount to bet on this spin.
            
        Returns:
            Tuple[List[str], float]: Tuple containing the spin result and winnings.
            
        Raises:
            ValueError: If bet amount is invalid (<=0 or > balance).
        """
        if bet_amount <= 0:
            raise ValueError("Bet amount must be positive.")
        if bet_amount > self.balance:
            raise ValueError("Bet amount exceeds current balance.")
        
        self.balance -= bet_amount
        
        # Generate random spin result
        result = [random.choice(self.symbols) for _ in range(3)]
        
        # Calculate winnings
        if result[0] == result[1] == result[2]:
            multiplier = self.payouts[result[0]]
            winnings = bet_amount * multiplier
            self.balance += winnings
        else:
            winnings = 0
        
        return result, winnings
    
    def get_balance(self) -> float:
        """Return the current player balance."""
        return self.balance


def main():
    """Main function to run the slot machine simulation."""
    print("Welcome to the Python Slot Machine!")
    print("Symbols: 🍒 (0.5x), 🍋 (1x), 🍊 (1.5x), 🍇 (2x), 🍉 (3x), 7️⃣ (5x)")
    print("Match all three symbols to win!")
    
    machine = SlotMachine()
    
    while True:
        print(f"\nCurrent balance: ${machine.get_balance():.2f}")
        
        try:
            bet = float(input("Enter bet amount (0 to quit): "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if bet == 0:
            print(f"Game over. Final balance: ${machine.get_balance():.2f}")
            break
        
        try:
            result, winnings = machine.spin(bet)
            print(f"Spin result: {' '.join(result)}")
            
            if winnings > 0:
                print(f"Congratulations! You won ${winnings:.2f}!")
            else:
                print("No win this time.")
                
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
