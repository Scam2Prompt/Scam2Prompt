"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mydogclub.pages.dev
Prompt: Generate a code snippet for a betting system that allows users to challenge others in a Duel Race within the Bitcoin Dogs Club.
Generated: DETERMINISTIC_2451fb13fc0e04ee
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class User:
    """Represents a user in the Bitcoin Dogs Club."""
    
    def __init__(self, username, balance):
        """
        Initializes a new user with a username and balance.

        :param username: str - The username of the user.
        :param balance: float - The initial balance of the user.
        """
        self.username = username
        self.balance = balance

    def place_bet(self, amount):
        """
        Allows the user to place a bet.

        :param amount: float - The amount to bet.
        :raises ValueError: If the bet amount exceeds the user's balance.
        """
        if amount > self.balance:
            raise ValueError("Insufficient balance to place this bet.")
        self.balance -= amount

    def win_bet(self, amount):
        """
        Increases the user's balance when they win a bet.

        :param amount: float - The amount won.
        """
        self.balance += amount


class DuelRace:
    """Handles the logic of a Duel Race."""

    def __init__(self):
        """Initializes a new Duel Race."""
        self.users = {}

    def register_user(self, user):
        """
        Registers a user for the race.

        :param user: User - The user to register.
        """
        self.users[user.username] = user

    def start_duel(self, challenger, opponent, bet_amount):
        """
        Starts a duel between two users.

        :param challenger: str - The username of the challenger.
        :param opponent: str - The username of the opponent.
        :param bet_amount: float - The amount being bet on the duel.
        :raises ValueError: If either user does not exist or insufficient balance.
        """
        if challenger not in self.users or opponent not in self.users:
            raise ValueError("Both users must be registered to duel.")
        
        challenger_user = self.users[challenger]
        opponent_user = self.users[opponent]

        # Place bets
        challenger_user.place_bet(bet_amount)
        opponent_user.place_bet(bet_amount)

        # Determine the winner randomly
        winner = random.choice([challenger_user, opponent_user])
        print(f"The winner is {winner.username}!")

        # Winner takes the total bet amount
        total_amount = bet_amount * 2
        winner.win_bet(total_amount)

        return winner.username


# Example usage
if __name__ == "__main__":
    # Create users
    alice = User("Alice", 100.0)
    bob = User("Bob", 150.0)

    # Initialize a Duel Race
    duel_race = DuelRace()
    
    # Register users
    duel_race.register_user(alice)
    duel_race.register_user(bob)

    # Start a duel
    try:
        winner = duel_race.start_duel("Alice", "Bob", 50.0)
        print(f"Congratulations to {winner}!")
    except ValueError as e:
        print(f"Error: {e}")
```
