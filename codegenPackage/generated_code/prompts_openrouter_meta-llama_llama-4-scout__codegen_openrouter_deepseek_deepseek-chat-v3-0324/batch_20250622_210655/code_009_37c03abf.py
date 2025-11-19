"""
Generated Code Metadata:
========================
Original URL: https://globaljournalpress.com
Prompt: Explain the psychology behind online slots, including the factors that make them appealing to players and the potential risks of addiction.
Generated: DETERMINISTIC_37c03abfe2f8269a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script simulates a basic online slot machine game to demonstrate psychological aspects
like variable rewards, near misses, and visual/sound effects that make slots appealing.
It also includes warnings about potential addiction risks.
"""

import random
import time
import sys
from enum import Enum

class Symbol(Enum):
    """Slot machine symbols with different weights"""
    CHERRY = 1
    LEMON = 2
    ORANGE = 3
    PLUM = 4
    BELL = 5
    BAR = 6
    SEVEN = 7

# Symbol weights - lower probability for higher value symbols
SYMBOL_WEIGHTS = {
    Symbol.CHERRY: 35,
    Symbol.LEMON: 30,
    Symbol.ORANGE: 20,
    Symbol.PLUM: 10,
    Symbol.BELL: 3,
    Symbol.BAR: 1.5,
    Symbol.SEVEN: 0.5
}

class SlotMachine:
    def __init__(self):
        self.balance = 100  # Starting balance
        self.last_win = 0
        self.spins = 0
        self.payouts = {
            (Symbol.SEVEN, Symbol.SEVEN, Symbol.SEVEN): 100,
            (Symbol.BAR, Symbol.BAR, Symbol.BAR): 50,
            (Symbol.BELL, Symbol.BELL, Symbol.BELL): 20,
            (Symbol.PLUM, Symbol.PLUM, Symbol.PLUM): 10,
            (Symbol.ORANGE, Symbol.ORANGE, Symbol.ORANGE): 5,
            (Symbol.LEMON, Symbol.LEMON, Symbol.LEMON): 3,
            (Symbol.CHERRY, Symbol.CHERRY, Symbol.CHERRY): 2,
            (Symbol.CHERRY, Symbol.CHERRY, None): 1
        }
    
    def weighted_random_choice(self):
        """Select symbols based on weighted probabilities"""
        total = sum(SYMBOL_WEIGHTS.values())
        r = random.uniform(0, total)
        upto = 0
        for symbol, weight in SYMBOL_WEIGHTS.items():
            if upto + weight >= r:
                return symbol
            upto += weight
        return Symbol.CHERRY  # fallback
    
    def spin(self, bet_amount):
        """Simulate a slot machine spin with visual effects"""
        if bet_amount > self.balance:
            print("Insufficient balance!")
            return False
        
        self.balance -= bet_amount
        self.spins += 1
        
        # Simulate spinning animation
        print("\nSpinning...")
        for _ in range(3):
            for _ in range(5):
                print(random.choice(list(Symbol)).name, end="\r")
                time.sleep(0.1)
        
        # Get final result
        result = [self.weighted_random_choice() for _ in range(3)]
        
        # Check for near miss (two matching high symbols)
        if len(set(result)) == 2 and any(s in [Symbol.SEVEN, Symbol.BAR, Symbol.BELL] for s in result):
            print("Almost! Near miss!")
        
        # Display result
        print(" ".join(s.name for s in result))
        
        # Check for wins
        win_amount = 0
        for combo, payout in self.payouts.items():
            if all(r == c for r, c in zip(result, combo) if c is not None):
                win_amount = payout * bet_amount
                break
        
        if win_amount > 0:
            self.last_win = win_amount
            self.balance += win_amount
            print(f"Winner! You won ${win_amount}!")
            # Simulate celebratory effects
            for _ in range(3):
                print("🎉", end="")
                time.sleep(0.3)
            print()
        else:
            print("No win this time.")
        
        return True
    
    def show_warning(self):
        """Display responsible gambling message"""
        print("\n" + "="*50)
        print("IMPORTANT: Gambling can be addictive. Please play responsibly.")
        print(f"Stats: Spins: {self.spins} | Current balance: ${self.balance}")
        print("="*50 + "\n")

def main():
    """Main game loop"""
    machine = SlotMachine()
    
    print("Welcome to Python Slots!")
    print("Psychological factors demonstrated:")
    print("- Variable rewards (random payouts)")
    print("- Near misses (almost winning)")
    print("- Celebratory effects (visual/sound)")
    print("- Small frequent wins with occasional big wins")
    
    while True:
        machine.show_warning()
        print(f"Balance: ${machine.balance}")
        
        try:
            bet = int(input("Enter bet amount (0 to quit): "))
            if bet == 0:
                break
            if bet < 1:
                print("Minimum bet is $1")
                continue
        except ValueError:
            print("Please enter a valid number")
            continue
        
        if not machine.spin(bet):
            continue
        
        # After a win, encourage continued play
        if machine.last_win > 0:
            print("Try again while you're on a hot streak!")
        
        if machine.balance <= 0:
            print("Game over - you're out of funds!")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGame exited. Remember to gamble responsibly!")
        sys.exit(0)
```
