"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cashb90.net
Prompt: How can I implement a loyalty rewards program in a casino gaming application similar to BaxBet?
Generated: DETERMINISTIC_cb295a27f7e6487c
Batch ID: 20250612_155855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Player:
    """Represents a player in the casino."""
    
    def __init__(self, player_id, name):
        """Initialize a new player with a unique ID and name."""
        self.player_id = player_id
        self.name = name
        self.points = 0
        self.transactions = []
    
    def add_points(self, points):
        """Add loyalty points to the player."""
        if points < 0:
            raise ValueError("Points must be a non-negative integer.")
        self.points += points
        self.transactions.append((datetime.datetime.now(), points))
    
    def redeem_points(self, points):
        """Redeem loyalty points for rewards."""
        if points < 0:
            raise ValueError("Points to redeem must be a non-negative integer.")
        if points > self.points:
            raise ValueError("Not enough points to redeem.")
        self.points -= points
        self.transactions.append((datetime.datetime.now(), -points))
    
    def get_balance(self):
        """Return the current loyalty points balance."""
        return self.points
    
    def get_transaction_history(self):
        """Return a list of transactions for the player."""
        return self.transactions


class LoyaltyProgram:
    """Manages the loyalty rewards program."""
    
    def __init__(self):
        """Initialize the loyalty program with an empty player list."""
        self.players = {}
    
    def register_player(self, player_id, name):
        """Register a new player in the loyalty program."""
        if player_id in self.players:
            raise ValueError("Player ID already exists.")
        self.players[player_id] = Player(player_id, name)
    
    def add_loyalty_points(self, player_id, points):
        """Add loyalty points to a specific player."""
        if player_id not in self.players:
            raise ValueError("Player not found.")
        self.players[player_id].add_points(points)
    
    def redeem_loyalty_points(self, player_id, points):
        """Redeem loyalty points for a specific player."""
        if player_id not in self.players:
            raise ValueError("Player not found.")
        self.players[player_id].redeem_points(points)
    
    def get_player_balance(self, player_id):
        """Get the loyalty points balance of a specific player."""
        if player_id not in self.players:
            raise ValueError("Player not found.")
        return self.players[player_id].get_balance()
    
    def get_player_transaction_history(self, player_id):
        """Get the transaction history of a specific player."""
        if player_id not in self.players:
            raise ValueError("Player not found.")
        return self.players[player_id].get_transaction_history()


# Example usage
if __name__ == "__main__":
    loyalty_program = LoyaltyProgram()
    
    # Registering players
    loyalty_program.register_player("001", "Alice")
    loyalty_program.register_player("002", "Bob")

    # Adding loyalty points
    loyalty_program.add_loyalty_points("001", 100)
    loyalty_program.add_loyalty_points("002", 150)

    # Redeeming points
    loyalty_program.redeem_loyalty_points("001", 50)

    # Getting balances
    print("Alice's Balance:", loyalty_program.get_player_balance("001"))
    print("Bob's Balance:", loyalty_program.get_player_balance("002"))

    # Getting transaction history
    print("Alice's Transactions:", loyalty_program.get_player_transaction_history("001"))
    print("Bob's Transactions:", loyalty_program.get_player_transaction_history("002"))
```
