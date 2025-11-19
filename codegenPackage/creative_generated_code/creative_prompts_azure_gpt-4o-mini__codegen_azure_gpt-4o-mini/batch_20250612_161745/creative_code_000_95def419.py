"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lethmixedslowpitch.com
Prompt: How can I create a round-robin schedule for my slowpitch softball tournament using Slo-Pitch Central's tools?
Generated: DETERMINISTIC_95def41911b63470
Batch ID: 20250612_161745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import itertools
from typing import List, Tuple

class RoundRobinScheduler:
    def __init__(self, teams: List[str]):
        """
        Initialize the RoundRobinScheduler with a list of teams.

        :param teams: A list of team names (strings).
        """
        self.teams = teams
        self.schedule = []

    def generate_schedule(self) -> List[Tuple[str, str]]:
        """
        Generate a round-robin schedule.

        :return: A list of tuples where each tuple contains two teams playing against each other.
        """
        if len(self.teams) < 2:
            raise ValueError("At least two teams are required to generate a schedule.")

        # Ensure an even number of teams by adding a dummy team if necessary
        if len(self.teams) % 2 != 0:
            self.teams.append("Bye")

        # Generate the schedule using a round-robin algorithm
        num_teams = len(self.teams)
        for round in range(num_teams - 1):
            round_matches = []
            for i in range(num_teams // 2):
                home = self.teams[i]
                away = self.teams[num_teams - 1 - i]
                round_matches.append((home, away))
            self.schedule.append(round_matches)

            # Rotate teams for the next round
            self.teams.insert(1, self.teams.pop())

        return self.schedule

    def display_schedule(self):
        """
        Display the generated schedule in a readable format.
        """
        for round_number, matches in enumerate(self.schedule, start=1):
            print(f"Round {round_number}:")
            for match in matches:
                print(f"{match[0]} vs {match[1]}")
            print()  # Add a newline for better readability

# Example usage
if __name__ == "__main__":
    try:
        teams = ["Team A", "Team B", "Team C", "Team D"]
        scheduler = RoundRobinScheduler(teams)
        scheduler.generate_schedule()
        scheduler.display_schedule()
    except ValueError as e:
        print(f"Error: {e}")
```
