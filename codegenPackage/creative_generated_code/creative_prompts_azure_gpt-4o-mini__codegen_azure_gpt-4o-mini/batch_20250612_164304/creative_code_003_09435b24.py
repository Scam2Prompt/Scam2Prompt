"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigtime-codes.pages.dev
Prompt: Generate a function that calculates the rewards from Prestige Portals based on completed challenges in Big Time.
Generated: DETERMINISTIC_09435b24c8a3c690
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_rewards(challenges_completed, portal_type):
    """
    Calculate rewards from Prestige Portals based on completed challenges in Big Time.

    Args:
        challenges_completed (int): The number of challenges completed.
        portal_type (str): The type of Prestige Portal ('gold', 'silver', 'bronze').

    Returns:
        float: The total rewards calculated based on the portal type and challenges completed.

    Raises:
        ValueError: If challenges_completed is negative or if portal_type is not recognized.
    """
    # Define reward multipliers for each portal type
    reward_multipliers = {
        'gold': 10.0,
        'silver': 5.0,
        'bronze': 2.0
    }
    
    # Validate input
    if challenges_completed < 0:
        raise ValueError("Number of challenges completed cannot be negative.")
    
    if portal_type not in reward_multipliers:
        raise ValueError("Invalid portal type. Must be 'gold', 'silver', or 'bronze'.")

    # Calculate total rewards
    total_rewards = challenges_completed * reward_multipliers[portal_type]
    
    return total_rewards

# Example usage
if __name__ == "__main__":
    try:
        completed_challenges = 5
        portal = 'gold'
        rewards = calculate_rewards(completed_challenges, portal)
        print(f"Total rewards from {completed_challenges} completed challenges in {portal} portal: {rewards}")
    except ValueError as e:
        print(f"Error calculating rewards: {e}")
```
