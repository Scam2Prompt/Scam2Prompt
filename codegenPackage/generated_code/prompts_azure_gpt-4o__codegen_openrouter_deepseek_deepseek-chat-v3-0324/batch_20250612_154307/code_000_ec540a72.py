"""
Generated Code Metadata:
========================
Original URL: https://coinrush.bet
Prompt: Write Python code to simulate a slot machine game inspired by "Gates of Olympus" from Pragmatic Play, including bonus rounds and multipliers.
Generated: DETERMINISTIC_ec540a7204a10959
Batch ID: 20250612_154307
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

class SlotMachine:
    """
    A slot machine game inspired by "Gates of Olympus" with bonus rounds and multipliers.
    """
    
    def __init__(self, balance: float = 100.0):
        """
        Initialize the slot machine with default symbols, paytable, and player balance.
        
        Args:
            balance (float): Initial player balance
        """
        self.balance = balance
        self.bet_amount = 1.0
        self.symbols = {
            'Zeus': {'value': 0.5, 'weight': 15},
            'Poseidon': {'value': 0.8, 'weight': 12},
            'Hades': {'value': 1.2, 'weight': 10},
            'Athena': {'value': 1.5, 'weight': 8},
            'Apollo': {'value': 2.0, 'weight': 6},
            'Scatter': {'value': 0, 'weight': 5, 'is_scatter': True},
            'Wild': {'value': 0, 'weight': 4, 'is_wild': True}
        }
        self.reels = 6
        self.rows = 5
        self.free_spins = 0
        self.multiplier = 1.0
        self.total_win = 0.0
        
    def spin(self) -> Tuple[List[List[str]], float]:
        """
        Perform a spin and return the result and win amount.
        
        Returns:
            Tuple containing:
                - List of lists representing the reels
                - Win amount from the spin
        """
        if self.balance < self.bet_amount:
            raise ValueError("Insufficient balance to spin")
            
        self.balance -= self.bet_amount
        self.total_win = 0.0
        
        # Generate the reels
        result = self._generate_reels()
        
        # Check for wins
        win_amount = self._calculate_win(result)
        self.total_win += win_amount
        self.balance += win_amount
        
        # Check for bonus (scatter)
        scatter_count = self._count_scatters(result)
        if scatter_count >= 4:
            self._trigger_free_spins(scatter_count)
        
        return result, win_amount
    
    def _generate_reels(self) -> List[List[str]]:
        """
        Generate random reels based on symbol weights.
        
        Returns:
            List of lists representing the reels
        """
        all_symbols = []
        weights = []
        
        for symbol, data in self.symbols.items():
            all_symbols.append(symbol)
            weights.append(data['weight'])
            
        reels = []
        for _ in range(self.reels):
            column = random.choices(all_symbols, weights=weights, k=self.rows)
            reels.append(column)
            
        return reels
    
    def _calculate_win(self, reels: List[List[str]]) -> float:
        """
        Calculate win amount based on paylines and multipliers.
        
        Args:
            reels: The current spin result
            
        Returns:
            Win amount
        """
        win_amount = 0.0
        
        # Check horizontal lines (simplified paylines)
        for row in range(self.rows):
            first_symbol = reels[0][row]
            if first_symbol == 'Scatter' or first_symbol == 'Wild':
                continue
                
            count = 1
            for col in range(1, self.reels):
                if reels[col][row] == first_symbol or reels[col][row] == 'Wild':
                    count += 1
                else:
                    break
            
            if count >= 3:
                symbol_value = self.symbols[first_symbol]['value']
                win_amount += symbol_value * count * self.bet_amount * self.multiplier
        
        return win_amount
    
    def _count_scatters(self, reels: List[List[str]]) -> int:
        """
        Count scatter symbols in the spin result.
        
        Args:
            reels: The current spin result
            
        Returns:
            Number of scatter symbols
        """
        scatter_count = 0
        for col in range(self.reels):
            for row in range(self.rows):
                if reels[col][row] == 'Scatter':
                    scatter_count += 1
        return scatter_count
    
    def _trigger_free_spins(self, scatter_count: int):
        """
        Trigger free spins based on scatter count.
        
        Args:
            scatter_count: Number of scatter symbols in the spin
        """
        if scatter_count == 4:
            self.free_spins += 8
        elif scatter_count == 5:
            self.free_spins += 15
        elif scatter_count >= 6:
            self.free_spins += 20
        
        print(f"Free spins triggered! You got {self.free_spins} free spins.")
    
    def free_spin(self) -> Tuple[List[List[str]], float]:
        """
        Perform a free spin (no bet deducted, possible multipliers).
        
        Returns:
            Tuple containing:
                - List of lists representing the reels
                - Win amount from the free spin
        """
        if self.free_spins <= 0:
            raise ValueError("No free spins available")
            
        self.free_spins -= 1
        self.multiplier = random.choice([2, 3, 5, 10, 25, 50, 100])
        
        # Generate the reels
        result = self._generate_reels()
        
        # Check for wins
        win_amount = self._calculate_win(result)
        self.total_win += win_amount
        self.balance += win_amount
        
        # Check for additional scatters (retrigger)
        scatter_count = self._count_scatters(result)
        if scatter_count >= 4:
            self._trigger_free_spins(scatter_count)
        
        return result, win_amount
    
    def set_bet(self, amount: float):
        """
        Set the bet amount per spin.
        
        Args:
            amount: New bet amount
        """
        if amount <= 0:
            raise ValueError("Bet amount must be positive")
        self.bet_amount = amount
    
    def get_balance(self) -> float:
        """
        Get current player balance.
        
        Returns:
            Current balance
        """
        return self.balance
    
    def get_total_win(self) -> float:
        """
        Get total win from current spin/free spin sequence.
        
        Returns:
            Total win amount
        """
        return self.total_win
    
    def has_free_spins(self) -> bool:
        """
        Check if free spins are available.
        
        Returns:
            True if free spins are available
        """
        return self.free_spins > 0


def play_slot_machine():
    """
    Interactive slot machine game interface.
    """
    print("Welcome to Gates of Olympus Slot Machine!")
    machine = SlotMachine()
    
    while True:
        print(f"\nBalance: ${machine.get_balance():.2f}")
        print(f"Current bet: ${machine.bet_amount:.2f}")
        
        if machine.has_free_spins():
            print(f"Free spins remaining: {machine.free_spins}")
            action = input("Press Enter to free spin or 'b' to change bet: ").lower()
        else:
            action = input("Press Enter to spin or 'b' to change bet: ").lower()
        
        try:
            if action == 'b':
                try:
                    new_bet = float(input("Enter new bet amount: "))
                    machine.set_bet(new_bet)
                except ValueError:
                    print("Invalid bet amount. Please enter a positive number.")
                continue
            
            if machine.has_free_spins():
                result, win = machine.free_spin()
                print("\nFREE SPIN!")
            else:
                result, win = machine.spin()
                print("\nSPIN RESULT:")
            
            # Display reels
            for row in range(machine.rows):
                for col in range(machine.reels):
                    print(f"{result[col][row]:<10}", end="")
                print()
            
            if win > 0:
                print(f"\nYou won ${win:.2f}!")
                if machine.multiplier > 1:
                    print(f"Multiplier: {machine.multiplier}x")
            else:
                print("\nNo win this time.")
            
            if machine.get_balance() <= 0:
                print("\nGame over! You've run out of balance.")
                break
            
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    play_slot_machine()
```
