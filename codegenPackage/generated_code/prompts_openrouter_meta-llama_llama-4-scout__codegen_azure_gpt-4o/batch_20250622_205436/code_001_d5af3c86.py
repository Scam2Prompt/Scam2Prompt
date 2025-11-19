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
    def __init__(self):
        """
        Initialize the lottery game with default settings.
        """
        self.pasaran_types = ["Hongkong", "Singapore"]
        self.bonus_pasaran = 5  # 5 Pasaran bonus
        self.new_member_bonus_percentage = 10  # 10% new member bonus

    def generate_lottery_numbers(self):
        """
        Generate random lottery numbers for the game.
        Returns:
            list: A list of 6 random numbers between 1 and 49.
        """
        return random.sample(range(1, 50), 6)

    def calculate_bonus(self, base_amount, is_new_member):
        """
        Calculate the total bonus based on the Pasaran bonus and new member bonus.
        Args:
            base_amount (float): The base amount to calculate bonuses on.
            is_new_member (bool): Whether the player is a new member.
        Returns:
            float: The total bonus amount.
        """
        pasaran_bonus = self.bonus_pasaran
        new_member_bonus = (base_amount * self.new_member_bonus_percentage / 100) if is_new_member else 0
        return pasaran_bonus + new_member_bonus

    def play_game(self, bet_amount, pasaran_choice, is_new_member):
        """
        Simulate the lottery game.
        Args:
            bet_amount (float): The amount the player bets.
            pasaran_choice (str): The chosen Pasaran type ("Hongkong" or "Singapore").
            is_new_member (bool): Whether the player is a new member.
        Returns:
            dict: A dictionary containing the game results.
        """
        if pasaran_choice not in self.pasaran_types:
            raise ValueError(f"Invalid Pasaran choice. Choose from {self.pasaran_types}.")

        # Generate lottery numbers
        lottery_numbers = self.generate_lottery_numbers()

        # Calculate total bonus
        total_bonus = self.calculate_bonus(bet_amount, is_new_member)

        # Simulate winning (for simplicity, assume a random chance of winning)
        is_winner = random.choice([True, False])

        # Prepare game results
        results = {
            "Pasaran": pasaran_choice,
            "Lottery Numbers": lottery_numbers,
            "Bet Amount": bet_amount,
            "Total Bonus": total_bonus,
            "Is Winner": is_winner
        }

        return results


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the game
        game = LotteryGame()

        # Player inputs
        bet_amount = 100.0  # Example bet amount
        pasaran_choice = "Hongkong"  # Example Pasaran choice
        is_new_member = True  # Example new member status

        # Play the game
        results = game.play_game(bet_amount, pasaran_choice, is_new_member)

        # Display results
        print("Lottery Game Results:")
        for key, value in results.items():
            print(f"{key}: {value}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
