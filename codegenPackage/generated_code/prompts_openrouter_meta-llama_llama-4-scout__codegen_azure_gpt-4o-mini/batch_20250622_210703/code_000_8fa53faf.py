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
import os

class Player:
    """Class to represent a handball player."""
    
    def __init__(self, name, age_group, contact_details):
        """
        Initialize a new player.

        :param name: str - Name of the player
        :param age_group: str - Age group of the player (e.g., KADETI, MLADINCI, STAREJŠI DEČKI)
        :param contact_details: dict - Contact details of the player (e.g., phone, email)
        """
        self.name = name
        self.age_group = age_group
        self.contact_details = contact_details

    def to_dict(self):
        """Convert player information to a dictionary."""
        return {
            'name': self.name,
            'age_group': self.age_group,
            'contact_details': self.contact_details
        }

class TeamManager:
    """Class to manage the handball team player information."""
    
    def __init__(self, team_name):
        """
        Initialize the team manager.

        :param team_name: str - Name of the team
        """
        self.team_name = team_name
        self.players = []
        self.data_file = f"{team_name}_players.json"
        self.load_players()

    def add_player(self, player):
        """Add a new player to the team."""
        self.players.append(player)
        self.save_players()

    def save_players(self):
        """Save player information to a JSON file."""
        try:
            with open(self.data_file, 'w') as file:
                json.dump([player.to_dict() for player in self.players], file, indent=4)
        except IOError as e:
            print(f"Error saving players to file: {e}")

    def load_players(self):
        """Load player information from a JSON file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    players_data = json.load(file)
                    self.players = [Player(**data) for data in players_data]
            except (IOError, json.JSONDecodeError) as e:
                print(f"Error loading players from file: {e}")

    def display_players(self):
        """Display all players in the team."""
        if not self.players:
            print("No players found.")
            return
        
        print(f"Players in {self.team_name}:")
        for player in self.players:
            print(f"Name: {player.name}, Age Group: {player.age_group}, Contact: {player.contact_details}")

def main():
    """Main function to manage the handball team."""
    team_manager = TeamManager("RK Kočevje")

    # Example of adding players
    player1 = Player("Janez Novak", "KADETI", {"phone": "012-345-678", "email": "janez.novak@example.com"})
    player2 = Player("Maja Kovač", "MLADINCI", {"phone": "987-654-321", "email": "maja.kovac@example.com"})
    
    team_manager.add_player(player1)
    team_manager.add_player(player2)

    # Display all players
    team_manager.display_players()

if __name__ == "__main__":
    main()
```
