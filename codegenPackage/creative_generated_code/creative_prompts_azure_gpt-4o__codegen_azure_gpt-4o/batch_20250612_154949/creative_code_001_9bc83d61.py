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
"""
Round-Robin Tournament Scheduler for a Slowpitch Softball League

This script generates a round-robin schedule for a given number of teams.
Each team plays against every other team exactly once in a fair and balanced manner.

Author: Professional Software Developer
"""

from itertools import permutations

def generate_round_robin_schedule(teams: list):
    """
    Generates a round-robin schedule for the given list of teams.
    
    :param teams: List of team names
    :return: List of rounds where each round contains matchups
    """
    if len(teams) < 2:
        raise ValueError("At least two teams are required to create a schedule.")

    # Ensure an even number of teams by adding a "bye" if necessary
    if len(teams) % 2 != 0:
        teams.append("Bye")  # A "Bye" represents no matchup for a team in that round

    num_teams = len(teams)
    num_rounds = num_teams - 1  # Total number of rounds required for round-robin
    schedule = []

    # Use a round-robin algorithm to generate matchups
    for round_number in range(num_rounds):
        round_matches = []
        for i in range(num_teams // 2):
            home = teams[i]
            away = teams[num_teams - 1 - i]
            if home != "Bye" and away != "Bye":
                round_matches.append((home, away))
        
        schedule.append(round_matches)

        # Rotate teams to generate the next round matchups
        teams = [teams[0]] + teams[-1:] + teams[1:-1]

    return schedule


def print_schedule(schedule: list):
    """
    Prints the tournament schedule in a human-readable format.
    
    :param schedule: List of rounds containing matchups
    """
    for round_number, round_matches in enumerate(schedule, start=1):
        print(f"Round {round_number}:")
        for home, away in round_matches:
            print(f"  {home} vs. {away}")
        print()


if __name__ == "__main__":
    try:
        # Example usage with a list of team names
        teams = ["Team A", "Team B", "Team C", "Team D", "Team E"]
        schedule = generate_round_robin_schedule(teams)
        print_schedule(schedule)
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
