"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockgametoken.pages.dev
Prompt: Develop a function to facilitate peer-to-peer $BLOCK token transfers within the BlockGames player network.
Generated: DETERMINISTIC_50701cce8f613662
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BlockToken:
    def __init__(self):
        """Initialize the BlockToken ledger with an empty dictionary."""
        self.ledger = {}

    def create_account(self, player_id):
        """Create a new account for a player with a balance of 0.

        Args:
            player_id (str): Unique identifier for the player.

        Raises:
            ValueError: If the account already exists.
        """
        if player_id in self.ledger:
            raise ValueError("Account already exists.")
        self.ledger[player_id] = 0.0

    def deposit(self, player_id, amount):
        """Deposit a specified amount into the player's account.

        Args:
            player_id (str): Unique identifier for the player.
            amount (float): Amount of tokens to deposit.

        Raises:
            ValueError: If the account does not exist or if the amount is negative.
        """
        if player_id not in self.ledger:
            raise ValueError("Account does not exist.")
        if amount < 0:
            raise ValueError("Deposit amount must be non-negative.")

        self.ledger[player_id] += amount

    def transfer(self, from_player, to_player, amount):
        """Transfer tokens from one player to another within the BlockGames network.

        Args:
            from_player (str): Unique identifier for the sender.
            to_player (str): Unique identifier for the recipient.
            amount (float): Amount of tokens to transfer.

        Raises:
            ValueError: If either account does not exist, if the amount is negative,
                        or if the sender has insufficient balance.
        """
        if from_player not in self.ledger or to_player not in self.ledger:
            raise ValueError("Both accounts must exist.")
        if amount < 0:
            raise ValueError("Transfer amount must be non-negative.")
        if self.ledger[from_player] < amount:
            raise ValueError("Insufficient balance for transfer.")

        self.ledger[from_player] -= amount
        self.ledger[to_player] += amount

    def get_balance(self, player_id):
        """Get the current balance of a player's account.

        Args:
            player_id (str): Unique identifier for the player.

        Returns:
            float: Current balance of the player's account.

        Raises:
            ValueError: If the account does not exist.
        """
        if player_id not in self.ledger:
            raise ValueError("Account does not exist.")
        return self.ledger[player_id]

# Example usage:
if __name__ == "__main__":
    # Create a BlockToken instance
    block_token = BlockToken()

    # Create accounts for players
    block_token.create_account("player1")
    block_token.create_account("player2")

    # Deposit tokens into player accounts
    block_token.deposit("player1", 100.0)

    # Transfer tokens between players
    block_token.transfer("player1", "player2", 50.0)

    # Print balances after transfer
    print("Player 1 Balance:", block_token.get_balance("player1"))  # Expected: 50.0
    print("Player 2 Balance:", block_token.get_balance("player2"))  # Expected: 50.0
```
