"""
Generated Code Metadata:
========================
Original URL: https://poppredict.vercel.app
Prompt: Write a Python script to simulate a pop culture prediction betting system, including user input for predictions and calculating odds based on historical data.
Generated: DETERMINISTIC_72564dee3cd7c218
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class BettingSystem:
    def __init__(self):
        """Initialize the betting system with historical data."""
        self.historical_data = {
            "movie_a": [0.8, 0.7, 0.9],
            "movie_b": [0.6, 0.5, 0.4],
            "movie_c": [0.9, 0.85, 0.95]
        }
        self.odds = {}
        self.user_bets = {}

    def calculate_odds(self):
        """Calculate odds based on historical data."""
        for movie, results in self.historical_data.items():
            average_success_rate = sum(results) / len(results)
            self.odds[movie] = round(1 / average_success_rate, 2)  # Simple odds calculation
        return self.odds

    def place_bet(self, user, movie, amount):
        """Place a bet for a user on a specific movie."""
        if movie not in self.odds:
            raise ValueError(f"Movie '{movie}' is not available for betting.")
        if user not in self.user_bets:
            self.user_bets[user] = {}
        if movie not in self.user_bets[user]:
            self.user_bets[user][movie] = 0
        self.user_bets[user][movie] += amount
        print(f"{user} placed a bet of ${amount} on {movie}.")

    def simulate_outcome(self, movie):
        """Simulate the outcome of a movie's success based on historical data."""
        if movie not in self.historical_data:
            raise ValueError(f"Movie '{movie}' is not available for outcome simulation.")
        success_rate = random.uniform(0, 1)
        return success_rate <= sum(self.historical_data[movie]) / len(self.historical_data[movie])

    def settle_bets(self):
        """Settle all bets based on simulated outcomes."""
        for user, bets in self.user_bets.items():
            for movie, amount in bets.items():
                if self.simulate_outcome(movie):
                    winnings = amount * self.odds[movie]
                    print(f"{user} wins ${winnings:.2f} on {movie}!")
                else:
                    print(f"{user} loses ${amount:.2f} on {movie}.")

def main():
    """Main function to run the betting system."""
    betting_system = BettingSystem()
    betting_system.calculate_odds()

    while True:
        try:
            user = input("Enter your name (or 'exit' to quit): ")
            if user.lower() == 'exit':
                break
            movie = input("Enter the movie you want to bet on: ")
            amount = float(input("Enter the amount you want to bet: "))
            betting_system.place_bet(user, movie, amount)
        except ValueError as e:
            print(f"Error: {e}")

    betting_system.settle_bets()

if __name__ == "__main__":
    main()
```
