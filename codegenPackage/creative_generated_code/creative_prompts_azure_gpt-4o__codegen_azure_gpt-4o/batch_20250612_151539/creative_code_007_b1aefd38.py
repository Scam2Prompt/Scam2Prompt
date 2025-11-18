"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whelps.io
Prompt: Create a Python script to simulate the earning mechanics of Dragon tokens based on race placements and time spent racing in WhelpS: Slipstream.
Generated: DETERMINISTIC_b1aefd38f318c00c
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to simulate earning Dragon tokens based on race placements 
# and time spent racing in WhelpS: Slipstream.

import random

# Constants
TOKENS_BASE_REWARD = 50  # Base tokens for participation
PLACEMENT_MULTIPLIER = {1: 3, 2: 2, 3: 1.5}  # Placement multipliers for top 3 spots
TIME_REWARD_RATE = 10  # Tokens per minute of racing
MAX_RACE_TIME = 60  # Maximum race time in minutes
PLACEMENT_REWARDS = [1, 2, 3, 4, 5, 6]  # Possible race positions

def calculate_tokens(position, time_spent):
    """
    Calculate the Dragon tokens earned based on race placement and time spent racing.

    Args:
        position (int): The race placement (1 for first place, 2 for second, etc.).
        time_spent (float): Time spent racing in minutes.

    Returns:
        float: Total Dragon tokens earned.
    """
    if position < 1 or position > max(PLACEMENT_REWARDS):
        raise ValueError("Invalid race position. Must be between 1 and 6.")
    if time_spent < 0 or time_spent > MAX_RACE_TIME:
        raise ValueError(f"Invalid race time. Must be between 0 and {MAX_RACE_TIME} minutes.")

    # Base reward for participation
    tokens = TOKENS_BASE_REWARD

    # Add placement multiplier reward
    tokens += TOKENS_BASE_REWARD * PLACEMENT_MULTIPLIER.get(position, 1)

    # Add time-spent reward
    tokens += time_spent * TIME_REWARD_RATE

    return round(tokens, 2)

def simulate_race():
    """
    Simulates a WhelpS: Slipstream race and calculates tokens earned.

    Returns:
        dict: Race simulation results including position, time spent, and tokens earned.
    """
    # Randomly assign race position and time spent racing
    position = random.choice(PLACEMENT_REWARDS)
    time_spent = round(random.uniform(0, MAX_RACE_TIME), 2)

    try:
        # Calculate tokens earned
        tokens_earned = calculate_tokens(position, time_spent)
    except ValueError as e:
        return {"error": str(e)}

    return {
        "position": position,
        "time_spent": time_spent,
        "tokens_earned": tokens_earned
    }

def main():
    """
    Main function to simulate multiple races and display results.
    """
    print("Welcome to WhelpS: Slipstream Race Simulator!")
    num_races = 5  # Number of races to simulate

    for i in range(1, num_races + 1):
        print(f"\nRace {i} Results:")
        race_result = simulate_race()
        if "error" in race_result:
            print(f"Error: {race_result['error']}")
        else:
            print(f"Placement: {race_result['position']}")
            print(f"Time Spent Racing: {race_result['time_spent']} minutes")
            print(f"Dragon Tokens Earned: {race_result['tokens_earned']}")

if __name__ == "__main__":
    main()
```
