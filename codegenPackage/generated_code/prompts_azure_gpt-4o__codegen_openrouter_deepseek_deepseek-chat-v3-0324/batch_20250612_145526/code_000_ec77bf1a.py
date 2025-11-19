"""
Generated Code Metadata:
========================
Original URL: https://aspjj.com
Prompt: "Write a Python script to simulate a slot machine game with features like auto-play and adjustable bet amounts, inspired by the mechanics of สล็อตเว็บตรง."
Generated: DETERMINISTIC_ec77bf1af7d1ba3f
Batch ID: 20250612_145526
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
import sys
from typing import List, Tuple, Dict

class SlotMachine:
    """
    A class to simulate a slot machine game with auto-play and adjustable bet features.
    """
    
    def __init__(self, initial_balance: float = 1000.00):
        """
        Initialize the slot machine with default symbols and paytable.
        
        Args:
            initial_balance (float): Starting balance for the player.
        """
        self.balance = initial_balance
        self.bet_amount = 10.00
        self.auto_play = False
        self.auto_play_spins = 10
        
        # Slot symbols and their weights (higher weight = less frequent)
        self.symbols: List[str] = ['🍒', '🍋', '🍊', '🍇', '🔔', '7️⃣']
        self.weights: List[int] = [30, 25, 20, 15, 8, 2]
        
        # Paytable: symbol -> [count: payout multiplier]
        self.paytable: Dict[str, List[Tuple[int, float]]] = {
            '🍒': [(3, 2.0), (2, 0.5)],
            '🍋': [(3, 3.0), (2, 1.0)],
            '🍊': [(3, 4.0), (2, 1.5)],
            '🍇': [(3, 5.0), (2, 2.0)],
            '🔔': [(3, 10.0), (2, 3.0)],
            '7️⃣': [(3, 20.0), (2, 5.0)]
        }
        
    def spin(self) -> Tuple[List[str], float]:
        """
        Simulate a single spin of the slot machine.
        
        Returns:
            Tuple[List[str], float]: The spin result and the win amount.
        """
        if self.balance < self.bet_amount:
            raise ValueError("Insufficient balance to place bet.")
        
        self.balance -= self.bet_amount
        result = random.choices(self.symbols, weights=self.weights, k=3)
        win_amount = self.calculate_win(result)
        self.balance += win_amount
        
        return result, win_amount
    
    def calculate_win(self, result: List[str]) -> float:
        """
        Calculate the win amount based on the spin result and paytable.
        
        Args:
            result (List[str]): The spin result (3 symbols).
            
        Returns:
            float: The win amount.
        """
        win_amount = 0.0
        
        # Count occurrences of each symbol
        symbol_counts = {}
        for symbol in result:
            symbol_counts[symbol] = symbol_counts.get(symbol, 0) + 1
        
        # Check paytable for winning combinations
        for symbol, count in symbol_counts.items():
            for combo in self.paytable[symbol]:
                if count >= combo[0]:
                    win_amount = max(win_amount, self.bet_amount * combo[1])
                    break
        
        return win_amount
    
    def auto_play_mode(self) -> None:
        """
        Run the slot machine in auto-play mode for a set number of spins.
        """
        if self.balance < self.bet_amount * self.auto_play_spins:
            print("Insufficient balance for auto-play spins.")
            return
        
        print(f"\nStarting auto-play for {self.auto_play_spins} spins...\n")
        for i in range(1, self.auto_play_spins + 1):
            result, win_amount = self.spin()
            print(f"Spin {i}: {' '.join(result)} | Win: {win_amount:.2f} | Balance: {self.balance:.2f}")
            time.sleep(0.5)
            
            if self.balance < self.bet_amount:
                print("\nBalance too low to continue auto-play.")
                break
    
    def change_bet(self, new_bet: float) -> None:
        """
        Change the current bet amount.
        
        Args:
            new_bet (float): The new bet amount.
        """
        if new_bet <= 0:
            raise ValueError("Bet amount must be positive.")
        self.bet_amount = new_bet
    
    def change_auto_play_spins(self, spins: int) -> None:
        """
        Change the number of auto-play spins.
        
        Args:
            spins (int): The new number of spins.
        """
        if spins <= 0:
            raise ValueError("Number of spins must be positive.")
        self.auto_play_spins = spins
    
    def display_menu(self) -> None:
        """
        Display the main menu of the slot machine.
        """
        print("\n" + "="*40)
        print(f"SLOT MACHINE | Balance: {self.balance:.2f} | Bet: {self.bet_amount:.2f}")
        print("="*40)
        print("1. Spin")
        print("2. Auto-play")
        print("3. Change bet amount")
        print("4. Change auto-play spins")
        print("5. Quit")
        print("="*40)
    
    def run(self) -> None:
        """
        Run the slot machine game loop.
        """
        print("Welcome to the Slot Machine!")
        print(f"Starting balance: {self.balance:.2f}")
        
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-5): ")
            
            try:
                if choice == "1":
                    result, win_amount = self.spin()
                    print(f"\nSpin result: {' '.join(result)}")
                    print(f"You {'won' if win_amount > 0 else 'lost'} {abs(win_amount):.2f}!")
                    print(f"Current balance: {self.balance:.2f}\n")
                elif choice == "2":
                    self.auto_play_mode()
                elif choice == "3":
                    new_bet = float(input("Enter new bet amount: "))
                    self.change_bet(new_bet)
                    print(f"Bet amount changed to {self.bet_amount:.2f}")
                elif choice == "4":
                    spins = int(input("Enter number of auto-play spins: "))
                    self.change_auto_play_spins(spins)
                    print(f"Auto-play spins changed to {self.auto_play_spins}")
                elif choice == "5":
                    print(f"\nThanks for playing! Final balance: {self.balance:.2f}")
                    sys.exit()
                else:
                    print("Invalid choice. Please try again.")
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    slot_machine = SlotMachine()
    slot_machine.run()
```
