"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jadobet.org
Prompt: Write a Python script to simulate a simple slot machine game, including customizable payout ratios and bonus features similar to those described on BaxBet.
Generated: DETERMINISTIC_f08c4af1d39daf8f
Batch ID: 20250612_154344
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
    def __init__(self, symbols, payout_ratios, bonus_symbol=None):
        """
        Initialize the slot machine with the given symbols and payout ratios.
        
        :param symbols: List of symbols to use in the slot machine
        :param payout_ratios: Dictionary with payout ratios for each symbol
        :param bonus_symbol: Symbol that triggers a bonus feature (optional)
        """
        self.symbols = symbols
        self.payout_ratios = payout_ratios
        self.bonus_symbol = bonus_symbol

    def spin(self):
        """
        Simulate a spin of the slot machine.
        
        :return: List of symbols resulting from the spin
        """
        return [random.choice(self.symbols) for _ in range(3)]

    def calculate_payout(self, spin_result):
        """
        Calculate the payout based on the spin result.

        :param spin_result: List of symbols from the spin
        :return: Payout amount based on the result
        """
        payout = 0
        unique_symbols = set(spin_result)

        # Check for payouts based on the symbols
        for symbol in unique_symbols:
            count = spin_result.count(symbol)
            if count > 1 and symbol in self.payout_ratios:
                payout += self.payout_ratios[symbol] * count

        # Check for bonus feature
        if self.bonus_symbol and spin_result.count(self.bonus_symbol) >= 2:
            payout += self.trigger_bonus()

        return payout

    def trigger_bonus(self):
        """
        Trigger the bonus feature.

        :return: Bonus payout amount
        """
        bonus_payout = 10  # Fixed bonus payout for simplicity
        print("Bonus feature activated! You win an extra payout of:", bonus_payout)
        return bonus_payout

def play_slot_machine():
    """
    Main function to play the slot machine.
    """
    # Define symbols and payout ratios
    symbols = ['A', 'B', 'C', 'D', 'E']
    payout_ratios = {'A': 2, 'B': 3, 'C': 5}

    # Create a SlotMachine instance
    slot_machine = SlotMachine(symbols, payout_ratios, bonus_symbol='A')

    while True:
        # Spin the slot machine
        input("Press Enter to spin the slot machine...")
        spin_result = slot_machine.spin()
        print("Spin result:", spin_result)

        # Calculate and display payout
        payout = slot_machine.calculate_payout(spin_result)
        print("Your payout is:", payout, "credits")

        # Check if the user wants to play again
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thank you for playing!")
            break

if __name__ == '__main__':
    try:
        play_slot_machine()
    except Exception as e:
        print("An error occurred:", str(e))
```
