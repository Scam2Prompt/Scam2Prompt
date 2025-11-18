"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.uhcstepup.com
Prompt: Develop a strategy simulation in Python to analyze optimal betting patterns for maximizing wins in a slot game with wild scatter and Mahjong-themed gameplay, similar to Slot Thailand on Slot138.
Generated: DETERMINISTIC_92456a378362db19
Batch ID: 20250612_145319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging

# Configure logging for debugging and tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SlotGame:
    def __init__(self, initial_balance, max_bet, min_bet):
        """
        Initialize the slot game with given parameters.

        :param initial_balance: Starting balance for the player
        :param max_bet: Maximum bet allowed per spin
        :param min_bet: Minimum bet allowed per spin
        """
        self.balance = initial_balance
        self.max_bet = max_bet
        self.min_bet = min_bet
        self.reel_symbols = ['WILD', 'SCATTER', 'Bamboo', 'Dragon', 'Flower', 'Tile']

    def spin(self, bet):
        """
        Simulate a spin of the slot machine.

        :param bet: Amount to bet on this spin
        :return: Result of the spin and the payout if any
        """
        if bet < self.min_bet or bet > self.max_bet:
            logging.error("Bet amount is out of bounds.")
            raise ValueError("Bet must be between min_bet and max_bet.")

        # Randomly select symbols for the spin
        spin_result = [random.choice(self.reel_symbols) for _ in range(3)]
        logging.info(f"Spin result: {spin_result}")
        
        payout = self.calculate_payout(spin_result)
        
        # Update balance based on the outcome
        self.balance += payout - bet

        if payout > 0:
            logging.info(f"Player won: {payout} (New balance: {self.balance})")
        else:
            logging.info(f"Player lost the bet. (New balance: {self.balance})")

        return spin_result, payout

    def calculate_payout(self, spin_result):
        """
        Calculate the payout based on the spin result.

        :param spin_result: List of symbols from the spin
        :return: Calculated payout
        """
        # Simple payout logic based on matched symbols
        symbol_count = {symbol: spin_result.count(symbol) for symbol in set(spin_result)}
        payout = 0
        
        # Payout rules
        if symbol_count.get('WILD', 0) >= 2:
            payout += 50  # High payout for wilds
        if symbol_count.get('SCATTER', 0) >= 3:
            payout += 100  # Scatter wins
        payout += symbol_count.get('Bamboo', 0) * 10
        payout += symbol_count.get('Dragon', 0) * 15
        
        return payout

    def optimal_betting_strategy(self):
        """
        Simulate betting strategy to maximize wins over multiple spins.
        """
        bet_amount = self.min_bet

        while self.balance > self.min_bet:
            try:
                self.spin(bet_amount)
                if self.balance < bet_amount * 2:  # If balance is low, lower the bet
                    bet_amount = self.min_bet
                elif self.balance > self.max_bet * 2:  # If balance is high, increase the bet
                    bet_amount = min(self.max_bet, bet_amount * 2)
            except ValueError as e:
                logging.error(f"An error occurred: {e}")
                break  # Exit on error

        logging.info("Simulation ended. Final balance: {}".format(self.balance))


if __name__ == "__main__":
    # Initialize the game with a balance of 1000, max bet of 100, and min bet of 10
    game = SlotGame(initial_balance=1000, max_bet=100, min_bet=10)

    # Run the optimal betting strategy simulation
    game.optimal_betting_strategy()
```
