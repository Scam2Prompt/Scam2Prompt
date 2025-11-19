"""
Generated Code Metadata:
========================
Original URL: https://lethmixedslowpitch.com
Prompt: Write a Python script to generate a round-robin schedule for a slowpitch softball tournament using the Round Robin Generator tool.
Generated: DETERMINISTIC_6fa6165d440d54a4
Batch ID: 20250622_212338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import itertools

def generate_round_robin_schedule(teams):
    """
    Generate a round-robin schedule for a slowpitch softball tournament.

    Args:
        teams (list): A list of team names.

    Returns:
        list: A list of tuples, where each tuple represents a matchup in the schedule.
    """
    # Check if the number of teams is even
    if len(teams) % 2 != 0:
        teams.append("BYE")  # Add a bye team if the number of teams is odd

    # Generate all possible matchups
    matchups = list(itertools.combinations(teams, 2))

    # Sort the matchups to ensure a round-robin schedule
    schedule = []
    for i in range(len(teams) - 1):
        round_matchups = []
        for j in range(len(teams) // 2):
            team1 = teams[j]
            team2 = teams[len(teams) - 1 - j]
            round_matchups.append((team1, team2))
        schedule.append(round_matchups)

        # Rotate the teams for the next round
        teams.insert(1, teams.pop())

    return schedule


def print_schedule(schedule):
    """
    Print the round-robin schedule in a readable format.

    Args:
        schedule (list): A list of tuples, where each tuple represents a matchup in the schedule.
    """
    for i, round_matchups in enumerate(schedule):
        print(f"Round {i + 1}:")
        for matchup in round_matchups:
            print(f"  {matchup[0]} vs. {matchup[1]}")
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
