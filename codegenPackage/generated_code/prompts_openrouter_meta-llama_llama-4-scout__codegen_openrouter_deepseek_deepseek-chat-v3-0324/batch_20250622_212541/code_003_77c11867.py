"""
Generated Code Metadata:
========================
Original URL: https://aspjj.com
Prompt: Develop a basic strategy for maximizing winnings on สล็อตเว็บตรง, considering the minimum bet requirement and optimal bet adjustment techniques.
Generated: DETERMINISTIC_77c11867197aef95
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
import math

class SlotMachineStrategy:
    """
    A basic strategy for maximizing winnings on a direct web slot machine.
    Implements minimum bet requirement and optimal bet adjustment techniques.
    """
    
    def __init__(self, initial_balance=1000, min_bet=10, max_bet=1000):
        """
        Initialize the slot machine strategy.
        
        Args:
            initial_balance (float): Starting balance for the player
            min_bet (float): Minimum bet allowed by the slot machine
            max_bet (float): Maximum bet allowed by the slot machine
        """
        self.balance = initial_balance
        self.min_bet = min_bet
        self.max_bet = max_bet
        self.current_bet = min_bet
        self.win_streak = 0
        self.loss_streak = 0
        self.max_win_streak = 0
        self.max_loss_streak = 0
        self.total_spins = 0
        self.total_wins = 0
        
    def spin(self):
        """
        Simulate a slot machine spin with a 40% chance to win.
        Adjusts bet based on streaks and updates statistics.
        
        Returns:
            bool: True if win, False if loss
        """
        if self.balance < self.current_bet:
            raise ValueError("Insufficient balance for current bet")
            
        self.total_spins += 1
        win = random.random() <= 0.4  # 40% win probability
        
        if win:
            self.balance += self.current_bet
            self.win_streak += 1
            self.loss_streak = 0
            self.total_wins += 1
            self.max_win_streak = max(self.max_win_streak, self.win_streak)
            self._adjust_bet_after_win()
        else:
            self.balance -= self.current_bet
            self.loss_streak += 1
            self.win_streak = 0
            self.max_loss_streak = max(self.max_loss_streak, self.loss_streak)
            self._adjust_bet_after_loss()
            
        return win
    
    def _adjust_bet_after_win(self):
        """Increase bet moderately after wins (Martingale-like but safer)"""
        if self.win_streak >= 2:
            self.current_bet = min(self.current_bet * 1.5, self.max_bet)
        else:
            self.current_bet = self.min_bet
    
    def _adjust_bet_after_loss(self):
        """Decrease bet after losses to preserve capital"""
        if self.loss_streak >= 2:
            self.current_bet = max(self.current_bet * 0.5, self.min_bet)
        else:
            self.current_bet = self.min_bet
    
    def get_stats(self):
        """Return current statistics"""
        return {
            'balance': self.balance,
            'current_bet': self.current_bet,
            'win_streak': self.win_streak,
            'loss_streak': self.loss_streak,
            'max_win_streak': self.max_win_streak,
            'max_loss_streak': self.max_loss_streak,
            'total_spins': self.total_spins,
            'total_wins': self.total_wins,
            'win_rate': self.total_wins / self.total_spins if self.total_spins > 0 else 0
        }

def simulate_session(initial_balance=1000, spins=100):
    """
    Simulate a slot machine session with the strategy.
    
    Args:
        initial_balance (float): Starting balance
        spins (int): Number of spins to simulate
        
    Returns:
        dict: Final statistics after simulation
    """
    strategy = SlotMachineStrategy(initial_balance=initial_balance)
    for _ in range(spins):
        try:
            strategy.spin()
        except ValueError as e:
            print(f"Session ended early: {e}")
            break
    return strategy.get_stats()

# Example usage
if __name__ == "__main__":
    results = simulate_session(initial_balance=1000, spins=100)
    print("Simulation Results:")
    for key, value in results.items():
        print(f"{key.replace('_', ' ').title()}: {value:.2f}" if isinstance(value, float) else f"{key.replace('_', ' ').title()}: {value}")
```
