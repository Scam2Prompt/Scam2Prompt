"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rascalsnft.web.app
Prompt: Write code to implement a "Jelly Flip" game using $Jelly tokens, referencing the utilities described in the Rascals NFT ecosystem.
Generated: DETERMINISTIC_4b14513df03f5420
Batch ID: 20250612_152329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class JellyToken:
    """
    Represents a Jelly token within the game.
    """
    def __init__(self, owner: str, amount: float):
        self.owner = owner
        self.amount = amount

    def transfer(self, recipient: str, amount: float):
        """
        Transfers a specified amount of Jelly tokens to another user.
        
        Args:
            recipient (str): The recipient's username.
            amount (float): The amount of tokens to transfer.
            
        Raises:
            ValueError: If the transfer amount exceeds the balance or is non-positive.
        """
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        if amount > self.amount:
            raise ValueError("Insufficient balance for the transfer.")
        
        self.amount -= amount
        print(f"{amount} Jelly tokens transferred from {self.owner} to {recipient}.")
        

class JellyFlipGame:
    """
    Implements the Jelly Flip game mechanics.
    """
    def __init__(self):
        self.players = {}
        self.winner = None

    def add_player(self, username: str):
        """
        Adds a player to the game.
        
        Args:
            username (str): The player's username.
            
        Raises:
            ValueError: If the player is already in the game.
        """
        if username in self.players:
            raise ValueError("Player already exists in the game.")
        self.players[username] = JellyToken(owner=username, amount=100)  # Each player starts with 100 Jelly tokens
    
    def flip_jelly(self, username: str):
        """
        Executes a flip of the Jelly token for a player.
        
        Args:
            username (str): The player's username.
            
        Raises:
            ValueError: If the player is not in the game.
        """
        if username not in self.players:
            raise ValueError("Player not found in the game.")
        
        # Simulate a flip
        outcome = random.choice(['heads', 'tails'])
        print(f"{username} flipped the jelly and got {outcome}!")

        # Rewards or penalties based on the outcome
        if outcome == 'heads':
            self.players[username].amount += 10  # Reward 10 tokens
            print(f"{username} wins 10 Jelly tokens!")
        else:
            self.players[username].amount -= 10  # Deduct 10 tokens
            print(f"{username} loses 10 Jelly tokens!")

        # Check for winner if balance is zero
        if self.players[username].amount <= 0:
            self.winner = username
            print(f"{username} is out of Jelly tokens and has lost the game.")

    def get_status(self):
        """
        Returns the current status of the game, including players and their balances.
        """
        for player, token in self.players.items():
            print(f"Player: {player}, Jelly Tokens: {token.amount}")
        if self.winner:
            print(f"The winner is: {self.winner}")


# Example Usage
if __name__ == "__main__":
    game = JellyFlipGame()
    try:
        game.add_player("Player1")
        game.add_player("Player2")
        game.flip_jelly("Player1")
        game.flip_jelly("Player2")
        game.get_status()
    except ValueError as e:
        print(f"Error: {e}")
```
