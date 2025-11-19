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

Below is a Python implementation for generating a round-robin schedule for a slow-pitch softball tournament. It assumes that you have a list of teams participating in the tournament and uses a simple algorithm to pair teams for each round.

```python
# Import required modules
import itertools

def generate_round_robin_schedule(teams):
    """
    Generates a round-robin schedule for the given teams.

    Args:
        teams (list): A list of team names (strings).

    Returns:
        dict: A dictionary with round numbers as keys and lists of matches (tuples) as values.
    """
    try:
        # Ensure the number of teams is even by adding a dummy team ("Bye") if necessary
        if len(teams) % 2 != 0:
            teams.append("Bye")

        # Number of rounds is equal to the number of teams - 1
        num_rounds = len(teams) - 1

        # Prepare the schedule dictionary
        schedule = {}

        # Generate rounds using a round-robin algorithm
        for round_num in range(num_rounds):
            matches = []
            for i in range(len(teams) // 2):
                # Pair teams for this round
                home = teams[i]
                away = teams[-(i + 1)]
                matches.append((home, away))
            
            # Add matches to the schedule
            schedule[round_num + 1] = matches
            
            # Rotate teams for the next round, keeping the first team fixed
            teams = [teams[0]] + teams[-1:] + teams[1:-1]

        return schedule

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred while generating the round-robin schedule: {str(e)}")
        return None


def print_schedule(schedule):
    """
    Prints the round-robin schedule in a readable format.

    Args:
        schedule (dict): The round-robin schedule returned by generate_round_robin_schedule.
    """
    try:
        if not schedule:
            print("No schedule to display.")
            return

        print("Round-Robin Schedule:")
        for round_num, matches in schedule.items():
            print(f"Round {round_num}:")
            for home, away in matches:
                print(f"  {home} vs {away}")
            print()

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred while printing the schedule: {str(e)}")


# Example usage
if __name__ == "__main__":
    # List of participating teams
    teams = ["Team A", "Team B", "Team C", "Team D", "Team E"]

    # Generate the round-robin schedule
    schedule = generate_round_robin_schedule(teams)

    # Print the schedule
    print_schedule(schedule)
```

This code will generate a round-robin schedule and print it in a formatted way. It includes error handling and follows Python best practices for readability and maintainability.
