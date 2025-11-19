"""
Generated Code Metadata:
========================
Original URL: https://mywanderloop.com
Prompt: Develop a slot machine simulation in Python that incorporates the bonus and promotional features of "Gates of Olympus Slot," as described on myWanderLoop.
Generated: DETERMINISTIC_04c0a7d169ccee3c
Batch ID: 20250612_153246
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

class GatesOfOlympusSlot:
    """
    A simulation of the Gates of Olympus slot machine with bonus and promotional features.
    """
    
    def __init__(self, balance: float = 100.00):
        """
        Initialize the slot machine with a starting balance.
        
        Args:
            balance (float): Initial player balance. Defaults to 100.00.
        """
        self.balance = balance
        self.bet_amount = 1.00
        self.symbols = ['Zeus', 'Poseidon', 'Hades', 'Athena', 'Apollo', 'Hermes', 'Ares', 'Dionysus']
        self.payouts = {
            'Zeus': [0, 0.2, 0.5, 2, 5, 10],
            'Poseidon': [0, 0.2, 0.5, 1.5, 4, 8],
            'Hades': [0, 0.1, 0.4, 1, 3, 6],
            'Athena': [0, 0.1, 0.3, 0.8, 2.5, 5],
            'Apollo': [0, 0.05, 0.2, 0.6, 2, 4],
            'Hermes': [0, 0.05, 0.2, 0.5, 1.5, 3],
            'Ares': [0, 0.05, 0.1, 0.4, 1, 2],
            'Dionysus': [0, 0.05, 0.1, 0.3, 0.8, 1.5]
        }
        self.multipliers = [1, 2, 3, 5, 10, 20, 50, 100]
        self.free_spins_active = False
        self.free_spins_remaining = 0
        self.current_multiplier = 1
    
    def set_bet(self, amount: float) -> bool:
        """
        Set the bet amount per spin.
        
        Args:
            amount (float): Bet amount.
            
        Returns:
            bool: True if bet is set successfully, False otherwise.
        """
        if amount <= 0:
            print("Bet amount must be positive.")
            return False
        if amount > self.balance:
            print("Insufficient balance for this bet.")
            return False
        self.bet_amount = amount
        return True
    
    def spin(self) -> Tuple[List[List[str]], float, bool]:
        """
        Simulate a spin of the slot machine.
        
        Returns:
            Tuple[List[List[str]], float, bool]: 
                - The reels result (5x6 grid)
                - The win amount
                - Whether a bonus feature was triggered
        """
        if self.balance < self.bet_amount:
            print("Insufficient balance to spin.")
            return [], 0.0, False
        
        if not self.free_spins_active:
            self.balance -= self.bet_amount
        
        # Generate the reels (5 columns, 6 rows each)
        reels = [[random.choice(self.symbols) for _ in range(6)] for _ in range(5)]
        
        # Calculate wins
        win_amount = self.calculate_win(reels)
        
        # Check for bonus features
        bonus_triggered = self.check_bonus_features(reels)
        
        if not self.free_spins_active:
            self.balance += win_amount
        
        return reels, win_amount, bonus_triggered
    
    def calculate_win(self, reels: List[List[str]]) -> float:
        """
        Calculate the win amount based on the reels.
        
        Args:
            reels (List[List[str]]): The 5x6 grid of symbols.
            
        Returns:
            float: The win amount.
        """
        win_amount = 0.0
        
        # Check for winning combinations (8 or more matching symbols)
        symbol_counts = {}
        for col in reels:
            for symbol in col:
                symbol_counts[symbol] = symbol_counts.get(symbol, 0) + 1
        
        for symbol, count in symbol_counts.items():
            if count >= 8:
                payout_index = min(count - 8, 5)  # Max payout at 13+ symbols
                win_amount += self.payouts[symbol][payout_index] * self.bet_amount * self.current_multiplier
        
        return win_amount
    
    def check_bonus_features(self, reels: List[List[str]]) -> bool:
        """
        Check if any bonus features are triggered.
        
        Args:
            reels (List[List[str]]): The 5x6 grid of symbols.
            
        Returns:
            bool: True if a bonus feature was triggered, False otherwise.
        """
        # Check for scatter symbols (Zeus) to trigger free spins
        scatter_count = sum(col.count('Zeus') for col in reels)
        
        if scatter_count >= 4:
            self.free_spins_remaining = scatter_count * 5  # 5 free spins per scatter
            self.free_spins_active = True
            self.current_multiplier = random.choice(self.multipliers)
            print(f"Free spins activated! {self.free_spins_remaining} spins remaining with x{self.current_multiplier} multiplier.")
            return True
        
        # Handle free spins countdown
        if self.free_spins_active:
            self.free_spins_remaining -= 1
            if self.free_spins_remaining <= 0:
                self.free_spins_active = False
                self.current_multiplier = 1
                print("Free spins ended.")
        
        return False
    
    def display_reels(self, reels: List[List[str]]) -> None:
        """
        Display the reels in a readable format.
        
        Args:
            reels (List[List[str]]): The 5x6 grid of symbols.
        """
        for row in range(6):
            print(" | ".join(reels[col][row] for col in range(5)))
    
    def play(self) -> None:
        """
        Main game loop for the slot machine.
        """
        print("Welcome to Gates of Olympus Slot!")
        print(f"Starting balance: ${self.balance:.2f}")
        
        while self.balance > 0:
            print("\n" + "="*40)
            print(f"Current balance: ${self.balance:.2f}")
            print(f"Current bet: ${self.bet_amount:.2f}")
            if self.free_spins_active:
                print(f"Free spins remaining: {self.free_spins_remaining} (Multiplier: x{self.current_multiplier})")
            
            action = input("Enter 'spin' to play, 'bet' to change bet, or 'quit' to exit: ").strip().lower()
            
            if action == 'quit':
                print(f"Thanks for playing! Final balance: ${self.balance:.2f}")
                break
            elif action == 'bet':
                try:
                    new_bet = float(input(f"Enter new bet amount (current: ${self.bet_amount:.2f}): "))
                    if not self.set_bet(new_bet):
                        continue
                except ValueError:
                    print("Invalid bet amount. Please enter a number.")
                    continue
            elif action == 'spin':
                reels, win, bonus = self.spin()
                print("\nSpinning...")
                time.sleep(1)
                self.display_reels(reels)
                if win > 0:
                    print(f"\nYou won ${win:.2f}!")
                if bonus:
                    time.sleep(1)  # Pause for dramatic effect
            else:
                print("Invalid command. Please try again.")
        
        if self.balance <= 0:
            print("Game over! Your balance has reached zero.")

# Example usage
if __name__ == "__main__":
    slot = GatesOfOlympusSlot()
    slot.play()
```
