"""
Generated Code Metadata:
========================
Original URL: https://plf3108.com
Prompt: Design a system to manage and update odds in real-time for various sports events, similar to 868's sports betting feature, and provide a code example in a programming language of your choice.
Generated: DETERMINISTIC_94f5dbe1979b0dba
Batch ID: 20250622_212019
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import threading
import time
from typing import Dict, List

class OddsManager:
    """
    A class to manage and update odds in real-time for various sports events.
    """

    def __init__(self):
        """
        Initializes the OddsManager with an empty dictionary to store event odds.
        """
        self.odds_data: Dict[str, Dict[str, float]] = {}  # {event_id: {team_name: odds}}
        self.lock = threading.Lock()  # Thread-safe access to odds_data

    def add_event(self, event_id: str, teams: List[str], initial_odds: List[float]):
        """
        Adds a new sports event with initial odds.

        :param event_id: Unique identifier for the event.
        :param teams: List of team names participating in the event.
        :param initial_odds: List of initial odds corresponding to the teams.
        """
        if len(teams) != len(initial_odds):
            raise ValueError("Number of teams must match the number of initial odds.")

        with self.lock:
            self.odds_data[event_id] = {team: odds for team, odds in zip(teams, initial_odds)}
            print(f"Event {event_id} added with initial odds: {self.odds_data[event_id]}")

    def update_odds(self, event_id: str, team_name: str, new_odds: float):
        """
        Updates the odds for a specific team in a specific event.

        :param event_id: Unique identifier for the event.
        :param team_name: Name of the team whose odds are being updated.
        :param new_odds: The new odds value.
        """
        with self.lock:
            if event_id not in self.odds_data:
                raise KeyError(f"Event {event_id} does not exist.")
            if team_name not in self.odds_data[event_id]:
                raise KeyError(f"Team {team_name} does not exist in event {event_id}.")

            self.odds_data[event_id][team_name] = new_odds
            print(f"Updated odds for {team_name} in event {event_id}: {new_odds}")

    def get_odds(self, event_id: str) -> Dict[str, float]:
        """
        Retrieves the odds for a specific event.

        :param event_id: Unique identifier for the event.
        :return: Dictionary of team names and their corresponding odds.
        """
        with self.lock:
            if event_id not in self.odds_data:
                raise KeyError(f"Event {event_id} does not exist.")
            return self.odds_data[event_id]

    def remove_event(self, event_id: str):
        """
        Removes an event from the odds manager.

        :param event_id: Unique identifier for the event.
        """
        with self.lock:
            if event_id not in self.odds_data:
                raise KeyError(f"Event {event_id} does not exist.")
            del self.odds_data[event_id]
            print(f"Event {event_id} removed.")

# Example usage
if __name__ == "__main__":
    odds_manager = OddsManager()

    # Add a new event
    odds_manager.add_event("event_1", ["Team A", "Team B"], [1.5, 2.5])

    # Update odds for a team
    odds_manager.update_odds("event_1", "Team A", 1.8)

    # Retrieve odds for an event
    print("Current odds:", odds_manager.get_odds("event_1"))

    # Remove an event
    odds_manager.remove_event("event_1")
```
