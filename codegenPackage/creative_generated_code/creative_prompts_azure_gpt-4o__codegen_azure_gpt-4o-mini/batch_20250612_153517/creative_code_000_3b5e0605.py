"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://republik.pages.dev
Prompt: Write a Python script to simulate a slot machine game with themes like "Gatot Kaca," "Mahjong Ways," and "Gates of Olympus," incorporating payout rates and jackpot mechanics similar to those described on ANGKA805.
Generated: DETERMINISTIC_3b5e0605ac8b1d7f
Batch ID: 20250612_153517
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
    def __init__(self, themes, payout_rates, jackpot_amount):
        """
        Initializes the SlotMachine with themes, payout rates, and a jackpot amount.
        
        :param themes: A list of slot machine themes
        :param payout_rates: A dictionary mapping each theme to its payout rate
        :param jackpot_amount: The amount for the jackpot
        """
        self.themes = themes
        self.payout_rates = payout_rates
        self.jackpot_amount = jackpot_amount

    def spin(self):
        """
        Simulates a spin of the slot machine by randomly selecting a theme.
        
        :return: The selected theme and the result of the spin
        """
        theme = random.choice(self.themes)
        payout = self.calculate_payout(theme)
        return theme, payout

    def calculate_payout(self, theme):
        """
        Calculates the payout based on the selected theme.

        :param theme: The theme selected for the spin
        :return: The calculated payout amount
        """
        if theme not in self.payout_rates:
            raise ValueError(f"Theme '{theme}' not found in payout rates.")
        
        # Determine if the player hits the jackpot
        if random.random() < 0.01:  # 1% chance for jackpot
            return self.jackpot_amount
        
        # Calculate payout based on the payout rate
        return random.uniform(1, self.payout_rates[theme])  # Random payout between 1 and payout rate

def main():
    # Define themes and corresponding payout rates
    themes = ["Gatot Kaca", "Mahjong Ways", "Gates of Olympus"]
    payout_rates = {
        "Gatot Kaca": 5.0,       # Maximum payout is 5 times the bet
        "Mahjong Ways": 4.5,     # Maximum payout is 4.5 times the bet
        "Gates of Olympus": 6.0   # Maximum payout is 6 times the bet
    }
    jackpot_amount = 1000.00   # Set the jackpot amount

    # Create a SlotMachine instance
    slot_machine = SlotMachine(themes, payout_rates, jackpot_amount)

    # Main game loop
    while True:
        try:
            input("Press Enter to spin the slot machine...")
            theme, payout = slot_machine.spin()
            print(f"Theme: {theme}, Payout: ${payout:.2f}")

            # Optional: Ask the player if they want to play again
            play_again = input("Do you want to play again? (y/n): ").strip().lower()
            if play_again != 'y':
                print("Thank you for playing!")
                break

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
