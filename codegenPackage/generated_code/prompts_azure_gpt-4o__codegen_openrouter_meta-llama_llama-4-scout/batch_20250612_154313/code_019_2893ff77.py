"""
Generated Code Metadata:
========================
Original URL: https://lidofi.us.com
Prompt: Write a Python script to simulate the Xóc Đĩa game based on WW88's rules and strategies for winning.
Generated: DETERMINISTIC_2893ff774dd3b83f
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class XocDia:
    """
    Simulates the Xóc Đĩa game based on WW88's rules and strategies.
    """

    def __init__(self):
        self.dice = ['Chẵn', 'Lẻ']
        self.betting_options = ['Chẵn', 'Lẻ', 'Tài', 'Hiếu']

    def roll_dice(self):
        """
        Simulate rolling 4 dice.

        Returns:
            int: The number of even dice.
        """
        # Roll 4 dice, each die has 2 sides (even, odd)
        dice_outcome = [random.choice([0, 1]) for _ in range(4)]
        # Count the number of even dice
        even_dice_count = sum(1 for die in dice_outcome if die == 0)
        return even_dice_count

    def determine_outcome(self, even_dice_count):
        """
        Determine the outcome of the game.

        Args:
            even_dice_count (int): The number of even dice.

        Returns:
            str: The outcome of the game ('Chẵn', 'Lẻ', 'Tài', 'Hiếu').
        """
        if even_dice_count % 2 == 0:
            outcome = 'Chẵn'
        else:
            outcome = 'Lẻ'

        if even_dice_count >= 3:
            outcome += ', Tài'
        elif even_dice_count <= 1:
            outcome += ', Hiếu'

        return outcome

    def play(self):
        """
        Play a round of Xóc Đĩa.

        Returns:
            dict: The outcome of the game and the betting options.
        """
        even_dice_count = self.roll_dice()
        outcome = self.determine_outcome(even_dice_count)

        print("Outcome:", outcome)

        # Betting
        betting_amount = float(input("Enter your betting amount: "))
        betting_option = input("Enter your betting option (Chẵn, Lẻ, Tài, Hiếu): ")

        if betting_option not in self.betting_options:
            print("Invalid betting option.")
            return

        # Determine win/loss
        if betting_option in outcome:
            print("You win!")
            return {'outcome': outcome, 'betting_amount': betting_amount, 'betting_option': betting_option, 'result': 'win'}
        else:
            print("You lose!")
            return {'outcome': outcome, 'betting_amount': betting_amount, 'betting_option': betting_option, 'result': 'loss'}

def main():
    game = XocDia()
    play_again = 'y'
    while play_again.lower() == 'y':
        game.play()
        play_again = input("Play again? (y/n): ")

if __name__ == "__main__":
    main()
```
