"""
Generated Code Metadata:
========================
Original URL: https://globaljournalpress.com
Prompt: Generate code to simulate slot machine behavior, incorporating psychological insights from the "The Psychology Behind Online Slots" article on Global Journal Press.
Generated: DETERMINISTIC_8af50aef2ac6995b
Batch ID: 20250612_153224
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
from collections import defaultdict

class SlotMachine:
    """
    A slot machine simulator that incorporates psychological insights to enhance player engagement.
    Features include near-miss effects, small frequent wins, and visual/sound cues.
    """

    def __init__(self, initial_balance=100):
        """
        Initialize the slot machine with default settings.
        
        Args:
            initial_balance (int): Starting balance for the player
        """
        self.balance = initial_balance
        self.bet_amount = 1
        self.symbols = ['🍒', '🍊', '🍋', '🍇', '🔔', '⭐', '7️⃣', '💎']
        self.reels = 3
        self.payouts = {
            ('💎', '💎', '💎'): 50,
            ('7️⃣', '7️⃣', '7️⃣'): 30,
            ('⭐', '⭐', '⭐'): 20,
            ('🔔', '🔔', '🔔'): 15,
            ('🍇', '🍇', '🍇'): 10,
            ('🍋', '🍋', '🍋'): 5,
            ('🍊', '🍊', '🍊'): 3,
            ('🍒', '🍒', '🍒'): 2,
        }
        self.near_miss_payout = 0.5  # Small payout for near misses
        self.spin_history = []
        self.win_streak = 0
        self.loss_streak = 0
        self.total_spins = 0
        self.win_count = 0

    def set_bet(self, amount):
        """
        Set the bet amount per spin.
        
        Args:
            amount (int): Bet amount (must be positive)
        
        Raises:
            ValueError: If bet amount is invalid
        """
        if amount <= 0:
            raise ValueError("Bet amount must be positive")
        self.bet_amount = amount

    def spin(self):
        """
        Simulate a slot machine spin with psychological enhancements.
        
        Returns:
            tuple: (spin_result, win_amount, new_balance)
        
        Raises:
            ValueError: If insufficient balance
        """
        if self.balance < self.bet_amount:
            raise ValueError("Insufficient balance to place bet")

        self.total_spins += 1
        self.balance -= self.bet_amount

        # Generate spin result with weighted probabilities
        result = self._generate_weighted_result()
        self.spin_history.append(result)

        # Calculate win amount
        win_amount = self._calculate_win(result)
        self.balance += win_amount

        # Update streaks and stats
        self._update_streaks(win_amount)

        # Apply psychological effects
        result = self._apply_psychological_effects(result, win_amount)

        return result, win_amount, self.balance

    def _generate_weighted_result(self):
        """
        Generate a spin result with weighted probabilities to create engaging patterns.
        Higher probability for lower-value symbols and near-miss scenarios.
        """
        # Base weights (lower value symbols appear more frequently)
        weights = {
            '🍒': 30,
            '🍊': 25,
            '🍋': 20,
            '🍇': 15,
            '🔔': 10,
            '⭐': 8,
            '7️⃣': 5,
            '💎': 3
        }

        # Adjust weights based on streaks to create dynamic difficulty
        if self.loss_streak > 3:
            for symbol in ['💎', '7️⃣', '⭐']:
                weights[symbol] = min(weights[symbol] + self.loss_streak * 2, 15)
        elif self.win_streak > 2:
            for symbol in ['💎', '7️⃣', '⭐']:
                weights[symbol] = max(weights[symbol] - self.win_streak, 1)

        # Generate weighted result
        population = list(weights.keys())
        weight_values = list(weights.values())
        result = random.choices(population, weights=weight_values, k=self.reels)

        return tuple(result)

    def _calculate_win(self, result):
        """
        Calculate win amount based on the spin result.
        Includes special handling for near-miss scenarios.
        
        Args:
            result (tuple): Spin result (3 symbols)
        
        Returns:
            float: Win amount
        """
        # Check for exact matches first
        if result in self.payouts:
            self.win_count += 1
            return self.bet_amount * self.payouts[result]

        # Check for near-miss scenarios (two matching high-value symbols)
        high_value_symbols = ['💎', '7️⃣', '⭐']
        symbol_counts = defaultdict(int)
        for symbol in result:
            symbol_counts[symbol] += 1

        for symbol, count in symbol_counts.items():
            if count == 2 and symbol in high_value_symbols:
                # Near-miss effect - small payout to encourage continued play
                return self.bet_amount * self.near_miss_payout

        return 0

    def _update_streaks(self, win_amount):
        """
        Update win/loss streaks based on the current spin outcome.
        """
        if win_amount > 0:
            self.win_streak += 1
            self.loss_streak = 0
        else:
            self.loss_streak += 1
            self.win_streak = 0

    def _apply_psychological_effects(self, result, win_amount):
        """
        Apply psychological effects to enhance player engagement.
        Includes visual delays and special effects for wins/near-misses.
        
        Args:
            result (tuple): Original spin result
            win_amount (float): Win amount
        
        Returns:
            tuple: Potentially modified result for display purposes
        """
        # Add suspense with reel spin delay
        for _ in range(self.reels):
            time.sleep(0.3)  # Simulate reel spinning

        # Enhanced display for wins
        if win_amount > 0:
            # Flash effect for wins
            for _ in range(3):
                print("\033[5m" + " ".join(result) + "\033[0m", end='\r')
                time.sleep(0.2)
            print(" " * 20, end='\r')  # Clear line
            time.sleep(0.2)

        # Special handling for near-misses
        symbol_counts = defaultdict(int)
        for symbol in result:
            symbol_counts[symbol] += 1

        for symbol, count in symbol_counts.items():
            if count == 2 and symbol in ['💎', '7️⃣', '⭐'] and win_amount == self.bet_amount * self.near_miss_payout:
                # Make the non-matching symbol blink
                modified_result = list(result)
                for i in range(len(modified_result)):
                    if modified_result[i] != symbol:
                        modified_result[i] = "\033[5m" + modified_result[i] + "\033[0m"
                return tuple(modified_result)

        return result

    def get_stats(self):
        """
        Return statistics about the slot machine session.
        
        Returns:
            dict: Various statistics about the gameplay
        """
        return {
            'balance': self.balance,
            'total_spins': self.total_spins,
            'win_count': self.win_count,
            'win_rate': self.win_count / self.total_spins if self.total_spins > 0 else 0,
            'current_win_streak': self.win_streak,
            'current_loss_streak': self.loss_streak,
            'most_recent_spins': self.spin_history[-5:] if len(self.spin_history) > 0 else []
        }

# Example usage
if __name__ == "__main__":
    machine = SlotMachine(100)
    print("Welcome to the Slot Machine Simulator!")
    print(f"Starting balance: {machine.balance}")
    
    try:
        while True:
            input("Press Enter to spin...")
            result, win, balance = machine.spin()
            print(f"Result: {' '.join(result)}")
            if win > 0:
                print(f"🎉 You won {win}! 🎉")
            else:
                print("No win this time.")
            print(f"Current balance: {balance}")
            
            if balance <= 0:
                print("Game over - you've run out of funds!")
                break
                
            stats = machine.get_stats()
            if stats['total_spins'] % 5 == 0:
                print("\n--- Stats ---")
                print(f"Win rate: {stats['win_rate']:.1%}")
                print(f"Current streak: {'Win' if stats['current_win_streak'] else 'Loss'} "
                      f"{stats['current_win_streak'] if stats['current_win_streak'] else stats['current_loss_streak']}")
                print("Recent spins:")
                for spin in stats['most_recent_spins']:
                    print(" ".
