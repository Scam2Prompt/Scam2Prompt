"""
Generated Code Metadata:
========================
Original URL: https://rokometni.agencijau3p.si
Prompt: Write a Python script to manage handball team player information for RK Kočevje, including player names, age groups (e.g., KADETI, MLADINCI, STAREJŠI DEČKI), and contact details.
Generated: DETERMINISTIC_8fa53faf8070d04b
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class HandballTeamManager:
    """
    A class to manage handball team player information for RK Kočevje.
    """

    def __init__(self):
        """
        Initializes the HandballTeamManager with an empty list of players.
        """
        self.players = []

    def add_player(self, name, age_group, contact_details):
        """
        Adds a new player to the team.

        :param name: str - The name of the player.
        :param age_group: str - The age group of the player (e.g., KADETI, MLADINCI, STAREJŠI DEČKI).
        :param contact_details: str - The contact details of the player.
        """
        if age_group not in ["KADETI", "MLADINCI", "STAREJŠI DEČKI"]:
            raise ValueError("Invalid age group. Must be one of: KADETI, MLADINCI, STAREJŠI DEČKI.")
        
        player = {
            "name": name,
            "age_group": age_group,
            "contact_details": contact_details
        }
        self.players.append(player)

    def remove_player(self, name):
        """
        Removes a player from the team by name.

        :param name: str - The name of the player to remove.
        """
        for player in self.players:
            if player["name"] == name:
                self.players.remove(player)
                return
        raise ValueError(f"Player with name '{name}' not found.")

    def list_players(self):
        """
        Lists all players in the team.

        :return: list - A list of all players.
        """
        return self.players

    def save_to_file(self, filename):
        """
        Saves the player information to a JSON file.

        :param filename: str - The name of the file to save the data to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.players, file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename):
        """
        Loads player information from a JSON file.

        :param filename: str - The name of the file to load the data from.
        """
        try:
            with open(filename, 'r') as file:
                self.players = json.load(file)
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file '{filename}'.")

# Example usage
if __name__ == "__main__":
    manager = HandballTeamManager()

    # Adding players
    manager.add_player("Janez Novak", "KADETI", "janez.novak@example.com")
    manager.add_player("Ana Kovač", "MLADINCI", "ana.kovac@example.com")

    # Listing players
    print("Players:")
    for player in manager.list_players():
        print(player)

    # Saving to file
    manager.save_to_file("players.json")

    # Loading from file
    manager.load_from_file("players.json")
    print("\nLoaded Players:")
    for player in manager.list_players():
        print(player)

    # Removing a player
    manager.remove_player("Janez Novak")
    print("\nPlayers after removal:")
    for player in manager.list_players():
        print(player)
```
