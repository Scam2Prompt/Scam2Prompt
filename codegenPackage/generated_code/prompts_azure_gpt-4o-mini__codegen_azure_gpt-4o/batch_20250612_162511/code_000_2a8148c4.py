"""
Generated Code Metadata:
========================
Original URL: https://simemes.vercel.app
Prompt: Write a Python script that simulates the registration process for the SIMemes game, including the allocation of resources like 10K Pebble and 50K Poop.
Generated: DETERMINISTIC_2a8148c44ad502a3
Batch ID: 20250612_162511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid

class SIMemesGameRegistration:
    """
    A class to handle the registration process for the SIMemes game.
    Each player is allocated initial resources: 10K Pebble and 50K Poop.
    """

    def __init__(self):
        # Dictionary to store registered players and their resources
        self.players = {}

    def register_player(self, player_name):
        """
        Registers a new player in the game.
        
        Args:
            player_name (str): The name of the player to register.
        
        Returns:
            dict: A dictionary containing the player's ID, name, and allocated resources.
        """
        if not player_name or not isinstance(player_name, str):
            raise ValueError("Player name must be a non-empty string.")

        # Generate a unique ID for the player
        player_id = str(uuid.uuid4())

        # Allocate initial resources
        initial_resources = {
            "Pebble": 10000,  # 10K Pebble
            "Poop": 50000     # 50K Poop
        }

        # Store player information
        self.players[player_id] = {
            "name": player_name,
            "resources": initial_resources
        }

        return {
            "player_id": player_id,
            "name": player_name,
            "resources": initial_resources
        }

    def get_player_info(self, player_id):
        """
        Retrieves information about a registered player.
        
        Args:
            player_id (str): The unique ID of the player.
        
        Returns:
            dict: A dictionary containing the player's name and resources.
        """
        if player_id not in self.players:
            raise KeyError(f"No player found with ID: {player_id}")

        return self.players[player_id]

    def list_all_players(self):
        """
        Lists all registered players and their resources.
        
        Returns:
            dict: A dictionary of all players with their IDs, names, and resources.
        """
        return self.players


# Main script
if __name__ == "__main__":
    try:
        # Create an instance of the registration system
        simemes_game = SIMemesGameRegistration()

        # Register a few players
        player1 = simemes_game.register_player("Alice")
        print(f"Player registered: {player1}")

        player2 = simemes_game.register_player("Bob")
        print(f"Player registered: {player2}")

        # Retrieve player information
        player_info = simemes_game.get_player_info(player1["player_id"])
        print(f"Player info: {player_info}")

        # List all registered players
        all_players = simemes_game.list_all_players()
        print(f"All registered players: {all_players}")

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")
```
