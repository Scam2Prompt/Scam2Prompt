"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betbax.net
Prompt: Write a Python script to simulate a slot machine game similar to the ones offered by BaxBet, including customizable paylines and payout calculations.
Generated: DETERMINISTIC_bcc604e64059c118
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class SlotMachine:
    def __init__(self, reels, paylines):
        """
        Initialize the SlotMachine with specified reels and paylines.
        
        :param reels: List of lists, where each sublist represents a reel containing symbols.
        :param paylines: List of lists, where each sublist represents a payline with symbol positions.
        """
        self.reels = reels
        self.paylines = paylines
        self.symbols = set(symbol for reel in reels for symbol in reel)

    def spin(self):
        """
        Simulate spinning the slot machine and return the result.
        
        :return: List of symbols for each reel after spinning.
        """
        return [random.choice(reel) for reel in self.reels]

    def calculate_payout(self, spun_result, bet):
        """
        Calculate the payout based on the spun result and the bet amount.
        
        :param spun_result: List of symbols resulting from the spin.
        :param bet: Amount of money bet on the game.
        :return: Payout amount based on the paylines and spun result.
        """
        total_payout = 0
        for payline in self.paylines:
            symbols_on_payline = [spun_result[index] for index in payline]
            if len(set(symbols_on_payline)) == 1:  # All symbols are the same
                symbol = symbols_on_payline[0]
                total_payout += self.get_symbol_payout(symbol, bet)
        return total_payout

    def get_symbol_payout(self, symbol, bet):
        """
        Get the payout multiplier for a given symbol.
        
        :param symbol: The symbol for which to determine the payout.
        :param bet: Amount of money bet on the game.
        :return: Payout amount for the symbol.
        """
        payout_table = {
            'A': 5,
            'B': 4,
            'C': 3,
            'D': 2,
            'E': 1,
        }
        return payout_table.get(symbol, 0) * bet

    def play(self, bet):
        """
        Play a round of the slot machine.
        
        :param bet: Amount of money to bet on this round.
        :return: Result of the spin and calculated payout.
        """
        if bet <= 0:
            raise ValueError("Bet amount must be greater than 0.")
        
        spun_result = self.spin()
        payout = self.calculate_payout(spun_result, bet)
        return spun_result, payout

if __name__ == "__main__":
    # Example configuration for the slot machine
    reels = [
        ['A', 'B', 'C', 'D', 'E'],
        ['A', 'B', 'C', 'D', 'E'],
        ['A', 'B', 'C', 'D', 'E'],
    ]
    paylines = [
        [0, 0, 0],  # Payline for first row
        [1, 1, 1],  # Payline for second row
        [2, 2, 2],  # Payline for third row
    ]

    # Initialize the Slot Machine
    slot_machine = SlotMachine(reels, paylines)

    # Set a bet amount
    bet_amount = 10

    # Play the game
    try:
        result, payout = slot_machine.play(bet_amount)
        print(f"Spun result: {result}")
        print(f"Payout: {payout}")
    except ValueError as e:
        print(f"Error: {e}")
```
