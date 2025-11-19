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
# Function to calculate rewards from Prestige Portals in Big Time
def calculate_rewards(challenges_completed):
    """
    Calculate rewards from Prestige Portals based on the number of challenges completed.

    Args:
        challenges_completed (int): The number of challenges completed by the player.

    Returns:
        dict: A dictionary containing reward details including XP, gold, and rare items.
    """
    # Input validation
    if not isinstance(challenges_completed, int) or challenges_completed < 0:
        raise ValueError("challenges_completed must be a non-negative integer")

    # Base rewards per challenge
    XP_PER_CHALLENGE = 100  # Experience points per challenge
    GOLD_PER_CHALLENGE = 50  # Gold per challenge
    RARE_ITEM_CHANCE_PER_CHALLENGE = 0.05  # Chance of rare item per challenge (5%)

    # Calculate rewards
    total_xp = challenges_completed * XP_PER_CHALLENGE
    total_gold = challenges_completed * GOLD_PER_CHALLENGE
    rare_items = 0

    # Simulate rare item drops (based on random probability)
    import random
    for _ in range(challenges_completed):
        if random.random() < RARE_ITEM_CHANCE_PER_CHALLENGE:
            rare_items += 1

    # Compile rewards into a result dictionary
    rewards = {
        "total_xp": total_xp,
        "total_gold": total_gold,
        "rare_items": rare_items
    }

    return rewards


# Example usage
if __name__ == "__main__":
    try:
        # Number of challenges completed by the player
        challenges = 20
        
        # Calculate and print rewards
        rewards = calculate_rewards(challenges)
        print(f"Rewards for completing {challenges} challenges:")
        print(f"  Total XP: {rewards['total_xp']}")
        print(f"  Total Gold: {rewards['total_gold']}")
        print(f"  Rare Items: {rewards['rare_items']}")
    except ValueError as e:
        print(f"Error: {e}")
```
