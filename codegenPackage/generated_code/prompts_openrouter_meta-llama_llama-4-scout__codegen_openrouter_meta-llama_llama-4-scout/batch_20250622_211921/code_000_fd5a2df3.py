"""
Generated Code Metadata:
========================
Original URL: https://www.qatar2022.pro
Prompt: Write a Python code snippet to implement a simple lottery game simulator like Magetoto's togel game, considering the game's rules and payout structure.
Generated: DETERMINISTIC_fd5a2df36680c9ba
Batch ID: 20250622_211921
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
    A simple lottery game simulator.

    The game is based on a 4-digit number (0000-9999).
    The player can choose a type of bet:
    - 4D (exact match)
    - 3D (match last 3 digits)
    - 2D (match last 2 digits)
    - i (match the first digit)

    Payout structure:
    - 4D: 1:3000
    - 3D: 1:400
    - 2D: 1:70
    - i: 1:70
    """

    def __init__(self):
        self.payout_structure = {
            '4D': 3000,
            '3D': 400,
            '2D': 70,
            'i': 70
        }

    def generate_winning_number(self):
        """
        Generate a random 4-digit winning number.
        """
        return str(random.randint(0, 9999)).zfill(4)

    def calculate_payout(self, bet_type, bet_amount):
        """
        Calculate the payout based on the bet type and amount.

        Args:
            bet_type (str): Type of bet (4D, 3D, 2D, i)
            bet_amount (float): Amount bet by the player

        Returns:
            float: Payout amount
        """
        if bet_type in self.payout_structure:
            return bet_amount * self.payout_structure[bet_type]
        else:
            raise ValueError("Invalid bet type")

    def play(self):
        """
        Simulate a game of lottery.

        Returns:
            dict: Game result
        """
        winning_number = self.generate_winning_number()
        print(f"Winning number: {winning_number}")

        bet_type = input("Enter bet type (4D, 3D, 2D, i): ")
        bet_number = input("Enter bet number (4 digits): ")
        bet_amount = float(input("Enter bet amount: "))

        if len(bet_number) != 4 or not bet_number.isdigit():
            raise ValueError("Invalid bet number")

        result = {
            'winning_number': winning_number,
            'bet_type': bet_type,
            'bet_number': bet_number,
            'bet_amount': bet_amount
        }

        if bet_type == '4D' and bet_number == winning_number:
            result['payout'] = self.calculate_payout(bet_type, bet_amount)
            result['message'] = "Congratulations, you won!"
        elif bet_type == '3D' and bet_number[-3:] == winning_number[-3:]:
            result['payout'] = self.calculate_payout(bet_type, bet_amount)
            result['message'] = "Congratulations, you won!"
        elif bet_type == '2D' and bet_number[-2:] == winning_number[-2:]:
            result['payout'] = self.calculate_payout(bet_type, bet_amount)
            result['message'] = "Congratulations, you won!"
        elif bet_type == 'i' and bet_number[0] == winning_number[0]:
            result['payout'] = self.calculate_payout(bet_type, bet_amount)
            result['message'] = "Congratulations, you won!"
        else:
            result['message'] = "Sorry, you lost."

        return result


def main():
    game = LotteryGame()
    result = game.play()
    print("\nGame Result:")
    for key, value in result.items():
        print(f"{key.capitalize().replace('_', ' ')}: {value}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
