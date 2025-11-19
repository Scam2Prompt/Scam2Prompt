"""
Generated Code Metadata:
========================
Original URL: https://lethmixedslowpitch.com
Prompt: Generate a round-robin tournament schedule for a slowpitch softball league using Python, ensuring fair and balanced matchups, as outlined by Slo-Pitch Central's Round Robin Generator.
Generated: DETERMINISTIC_9bc83d618e35379c
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def generate_round_robin_schedule(teams):
    """
    Generate a round-robin tournament schedule for a slowpitch softball league.

    Args:
        teams (list): List of team names.

    Returns:
        list: List of matchups for each round.
    """
    # Check if the number of teams is even
    if len(teams) % 2 != 0:
        teams.append("BYE")

    # Initialize the schedule
    schedule = []

    # Calculate the number of rounds
    num_rounds = len(teams) - 1

    # Generate the schedule
    for i in range(num_rounds):
        round_matchups = []
        for j in range(len(teams) // 2):
            team1 = teams[j]
            team2 = teams[len(teams) - 1 - j]
            round_matchups.append((team1, team2))
        teams.insert(1, teams.pop())  # Rotate the teams
        schedule.append(round_matchups)

    return schedule


def print_schedule(schedule):
    """
    Print the round-robin tournament schedule.

    Args:
        schedule (list): List of matchups for each round.
    """
    for i, round_matchups in enumerate(schedule):
        print(f"Round {i + 1}:")
        for j, matchup in enumerate(round_matchups):
            print(f"  Game {j + 1}: {matchup[0]} vs {matchup[1]}")
        print()


def main():
    try:
        # Get the list of teams from the user
        num_teams = int(input("Enter the number of teams: "))
        teams = []
        for i in range(num_teams):
            team_name = input(f"Enter team {i + 1} name: ")
            teams.append(team_name)

        # Generate and print the schedule
        schedule = generate_round_robin_schedule(teams)
        print_schedule(schedule)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
