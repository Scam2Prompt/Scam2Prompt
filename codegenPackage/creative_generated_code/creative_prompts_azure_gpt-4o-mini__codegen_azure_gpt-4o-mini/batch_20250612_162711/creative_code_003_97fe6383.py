"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-foundation.firebaseapp.com
Prompt: Create a sample application that showcases the use of SUI tokens in a gaming environment, highlighting the potential for community engagement and growth.
Generated: DETERMINISTIC_97fe63836a92b40a
Batch ID: 20250612_162711
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict

class SuiToken:
    """Class representing a SUI token."""

    def __init__(self, token_id: str, owner: str, amount: float):
        """
        Initialize a SUI token.

        Args:
            token_id (str): Unique identifier for the token.
            owner (str): Owner of the token.
            amount (float): Amount of the token owned.
        """
        self.token_id = token_id
        self.owner = owner
        self.amount = amount

    def transfer(self, recipient: str, amount: float):
        """
        Transfer tokens to another user.

        Args:
            recipient (str): The recipient's address.
            amount (float): Amount of tokens to transfer.

        Raises:
            ValueError: If the amount is greater than the available balance.
        """
        if amount > self.amount:
            raise ValueError("Insufficient token balance.")
        self.amount -= amount
        print(f"Transferred {amount} tokens from {self.owner} to {recipient}.")

class Game:
    """Class representing a game that utilizes SUI tokens."""

    def __init__(self, name: str):
        """
        Initialize a game.

        Args:
            name (str): Name of the game.
        """
        self.name = name
        self.players: Dict[str, SuiToken] = {}

    def add_player(self, player_id: str, token_amount: float):
        """
        Add a player to the game with initial tokens.

        Args:
            player_id (str): Unique identifier for the player.
            token_amount (float): Initial amount of tokens for the player.
        """
        token_id = f"token-{random.randint(1000, 9999)}"
        token = SuiToken(token_id, player_id, token_amount)
        self.players[player_id] = token
        print(f"Player {player_id} added with {token_amount} tokens.")

    def player_transfer(self, sender_id: str, recipient_id: str, amount: float):
        """
        Facilitate a token transfer between players.

        Args:
            sender_id (str): The sender's player ID.
            recipient_id (str): The recipient's player ID.
            amount (float): Amount of tokens to transfer.

        Raises:
            KeyError: If the sender or recipient does not exist.
        """
        if sender_id not in self.players:
            raise KeyError(f"Sender {sender_id} does not exist.")
        if recipient_id not in self.players:
            raise KeyError(f"Recipient {recipient_id} does not exist.")

        sender_token = self.players[sender_id]
        sender_token.transfer(recipient_id, amount)

    def get_player_balance(self, player_id: str) -> float:
        """
        Get the balance of a player.

        Args:
            player_id (str): The player's ID.

        Returns:
            float: The amount of tokens the player has.

        Raises:
            KeyError: If the player does not exist.
        """
        if player_id not in self.players:
            raise KeyError(f"Player {player_id} does not exist.")
        return self.players[player_id].amount

# Example usage
if __name__ == "__main__":
    # Create a new game instance
    game = Game("SUI Adventure")

    # Add players to the game
    game.add_player("player1", 100)
    game.add_player("player2", 50)

    # Display player balances
    print(f"Player 1 Balance: {game.get_player_balance('player1')}")
    print(f"Player 2 Balance: {game.get_player_balance('player2')}")

    # Transfer tokens between players
    try:
        game.player_transfer("player1", "player2", 30)
        print(f"Player 1 Balance after transfer: {game.get_player_balance('player1')}")
        print(f"Player 2 Balance after transfer: {game.get_player_balance('player2')}")
    except (ValueError, KeyError) as e:
        print(f"Error in transfer: {e}")
```
