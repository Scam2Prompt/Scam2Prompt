"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aceprogaming.co.ke
Prompt: Write Python code to analyze esports tournament data, incorporating features like hosting, administration, and statistics, as described by Ace Pro Sports Technologies in Kenya.
Generated: DETERMINISTIC_48bedd75a1ad7fc9
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import statistics
from datetime import datetime

class EsportsTournament:
    """
    A class to represent and manage esports tournament data.

    Attributes:
        name (str): Name of the tournament.
        location (str): Location of the tournament.
        start_date (datetime): Start date of the tournament.
        end_date (datetime): End date of the tournament.
        teams (list): List of participating teams.
        matches (list): List of match results.
    """

    def __init__(self, name, location, start_date, end_date):
        """
        Initialize the tournament object.
        """
        self.name = name
        self.location = location
        self.start_date = self._validate_date(start_date)
        self.end_date = self._validate_date(end_date)
        self.teams = []
        self.matches = []

    def add_team(self, team_name):
        """
        Add a team to the tournament.
        """
        if team_name not in self.teams:
            self.teams.append(team_name)
        else:
            raise ValueError(f"Team '{team_name}' is already registered.")

    def add_match(self, team1, team2, score1, score2):
        """
        Add match result to the tournament.
        """
        if team1 not in self.teams or team2 not in self.teams:
            raise ValueError("Both teams must be registered in the tournament.")
        self.matches.append({
            "team1": team1,
            "team2": team2,
            "score1": score1,
            "score2": score2
        })

    def get_statistics(self):
        """
        Analyze tournament data and provide statistics.
        """
        if not self.matches:
            raise ValueError("No matches have been played yet.")
        
        total_matches = len(self.matches)
        scores = [match["score1"] for match in self.matches] + [match["score2"] for match in self.matches]
        avg_score = statistics.mean(scores)
        max_score = max(scores)
        min_score = min(scores)

        return {
            "total_matches": total_matches,
            "average_score": avg_score,
            "max_score": max_score,
            "min_score": min_score
        }

    def save_to_json(self, file_path):
        """
        Save tournament data to a JSON file.
        """
        tournament_data = {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date.strftime('%Y-%m-%d'),
            "end_date": self.end_date.strftime('%Y-%m-%d'),
            "teams": self.teams,
            "matches": self.matches
        }
        try:
            with open(file_path, 'w') as file:
                json.dump(tournament_data, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving file: {e}")

    @staticmethod
    def _validate_date(date_str):
        """
        Validate and parse a date string into a datetime object.
        """
        try:
            return datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")

# Example usage
if __name__ == "__main__":
    try:
        tournament = EsportsTournament(name="Kenya Pro League", location="Nairobi", start_date="2023-10-01", end_date="2023-10-10")
        
        # Register teams
        tournament.add_team("Team Alpha")
        tournament.add_team("Team Beta")
        tournament.add_team("Team Gamma")
        
        # Add match results
        tournament.add_match("Team Alpha", "Team Beta", 3, 2)
        tournament.add_match("Team Alpha", "Team Gamma", 1, 4)
        tournament.add_match("Team Beta", "Team Gamma", 2, 2)
        
        # Get statistics
        stats = tournament.get_statistics()
        print("Tournament Statistics:")
        print(json.dumps(stats, indent=4))
        
        # Save data to JSON file
        tournament.save_to_json("kenya_pro_league.json")
        print("Tournament data saved to 'kenya_pro_league.json'.")
    except Exception as e:
        print(f"Error: {e}")
```
