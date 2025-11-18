"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://avto-world-voditela.club
Prompt: Create a Python script to simulate virtual betting on a platform like "快3大小单双平台" and calculate the odds of winning.
Generated: DETERMINISTIC_8dc9790d0104927d
Batch ID: 20250612_154222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class VirtualBettingPlatform:
    """
    A class to simulate virtual betting on a platform like "快3大小单双平台."
    """

    def __init__(self):
        """
        Initializes the betting platform with possible outcomes and odds.
        """
        self.possible_outcomes = ['Big', 'Small', 'Odd', 'Even']
        self.odds = {
            'Big': 0.5,   # Probability of 'Big'
            'Small': 0.5, # Probability of 'Small'
            'Odd': 0.5,   # Probability of 'Odd'
            'Even': 0.5   # Probability of 'Even'
        }

    def place_bet(self, bet_choice, amount):
        """
        Simulates placing a bet on the platform.
        
        :param bet_choice: The choice of bet (e.g., 'Big', 'Small', 'Odd', 'Even').
        :param amount: The amount of money being wagered.
        :return: Tuple (win_status, payout)
        """
        # Validate bet choice
        if bet_choice not in self.possible_outcomes:
            raise ValueError(f"Invalid bet choice: {bet_choice}. Valid options are {self.possible_outcomes}.")

        # Simulate random outcome
        outcome = random.choice(self.possible_outcomes)

        # Determine win status
        win_status = (bet_choice == outcome)
        payout = amount * 2 if win_status else 0  # Bet pays 2x on win, 0 on loss

        # Return results
        return win_status, payout, outcome

    def calculate_odds(self, bet_choice):
        """
        Calculates the odds of winning for a given bet choice.
        
        :param bet_choice: The choice of bet (e.g., 'Big', 'Small', 'Odd', 'Even').
        :return: The probability of winning for the given bet choice.
        """
        # Validate bet choice
        if bet_choice not in self.odds:
            raise ValueError(f"Invalid bet choice: {bet_choice}. Valid options are {self.possible_outcomes}.")

        return self.odds[bet_choice]


def main():
    """
    Main function to execute simulation of virtual betting.
    """
    # Instantiate the betting platform
    platform = VirtualBettingPlatform()

    print("Welcome to the Virtual Betting Platform!\n")
    print("Available betting options: 'Big', 'Small', 'Odd', 'Even'\n")

    try:
        # User inputs
        bet_choice = input("Enter your bet choice: ").strip()
        amount = float(input("Enter the amount you want to wager: "))

        # Calculate odds
        odds = platform.calculate_odds(bet_choice)
        print(f"The odds of winning for '{bet_choice}' are: {odds * 100:.2f}%\n")

        # Place bet and get result
        win_status, payout, outcome = platform.place_bet(bet_choice, amount)

        # Display results
        print(f"Outcome of the roll: {outcome}")
        if win_status:
            print(f"Congratulations! You won. Your payout is: ${payout:.2f}")
        else:
            print(f"Sorry, you lost. Better luck next time!")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
