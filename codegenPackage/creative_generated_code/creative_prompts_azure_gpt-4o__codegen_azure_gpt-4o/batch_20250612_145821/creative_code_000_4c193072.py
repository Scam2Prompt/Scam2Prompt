"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibariumdao.io
Prompt: Write a Python script to simulate a basic betting system for sports games, incorporating odds and payout calculations similar to the features described on S666.
Generated: DETERMINISTIC_4c193072199bdacb
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class BettingSystem:
    """
    A basic sports betting simulation system.
    """

    def __init__(self):
        """
        Initialize the system with predefined teams and odds.
        """
        self.games = {
            "Team A vs Team B": {"Team A": 1.8, "Team B": 2.0},
            "Team C vs Team D": {"Team C": 1.5, "Team D": 2.5},
            "Team E vs Team F": {"Team E": 2.2, "Team F": 1.7},
        }

    def display_games(self):
        """
        Display available games and their odds.
        """
        print("\nAvailable Games and Odds:")
        for game, odds in self.games.items():
            print(f"{game}: {', '.join([f'{team} (odds: {odds[team]})' for team in odds])}")

    def place_bet(self, game, team, amount):
        """
        Place a bet on a team in a specific game.
        Args:
            game (str): The game to bet on.
            team (str): The team to bet on.
            amount (float): The amount to bet.

        Returns:
            dict: Result of the bet, including payout or loss.
        """
        if game not in self.games:
            raise ValueError("Invalid game selection.")
        if team not in self.games[game]:
            raise ValueError("Invalid team selection.")
        if amount <= 0:
            raise ValueError("Bet amount must be greater than zero.")

        # Simulate game result
        winning_team = random.choice(list(self.games[game].keys()))
        odds = self.games[game][team]

        print(f"\nGame Result: {winning_team} won.")

        if team == winning_team:
            payout = round(amount * odds, 2)  # Calculate payout
            return {"success": True, "payout": payout, "message": f"You won! Payout: ${payout}"}
        else:
            return {"success": False, "payout": 0.0, "message": "You lost the bet. Better luck next time!"}

    def run(self):
        """
        Main method to run the betting system.
        """
        print("Welcome to the Sports Betting System!")
        while True:
            self.display_games()
            try:
                # Get user input for game and bet
                game = input("\nEnter the game you want to bet on (e.g., 'Team A vs Team B'): ").strip()
                team = input("Enter the team you want to bet on: ").strip()
                amount = float(input("Enter the bet amount: "))

                # Place the bet
                result = self.place_bet(game, team, amount)
                print(result["message"])
                print(f"Your payout: ${result['payout']}\n")

            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

            # Ask if the user wants to continue
            cont = input("Do you want to place another bet? (yes/no): ").strip().lower()
            if cont != "yes":
                print("Thank you for using the Sports Betting System! Goodbye!")
                break


if __name__ == "__main__":
    # Run the betting system
    system = BettingSystem()
    system.run()
```
