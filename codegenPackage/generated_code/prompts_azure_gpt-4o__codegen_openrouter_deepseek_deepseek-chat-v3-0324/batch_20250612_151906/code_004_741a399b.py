"""
Generated Code Metadata:
========================
Original URL: https://metacade-web.pages.dev
Prompt: Create a script to display tournament leaderboards for a gaming platform, similar to Metacade's competitive gaming features.
Generated: DETERMINISTIC_741a399bf7466587
Batch ID: 20250612_151906
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
from typing import List, Dict, Optional

class Tournament:
    """Represents a gaming tournament with participants and scores."""
    
    def __init__(self, name: str, start_date: str, end_date: str):
        """
        Initialize a tournament.
        
        Args:
            name: Name of the tournament
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
        """
        self.name = name
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        self.participants: Dict[str, int] = {}  # username: score
        
    def add_participant(self, username: str, initial_score: int = 0) -> None:
        """Add a participant to the tournament."""
        if username in self.participants:
            raise ValueError(f"Participant {username} already exists")
        self.participants[username] = initial_score
        
    def update_score(self, username: str, score_change: int) -> None:
        """Update a participant's score."""
        if username not in self.participants:
            raise ValueError(f"Participant {username} not found")
        self.participants[username] += score_change
        
    def get_leaderboard(self, top_n: Optional[int] = None) -> List[Dict[str, int]]:
        """
        Get the tournament leaderboard sorted by score.
        
        Args:
            top_n: Optional limit to top N players
            
        Returns:
            List of dicts with username and score, sorted descending
        """
        sorted_players = sorted(
            self.participants.items(),
            key=lambda item: item[1],
            reverse=True
        )
        
        if top_n is not None:
            sorted_players = sorted_players[:top_n]
            
        return [{"username": username, "score": score} for username, score in sorted_players]
    
    def is_active(self) -> bool:
        """Check if the tournament is currently active."""
        now = datetime.now()
        return self.start_date <= now <= self.end_date
    
    def to_json(self) -> str:
        """Serialize tournament data to JSON."""
        data = {
            "name": self.name,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "participants": self.participants
        }
        return json.dumps(data)
    
    @classmethod
    def from_json(cls, json_str: str) -> 'Tournament':
        """Deserialize JSON data to Tournament object."""
        data = json.loads(json_str)
        tournament = cls(
            name=data["name"],
            start_date=data["start_date"],
            end_date=data["end_date"]
        )
        tournament.participants = data["participants"]
        return tournament


class TournamentManager:
    """Manages multiple tournaments and provides leaderboard functionality."""
    
    def __init__(self):
        self.tournaments: Dict[str, Tournament] = {}  # name: Tournament
        
    def create_tournament(self, name: str, start_date: str, end_date: str) -> Tournament:
        """Create and store a new tournament."""
        if name in self.tournaments:
            raise ValueError(f"Tournament {name} already exists")
            
        tournament = Tournament(name, start_date, end_date)
        self.tournaments[name] = tournament
        return tournament
    
    def get_tournament(self, name: str) -> Tournament:
        """Retrieve a tournament by name."""
        if name not in self.tournaments:
            raise ValueError(f"Tournament {name} not found")
        return self.tournaments[name]
    
    def get_active_tournaments(self) -> List[Tournament]:
        """Get all currently active tournaments."""
        return [t for t in self.tournaments.values() if t.is_active()]
    
    def get_global_leaderboard(self, top_n: Optional[int] = None) -> List[Dict[str, int]]:
        """
        Get a combined leaderboard across all active tournaments.
        
        Args:
            top_n: Optional limit to top N players
            
        Returns:
            List of dicts with username and total score, sorted descending
        """
        combined_scores: Dict[str, int] = {}
        
        for tournament in self.get_active_tournaments():
            for username, score in tournament.participants.items():
                combined_scores[username] = combined_scores.get(username, 0) + score
                
        sorted_players = sorted(
            combined_scores.items(),
            key=lambda item: item[1],
            reverse=True
        )
        
        if top_n is not None:
            sorted_players = sorted_players[:top_n]
            
        return [{"username": username, "score": score} for username, score in sorted_players]
    
    def save_to_file(self, filename: str) -> None:
        """Save all tournaments to a JSON file."""
        data = {
            "tournaments": {
                name: tournament.to_json()
                for name, tournament in self.tournaments.items()
            }
        }
        with open(filename, 'w') as f:
            json.dump(data, f)
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'TournamentManager':
        """Load tournaments from a JSON file."""
        manager = cls()
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for name, tournament_json in data["tournaments"].items():
                    manager.tournaments[name] = Tournament.from_json(tournament_json)
        except FileNotFoundError:
            pass  # Return empty manager if file doesn't exist
        return manager


def display_leaderboard(leaderboard: List[Dict[str, int]], title: str = "Leaderboard") -> None:
    """Display a formatted leaderboard in the console."""
    print(f"\n=== {title} ===")
    print("{:<5} {:<20} {:<10}".format("Rank", "Username", "Score"))
    print("-" * 35)
    
    for rank, entry in enumerate(leaderboard, start=1):
        print("{:<5} {:<20} {:<10}".format(
            rank,
            entry["username"],
            entry["score"]
        ))


# Example usage
if __name__ == "__main__":
    # Initialize manager
    manager = TournamentManager()
    
    # Try to load existing data
    manager = TournamentManager.load_from_file("tournaments.json")
    
    # Create some tournaments
    try:
        manager.create_tournament(
            "Summer Championship",
            "2023-06-01",
            "2023-08-31"
        )
        
        manager.create_tournament(
            "Winter Showdown",
            "2023-12-01",
            "2024-02-28"
        )
    except ValueError as e:
        print(f"Tournament creation error: {e}")
    
    # Add participants and scores
    summer = manager.get_tournament("Summer Championship")
    try:
        summer.add_participant("player1", 100)
        summer.add_participant("player2", 150)
        summer.add_participant("player3", 75)
        
        summer.update_score("player1", 50)
        summer.update_score("player3", 25)
    except ValueError as e:
        print(f"Participant error: {e}")
    
    # Display leaderboards
    display_leaderboard(summer.get_leaderboard(), "Summer Championship Leaderboard")
    display_leaderboard(manager.get_global_leaderboard(), "Global Leaderboard")
    
    # Save data
    manager.save_to_file("tournaments.json")
```
