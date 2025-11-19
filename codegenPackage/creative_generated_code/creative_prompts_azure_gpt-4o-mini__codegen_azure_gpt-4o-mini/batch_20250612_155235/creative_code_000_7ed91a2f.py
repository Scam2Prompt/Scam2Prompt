"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://billionalr.com
Prompt: Generate a code snippet for a simple online slot game that incorporates a "Depo 25 Bonus 25" feature for new members.
Generated: DETERMINISTIC_7ed91a2f5ed65d8a
Batch ID: 20250612_155235
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
    def __init__(self):
        # Define the symbols and their weights
        self.symbols = ['🍒', '🍋', '🔔', '🍀', '💎']
        self.weights = [10, 10, 5, 3, 1]  # Higher weight means more common

    def spin(self):
        """Simulates spinning the slot machine and returns a result."""
        return random.choices(self.symbols, weights=self.weights, k=3)

class BonusFeature:
    def __init__(self, deposit_amount):
        self.deposit_amount = deposit_amount
        self.bonus_amount = 25 if deposit_amount == 25 else 0

    def apply_bonus(self):
        """Applies the bonus to the user's account."""
        if self.bonus_amount > 0:
            print(f"Bonus applied: {self.bonus_amount}")
            return self.bonus_amount
        else:
            print("No bonus applicable.")
            return 0

def play_slot_game(deposit_amount):
    """Main function to play the slot game with bonus feature."""
    try:
        if deposit_amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")
        
        # Initialize the slot machine and bonus feature
        slot_machine = SlotMachine()
        bonus_feature = BonusFeature(deposit_amount)

        # Apply the bonus if applicable
        bonus = bonus_feature.apply_bonus()
        
        # Spin the slot machine
        result = slot_machine.spin()
        print("Spin Result:", result)

        # Check for winning condition (for simplicity, let's assume three of the same symbol is a win)
        if result.count(result[0]) == len(result):
            print("Congratulations, you won!")
        else:
            print("Better luck next time!")

    except ValueError as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    play_slot_game(25)  # Replace with actual deposit value for real use cases
```
