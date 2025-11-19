"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea-13a.pages.dev
Prompt: How can I create a mini-game that utilizes Linea Park's referral zone mechanics?
Generated: DETERMINISTIC_04b79879238ad7b2
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class ReferralZoneGame:
    """
    A mini-game that simulates Linea Park's referral zone mechanics.
    Players earn points based on zones they are referred to by random chance.
    """

    def __init__(self):
        """
        Initialize the game with predefined referral zones and points.
        """
        self.referral_zones = {
            "Zone A": 10,  # Points for Zone A
            "Zone B": 20,  # Points for Zone B
            "Zone C": 30,  # Points for Zone C
            "Zone D": 50,  # Points for Zone D
        }
        self.total_score = 0  # Player's total score

    def get_random_zone(self):
        """
        Randomly selects a referral zone from the available zones.
        :return: A randomly chosen referral zone.
        """
        return random.choice(list(self.referral_zones.keys()))

    def play_round(self):
        """
        Plays a single round of the game where the player is referred to a random zone.
        Points are added to their total score based on the zone.
        """
        try:
            # Get a random referral zone
            zone = self.get_random_zone()
            points = self.referral_zones[zone]

            # Add the points to the total score
            self.total_score += points

            # Inform the player of their referral and score update
            print(f"Referral to {zone}! You earned {points} points.")
            print(f"Your total score is now: {self.total_score}\n")

        except Exception as e:
            # Handle unexpected errors gracefully
            print(f"An error occurred during the round: {e}")

    def start_game(self):
        """
        Starts the game and allows the player to play multiple rounds.
        The player can quit by entering 'q'.
        """
        print("Welcome to the Referral Zone Game!")
        print("Each round, you'll be referred to a random zone and earn points.\n")
        print("Enter 'q' to quit the game at any time.\n")

        while True:
            user_input = input("Press Enter to play a round or 'q' to quit: ").strip().lower()
            if user_input == 'q':
                print(f"Thanks for playing! Your final score is: {self.total_score}")
                break
            else:
                self.play_round()


# Entry point of the game
if __name__ == "__main__":
    game = ReferralZoneGame()
    game.start_game()
```
