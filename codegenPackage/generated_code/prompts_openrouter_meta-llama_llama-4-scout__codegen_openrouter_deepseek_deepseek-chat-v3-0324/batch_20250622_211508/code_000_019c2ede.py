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
import os
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class TournamentManager:
    """
    A class to manage esports tournament data including teams, players, matches, and scores.
    """

    def __init__(self, data_file: str = "tournament_data.json"):
        """
        Initialize the TournamentManager with a data file.

        Args:
            data_file (str): Path to the JSON file storing tournament data.
        """
        self.data_file = data_file
        self.data = self._load_data()

    def _load_data(self) -> Dict:
        """
        Load tournament data from the JSON file. If the file doesn't exist, initialize with empty data.

        Returns:
            Dict: Tournament data.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as file:
                    return json.load(file)
            return {
                "teams": {},
                "players": {},
                "matches": {},
                "tournaments": {}
            }
        except Exception as e:
            raise RuntimeError(f"Failed to load data: {e}")

    def _save_data(self) -> None:
        """
        Save the current tournament data to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.data, file, indent=4)
        except Exception as e:
            raise RuntimeError(f"Failed to save data: {e}")

    def add_team(self, team_id: str, name: str, coach: str) -> None:
        """
        Add a new team to the tournament data.

        Args:
            team_id (str): Unique identifier for the team.
            name (str): Name of the team.
            coach (str): Name of the team's coach.
        """
        if team_id in self.data["teams"]:
            raise ValueError(f"Team with ID {team_id} already exists.")
        self.data["teams"][team_id] = {
            "name": name,
            "coach": coach,
            "players": []
        }
        self._save_data()

    def add_player(self, player_id: str, name: str, team_id: str, role: str) -> None:
        """
        Add a new player to a team.

        Args:
            player_id (str): Unique identifier for the player.
            name (str): Name of the player.
            team_id (str): ID of the team the player belongs to.
            role (str): Role of the player (e.g., 'Captain', 'Support').
        """
        if player_id in self.data["players"]:
            raise ValueError(f"Player with ID {player_id} already exists.")
        if team_id not in self.data["teams"]:
            raise ValueError(f"Team with ID {team_id} does not exist.")
        
        self.data["players"][player_id] = {
            "name": name,
            "team_id": team_id,
            "role": role
        }
        self.data["teams"][team_id]["players"].append(player_id)
        self._save_data()

    def create_tournament(self, tournament_id: str, name: str, start_date: str, end_date: str) -> None:
        """
        Create a new tournament.

        Args:
            tournament_id (str): Unique identifier for the tournament.
            name (str): Name of the tournament.
            start_date (str): Start date in 'YYYY-MM-DD' format.
            end_date (str): End date in 'YYYY-MM-DD' format.
        """
        if tournament_id in self.data["tournaments"]:
            raise ValueError(f"Tournament with ID {tournament_id} already exists.")
        
        try:
            datetime.strptime(start_date, "%Y-%m-%d")
            datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")

        self.data["tournaments"][tournament_id] = {
            "name": name,
            "start_date": start_date,
            "end_date": end_date,
            "matches": []
        }
        self._save_data()

    def schedule_match(
        self,
        match_id: str,
        tournament_id: str,
        team1_id: str,
        team2_id: str,
        scheduled_time: str,
        venue: str
    ) -> None:
        """
        Schedule a match between two teams in a tournament.

        Args:
            match_id (str): Unique identifier for the match.
            tournament_id (str): ID of the tournament.
            team1_id (str): ID of the first team.
            team2_id (str): ID of the second team.
            scheduled_time (str): Scheduled time in 'YYYY-MM-DD HH:MM' format.
            venue (str): Venue of the match.
        """
        if match_id in self.data["matches"]:
            raise ValueError(f"Match with ID {match_id} already exists.")
        if tournament_id not in self.data["tournaments"]:
            raise ValueError(f"Tournament with ID {tournament_id} does not exist.")
        if team1_id not in self.data["teams"] or team2_id not in self.data["teams"]:
            raise ValueError("One or both teams do not exist.")

        try:
            datetime.strptime(scheduled_time, "%Y-%m-%d %H:%M")
        except ValueError:
            raise ValueError("Invalid datetime format. Use 'YYYY-MM-DD HH:MM'.")

        self.data["matches"][match_id] = {
            "tournament_id": tournament_id,
            "team1_id": team1_id,
            "team2_id": team2_id,
            "scheduled_time": scheduled_time,
            "venue": venue,
            "score": None,
            "winner": None
        }
        self.data["tournaments"][tournament_id]["matches"].append(match_id)
        self._save_data()

    def record_score(self, match_id: str, score: Tuple[int, int], winner_id: str) -> None:
        """
        Record the score and winner of a match.

        Args:
            match_id (str): ID of the match.
            score (Tuple[int, int]): Scores of team1 and team2.
            winner_id (str): ID of the winning team.
        """
        if match_id not in self.data["matches"]:
            raise ValueError(f"Match with ID {match_id} does not exist.")
        if winner_id not in (self.data["matches"][match_id]["team1_id"], self.data["matches"][match_id]["team2_id"]):
            raise ValueError("Winner must be one of the participating teams.")

        self.data["matches"][match_id]["score"] = score
        self.data["matches"][match_id]["winner"] = winner_id
        self._save_data()

    def get_team_info(self, team_id: str) -> Dict:
        """
        Retrieve information about a team.

        Args:
            team_id (str): ID of the team.

        Returns:
            Dict: Team information.
        """
        if team_id not in self.data["teams"]:
            raise ValueError(f"Team with ID {team_id} does not exist.")
        return self.data["teams"][team_id]

    def get_player_info(self, player_id: str) -> Dict:
        """
        Retrieve information about a player.

        Args:
            player_id (str): ID of the player.

        Returns:
            Dict: Player information.
        """
        if player_id not in self.data["players"]:
            raise ValueError(f"Player with ID {player_id} does not exist.")
        return self.data["players"][player_id]

    def get_tournament_matches(self, tournament_id: str) -> List[Dict]:
        """
        Retrieve all matches in a tournament.

        Args:
            tournament_id (str): ID of the tournament.

        Returns:
            List[Dict]: List of matches.
        """
        if tournament_id not in self.data["tournaments"]:
            raise ValueError(f"Tournament with ID {tournament_id} does not exist.")
        
        matches = []
        for match_id in self.data["tournaments"][tournament_id]["matches"]:
            matches.append(self.data["matches"][match_id])
        return matches

# Example usage
if __name__ == "__main__":
    manager = TournamentManager()

    # Add teams
    manager.add_team("T1", "Team Alpha", "Coach A")
    manager.add_team("T2", "Team Bravo", "Coach B")

    # Add players
    manager.add_player("P1", "Player One", "T1", "Captain")
    manager.add_player("P2", "Player Two", "T1", "Support")
    manager.add_player("P3", "Player Three", "T2", "Captain")

    # Create tournament
    manager.create_tournament("TN1", "Kenya Esports Cup", "2023-12-01", "2023-12-10")

    # Schedule matches
    manager.schedule_match("M1", "TN1", "T1", "T2", "2023-12-05 14:00", "Nairobi Arena")

    # Record score
    manager.record
