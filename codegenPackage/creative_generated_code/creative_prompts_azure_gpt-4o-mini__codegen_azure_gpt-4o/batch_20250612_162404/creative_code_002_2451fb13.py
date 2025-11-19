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
import uuid
from datetime import datetime

class BettingSystem:
    def __init__(self):
        """
        Initialize the Betting System with empty user and duel race data.
        """
        self.users = {}  # User data storage in the format {user_id: user_info}
        self.duel_races = {}  # Duel race storage in the format {race_id: race_info}

    def register_user(self, username):
        """
        Register a new user to the Bitcoin Dogs Club.

        :param username: The username of the new user.
        :return: A unique user ID.
        """
        user_id = str(uuid.uuid4())
        self.users[user_id] = {
            'username': username,
            'balance': 0,  # Initial balance is set to 0
        }
        return user_id

    def deposit_funds(self, user_id, amount):
        """
        Deposit funds into a user's account.

        :param user_id: The ID of the user depositing funds.
        :param amount: The amount to deposit.
        :return: Success message or error message.
        """
        if user_id not in self.users:
            return "Error: User not found."
        if amount <= 0:
            return "Error: Deposit amount must be greater than zero."

        self.users[user_id]['balance'] += amount
        return f"Deposit successful. Current balance: {self.users[user_id]['balance']}"

    def create_duel(self, challenger_id, opponent_id, stake_amount):
        """
        Create a new Duel Race between two users.

        :param challenger_id: The ID of the challenger.
        :param opponent_id: The ID of the opponent.
        :param stake_amount: The amount each user will stake in the race.
        :return: Race ID or error message.
        """
        if challenger_id not in self.users or opponent_id not in self.users:
            return "Error: One or both users not found."
        if stake_amount <= 0:
            return "Error: Stake amount must be greater than zero."
        if self.users[challenger_id]['balance'] < stake_amount or self.users[opponent_id]['balance'] < stake_amount:
            return "Error: Insufficient balance for one or both users."

        # Deduct funds from users' balances
        self.users[challenger_id]['balance'] -= stake_amount
        self.users[opponent_id]['balance'] -= stake_amount

        race_id = str(uuid.uuid4())
        self.duel_races[race_id] = {
            'challenger_id': challenger_id,
            'opponent_id': opponent_id,
            'stake_amount': stake_amount,
            'created_at': datetime.now(),
            'winner': None,  # Winner will be decided later
        }
        return f"Duel created successfully. Race ID: {race_id}"

    def decide_winner(self, race_id, winner_id):
        """
        Decide the winner for a specific Duel Race.

        :param race_id: The ID of the race.
        :param winner_id: The ID of the user who won the race.
        :return: Success message or error message.
        """
        if race_id not in self.duel_races:
            return "Error: Race not found."
        if winner_id not in self.users:
            return "Error: Winner not found."
        race = self.duel_races[race_id]
        if winner_id != race['challenger_id'] and winner_id != race['opponent_id']:
            return "Error: Winner must be one of the participants."

        # Assign winnings to the winner
        total_stake = race['stake_amount'] * 2
        self.users[winner_id]['balance'] += total_stake
        race['winner'] = winner_id
        return f"Winner decided successfully. {self.users[winner_id]['username']} wins {total_stake} BTC!"

    def get_user_info(self, user_id):
        """
        Get information about a specific user.

        :param user_id: The ID of the user.
        :return: User information or error message.
        """
        if user_id not in self.users:
            return "Error: User not found."
        return self.users[user_id]

    def get_duel_info(self, race_id):
        """
        Get information about a specific Duel Race.

        :param race_id: The ID of the race.
        :return: Race information or error message.
        """
        if race_id not in self.duel_races:
            return "Error: Race not found."
        return self.duel_races[race_id]


# Example Usage
if __name__ == "__main__":
    system = BettingSystem()

    # Register users
    user1 = system.register_user("Alice")
    user2 = system.register_user("Bob")

    # Deposit funds
    print(system.deposit_funds(user1, 50))
    print(system.deposit_funds(user2, 50))

    # Create a duel race
    race_id = system.create_duel(user1, user2, 20)
    print(race_id)

    # Decide the winner
    print(system.decide_winner(race_id.split(": ")[-1], user1))

    # Get user info
    print(system.get_user_info(user1))
    print(system.get_user_info(user2))

    # Get duel info
    print(system.get_duel_info(race_id.split(": ")[-1]))
```
