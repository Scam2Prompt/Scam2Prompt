"""
Generated Code Metadata:
========================
Original URL: https://amamam-ble.pages.dev
Prompt: Generate a function that calculates the potential earnings from inviting friends to play Hamster Kombat, based on the game's mechanics described on the site.
Generated: DETERMINISTIC_641c2aa9ab127bbd
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_hamster_kombat_earnings(
    initial_friends: int,
    invite_rate: float,
    conversion_rate: float,
    base_earn_per_user: float,
    days: int,
    max_friends: int = None
) -> float:
    """
    Calculate potential earnings from inviting friends to play Hamster Kombat.

    Args:
        initial_friends: Number of friends already invited
        invite_rate: Daily rate at which each user invites new friends (0-1)
        conversion_rate: Percentage of invited friends who actually join (0-1)
        base_earn_per_user: Base earnings per active user per day
        days: Number of days to simulate
        max_friends: Maximum number of friends that can be invited (optional)

    Returns:
        Total potential earnings over the simulation period
    """
    try:
        # Validate input parameters
        if initial_friends < 0:
            raise ValueError("Initial friends cannot be negative")
        if not 0 <= invite_rate <= 1:
            raise ValueError("Invite rate must be between 0 and 1")
        if not 0 <= conversion_rate <= 1:
            raise ValueError("Conversion rate must be between 0 and 1")
        if base_earn_per_user < 0:
            raise ValueError("Base earnings cannot be negative")
        if days < 1:
            raise ValueError("Simulation period must be at least 1 day")
        if max_friends is not None and max_friends < 0:
            raise ValueError("Max friends cannot be negative")

        total_friends = initial_friends
        total_earnings = 0.0

        for day in range(days):
            # Calculate new invites for this day
            new_invites = total_friends * invite_rate
            
            # Apply conversion rate and max friends limit if specified
            converted_friends = new_invites * conversion_rate
            if max_friends is not None:
                remaining_capacity = max(0, max_friends - total_friends)
                converted_friends = min(converted_friends, remaining_capacity)
            
            # Update totals
            total_friends += converted_friends
            daily_earnings = total_friends * base_earn_per_user
            total_earnings += daily_earnings

        return round(total_earnings, 2)

    except ValueError as e:
        print(f"Error in calculation: {e}")
        return 0.0
    except Exception as e:
        print(f"Unexpected error: {e}")
        return 0.0
```
