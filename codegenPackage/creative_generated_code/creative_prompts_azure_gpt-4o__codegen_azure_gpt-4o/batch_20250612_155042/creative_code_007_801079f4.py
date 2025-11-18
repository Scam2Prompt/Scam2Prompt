"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simemes.vercel.app
Prompt: Create a game logic module in Python for SIMemes that incorporates the "Friend today, Rivals tomorrow" dynamic, allowing players to form alliances and betray others.
Generated: DETERMINISTIC_801079f45b7271b5
Batch ID: 20250612_155042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random


class SIMemesGame:
    """
    SIMemes Game Logic Module
    Implements "Friend today, Rivals tomorrow" dynamic where players can form alliances or betray others.
    """

    def __init__(self):
        self.players = {}  # Dictionary to store player data: {player_id: {"name": str, "alliance": set, "betrayals": int}}

    def add_player(self, player_id, name):
        """
        Adds a new player to the game.
        
        :param player_id: Unique identifier for the player.
        :param name: Name of the player.
        """
        if player_id in self.players:
            raise ValueError("Player ID already exists.")
        self.players[player_id] = {"name": name, "alliance": set(), "betrayals": 0}

    def form_alliance(self, player_id, ally_id):
        """
        Forms an alliance between two players.
        
        :param player_id: ID of the initiating player.
        :param ally_id: ID of the player to form an alliance with.
        """
        if player_id not in self.players or ally_id not in self.players:
            raise ValueError("One or both players do not exist.")
        if ally_id in self.players[player_id]["alliance"]:
            raise ValueError("Alliance already exists between these players.")
        self.players[player_id]["alliance"].add(ally_id)
        self.players[ally_id]["alliance"].add(player_id)

    def betray_ally(self, player_id, ally_id):
        """
        Betrays an ally, removing them from the alliance and incrementing the betrayal count.
        
        :param player_id: ID of the betraying player.
        :param ally_id: ID of the betrayed player.
        """
        if player_id not in self.players or ally_id not in self.players:
            raise ValueError("One or both players do not exist.")
        if ally_id not in self.players[player_id]["alliance"]:
            raise ValueError("Players are not allies.")
        self.players[player_id]["alliance"].remove(ally_id)
        self.players[ally_id]["alliance"].remove(player_id)
        self.players[player_id]["betrayals"] += 1

    def get_player_status(self, player_id):
        """
        Retrieves the status of a player, including alliances and betrayal count.
        
        :param player_id: ID of the player to query.
        :return: Dictionary with the player's name, alliances, and betrayal count.
        """
        if player_id not in self.players:
            raise ValueError("Player does not exist.")
        player = self.players[player_id]
        alliance_names = [self.players[ally_id]["name"] for ally_id in player["alliance"]]
        return {
            "name": player["name"],
            "alliances": alliance_names,
            "betrayals": player["betrayals"],
        }

    def simulate_random_betrayals(self):
        """
        Randomly selects players and simulates betrayals between them.
        """
        if len(self.players) < 2:
            raise ValueError("Not enough players to simulate betrayals.")
        
        # Get list of players who have alliances
        eligible_players = [
            player_id for player_id, data in self.players.items() if data["alliance"]
        ]
        
        if not eligible_players:
            raise ValueError("No alliances exist to betray.")
        
        # Randomly pick a betraying player and an ally
        betrayer_id = random.choice(eligible_players)
        ally_id = random.choice(list(self.players[betrayer_id]["alliance"]))
        
        self.betray_ally(betrayer_id, ally_id)

    def display_all_players(self):
        """
        Displays the status of all players in the game.
        """
        for player_id, data in self.players.items():
            status = self.get_player_status(player_id)
            print(
                f"Player: {status['name']}\nAlliances: {', '.join(status['alliances'])}\nBetrayals: {status['betrayals']}\n"
            )


# Example usage:
# Create a game instance
game = SIMemesGame()

# Add players
game.add_player(1, "Alice")
game.add_player(2, "Bob")
game.add_player(3, "Charlie")

# Form alliances
game.form_alliance(1, 2)  # Alice and Bob form an alliance
game.form_alliance(2, 3)  # Bob and Charlie form an alliance

# Simulate betrayals
game.simulate_random_betrayals()

# Display all players
game.display_all_players()
```
