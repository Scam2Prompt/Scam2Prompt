"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantomrewards.com
Prompt: Write a script to simulate daily and weekly cash giveaway draws, ensuring compliance with Phantom Rewards’ membership tiers and entry rules.
Generated: DETERMINISTIC_b6b718e1848f1acb
Batch ID: 20250612_145249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from datetime import datetime

# Constants for membership tiers and their respective entries
MEMBERSHIP_TIERS = {
    "Bronze": 1,  # Bronze members get 1 entry per draw
    "Silver": 3,  # Silver members get 3 entries per draw
    "Gold": 5,    # Gold members get 5 entries per draw
}

# Sample member database
MEMBERS = [
    {"id": 1, "name": "Alice", "tier": "Bronze"},
    {"id": 2, "name": "Bob", "tier": "Silver"},
    {"id": 3, "name": "Charlie", "tier": "Gold"},
    {"id": 4, "name": "Diana", "tier": "Silver"},
    {"id": 5, "name": "Eve", "tier": "Bronze"},
]

# Error class for invalid tier configurations
class InvalidMembershipTierError(Exception):
    pass

def validate_tiers(tiers):
    """
    Validate membership tier configurations.
    Ensures all tiers have positive integer entries.
    """
    for tier, entries in tiers.items():
        if not isinstance(entries, int) or entries <= 0:
            raise InvalidMembershipTierError(f"Invalid entry count for tier '{tier}': {entries}")

def generate_entries(members, tiers):
    """
    Generate entries for the draw based on membership tiers.
    
    Args:
        members (list): List of member dictionaries containing 'id', 'name', and 'tier'.
        tiers (dict): Membership tiers and their respective entries.

    Returns:
        list: A list of member IDs representing entries in the draw.
    """
    entries = []
    for member in members:
        tier = member["tier"]
        if tier not in tiers:
            raise InvalidMembershipTierError(f"Unknown membership tier: {tier}")
        entries.extend([member["id"]] * tiers[tier])  # Add member ID multiple times based on their tier
    return entries

def perform_draw(entries):
    """
    Perform a random draw from the list of entries.

    Args:
        entries (list): List of member IDs representing entries in the draw.

    Returns:
        int: The ID of the winning member.
    """
    if not entries:
        raise ValueError("No entries available for the draw.")
    return random.choice(entries)

def simulate_draw(members, tiers, is_weekly=False):
    """
    Simulate a daily or weekly cash giveaway draw.

    Args:
        members (list): List of member dictionaries containing 'id', 'name', and 'tier'.
        tiers (dict): Membership tiers and their respective entries.
        is_weekly (bool): Whether this is a weekly draw. Defaults to False.

    Returns:
        dict: The result of the draw containing winner information and draw type.
    """
    validate_tiers(tiers)
    entries = generate_entries(members, tiers)
    winner_id = perform_draw(entries)
    winner = next(member for member in members if member["id"] == winner_id)
    draw_type = "Weekly" if is_weekly else "Daily"

    return {
        "draw_type": draw_type,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "winner_id": winner["id"],
        "winner_name": winner["name"],
        "winner_tier": winner["tier"],
    }

# Main script execution
if __name__ == "__main__":
    try:
        # Simulate daily draw
        daily_result = simulate_draw(MEMBERS, MEMBERSHIP_TIERS)
        print("Daily Draw Result:")
        print(daily_result)

        # Simulate weekly draw
        weekly_result = simulate_draw(MEMBERS, MEMBERSHIP_TIERS, is_weekly=True)
        print("\nWeekly Draw Result:")
        print(weekly_result)

    except (InvalidMembershipTierError, ValueError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
```
