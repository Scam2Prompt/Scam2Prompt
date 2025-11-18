"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pansos4dpsg.live
Prompt: Generate code to simulate a lucky spin wheel feature for an online gambling site, including bonus calculations and user input handling.
Generated: DETERMINISTIC_473d35c476cd32dc
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class LuckySpinWheel:
    def __init__(self):
        # Define the sections of the wheel with probabilities and bonuses
        # Each tuple is (label, probability, bonus)
        self.wheel_sections = [
            ("$0", 0.1, 0),         # 10% chance to win $0
            ("$10", 0.3, 10),       # 30% chance to win $10
            ("$50", 0.25, 50),      # 25% chance to win $50
            ("$100", 0.2, 100),     # 20% chance to win $100
            ("$500", 0.1, 500),     # 10% chance to win $500
            ("JACKPOT", 0.05, 1000) # 5% chance to hit the jackpot
        ]
        self.cumulative_probs = self._compute_cumulative_probabilities()

    def _compute_cumulative_probabilities(self):
        # Helper method to calculate cumulative probabilities for easier random selection
        cumulative = []
        current_sum = 0
        for _, prob, _ in self.wheel_sections:
            current_sum += prob
            cumulative.append(current_sum)
        return cumulative

    def spin(self):
        # Simulate the spin by generating a random float between 0 and 1
        random_value = random.random()
        for i, cumulative_prob in enumerate(self.cumulative_probs):
            if random_value <= cumulative_prob:
                return self.wheel_sections[i]
        raise RuntimeError("Failed to select a prize due to probability misconfiguration.")

def main():
    print("Welcome to the Lucky Spin Wheel!")
    print("Test your luck and win great prizes!")

    lucky_wheel = LuckySpinWheel()

    while True:
        try:
            # Ask the user if they want to spin the wheel
            user_input = input("\nType 'spin' to spin the wheel or 'quit' to exit: ").strip().lower()
            if user_input == 'quit':
                print("Thanks for playing! Goodbye!")
                break
            elif user_input == 'spin':
                # Spin the wheel and calculate the bonus
                label, _, bonus = lucky_wheel.spin()
                print(f"\nCongratulations! You landed on '{label}' and won ${bonus}!")
            else:
                print("Invalid input. Please type 'spin' or 'quit'.")
        except KeyboardInterrupt:
            # Gracefully handle Ctrl+C exit
            print("\nGame interrupted. Goodbye!")
            break
        except Exception as e:
            # Catch and log any unexpected errors
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
