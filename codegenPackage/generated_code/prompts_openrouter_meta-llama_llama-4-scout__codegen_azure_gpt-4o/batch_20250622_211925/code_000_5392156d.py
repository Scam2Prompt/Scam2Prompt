"""
Generated Code Metadata:
========================
Original URL: https://downtownspokanehotels.com
Prompt: "Write a Python script to simulate a Togel HK game, considering the rules and betting options described on Holyslots88, including 2D, 3D, and 4D bets."
Generated: DETERMINISTIC_5392156d2daf0121
Batch ID: 20250622_211925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class TogelHKGame:
    """
    A class to simulate a Togel HK game with 2D, 3D, and 4D betting options.
    """

    def __init__(self):
        """
        Initialize the game with a random 4-digit winning number.
        """
        self.winning_number = self.generate_winning_number()

    @staticmethod
    def generate_winning_number():
        """
        Generate a random 4-digit winning number.
        Returns:
            str: A 4-digit string representing the winning number.
        """
        return f"{random.randint(0, 9999):04}"

    def check_bet(self, bet_type, bet_number):
        """
        Check if the bet matches the winning number based on the bet type.
        Args:
            bet_type (str): The type of bet ('2D', '3D', '4D').
            bet_number (str): The number the player is betting on.
        Returns:
            bool: True if the bet matches the winning number, False otherwise.
        """
        if bet_type == '2D':
            return bet_number == self.winning_number[-2:]
        elif bet_type == '3D':
            return bet_number == self.winning_number[-3:]
        elif bet_type == '4D':
            return bet_number == self.winning_number
        else:
            raise ValueError("Invalid bet type. Please choose '2D', '3D', or '4D'.")

    def play(self):
        """
        Simulate the Togel HK game.
        """
        print("Welcome to the Togel HK Game!")
        print("Winning number has been generated.")
        print("Available bet types: 2D, 3D, 4D")

        try:
            # Get user input for bet type and number
            bet_type = input("Enter your bet type (2D, 3D, 4D): ").strip().upper()
            bet_number = input(f"Enter your {bet_type} bet number: ").strip()

            # Validate bet number length
            if bet_type == '2D' and len(bet_number) != 2:
                raise ValueError("2D bet number must be exactly 2 digits.")
            elif bet_type == '3D' and len(bet_number) != 3:
                raise ValueError("3D bet number must be exactly 3 digits.")
            elif bet_type == '4D' and len(bet_number) != 4:
                raise ValueError("4D bet number must be exactly 4 digits.")

            # Check the bet
            if self.check_bet(bet_type, bet_number):
                print(f"Congratulations! You won! The winning number was {self.winning_number}.")
            else:
                print(f"Sorry, you lost. The winning number was {self.winning_number}.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Create a game instance and start the game
    game = TogelHKGame()
    game.play()
```
