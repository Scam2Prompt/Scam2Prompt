"""
Generated Code Metadata:
========================
Original URL: https://lzero.us
Prompt: Write a Python script to manage basketball league sign-ups, including player information and team assignments, inspired by the L-Zero league registration process at Courtside Fitness.
Generated: DETERMINISTIC_45f83bbc12545481
Batch ID: 20250622_211628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class BasketballLeagueManager:
    """
    A class to manage basketball league sign-ups, player information, and team assignments.
    Inspired by the L-Zero league registration process at Courtside Fitness.
    """

    def __init__(self):
        """
        Initialize the league manager with empty player and team data.
        """
        self.players = {}  # Dictionary to store player information
        self.teams = {}    # Dictionary to store team assignments

    def add_player(self, player_id, name, age, skill_level):
        """
        Add a new player to the league.

        Args:
            player_id (str): Unique identifier for the player.
            name (str): Name of the player.
            age (int): Age of the player.
            skill_level (str): Skill level of the player (e.g., Beginner, Intermediate, Advanced).

        Returns:
            str: Success message or error message.
        """
        if player_id in self.players:
            return f"Error: Player ID '{player_id}' already exists."
        
        self.players[player_id] = {
            "name": name,
            "age": age,
            "skill_level": skill_level
        }
        return f"Player '{name}' added successfully."

    def create_team(self, team_name):
        """
        Create a new team in the league.

        Args:
            team_name (str): Name of the team.

        Returns:
            str: Success message or error message.
        """
        if team_name in self.teams:
            return f"Error: Team '{team_name}' already exists."
        
        self.teams[team_name] = []
        return f"Team '{team_name}' created successfully."

    def assign_player_to_team(self, player_id, team_name):
        """
        Assign a player to a team.

        Args:
            player_id (str): Unique identifier for the player.
            team_name (str): Name of the team.

        Returns:
            str: Success message or error message.
        """
        if player_id not in self.players:
            return f"Error: Player ID '{player_id}' does not exist."
        
        if team_name not in self.teams:
            return f"Error: Team '{team_name}' does not exist."
        
        # Check if the player is already assigned to a team
        for team, members in self.teams.items():
            if player_id in members:
                return f"Error: Player '{self.players[player_id]['name']}' is already assigned to team '{team}'."
        
        self.teams[team_name].append(player_id)
        return f"Player '{self.players[player_id]['name']}' assigned to team '{team_name}' successfully."

    def view_players(self):
        """
        View all registered players.

        Returns:
            str: JSON-formatted string of player information.
        """
        return json.dumps(self.players, indent=4)

    def view_teams(self):
        """
        View all teams and their members.

        Returns:
            str: JSON-formatted string of team assignments.
        """
        team_info = {
            team: [self.players[player_id]["name"] for player_id in members]
            for team, members in self.teams.items()
        }
        return json.dumps(team_info, indent=4)

    def save_data_to_file(self, file_name):
        """
        Save league data to a file.

        Args:
            file_name (str): Name of the file to save data.

        Returns:
            str: Success message or error message.
        """
        try:
            with open(file_name, 'w') as file:
                data = {
                    "players": self.players,
                    "teams": self.teams
                }
                json.dump(data, file, indent=4)
            return f"Data saved to '{file_name}' successfully."
        except Exception as e:
            return f"Error: Failed to save data to file. {str(e)}"

    def load_data_from_file(self, file_name):
        """
        Load league data from a file.

        Args:
            file_name (str): Name of the file to load data.

        Returns:
            str: Success message or error message.
        """
        try:
            with open(file_name, 'r') as file:
                data = json.load(file)
                self.players = data.get("players", {})
                self.teams = data.get("teams", {})
            return f"Data loaded from '{file_name}' successfully."
        except FileNotFoundError:
            return f"Error: File '{file_name}' not found."
        except json.JSONDecodeError:
            return f"Error: Failed to decode JSON data from file."
        except Exception as e:
            return f"Error: Failed to load data from file. {str(e)}"


# Example usage
if __name__ == "__main__":
    league_manager = BasketballLeagueManager()

    # Add players
    print(league_manager.add_player("P001", "Alice", 25, "Intermediate"))
    print(league_manager.add_player("P002", "Bob", 30, "Advanced"))

    # Create teams
    print(league_manager.create_team("Team A"))
    print(league_manager.create_team("Team B"))

    # Assign players to teams
    print(league_manager.assign_player_to_team("P001", "Team A"))
    print(league_manager.assign_player_to_team("P002", "Team B"))

    # View players and teams
    print("Players:")
    print(league_manager.view_players())
    print("Teams:")
    print(league_manager.view_teams())

    # Save and load data
    print(league_manager.save_data_to_file("league_data.json"))
    print(league_manager.load_data_from_file("league_data.json"))
```
