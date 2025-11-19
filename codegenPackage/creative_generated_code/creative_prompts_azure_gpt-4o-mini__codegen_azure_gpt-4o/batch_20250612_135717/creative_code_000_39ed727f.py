"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://todaythegames.com
Prompt: Generate a code snippet for a social casino game that allows players to spin a virtual wheel and win virtual credits, similar to the Super Wheel featured on todaythegames.com.
Generated: DETERMINISTIC_39ed727f67e6e95f
Batch ID: 20250612_135717
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class SocialCasinoGame:
    """
    A class representing a social casino game where players can spin a virtual wheel to win virtual credits.
    """

    def __init__(self):
        """
        Initialize the wheel with predefined prizes and set initial player credits.
        """
        self.wheel_prizes = [0, 50, 100, 200, 500, 1000]  # Possible prizes on the wheel
        self.player_credits = 0  # Virtual credits the player has

    def spin_wheel(self):
        """
        Simulates spinning the wheel and adds the won credits to the player's total.
        Returns:
            int: The amount of credits won.
        """
        try:
            # Randomly select a prize from the wheel
            prize_index = random.randint(0, len(self.wheel_prizes) - 1)
            prize_won = self.wheel_prizes[prize_index]

            # Add the prize won to the player's total credits
            self.player_credits += prize_won

            # Log the win and return the prize won
            print(f"Congratulations! You won {prize_won} credits!")
            return prize_won
        except Exception as e:
            # Handle unexpected errors during the spin
            print(f"An error occurred while spinning the wheel: {e}")
            return 0

    def get_player_credits(self):
        """
        Returns the total credits the player currently has.
        Returns:
            int: The total credits of the player.
        """
        return self.player_credits


# Main function to demonstrate the game
def main():
    """
    Entry point for the Social Casino Game.
    Allows the player to spin the wheel multiple times and check their total credits.
    """
    game = SocialCasinoGame()
    print("Welcome to the Social Casino Game!")

    while True:
        # Ask the player for their action
        print("\nMenu:")
        print("1. Spin the wheel")
        print("2. Check total credits")
        print("3. Quit the game")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            # Spin the wheel
            game.spin_wheel()
        elif choice == "2":
            # Display total credits
            print(f"You currently have {game.get_player_credits()} credits.")
        elif choice == "3":
            # Quit the game
            print("Thanks for playing! Goodbye!")
            break
        else:
            # Handle invalid input
            print("Invalid choice. Please try again.")


# Run the game
if __name__ == "__main__":
    main()
```
