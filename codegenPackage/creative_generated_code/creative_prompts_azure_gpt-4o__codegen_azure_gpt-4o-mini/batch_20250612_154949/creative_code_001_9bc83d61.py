"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lethmixedslowpitch.com
Prompt: Generate a round-robin tournament schedule for a slowpitch softball league using Python, ensuring fair and balanced matchups, as outlined by Slo-Pitch Central's Round Robin Generator.
Generated: DETERMINISTIC_9bc83d618e35379c
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math
from typing import List, Tuple

def generate_round_robin_schedule(teams: List[str]) -> List[List[Tuple[str, str]]]:
    """
    Generates a round-robin tournament schedule for a given list of teams.
    
    Parameters:
        teams (List[str]): A list of team names participating in the tournament.

    Returns:
        List[List[Tuple[str, str]]]: A schedule where each round contains matchups.
    """
    if len(teams) < 2:
        raise ValueError("At least two teams are required to generate a schedule.")
    
    # Ensure even number of teams by adding a dummy team if necessary
    if len(teams) % 2 != 0:
        teams.append("Bye")

    num_teams = len(teams)
    num_rounds = num_teams - 1
    matches_per_round = num_teams // 2

    schedule = []

    # Generate the schedule
    for round in range(num_rounds):
        round_matches = []
        
        for match in range(matches_per_round):
            home = teams[match]
            away = teams[num_teams - 1 - match]
            round_matches.append((home, away))
        
        schedule.append(round_matches)

        # Rotate teams for next round
        teams = [teams[0]] + [teams[-1]] + teams[1:-1]

    return schedule

def print_schedule(schedule: List[List[Tuple[str, str]]]) -> None:
    """
    Prints the round-robin schedule in a readable format.
    
    Parameters:
        schedule (List[List[Tuple[str, str]]]): The tournament schedule to print.
    """
    for round_number, matches in enumerate(schedule, start=1):
        print(f"Round {round_number}:")
        for home, away in matches:
            print(f"  {home} vs {away}")
        print()  # Print a blank line between rounds

if __name__ == "__main__":
    # Example usage
    teams_list = [
        "Team A",
        "Team B",
        "Team C",
        "Team D",
        "Team E"
    ]

    try:
        tournament_schedule = generate_round_robin_schedule(teams_list)
        print_schedule(tournament_schedule)
    except ValueError as e:
        print(f"Error: {e}")
```
