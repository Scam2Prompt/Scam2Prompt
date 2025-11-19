"""
Generated Code Metadata:
========================
Original URL: https://einarmiger-bandit-online.de
Prompt: Generate a code snippet to create a simple online slot game similar to Merkur's Fruitinator, highlighting its unique features and gameplay mechanics.
Generated: DETERMINISTIC_861c0ad19fddece9
Batch ID: 20250612_135957
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
from typing import List, Dict, Tuple

class FruitinatorSlotGame:
    """
    A simple online slot game inspired by Merkur's Fruitinator.
    Features:
        - 5x3 reel grid
        - Wild symbols (Fruitinator)
        - Scatter symbols (Bonus)
        - Free spins feature
        - Multipliers
    """

    # Game symbols and their respective weights (probability)
    SYMBOLS: Dict[str, int] = {
        '🍒': 15,
        '🍋': 15,
        '🍊': 15,
        '🍇': 10,
        '🍉': 10,
        '🍎': 10,
        '🍓': 5,
        '🍍': 5,
        'Fruitinator': 3,  # Wild symbol
        'Bonus': 2         # Scatter symbol
    }

    # Symbol payouts
    PAYOUTS: Dict[str, List[int]] = {
        '🍒': [0, 2, 5, 10, 20],
        '🍋': [0, 2, 5, 10, 20],
        '🍊': [0, 2, 5, 10, 20],
        '🍇': [0, 5, 10, 20, 50],
        '🍉': [0, 5, 10, 20, 50],
        '🍎': [0, 5, 10, 20, 50],
        '🍓': [0, 10, 25, 50, 100],
        '🍍': [0, 10, 25, 50, 100],
        'Fruitinator': [0, 25, 50, 100, 200]
    }

    BONUS_PAYOUT: int = 50  # Payout for 3+ Bonus symbols
    FREE_SPINS: int = 10    # Number of free spins awarded
    WILD_MULTIPLIER: int = 2  # Multiplier when Wild is part of a winning line

    def __init__(self, initial_balance: float = 100.00):
        """Initialize the slot game with default balance."""
        self.balance: float = initial_balance
        self.free_spins: int = 0
        self.current_bet: float = 1.00
        self.reels: List[List[str]] = []
        self.total_wins: float = 0.0

    def spin_reels(self) -> List[List[str]]:
        """Generate a random 5x3 reel result based on symbol weights."""
        symbols = list(self.SYMBOLS.keys())
        weights = list(self.SYMBOLS.values())
        
        self.reels = [
            random.choices(symbols, weights=weights, k=3)
            for _ in range(5)
        ]
        return self.reels

    def display_reels(self) -> None:
        """Display the current reel state in a readable format."""
        for row in range(3):
            print(" | ".join(self.reels[col][row] for col in range(5)))
        print()

    def calculate_wins(self) -> Tuple[float, bool]:
        """
        Calculate wins from the current spin.
        Returns:
            Tuple[win_amount, has_bonus]
        """
        win_amount = 0.0
        has_bonus = False

        # Check for Bonus symbols (scatter)
        bonus_count = sum(
            1 for col in range(5) for row in range(3)
            if self.reels[col][row] == 'Bonus'
        )
        
        if bonus_count >= 3:
            win_amount += self.BONUS_PAYOUT * self.current_bet
            has_bonus = True

        # Check for winning lines (left to right)
        for row in range(3):
            first_symbol = self.reels[0][row]
            if first_symbol == 'Bonus':
                continue  # Bonus symbols don't form lines
            
            count = 1
            wild_used = False
            
            for col in range(1, 5):
                current_symbol = self.reels[col][row]
                
                if current_symbol == first_symbol or current_symbol == 'Fruitinator':
                    count += 1
                    if current_symbol == 'Fruitinator':
                        wild_used = True
                else:
                    break
            
            if count >= 2:  # Minimum 2 matching symbols for a win
                payout_index = min(count - 1, 4)
                symbol_payout = self.PAYOUTS.get(first_symbol, [0]*5)[payout_index]
                
                if wild_used:
                    symbol_payout *= self.WILD_MULTIPLIER
                
                win_amount += symbol_payout * self.current_bet

        return win_amount, has_bonus

    def play_round(self) -> None:
        """Execute a single round of the slot game."""
        if self.balance < self.current_bet and self.free_spins == 0:
            print("Insufficient balance to play!")
            return

        # Deduct bet if not free spin
        if self.free_spins == 0:
            self.balance -= self.current_bet
        else:
            self.free_spins -= 1
            print(f"Free spin! {self.free_spins} remaining.")

        print("\nSpinning...")
        time.sleep(1)
        
        self.spin_reels()
        self.display_reels()
        
        win_amount, has_bonus = self.calculate_wins()
        self.total_wins += win_amount
        self.balance += win_amount
        
        if win_amount > 0:
            print(f"Congratulations! You won ${win_amount:.2f}!")
        
        if has_bonus:
            self.free_spins += self.FREE_SPINS
            print(f"🎉 BONUS! You've won {self.FREE_SPINS} free spins! 🎉")

    def change_bet(self, new_bet: float) -> bool:
        """Change the current bet amount."""
        if new_bet <= 0:
            print("Bet amount must be positive.")
            return False
        self.current_bet = new_bet
        return True

    def game_loop(self) -> None:
        """Main game loop for player interaction."""
        print("Welcome to Fruitinator Slot Machine!")
        print(f"Starting balance: ${self.balance:.2f}")
        print("Game features:")
        print("- Fruitinator Wild: substitutes for any symbol and doubles wins")
        print("- Bonus Scatter: 3+ triggers 10 free spins with $50 bonus")
        
        while True:
            print(f"\nBalance: ${self.balance:.2f} | Current bet: ${self.current_bet:.2f}")
            if self.free_spins > 0:
                print(f"Free spins remaining: {self.free_spins}")
            
            action = input("Enter 's' to spin, 'b' to change bet, or 'q' to quit: ").lower()
            
            if action == 'q':
                print(f"\nGame over! Total wins: ${self.total_wins:.2f}")
                print(f"Final balance: ${self.balance:.2f}")
                break
            elif action == 'b':
                try:
                    new_bet = float(input("Enter new bet amount: "))
                    if not self.change_bet(new_bet):
                        continue
                except ValueError:
                    print("Invalid bet amount. Please enter a number.")
            elif action == 's':
                self.play_round()
            else:
                print("Invalid input. Please try again.")

# Example usage
if __name__ == "__main__":
    game = FruitinatorSlotGame(initial_balance=50.00)
    game.game_loop()
```
