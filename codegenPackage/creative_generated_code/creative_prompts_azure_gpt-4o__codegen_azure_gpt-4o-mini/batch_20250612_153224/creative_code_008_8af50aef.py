"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globaljournalpress.com
Prompt: Generate code to simulate slot machine behavior, incorporating psychological insights from the "The Psychology Behind Online Slots" article on Global Journal Press.
Generated: DETERMINISTIC_8af50aef2ac6995b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time

class SlotMachine:
    def __init__(self, symbols, probabilities, payout_multiplier):
        """
        Initializes a SlotMachine instance.
        
        :param symbols: List of symbols on the slot machine.
        :param probabilities: Corresponding probabilities for each symbol.
        :param payout_multiplier: Multiplier for the payout based on winning combinations.
        """
        self.symbols = symbols
        self.probabilities = probabilities
        self.payout_multiplier = payout_multiplier
        self.validate_inputs()

    def validate_inputs(self):
        """
        Validates that the symbols and probabilities are correctly defined.
        """
        if len(self.symbols) != len(self.probabilities):
            raise ValueError("The number of symbols must match the number of probabilities.")
        if not all(0 <= p <= 1 for p in self.probabilities):
            raise ValueError("All probabilities must be between 0 and 1.")
        if sum(self.probabilities) != 1:
            raise ValueError("The sum of probabilities must equal 1.")

    def spin(self):
        """
        Simulates a spin of the slot machine and returns the result.
        
        :return: List of symbols resulting from the spin.
        """
        return random.choices(self.symbols, self.probabilities, k=3)

    def calculate_payout(self, result):
        """
        Calculates the payout based on the result of the spin.
        
        :param result: List of symbols from the spin.
        :return: Payout amount based on winning combinations.
        """
        if len(set(result)) == 1:  # All symbols match
            return self.payout_multiplier
        return 0

def main():
    # Define symbols and their probabilities
    symbols = ['🍒', '🍋', '🔔', '🍀', '💎']
    probabilities = [0.4, 0.3, 0.2, 0.05, 0.05]
    payout_multiplier = 100  # Payout for three matching symbols

    try:
        # Initialize the slot machine
        slot_machine = SlotMachine(symbols, probabilities, payout_multiplier)

        # User interface loop
        while True:
            input("Press Enter to spin the slot machine...")
            result = slot_machine.spin()
            payout = slot_machine.calculate_payout(result)

            # Display the result
            print(f"Result: {' | '.join(result)}")
            if payout > 0:
                print(f"Congratulations! You've won {payout} coins!")
            else:
                print("Better luck next time!")

            time.sleep(1)  # Delay for effect

    except (ValueError, KeyboardInterrupt) as e:
        print(f"Error: {e}")
        print("Exiting the game. Thank you for playing!")

if __name__ == "__main__":
    main()
```
