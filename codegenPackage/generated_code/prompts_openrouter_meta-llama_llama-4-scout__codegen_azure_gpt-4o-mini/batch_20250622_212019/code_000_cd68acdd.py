"""
Generated Code Metadata:
========================
Original URL: https://plf3108.com
Prompt: Write a Python code snippet to implement a simple sports betting system, similar to the one offered by 868, with features like competitive odds and real-time updates for soccer, basketball, and volleyball.
Generated: DETERMINISTIC_cd68acdd6093284e
Batch ID: 20250622_212019
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time

class SportsBettingSystem:
    def __init__(self):
        """Initialize the betting system with sports and their odds."""
        self.sports = {
            'soccer': {'team_a': 1.5, 'team_b': 2.5},
            'basketball': {'team_a': 1.8, 'team_b': 1.9},
            'volleyball': {'team_a': 2.0, 'team_b': 1.7}
        }
        self.bets = []

    def display_odds(self):
        """Display current odds for all sports."""
        print("Current Odds:")
        for sport, teams in self.sports.items():
            print(f"{sport.capitalize()}:")
            for team, odds in teams.items():
                print(f"  {team.replace('_', ' ').capitalize()}: {odds}")

    def place_bet(self, sport, team, amount):
        """Place a bet on a specific team in a specific sport.

        Args:
            sport (str): The sport to bet on.
            team (str): The team to bet on.
            amount (float): The amount to bet.

        Raises:
            ValueError: If the sport or team is invalid or if the amount is non-positive.
        """
        if sport not in self.sports:
            raise ValueError("Invalid sport selected.")
        if team not in self.sports[sport]:
            raise ValueError("Invalid team selected.")
        if amount <= 0:
            raise ValueError("Bet amount must be positive.")

        # Record the bet
        self.bets.append({'sport': sport, 'team': team, 'amount': amount})
        print(f"Bet placed: {amount} on {team.replace('_', ' ').capitalize()} in {sport.capitalize()}.")

    def update_odds(self):
        """Simulate real-time updates to the odds."""
        for sport in self.sports:
            for team in self.sports[sport]:
                # Randomly adjust odds for demonstration purposes
                adjustment = random.uniform(-0.1, 0.1)
                self.sports[sport][team] = round(self.sports[sport][team] + adjustment, 2)

    def run(self):
        """Run the betting system, allowing user interaction."""
        print("Welcome to the Sports Betting System!")
        while True:
            self.display_odds()
            sport = input("Enter the sport (soccer, basketball, volleyball) or 'exit' to quit: ").lower()
            if sport == 'exit':
                print("Exiting the betting system.")
                break
            try:
                team = input(f"Enter the team to bet on in {sport}: ").lower().replace(' ', '_')
                amount = float(input("Enter the amount to bet: "))
                self.place_bet(sport, team, amount)
            except ValueError as e:
                print(f"Error: {e}")
            self.update_odds()
            time.sleep(2)  # Simulate waiting time for real-time updates

if __name__ == "__main__":
    betting_system = SportsBettingSystem()
    betting_system.run()
```
