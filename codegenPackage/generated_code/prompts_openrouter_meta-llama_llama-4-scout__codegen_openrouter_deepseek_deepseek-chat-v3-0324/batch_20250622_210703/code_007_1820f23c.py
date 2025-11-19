"""
Generated Code Metadata:
========================
Original URL: https://rheapratas.com
Prompt: Write a code snippet that demonstrates how to implement a bonus buy feature in a slot machine game, similar to those described on this webpage.
Generated: DETERMINISTIC_1820f23cfacb1bdb
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Optional, List, Dict

class SlotMachine:
    def __init__(self):
        self.symbols = ['🍒', '🍋', '🍊', '🍇', '🍉', '7️⃣']
        self.payouts = {
            '🍒': {3: 2, 4: 5, 5: 10},
            '🍋': {3: 3, 4: 7, 5: 15},
            '🍊': {3: 4, 4: 10, 5: 20},
            '🍇': {3: 5, 4: 15, 5: 30},
            '🍉': {3: 7, 4: 20, 5: 50},
            '7️⃣': {3: 10, 4: 30, 5: 100}
        }
        self.balance = 100
        self.bonus_active = False
        self.bonus_cost = 50
        self.bonus_multiplier = 2
        self.bonus_spins = 5

    def spin(self) -> List[str]:
        """Simulate a slot machine spin and return the result."""
        if self.balance < 1:
            raise ValueError("Insufficient balance to spin")
        
        self.balance -= 1
        return [random.choice(self.symbols) for _ in range(5)]

    def calculate_payout(self, result: List[str]) -> int:
        """Calculate payout based on spin result."""
        symbol_counts = {}
        for symbol in self.symbols:
            count = result.count(symbol)
            if count >= 3:
                symbol_counts[symbol] = count
        
        payout = 0
        for symbol, count in symbol_counts.items():
            payout += self.payouts[symbol][count]
        
        if self.bonus_active:
            payout *= self.bonus_multiplier
            self.bonus_spins -= 1
            if self.bonus_spins <= 0:
                self.bonus_active = False
        
        self.balance += payout
        return payout

    def buy_bonus(self) -> bool:
        """Purchase bonus feature if sufficient balance."""
        if self.balance < self.bonus_cost:
            return False
        
        self.balance -= self.bonus_cost
        self.bonus_active = True
        self.bonus_spins = 5
        return True

    def get_game_state(self) -> Dict:
        """Return current game state."""
        return {
            'balance': self.balance,
            'bonus_active': self.bonus_active,
            'bonus_spins_remaining': self.bonus_spins,
            'bonus_multiplier': self.bonus_multiplier
        }

# Example usage
if __name__ == "__main__":
    slot = SlotMachine()
    
    # Normal spin
    result = slot.spin()
    payout = slot.calculate_payout(result)
    print(f"Spin result: {result}, Payout: {payout}")
    
    # Buy bonus feature
    if slot.buy_bonus():
        print("Bonus purchased!")
        
        # Spin with bonus active
        for _ in range(5):
            result = slot.spin()
            payout = slot.calculate_payout(result)
            print(f"Bonus spin result: {result}, Payout: {payout}")
    else:
        print("Not enough balance to buy bonus")
    
    print(f"Final balance: {slot.balance}")
```
