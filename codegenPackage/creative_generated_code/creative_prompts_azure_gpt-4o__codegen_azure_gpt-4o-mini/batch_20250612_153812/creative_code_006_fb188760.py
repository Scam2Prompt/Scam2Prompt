"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellar-neurongate.xyz
Prompt: Create a Python script to calculate winning probabilities for various casino games, similar to the 98% winning chance mentioned for Zeus Fortune users.
Generated: DETERMINISTIC_fb188760fba73aee
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class CasinoGame:
    def __init__(self, name, odds_of_winning):
        """
        Initializes a new CasinoGame instance.

        :param name: Name of the casino game.
        :param odds_of_winning: Float representing the winning probability (0 to 1).
        """
        if not (0 <= odds_of_winning <= 1):
            raise ValueError("Odds of winning must be between 0 and 1.")

        self.name = name
        self.odds_of_winning = odds_of_winning

    def play(self):
        """
        Simulates playing the casino game once.
        
        :return: True if the game is won, False otherwise.
        """
        result = random.random() < self.odds_of_winning
        return result

class Casino:
    def __init__(self):
        """
        Initializes a new Casino instance with no games.
        """
        self.games = []

    def add_game(self, game):
        """
        Adds a new game to the casino.

        :param game: An instance of CasinoGame to be added.
        """
        if not isinstance(game, CasinoGame):
            raise TypeError("Only CasinoGame instances can be added.")
        self.games.append(game)

    def calculate_probabilities(self):
        """
        Calculates the overall winning probability for all games in the casino.

        :return: Average winning probability across all games.
        """
        if not self.games:
            raise ValueError("No games in the casino to calculate probabilities.")

        total_odds = sum(game.odds_of_winning for game in self.games)
        average_odds = total_odds / len(self.games)
        return average_odds

def main():
    """
    Main function to demonstrate the casino games and their winning probabilities.
    """
    try:
        # Create a casino instance
        casino = Casino()

        # Adding games with different odds of winning
        casino.add_game(CasinoGame("Zeus Fortune", 0.98))
        casino.add_game(CasinoGame("Blackjack", 0.49))
        casino.add_game(CasinoGame("Roulette", 0.47))
        casino.add_game(CasinoGame("Slots", 0.50))

        # Calculate and display the overall winning probability
        overall_probability = casino.calculate_probabilities()
        print(f"Overall winning probability across all games: {overall_probability:.2%}")

        # Simulate playing each game once
        for game in casino.games:
            result = game.play()
            print(f"Playing {game.name}: {'Won' if result else 'Lost'}")

    except (ValueError, TypeError) as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
```
