"""
Generated Code Metadata:
========================
Original URL: https://betbax.net
Prompt: Write a Python script to simulate a slot machine game similar to the ones offered by BaxBet, including customizable paylines and payout calculations.
Generated: DETERMINISTIC_bcc604e64059c118
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class SlotMachine:
    def __init__(self, symbols, paylines):
        """
        Initializes the SlotMachine with given symbols and paylines.

        :param symbols: List of symbols available on the slot machine.
        :param paylines: List of paylines, where each payline is a list of positions.
        """
        self.symbols = symbols
        self.paylines = paylines

    def spin(self):
        """
        Simulates a spin of the slot machine.

        :return: A list of lists representing the result of the spin.
        """
        return [[random.choice(self.symbols) for _ in range(3)] for _ in range(3)]

    def calculate_payout(self, spin_result):
        """
        Calculates the payout based on the spin result and defined paylines.

        :param spin_result: The result of the spin as a list of lists.
        :return: Total payout based on the paylines.
        """
        payout = 0
        for payline in self.paylines:
            symbols_in_payline = [spin_result[row][col] for row, col in payline]
            if len(set(symbols_in_payline)) == 1:  # All symbols in the payline are the same
                payout += self.get_symbol_value(symbols_in_payline[0])
        return payout

    def get_symbol_value(self, symbol):
        """
        Returns the payout value for a given symbol.

        :param symbol: The symbol for which to get the payout value.
        :return: Payout value for the symbol.
        """
        # Define payout values for each symbol
        payout_values = {
            'A': 10,
            'B': 20,
            'C': 30,
            'D': 40,
            'E': 50
        }
        return payout_values.get(symbol, 0)

def main():
    # Define symbols and paylines
    symbols = ['A', 'B', 'C', 'D', 'E']
    paylines = [
        [(0, 0), (1, 0), (2, 0)],  # Vertical line 1
        [(0, 1), (1, 1), (2, 1)],  # Vertical line 2
        [(0, 2), (1, 2), (2, 2)],  # Vertical line 3
        [(0, 0), (1, 1), (2, 2)],  # Diagonal line
        [(0, 2), (1, 1), (2, 0)]   # Reverse diagonal line
    ]

    # Create a SlotMachine instance
    slot_machine = SlotMachine(symbols, paylines)

    # Simulate a spin
    spin_result = slot_machine.spin()
    print("Spin Result:")
    for row in spin_result:
        print(row)

    # Calculate and display payout
    payout = slot_machine.calculate_payout(spin_result)
    print(f"Payout: {payout}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
