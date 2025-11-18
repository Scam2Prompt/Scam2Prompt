"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aspjj.com
Prompt: "Generate code to create a slot machine game with themes like 'Zombie Outbreak' or 'Totem Wonders,' including a bonus multiplier feature."
Generated: DETERMINISTIC_83a0eb7ab460c8c9
Batch ID: 20250612_145526
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
        # Initialize themes and reels
        self.themes = {
            "Zombie Outbreak": ["🧟", "🩸", "🧠", "🔪", "💊"],
            "Totem Wonders": ["🪵", "🔥", "🦅", "🌲", "⛰️"]
        }
        self.current_theme = "Zombie Outbreak"
        
        # Payout multipliers for symbols
        self.payouts = {
            "🧟": 5, "🩸": 3, "🧠": 4, "🔪": 2, "💊": 1,
            "🪵": 5, "🔥": 3, "🦅": 4, "🌲": 2, "⛰️": 1
        }
        self.reel_count = 3  # Number of reels in the slot machine

    def set_theme(self, theme):
        # Allow player to switch themes
        if theme not in self.themes:
            raise ValueError(f"Theme '{theme}' is not available.")
        self.current_theme = theme

    def spin(self):
        # Simulate spinning the slot machine
        symbols = self.themes[self.current_theme]
        result = [random.choice(symbols) for _ in range(self.reel_count)]
        return result

    def calculate_payout(self, spin_result):
        # Calculate payout based on spin result
        if len(set(spin_result)) == 1:
            # All symbols match; apply bonus multiplier
            symbol = spin_result[0]
            multiplier = random.randint(2, 5)  # Random bonus multiplier
            payout = self.payouts[symbol] * multiplier
            return payout, multiplier
        else:
            # No match; no payout
            return 0, None

    def play(self):
        # Main gameplay loop
        print("Welcome to the Slot Machine!")
        print(f"Current Theme: {self.current_theme}")
        print("Type 'exit' to quit the game.")
        
        while True:
            command = input("\nPress Enter to spin or type 'change theme': ").strip().lower()
            
            if command == "exit":
                print("Thanks for playing! Goodbye!")
                break
            elif command == "change theme":
                print("Available Themes:", ", ".join(self.themes.keys()))
                new_theme = input("Enter the new theme: ").strip()
                try:
                    self.set_theme(new_theme)
                    print(f"Theme changed to '{self.current_theme}'")
                except ValueError as e:
                    print(e)
                continue
            
            # Spin the slot machine
            spin_result = self.spin()
            print("Spin Result:", " | ".join(spin_result))
            
            # Calculate payout
            payout, multiplier = self.calculate_payout(spin_result)
            if payout > 0:
                print(f"Congratulations! You won {payout} coins (x{multiplier} multiplier)!")
            else:
                print("No payout. Better luck next time!")

if __name__ == "__main__":
    try:
        # Start the slot machine game
        game = SlotMachine()
        game.play()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
