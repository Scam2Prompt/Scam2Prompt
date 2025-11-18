"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grampreico.com
Prompt: Write Python code to simulate a slot machine game with high RTP values and customizable themes, inspired by the features of nagoya168 online.
Generated: DETERMINISTIC_68a9ddcc1771272f
Batch ID: 20250612_151412
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
    def __init__(self, symbols, theme_name, rtp):
        """
        Initialize the SlotMachine with symbols, theme name, and RTP (Return to Player) value.
        
        :param symbols: List of symbols used in the slot machine.
        :param theme_name: Name of the slot machine theme.
        :param rtp: Return to Player percentage (float value between 0 and 1).
        """
        if not (0 < rtp <= 1):
            raise ValueError("RTP must be a float between 0 and 1.")
        
        self.symbols = symbols
        self.theme_name = theme_name
        self.rtp = rtp
        self.reel_spin_results = []

    def spin(self, num_reels=3):
        """
        Spin the slot machine and return the result.
        
        :param num_reels: Number of reels to spin.
        :return: List of symbols resulting from the spin.
        """
        if num_reels <= 0:
            raise ValueError("Number of reels must be a positive integer.")
        
        self.reel_spin_results = [random.choice(self.symbols) for _ in range(num_reels)]
        return self.reel_spin_results

    def calculate_payout(self):
        """
        Calculate the payout based on the current spin results.
        
        :return: Payout amount based on the spin results.
        """
        payout_table = self.get_payout_table()
        return payout_table.get(tuple(self.reel_spin_results), 0)

    def get_payout_table(self):
        """
        Define a payout table based on symbol combinations.
        
        :return: Dictionary representing the payout table.
        """
        return {
            ('🍒', '🍒', '🍒'): 10,  # Three cherries payout
            ('🍋', '🍋', '🍋'): 5,   # Three lemons payout
            ('🍊', '🍊', '🍊'): 3,   # Three oranges payout
            ('🔔', '🔔', '🔔'): 15,  # Three bells payout
            ('💎', '💎', '💎'): 20,  # Three diamonds payout
            # Add more symbol combinations as needed
        }

    def display_theme(self):
        """
        Display the theme of the slot machine.
        """
        print(f"Welcome to the {self.theme_name} Slot Machine!")

def main():
    # Define symbols for the slot machine
    symbols = ['🍒', '🍋', '🍊', '🔔', '💎']
    
    # Create a SlotMachine instance
    slot_machine = SlotMachine(symbols, "Fruity Fun", 0.95)
    
    # Display the theme
    slot_machine.display_theme()

    # Spin the slot machine
    try:
        results = slot_machine.spin(num_reels=3)
        print(f"Spin Results: {results}")

        # Calculate and display payout
        payout = slot_machine.calculate_payout()
        print(f"Payout: {payout}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
