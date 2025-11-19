"""
Generated Code Metadata:
========================
Original URL: https://craves.io
Prompt: Generate a Python code snippet to simulate a simple lottery game using the Pasaran Hongkong or Pasaran Singapore rules, including a 5 Pasaran bonus and a 10% new member bonus.
Generated: DETERMINISTIC_d5af3c860e32dc87
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class LotteryGame:
    """
    Simulates a simple lottery game using Pasaran Hongkong or Pasaran Singapore rules.
    """

    def __init__(self, pasaran_type):
        """
        Initializes the lottery game.

        Args:
            pasaran_type (str): Type of pasaran, either 'hongkong' or 'singapore'.
        """
        self.pasaran_type = pasaran_type.lower()
        if self.pasaran_type not in ['hongkong', 'singapore']:
            raise ValueError("Invalid pasaran type. Must be 'hongkong' or 'singapore'.")

    def generate_numbers(self):
        """
        Generates a set of random numbers based on the pasaran type.

        Returns:
            list: A list of 6 random numbers between 1 and 49.
        """
        return random.sample(range(1, 50), 6)

    def calculate_prize(self, user_numbers, drawn_numbers):
        """
        Calculates the prize based on the user's numbers and the drawn numbers.

        Args:
            user_numbers (list): The user's 6 numbers.
            drawn_numbers (list): The drawn 6 numbers.

        Returns:
            int: The prize amount.
        """
        matches = len(set(user_numbers) & set(drawn_numbers))
        if matches == 6:
            return 1000000  # Jackpot
        elif matches == 5:
            return 50000  # 5 Pasaran bonus
        else:
            return 0

    def apply_new_member_bonus(self, prize):
        """
        Applies a 10% bonus for new members.

        Args:
            prize (int): The prize amount.

        Returns:
            int: The prize amount with the bonus applied.
        """
        return prize + (prize * 0.1)

    def play(self):
        """
        Simulates a game of lottery.

        Returns:
            dict: A dictionary containing the user's numbers, drawn numbers, prize, and bonus.
        """
        user_numbers = self.generate_numbers()
        drawn_numbers = self.generate_numbers()
        prize = self.calculate_prize(user_numbers, drawn_numbers)
        bonus = self.apply_new_member_bonus(prize) if prize > 0 else 0
        return {
            'user_numbers': user_numbers,
            'drawn_numbers': drawn_numbers,
            'prize': prize,
            'bonus': bonus
        }

def main():
    try:
        game = LotteryGame('hongkong')
        result = game.play()
        print("User Numbers:", result['user_numbers'])
        print("Drawn Numbers:", result['drawn_numbers'])
        print("Prize:", result['prize'])
        print("Bonus:", result['bonus'])
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()
```
