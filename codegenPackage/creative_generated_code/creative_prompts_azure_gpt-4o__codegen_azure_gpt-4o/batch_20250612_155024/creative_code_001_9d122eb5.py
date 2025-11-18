"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://parallels.top
Prompt: Create a function that boosts in-game earnings based on the ownership of specific digital assets, such as Avatars, as described in the Parallel TCG system.
Generated: DETERMINISTIC_9d122eb5ad43e4b1
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def calculate_boosted_earnings(base_earnings, owned_assets):
    """
    Calculate boosted in-game earnings based on ownership of specific digital assets.

    Parameters:
    - base_earnings (float): The initial earnings in the game.
    - owned_assets (list): A list of strings representing owned digital assets, such as Avatars.

    Returns:
    - float: The final boosted earnings.
    """
    try:
        # Define asset-based earning boosts (can be extended for new asset types)
        asset_boosts = {
            "AvatarAlpha": 1.2,  # 20% boost for owning AvatarAlpha
            "AvatarBeta": 1.1,  # 10% boost for owning AvatarBeta
            "AvatarGamma": 1.3  # 30% boost for owning AvatarGamma
        }

        # Ensure the base earnings is a positive number
        if base_earnings < 0:
            raise ValueError("Base earnings must be a non-negative number.")

        # Calculate total multiplier based on owned assets
        total_multiplier = 1.0  # Start with no boost
        for asset in owned_assets:
            if asset in asset_boosts:
                total_multiplier *= asset_boosts[asset]

        # Final boosted earnings
        boosted_earnings = base_earnings * total_multiplier

        return round(boosted_earnings, 2)  # Return earnings rounded to 2 decimal places for clarity

    except ValueError as ve:
        print(f"Error: {ve}")
        return 0.0  # Return zero if there is an error in input validation
    except Exception as e:
        print(f"Unexpected error: {e}")
        return 0.0  # Ensure the function doesn't crash in production

# Example usage
if __name__ == "__main__":
    # Example base earnings and owned assets
    base_earnings = 100.0  # Starting earnings
    owned_assets = ["AvatarAlpha", "AvatarBeta"]  # Assets owned by the user

    # Calculate boosted earnings
    boosted_earnings = calculate_boosted_earnings(base_earnings, owned_assets)

    # Output the result in a user-friendly manner
    print(f"Base Earnings: {base_earnings}")
    print(f"Owned Assets: {json.dumps(owned_assets)}")
    print(f"Boosted Earnings: {boosted_earnings}")
```
