"""
Generated Code Metadata:
========================
Original URL: https://namestajnovidom.com
Prompt: Write a program to simulate small-scale betting games with quick results, inspired by the 미니게임 사이트 features outlined on the 토토플레이 webpage.
Generated: DETERMINISTIC_6037b528141cf46b
Batch ID: 20250612_151334
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
from typing import Optional, Dict, List

class MiniGameSimulator:
    """
    A small-scale betting game simulator with quick results.
    Inspired by mini-game features found on betting sites.
    """
    
    def __init__(self, initial_balance: float = 1000.0):
        """
        Initialize the game simulator with an optional starting balance.
        
        Args:
            initial_balance: Starting balance for the player (default: 1000.0)
        """
        self.balance = initial_balance
        self.game_history = []
        
    def check_balance(self) -> float:
        """Return the current player balance."""
        return self.balance
    
    def add_funds(self, amount: float) -> bool:
        """
        Add funds to the player's balance.
        
        Args:
            amount: Amount to add (must be positive)
            
        Returns:
            bool: True if successful, False if amount is invalid
        """
        if amount <= 0:
            return False
        self.balance += amount
        return True
    
    def play_coin_flip(self, bet_amount: float, player_choice: str) -> Optional[Dict]:
        """
        Simulate a coin flip game.
        
        Args:
            bet_amount: Amount to bet (must be <= balance and > 0)
            player_choice: Either 'heads' or 'tails'
            
        Returns:
            dict: Game result containing outcome, win/loss, and new balance
            None: If bet is invalid
        """
        if bet_amount <= 0 or bet_amount > self.balance or player_choice.lower() not in ['heads', 'tails']:
            return None
            
        self.balance -= bet_amount
        outcome = random.choice(['heads', 'tails'])
        win = outcome == player_choice.lower()
        
        if win:
            winnings = bet_amount * 1.95  # 5% house edge
            self.balance += winnings
        else:
            winnings = 0
            
        result = {
            'game': 'coin_flip',
            'bet': bet_amount,
            'choice': player_choice,
            'outcome': outcome,
            'win': win,
            'winnings': winnings,
            'new_balance': self.balance,
            'timestamp': time.time()
        }
        
        self.game_history.append(result)
        return result
    
    def play_dice_roll(self, bet_amount: float, player_choice: int) -> Optional[Dict]:
        """
        Simulate a dice roll game (1-6).
        
        Args:
            bet_amount: Amount to bet (must be <= balance and > 0)
            player_choice: Number between 1 and 6
            
        Returns:
            dict: Game result containing outcome, win/loss, and new balance
            None: If bet is invalid
        """
        if bet_amount <= 0 or bet_amount > self.balance or player_choice not in range(1, 7):
            return None
            
        self.balance -= bet_amount
        outcome = random.randint(1, 6)
        win = outcome == player_choice
        
        if win:
            winnings = bet_amount * 5.7  # ~5.26% house edge
            self.balance += winnings
        else:
            winnings = 0
            
        result = {
            'game': 'dice_roll',
            'bet': bet_amount,
            'choice': player_choice,
            'outcome': outcome,
            'win': win,
            'winnings': winnings,
            'new_balance': self.balance,
            'timestamp': time.time()
        }
        
        self.game_history.append(result)
        return result
    
    def play_slot_machine(self, bet_amount: float) -> Optional[Dict]:
        """
        Simulate a simple 3-reel slot machine.
        
        Args:
            bet_amount: Amount to bet (must be <= balance and > 0)
            
        Returns:
            dict: Game result containing outcome, win/loss, and new balance
            None: If bet is invalid
        """
        if bet_amount <= 0 or bet_amount > self.balance:
            return None
            
        self.balance -= bet_amount
        symbols = ['🍒', '🍋', '🍊', '🍇', '🔔', '7️⃣']
        reels = [random.choice(symbols) for _ in range(3)]
        
        # Count unique symbols
        unique_symbols = len(set(reels))
        
        if unique_symbols == 1:  # All three same
            multiplier = 10
        elif reels.count('7️⃣') == 2:  # Two 7s
            multiplier = 5
        elif unique_symbols == 2:  # Two same
            multiplier = 2
        else:
            multiplier = 0
            
        winnings = bet_amount * multiplier
        self.balance += winnings
        
        result = {
            'game': 'slot_machine',
            'bet': bet_amount,
            'outcome': ' '.join(reels),
            'win': winnings > 0,
            'winnings': winnings,
            'new_balance': self.balance,
            'timestamp': time.time()
        }
        
        self.game_history.append(result)
        return result
    
    def get_game_history(self, limit: int = 10) -> List[Dict]:
        """
        Retrieve game history, most recent first.
        
        Args:
            limit: Maximum number of games to return (default: 10)
            
        Returns:
            list: Game history records
        """
        return sorted(self.game_history, key=lambda x: x['timestamp'], reverse=True)[:limit]
    
    def reset(self, new_balance: float = 1000.0) -> None:
        """
        Reset the game simulator with a new balance.
        
        Args:
            new_balance: Starting balance for the player (default: 1000.0)
        """
        self.balance = new_balance
        self.game_history = []

# Example usage
if __name__ == "__main__":
    game = MiniGameSimulator()
    
    # Play some games
    print("Starting balance:", game.check_balance())
    
    coin_result = game.play_coin_flip(100, 'heads')
    print("Coin flip result:", coin_result)
    
    dice_result = game.play_dice_roll(50, 3)
    print("Dice roll result:", dice_result)
    
    slot_result = game.play_slot_machine(200)
    print("Slot machine result:", slot_result)
    
    print("Current balance:", game.check_balance())
    print("Last 5 games:", game.get_game_history(5))
```
