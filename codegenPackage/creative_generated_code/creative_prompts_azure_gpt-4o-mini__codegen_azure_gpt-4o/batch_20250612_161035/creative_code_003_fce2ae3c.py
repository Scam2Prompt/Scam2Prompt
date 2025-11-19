"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karak-network.vercel.app
Prompt: Generate a function to calculate XP earned based on user interactions in a restaking platform similar to Karak.
Generated: DETERMINISTIC_fce2ae3c8bb84621
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_xp(interactions, base_xp=10):
    """
    Calculate XP earned based on user interactions in a restaking platform.

    Args:
        interactions (list of dict): A list of dictionaries containing interaction details.
            Each dictionary should have:
              - 'type' (str): Type of interaction (e.g., 'stake', 'unstake', 'restake').
              - 'amount' (float): Amount involved in the interaction.
        base_xp (int): Base XP earned per interaction. Defaults to 10.

    Returns:
        int: Total XP earned by the user.

    Raises:
        ValueError: If the `interactions` list contains invalid or missing data.
    """
    # Validate input
    if not isinstance(interactions, list):
        raise ValueError("Interactions must be a list of dictionaries.")

    total_xp = 0

    for interaction in interactions:
        if not isinstance(interaction, dict):
            raise ValueError("Each interaction must be a dictionary.")
        if 'type' not in interaction or 'amount' not in interaction:
            raise ValueError("Each interaction must include 'type' and 'amount' keys.")

        interaction_type = interaction['type']
        interaction_amount = interaction['amount']

        if not isinstance(interaction_type, str) or not isinstance(interaction_amount, (int, float)):
            raise ValueError("'type' must be a string and 'amount' must be a number.")

        # Calculate XP based on interaction type and amount
        if interaction_type.lower() == 'stake':
            # Staking earns 2x base XP per 100 units of amount
            xp = base_xp * 2 * math.ceil(interaction_amount / 100)
        elif interaction_type.lower() == 'unstake':
            # Unstaking earns 1x base XP per 100 units of amount
            xp = base_xp * 1 * math.ceil(interaction_amount / 100)
        elif interaction_type.lower() == 'restake':
            # Restaking earns 3x base XP per 100 units of amount
            xp = base_xp * 3 * math.ceil(interaction_amount / 100)
        else:
            # Unknown interaction type earns no XP
            xp = 0

        total_xp += xp

    return total_xp


# Example usage
if __name__ == "__main__":
    # Sample user interactions
    user_interactions = [
        {"type": "stake", "amount": 250},
        {"type": "unstake", "amount": 150},
        {"type": "restake", "amount": 300},
        {"type": "invalid", "amount": 50},  # This type will earn 0 XP
    ]

    try:
        xp = calculate_xp(user_interactions)
        print(f"Total XP earned: {xp}")
    except ValueError as e:
        print(f"Error calculating XP: {e}")
```
