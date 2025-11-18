"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mywanderloop.com
Prompt: Write Python code to simulate the "Gates of Olympus Slot" game, including payout ratios, bonus mechanics, and promotional features as described on the myWanderLoop website.
Generated: DETERMINISTIC_8af986dc171457ac
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class GatesOfOlympusSlot:
    def __init__(self):
        # Initialize game parameters
        self.symbols = ['Zeus', 'Lightning', 'Crown', 'Ring', 'Heart', 'Diamond']
        self.payout_ratios = {
            'Zeus': 50,
            'Lightning': 20,
            'Crown': 15,
            'Ring': 10,
            'Heart': 5,
            'Diamond': 2
        }
        self.bonus_multiplier = 1
        self.bonus_round_active = False
        
    def spin_reels(self):
        """Simulates spinning the slot machine reels."""
        return [random.choice(self.symbols) for _ in range(5)]

    def calculate_payout(self, results):
        """Calculates the payout based on the spin results."""
        payout = 0
        for symbol in results:
            payout += self.payout_ratios.get(symbol, 0)
        
        # Apply bonus multiplier if active
        if self.bonus_round_active:
            payout *= self.bonus_multiplier
            self.reset_bonus()  # Reset after applying
            
        return payout

    def activate_bonus_round(self):
        """Activates the bonus round with a random multiplier."""
        self.bonus_multiplier = random.randint(2, 5)
        self.bonus_round_active = True

    def reset_bonus(self):
        """Resets the bonus round state."""
        self.bonus_multiplier = 1
        self.bonus_round_active = False

    def play_game(self):
        """Main game loop for playing the slot machine."""
        print("Welcome to Gates of Olympus Slot!")
        
        while True:
            user_input = input("Press 's' to spin or 'q' to quit: ").lower()
            if user_input == 's':
                results = self.spin_reels()
                print(f"Spin results: {results}")

                payout = self.calculate_payout(results)
                print(f"You won: {payout} coins!")
                
                # Randomly decide to activate the bonus round
                if random.random() < 0.3:  # 30% chance to activate bonus
                    self.activate_bonus_round()
                    print(f"Bonus round activated! Multiplier: x{self.bonus_multiplier}")

            elif user_input == 'q':
                print("Thanks for playing! Goodbye!")
                break
            
            else:
                print("Invalid input. Please enter 's' to spin or 'q' to quit.")

if __name__ == "__main__":
    try:
        game = GatesOfOlympusSlot()
        game.play_game()
    except Exception as e:
        print(f"An error occurred: {e}")
```
