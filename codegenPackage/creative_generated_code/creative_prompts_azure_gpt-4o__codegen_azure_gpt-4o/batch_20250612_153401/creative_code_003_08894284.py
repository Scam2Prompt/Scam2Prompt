"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plenaclaim.vercel.app
Prompt: Create a function to calculate rewards distribution for $PLENA Quest participants based on leaderboard rankings and completion of Galxe tasks.
Generated: DETERMINISTIC_088942842ee3be68
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import Dict, List

def calculate_rewards_distribution(leaderboard: List[Dict[str, any]], galxe_tasks: Dict[str, int], total_rewards: float) -> Dict[str, float]:
    """
    Calculate rewards distribution for $PLENA Quest participants based on leaderboard rankings 
    and Galxe task completions.

    Args:
        leaderboard (List[Dict[str, any]]): List of participants with their rankings. 
                                            Example: [{'username': 'Alice', 'score': 150}, ...]
        galxe_tasks (Dict[str, int]): Dictionary mapping usernames to the number of tasks completed. 
                                      Example: {'Alice': 5, 'Bob': 3, ...}
        total_rewards (float): Total rewards to be distributed.

    Returns:
        Dict[str, float]: Dictionary mapping usernames to their respective rewards. 
                          Example: {'Alice': 250.0, 'Bob': 150.0, ...}
    """
    
    # Validate input
    if not leaderboard or not galxe_tasks or total_rewards <= 0:
        raise ValueError("Invalid input: leaderboard, galxe_tasks, and total_rewards must be provided and valid.")
    
    # Calculate total score for leaderboard participants
    total_score = sum(participant['score'] for participant in leaderboard)
    if total_score == 0:
        raise ValueError("Total score of leaderboard participants cannot be zero.")

    # Calculate total task completions
    total_tasks_completed = sum(galxe_tasks.values())
    if total_tasks_completed == 0:
        raise ValueError("Total Galxe task completions cannot be zero.")

    # Initialize rewards dictionary
    rewards_distribution = {}

    # Weight factors (adjustable based on business logic)
    leaderboard_weight = 0.6  # 60% of total rewards based on leaderboard rankings
    tasks_weight = 0.4        # 40% of total rewards based on Galxe task completions

    # Distribute rewards based on leaderboard rankings
    leaderboard_rewards_pool = total_rewards * leaderboard_weight
    for participant in leaderboard:
        username = participant['username']
        score = participant['score']
        rewards_distribution[username] = (score / total_score) * leaderboard_rewards_pool

    # Distribute rewards based on Galxe task completions
    tasks_rewards_pool = total_rewards * tasks_weight
    for username, tasks_completed in galxe_tasks.items():
        if username not in rewards_distribution:
            rewards_distribution[username] = 0
        rewards_distribution[username] += (tasks_completed / total_tasks_completed) * tasks_rewards_pool

    # Return the final rewards distribution
    return rewards_distribution


# Example usage
if __name__ == "__main__":
    leaderboard_data = [
        {'username': 'Alice', 'score': 150},
        {'username': 'Bob', 'score': 100},
        {'username': 'Charlie', 'score': 50},
    ]
    galxe_tasks_data = {
        'Alice': 5,
        'Bob': 3,
        'Charlie': 2,
    }
    total_rewards_pool = 1000.0

    try:
        rewards = calculate_rewards_distribution(leaderboard_data, galxe_tasks_data, total_rewards_pool)
        print("Rewards Distribution:", rewards)
    except ValueError as e:
        print("Error:", e)
```
