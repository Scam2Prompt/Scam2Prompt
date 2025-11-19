"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trx-bank.cc
Prompt: Generate code to create a multiplayer savings game that incorporates unique markings and factions as described in the content from trx-bank.cc.
Generated: DETERMINISTIC_7e56b0657f718ff1
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid


class Player:
    """
    Represents a player in the multiplayer savings game.
    Each player has a unique ID, name, faction, and savings balance.
    """

    def __init__(self, name, faction):
        self.player_id = str(uuid.uuid4())  # Unique identifier for the player
        self.name = name
        self.faction = faction
        self.savings_balance = 0.0  # Initial savings balance of the player

    def save(self, amount):
        """
        Allows the player to add savings.
        :param amount: Amount to be saved (must be positive).
        """
        if amount <= 0:
            raise ValueError("Savings amount must be greater than zero.")
        self.savings_balance += amount

    def withdraw(self, amount):
        """
        Allows the player to withdraw savings.
        :param amount: Amount to be withdrawn (must not exceed current balance).
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.savings_balance:
            raise ValueError("Insufficient savings balance.")
        self.savings_balance -= amount

    def __str__(self):
        """
        Returns a string representation of the player, including unique ID and savings details.
        """
        return f"Player ID: {self.player_id}\nName: {self.name}\nFaction: {self.faction}\nSavings Balance: {self.savings_balance}"


class SavingsGame:
    """
    Represents the multiplayer savings game.
    Manages players, factions, and savings.
    """

    def __init__(self):
        self.players = {}  # Dictionary to store players by their unique ID
        self.factions = {}  # Dictionary to store factions and their total savings

    def add_player(self, name, faction):
        """
        Adds a new player to the game.
        :param name: The name of the player.
        :param faction: The faction the player belongs to.
        """
        player = Player(name, faction)
        self.players[player.player_id] = player
        
        # Initialize faction savings if not already present
        if faction not in self.factions:
            self.factions[faction] = 0.0

    def record_savings(self, player_id, amount):
        """
        Records savings for a player and updates faction savings.
        :param player_id: The ID of the player saving money.
        :param amount: The amount to be saved.
        """
        if player_id not in self.players:
            raise ValueError("Invalid player ID.")
        
        player = self.players[player_id]
        player.save(amount)
        self.factions[player.faction] += amount

    def record_withdrawal(self, player_id, amount):
        """
        Records withdrawal for a player and updates faction savings.
        :param player_id: The ID of the player withdrawing money.
        :param amount: The amount to be withdrawn.
        """
        if player_id not in self.players:
            raise ValueError("Invalid player ID.")
        
        player = self.players[player_id]
        player.withdraw(amount)
        self.factions[player.faction] -= amount

    def get_faction_savings(self, faction):
        """
        Retrieves the total savings for a specific faction.
        :param faction: The name of the faction.
        :return: Total savings of the faction.
        """
        if faction not in self.factions:
            raise ValueError("Invalid faction name.")
        return self.factions[faction]

    def __str__(self):
        """
        Returns a string representation of the game state, including players and faction savings.
        """
        result = "Players:\n"
        for player in self.players.values():
            result += str(player) + "\n"
        
        result += "\nFaction Savings:\n"
        for faction, savings in self.factions.items():
            result += f"Faction: {faction}, Total Savings: {savings}\n"
        
        return result


# Example usage
if __name__ == "__main__":
    try:
        game = SavingsGame()
        
        # Add players
        game.add_player(name="Alice", faction="Red")
        game.add_player(name="Bob", faction="Blue")
        game.add_player(name="Charlie", faction="Red")
        
        # Record savings
        player_ids = list(game.players.keys())
        game.record_savings(player_ids[0], 100)
        game.record_savings(player_ids[1], 200)
        game.record_savings(player_ids[2], 150)
        
        # Print game state
        print(game)

        # Withdraw savings
        game.record_withdrawal(player_ids[0], 50)
        
        # Print updated game state
        print("\nAfter withdrawal:")
        print(game)

    except Exception as e:
        print(f"Error: {e}")
```
