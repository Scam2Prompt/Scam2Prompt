"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lethmixedslowpitch.com
Prompt: What features does Slo-Pitch Central offer for organizing and managing slo-pitch events effectively?
Generated: DETERMINISTIC_b8b7c61f6722b89c
Batch ID: 20250612_161745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Slo-Pitch Central Event Management System

This script provides an implementation for managing slo-pitch events, including features
for organizing teams, scheduling matches, and tracking results. The code is designed to be 
production-ready with proper error handling, documentation, and class-based structure.
"""

class Team:
    """Class representing a Slo-Pitch team."""
    
    def __init__(self, name):
        """Initialize a new Team with a name."""
        if not name:
            raise ValueError("Team name cannot be empty.")
        self.name = name
        self.players = []

    def add_player(self, player_name):
        """Add a player to the team."""
        if player_name in self.players:
            raise ValueError(f"Player {player_name} is already in the team.")
        self.players.append(player_name)

    def __str__(self):
        """Return a string representation of the Team."""
        return f"Team: {self.name}, Players: {', '.join(self.players)}"


class Match:
    """Class representing a Slo-Pitch match."""
    
    def __init__(self, team_a, team_b, date):
        """Initialize a new Match with two teams and a date."""
        if not isinstance(team_a, Team) or not isinstance(team_b, Team):
            raise ValueError("Both team_a and team_b must be instances of Team.")
        self.team_a = team_a
        self.team_b = team_b
        self.date = date
        self.score_a = 0
        self.score_b = 0

    def record_score(self, score_a, score_b):
        """Record the final score for the match."""
        if score_a < 0 or score_b < 0:
            raise ValueError("Scores must be non-negative.")
        self.score_a = score_a
        self.score_b = score_b

    def __str__(self):
        """Return a string representation of the Match."""
        return (f"Match on {self.date}: {self.team_a.name} vs {self.team_b.name}, "
                f"Score: {self.score_a}-{self.score_b}")


class Event:
    """Class representing a Slo-Pitch event."""
    
    def __init__(self, name):
        """Initialize a new Event with a name."""
        if not name:
            raise ValueError("Event name cannot be empty.")
        self.name = name
        self.teams = []
        self.matches = []

    def add_team(self, team):
        """Add a team to the event."""
        if not isinstance(team, Team):
            raise ValueError("team must be an instance of Team.")
        if team in self.teams:
            raise ValueError(f"Team {team.name} is already registered for the event.")
        self.teams.append(team)

    def schedule_match(self, team_a, team_b, date):
        """Schedule a match between two teams on a specific date."""
        if team_a not in self.teams or team_b not in self.teams:
            raise ValueError("Both teams must be part of the event.")
        match = Match(team_a, team_b, date)
        self.matches.append(match)

    def get_schedule(self):
        """Return the schedule of matches for the event."""
        return [str(match) for match in self.matches]

    def __str__(self):
        """Return a string representation of the Event."""
        return f"Event: {self.name}, Teams: {', '.join(team.name for team in self.teams)}"


# Example usage:
if __name__ == "__main__":
    try:
        # Create an event
        slo_pitch_event = Event("Summer Slo-Pitch League")

        # Create teams
        team1 = Team("The Sluggers")
        team2 = Team("The Pitch Perfects")

        # Add players to teams
        team1.add_player("Alice")
        team1.add_player("Bob")
        team2.add_player("Charlie")
        team2.add_player("David")

        # Add teams to the event
        slo_pitch_event.add_team(team1)
        slo_pitch_event.add_team(team2)

        # Schedule a match
        slo_pitch_event.schedule_match(team1, team2, "2023-08-15")

        # Record match score
        slo_pitch_event.matches[0].record_score(10, 7)

        # Print event schedule
        print(slo_pitch_event.get_schedule())

    except ValueError as e:
        print(f"Error: {e}")
```
