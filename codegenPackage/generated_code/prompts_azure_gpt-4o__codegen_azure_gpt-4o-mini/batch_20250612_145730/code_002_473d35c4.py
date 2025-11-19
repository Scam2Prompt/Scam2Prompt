"""
Generated Code Metadata:
========================
Original URL: https://pansos4dpsg.live
Prompt: Generate code to simulate a lucky spin wheel feature for an online gambling site, including bonus calculations and user input handling.
Generated: DETERMINISTIC_473d35c476cd32dc
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class SpinWheel:
    def __init__(self):
        # Define the segments of the spin wheel with their corresponding rewards
        self.segments = {
            "100": 100,
            "200": 200,
            "300": 300,
            "Bonus": 500,
            "Lose": 0
        }
        self.total_spins = 0
        self.total_winnings = 0

    def spin(self):
        """Simulate spinning the wheel and return the result."""
        result = random.choice(list(self.segments.keys()))
        return result

    def calculate_bonus(self, result):
        """Calculate bonus based on the result of the spin."""
        if result == "Bonus":
            bonus = random.randint(100, 1000)  # Random bonus between 100 and 1000
            print(f"Congratulations! You received a bonus of {bonus}!")
            return bonus
        return 0

    def play(self):
        """Main method to handle user input and simulate the spin wheel."""
        while True:
            user_input = input("Press 's' to spin the wheel or 'q' to quit: ").strip().lower()
            if user_input == 's':
                self.total_spins += 1
                result = self.spin()
                print(f"You spun: {result}")

                # Calculate winnings based on the result
                winnings = self.segments[result]
                self.total_winnings += winnings
                print(f"You won: {winnings}")

                # Calculate any bonus
                bonus = self.calculate_bonus(result)
                self.total_winnings += bonus

                print(f"Total winnings so far: {self.total_winnings}")
            elif user_input == 'q':
                print("Thank you for playing!")
                print(f"Total spins: {self.total_spins}, Total winnings: {self.total_winnings}")
                break
            else:
                print("Invalid input. Please enter 's' to spin or 'q' to quit.")

if __name__ == "__main__":
    try:
        game = SpinWheel()
        game.play()
    except Exception as e:
        print(f"An error occurred: {e}")
```
