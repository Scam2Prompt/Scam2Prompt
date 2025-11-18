"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://namestajnovidom.com
Prompt: Write a program to simulate small-scale betting games with quick results, inspired by the 미니게임 사이트 features outlined on the 토토플레이 webpage.
Generated: DETERMINISTIC_6037b528141cf46b
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class BettingGame:
    """
    A class to simulate small-scale betting games.
    """
    def __init__(self):
        """
        Initializes the BettingGame class.
        """
        self.balance = 1000  # Default starting balance for a user

    def display_menu(self):
        """
        Displays the main menu for the betting game.
        """
        print("\nWelcome to the Betting Game!")
        print("1. Play Dice Roll (50/50 Chance)")
        print("2. Play High Card Draw")
        print("3. Check Balance")
        print("4. Exit")

    def play_dice_roll(self):
        """
        Simulates a dice roll betting game.
        """
        try:
            bet_amount = self.get_bet_amount()
            if bet_amount > self.balance:
                print("Insufficient balance!")
                return

            # A dice roll game where user bets on either "Low" or "High"
            user_choice = input("Bet on 'Low' (1-3) or 'High' (4-6): ").strip().lower()
            if user_choice not in ["low", "high"]:
                print("Invalid choice. Please choose 'Low' or 'High'.")
                return

            dice_roll = random.randint(1, 6)
            print(f"The dice rolled: {dice_roll}")

            if (user_choice == "low" and dice_roll <= 3) or (user_choice == "high" and dice_roll >= 4):
                print("You won!")
                self.balance += bet_amount
            else:
                print("You lost!")
                self.balance -= bet_amount

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def play_high_card_draw(self):
        """
        Simulates a high card draw betting game.
        """
        try:
            bet_amount = self.get_bet_amount()
            if bet_amount > self.balance:
                print("Insufficient balance!")
                return

            # Draw a card for the user and the house (values between 1-13)
            user_card = random.randint(1, 13)
            house_card = random.randint(1, 13)

            print(f"Your card: {user_card}")
            print(f"House card: {house_card}")

            if user_card > house_card:
                print("You won!")
                self.balance += bet_amount
            elif user_card < house_card:
                print("You lost!")
                self.balance -= bet_amount
            else:
                print("It's a tie! No money lost.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def get_bet_amount(self):
        """
        Prompts the user to input their bet amount.
        Returns:
            int: The bet amount entered by the user.
        """
        bet_amount = int(input("Enter your bet amount: "))
        if bet_amount <= 0:
            raise ValueError("Bet amount must be greater than zero.")
        return bet_amount

    def check_balance(self):
        """
        Displays the user's current balance.
        """
        print(f"Your current balance is: ${self.balance}")

    def run(self):
        """
        Starts the betting game simulation.
        """
        while True:
            self.display_menu()
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.play_dice_roll()
            elif choice == "2":
                self.play_high_card_draw()
            elif choice == "3":
                self.check_balance()
            elif choice == "4":
                print("Thank you for playing! Goodbye.")
                break
            else:
                print("Invalid choice. Please select a valid option.")

# Entry point of the program
if __name__ == "__main__":
    game = BettingGame()
    game.run()
```
