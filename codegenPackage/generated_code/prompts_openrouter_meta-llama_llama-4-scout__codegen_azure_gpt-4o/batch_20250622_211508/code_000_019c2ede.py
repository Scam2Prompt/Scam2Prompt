"""
Generated Code Metadata:
========================
Original URL: https://aceprogaming.co.ke
Prompt: Write a Python script to manage esports tournament data, including team and player information, match schedules, and scores, inspired by Ace Pro Sports Technologies' operations in Kenya.
Generated: DETERMINISTIC_019c2ede139d2c54
Batch ID: 20250622_211508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime


class EsportsTournamentManager:
    """
    A class to manage esports tournament data including teams, players, match schedules, and scores.
    """

    def __init__(self):
        # Initialize data structures to store tournament information
        self.teams = {}  # Format: {team_id: {"name": str, "players": [str]}}
        self.matches = {}  # Format: {match_id: {"teams": [team_id, team_id], "schedule": datetime, "scores": [int, int]}}

    def add_team(self, team_id, team_name, players):
        """
        Add a new team to the tournament.

        :param team_id: Unique identifier for the team.
        :param team_name: Name of the team.
        :param players: List of player names in the team.
        """
        if team_id in self.teams:
            raise ValueError(f"Team ID '{team_id}' already exists.")
        self.teams[team_id] = {"name": team_name, "players": players}

    def add_match(self, match_id, team_ids, schedule):
        """
        Add a new match to the tournament.

        :param match_id: Unique identifier for the match.
        :param team_ids: List of two team IDs participating in the match.
        :param schedule: Scheduled date and time for the match (datetime object).
        """
        if match_id in self.matches:
            raise ValueError(f"Match ID '{match_id}' already exists.")
        if len(team_ids) != 2 or any(team_id not in self.teams for team_id in team_ids):
            raise ValueError("Invalid team IDs provided.")
        self.matches[match_id] = {"teams": team_ids, "schedule": schedule, "scores": [None, None]}

    def record_match_score(self, match_id, scores):
        """
        Record the scores for a match.

        :param match_id: Unique identifier for the match.
        :param scores: List of two scores corresponding to the two teams.
        """
        if match_id not in self.matches:
            raise ValueError(f"Match ID '{match_id}' does not exist.")
        if len(scores) != 2 or not all(isinstance(score, int) for score in scores):
            raise ValueError("Scores must be a list of two integers.")
        self.matches[match_id]["scores"] = scores

    def get_team_info(self, team_id):
        """
        Retrieve information about a team.

        :param team_id: Unique identifier for the team.
        :return: Dictionary containing team information.
        """
        if team_id not in self.teams:
            raise ValueError(f"Team ID '{team_id}' does not exist.")
        return self.teams[team_id]

    def get_match_info(self, match_id):
        """
        Retrieve information about a match.

        :param match_id: Unique identifier for the match.
        :return: Dictionary containing match information.
        """
        if match_id not in self.matches:
            raise ValueError(f"Match ID '{match_id}' does not exist.")
        return self.matches[match_id]

    def save_data_to_file(self, file_path):
        """
        Save tournament data to a JSON file.

        :param file_path: Path to the file where data will be saved.
        """
        data = {"teams": self.teams, "matches": self.matches}
        try:
            with open(file_path, "w") as file:
                json.dump(data, file, default=str, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save data to file: {e}")

    def load_data_from_file(self, file_path):
        """
        Load tournament data from a JSON file.

        :param file_path: Path to the file from which data will be loaded.
        """
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                self.teams = data.get("teams", {})
                self.matches = data.get("matches", {})
        except IOError as e:
            raise IOError(f"Failed to load data from file: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse JSON data: {e}")


# Example usage
if __name__ == "__main__":
    manager = EsportsTournamentManager()

    # Add teams
    manager.add_team("team1", "Warriors", ["Alice", "Bob", "Charlie"])
    manager.add_team("team2", "Titans", ["Dave", "Eve", "Frank"])

    # Add a match
    match_date = datetime(2023, 11, 15, 18, 0)  # November 15, 2023, 6:00 PM
    manager.add_match("match1", ["team1", "team2"], match_date)

    # Record scores
    manager.record_match_score("match1", [3, 2])

    # Retrieve and display information
    print("Team Info:", manager.get_team_info("team1"))
    print("Match Info:", manager.get_match_info("match1"))

    # Save and load data
    manager.save_data_to_file("tournament_data.json")
    manager.load_data_from_file("tournament_data.json")
```
