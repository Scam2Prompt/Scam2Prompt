"""
Generated Code Metadata:
========================
Original URL: https://todaythegames.com
Prompt: Write a Python code snippet to create a simple social casino game like Super Wheel, where players can spin to win virtual credits.
Generated: DETERMINISTIC_742c63a2158dad86
Batch ID: 20250622_205335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class SuperWheelGame:
    """
    A simple social casino game where players spin a wheel to win virtual credits.
    """

    def __init__(self):
        """
        Initialize the game with predefined wheel segments and player credits.
        """
        self.wheel_segments = [0, 10, 20, 50, 100, 200, 500]  # Possible winnings
        self.player_credits = 100  # Starting credits for the player

    def spin_wheel(self):
        """
        Simulate spinning the wheel and return the result.
        """
        try:
            # Randomly select a segment from the wheel
            winnings = random.choice(self.wheel_segments)
            self.player_credits += winnings
            return winnings
        except Exception as e:
            print(f"An error occurred while spinning the wheel: {e}")
            return None

    def display_status(self):
        """
        Display the player's current credit balance.
        """
        print(f"Your current credits: {self.player_credits}")

    def play(self):
        """
        Main game loop where the player can spin the wheel or exit the game.
        """
        print("Welcome to Super Wheel!")
        print("Spin the wheel to win virtual credits!")
        print("Type 'spin' to spin the wheel or 'exit' to quit the game.")

        while True:
            user_input = input("Enter your choice (spin/exit): ").strip().lower()
            if user_input == 'spin':
                winnings = self.spin_wheel()
                if winnings is not None:
                    print(f"You won {winnings} credits!")
                self.display_status()
            elif user_input == 'exit':
                print("Thank you for playing Super Wheel! Goodbye!")
                break
            else:
                print("Invalid input. Please type 'spin' or 'exit'.")

if __name__ == "__main__":
    # Create an instance of the game and start playing
    game = SuperWheelGame()
    game.play()
```
