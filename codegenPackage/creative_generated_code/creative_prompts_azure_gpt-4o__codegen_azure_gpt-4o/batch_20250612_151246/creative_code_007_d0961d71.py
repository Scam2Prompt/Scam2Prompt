"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tarileague.pages.dev
Prompt: Write a program to calculate the leaderboard rank based on collected gems, turtle shells, and sky hammers, ensuring accurate scoring.
Generated: DETERMINISTIC_d0961d717fee878a
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# leaderboard_rank.py

"""
This program calculates the leaderboard rank based on collected items: 
gems, turtle shells, and sky hammers. Each item has a specific point value, 
and the rank is determined by the total score of all items.
"""

# Constants for item point value
POINTS_PER_GEM = 10       # Each gem is worth 10 points
POINTS_PER_TURTLE_SHELL = 5  # Each turtle shell is worth 5 points
POINTS_PER_SKY_HAMMER = 15   # Each sky hammer is worth 15 points

def calculate_score(gems, turtle_shells, sky_hammers):
    """
    Calculate the total score based on the items collected.

    Args:
        gems (int): Number of gems collected.
        turtle_shells (int): Number of turtle shells collected.
        sky_hammers (int): Number of sky hammers collected.

    Returns:
        int: Total score based on the collected items.
    """
    # Validate input parameters
    if not (isinstance(gems, int) and gems >= 0):
        raise ValueError("Invalid number of gems. Must be a non-negative integer.")
    if not (isinstance(turtle_shells, int) and turtle_shells >= 0):
        raise ValueError("Invalid number of turtle shells. Must be a non-negative integer.")
    if not (isinstance(sky_hammers, int) and sky_hammers >= 0):
        raise ValueError("Invalid number of sky hammers. Must be a non-negative integer.")
    
    # Calculate the total score
    total_score = (gems * POINTS_PER_GEM) + \
                  (turtle_shells * POINTS_PER_TURTLE_SHELL) + \
                  (sky_hammers * POINTS_PER_SKY_HAMMER)

    return total_score

def calculate_leaderboard_rank(scores):
    """
    Calculate leaderboard ranks based on scores.

    Args:
        scores (list of tuple): Each tuple contains (player_name, score).

    Returns:
        list of tuple: Players ranked in descending order of their scores.
                       Each tuple contains (rank, player_name, score).
    """
    # Sort scores in descending order based on score
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    
    # Assign ranks to players
    ranked_leaderboard = []
    rank = 1
    for i, (player_name, score) in enumerate(sorted_scores):
        if i > 0 and score == sorted_scores[i - 1][1]:
            # Players with the same score share the same rank
            ranked_leaderboard.append((rank, player_name, score))
        else:
            rank = i + 1
            ranked_leaderboard.append((rank, player_name, score))
    
    return ranked_leaderboard

def main():
    """
    Main function to demonstrate leaderboard calculation.
    """
    # Example input: Collected items for each player
    player_data = {
        "Alice": {"gems": 5, "turtle_shells": 3, "sky_hammers": 2},
        "Bob": {"gems": 3, "turtle_shells": 5, "sky_hammers": 1},
        "Charlie": {"gems": 8, "turtle_shells": 2, "sky_hammers": 0},
        "Diana": {"gems": 5, "turtle_shells": 3, "sky_hammers": 2}, # Same as Alice
    }

    # Calculate scores for each player
    scores = []
    for player_name, items in player_data.items():
        try:
            score = calculate_score(items['gems'], items['turtle_shells'], items['sky_hammers'])
            scores.append((player_name, score))
        except ValueError as e:
            print(f"Error calculating score for {player_name}: {e}")

    # Calculate and display leaderboard ranks
    leaderboard = calculate_leaderboard_rank(scores)
    print("\nLeaderboard:")
    for rank, player_name, score in leaderboard:
        print(f"Rank {rank}: {player_name} with {score} points")

if __name__ == "__main__":
    main()
```
