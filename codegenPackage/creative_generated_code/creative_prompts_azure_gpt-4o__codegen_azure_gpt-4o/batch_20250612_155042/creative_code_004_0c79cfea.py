"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simemes.vercel.app
Prompt: Design an algorithm in Python to calculate the rewards for players based on their registration tier (e.g., Pebble x50 for 10K, Poop x1M for 50K, etc.) as described on the SIMemes site.
Generated: DETERMINISTIC_0c79cfeacbca8d76
Batch ID: 20250612_155042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python program to calculate player rewards based on their registration tier.

# Constants for reward tiers
REWARD_TIERS = {
    10000: {'Pebble': 50},    # Example: Tier for 10K points
    50000: {'Poop': 1000000} # Example: Tier for 50K points
}

def calculate_rewards(player_points):
    """
    Calculate rewards for players based on their registration points.
    
    Args:
        player_points (int): The number of registration points the player has.

    Returns:
        dict: A dictionary containing the rewards and their corresponding quantities.
              Returns an empty dictionary if no reward tier is matched.
    """
    # Validate input
    if not isinstance(player_points, int) or player_points < 0:
        raise ValueError("Player points must be a non-negative integer.")
    
    # Sort tiers by points in descending order
    sorted_tiers = sorted(REWARD_TIERS.keys(), reverse=True)
    
    for tier_points in sorted_tiers:
        if player_points >= tier_points:
            return REWARD_TIERS[tier_points]
    
    # Return empty dictionary if no tier matches
    return {}

def main():
    """
    Main function to take input from the user and display rewards.
    """
    try:
        # Ask the user for their registration points
        player_points = int(input("Enter your registration points: "))
        
        # Calculate rewards
        rewards = calculate_rewards(player_points)
        
        # Display the rewards to the player
        if rewards:
            print("Congratulations! You have earned the following rewards:")
            for reward, quantity in rewards.items():
                print(f"- {reward}: x{quantity}")
        else:
            print("Sorry, no rewards available for your registration points.")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
