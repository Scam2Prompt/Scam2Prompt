"""
Generated Code Metadata:
========================
Original URL: https://billionalr.com
Prompt: Generate a code snippet for a simple online slot game that incorporates a "Depo 25 Bonus 25" feature for new members.
Generated: DETERMINISTIC_7ed91a2f5ed65d8a
Batch ID: 20250612_155235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Dict, Tuple, Optional

class SlotGame:
    """
    A simple online slot game with a "Depo 25 Bonus 25" feature for new members.
    """
    
    def __init__(self):
        self.symbols = ['🍒', '🍋', '🍊', '🍇', '🔔', '7️⃣']
        self.payouts = {
            ('7️⃣', '7️⃣', '7️⃣'): 100,
            ('🔔', '🔔', '🔔'): 50,
            ('🍇', '🍇', '🍇'): 20,
            ('🍊', '🍊', '🍊'): 10,
            ('🍋', '🍋', '🍋'): 5,
            ('🍒', '🍒', '🍒'): 3
        }
        self.balance = 0
        self.bonus_active = False
        self.bonus_balance = 0
    
    def deposit(self, amount: float, is_new_member: bool = False) -> bool:
        """
        Deposit money into the game balance.
        If new member and depositing 25, activate bonus.
        """
        if amount <= 0:
            print("Deposit amount must be positive.")
            return False
        
        self.balance += amount
        
        if is_new_member and amount == 25:
            self.bonus_active = True
            self.bonus_balance = 25
            print("🎉 Bonus activated! You received 25 bonus credits!")
        
        return True
    
    def spin(self, bet: float) -> Tuple[Tuple[str, str, str], Optional[float]]:
        """
        Spin the slot reels and return the result and winnings.
        """
        if bet <= 0:
            print("Bet must be positive.")
            return (None, None)
        
        if self.balance + self.bonus_balance < bet:
            print("Insufficient balance.")
            return (None, None)
        
        # Deduct bet from bonus first, then from main balance
        if self.bonus_active and self.bonus_balance > 0:
            deduction = min(bet, self.bonus_balance)
            self.bonus_balance -= deduction
            bet -= deduction
            if bet > 0:
                self.balance -= bet
        else:
            self.balance -= bet
        
        # Generate random result
        result = (
            random.choice(self.symbols),
            random.choice(self.symbols),
            random.choice(self.symbols)
        )
        
        # Calculate winnings
        winnings = self.payouts.get(result, 0) * bet
        
        if winnings > 0:
            self.balance += winnings
            print(f"🎉 You won {winnings} credits!")
        
        return (result, winnings if winnings > 0 else None)
    
    def get_balance(self) -> Dict[str, float]:
        """
        Return the current balance and bonus balance.
        """
        return {
            'balance': self.balance,
            'bonus_balance': self.bonus_balance
        }

# Example usage
if __name__ == "__main__":
    game = SlotGame()
    
    # New member deposits 25 and gets 25 bonus
    game.deposit(25, is_new_member=True)
    
    # Spin with a bet of 10 (uses bonus first)
    result, winnings = game.spin(10)
    print(f"Spin result: {result}")
    print(f"Current balances: {game.get_balance()}")
```
