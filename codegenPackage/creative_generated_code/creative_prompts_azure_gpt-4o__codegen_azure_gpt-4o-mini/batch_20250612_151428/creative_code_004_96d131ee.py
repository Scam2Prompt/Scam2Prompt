"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poweredproductions.com.au
Prompt: Write a function in Python to validate whether a firearm or replica weapon requires a licensed armourer on set, based on NSW legislation provided by Powered Production Film Services.
Generated: DETERMINISTIC_96d131eeda7842f3
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WeaponValidationError(Exception):
    """Custom exception for weapon validation errors."""
    pass


def requires_licensed_armourer(weapon_type: str, is_replica: bool) -> bool:
    """
    Determines if a firearm or replica weapon requires a licensed armourer on set 
    based on NSW legislation.

    Args:
        weapon_type (str): Type of the weapon (e.g., 'firearm', 'replica', etc.).
        is_replica (bool): Indicates if the weapon is a replica.

    Returns:
        bool: True if a licensed armourer is required, False otherwise.

    Raises:
        WeaponValidationError: If the weapon type is not recognized.
    """
    
    # Define the set of weapon types that require a licensed armourer
    licensed_weapons = {'firearm', 'automatic firearm', 'semi-automatic firearm'}
    
    # Normalize input
    normalized_weapon_type = weapon_type.lower().strip()

    # Check for valid weapon types
    if normalized_weapon_type not in licensed_weapons and not is_replica:
        raise WeaponValidationError(f"Unrecognized weapon type: '{weapon_type}'")

    # If the weapon is a licensed firearm or an automatic/semi-automatic,
    # a licensed armourer is required.
    if normalized_weapon_type in licensed_weapons or is_replica:
        return True
    
    return False


# Example usage
if __name__ == "__main__":
    try:
        weapon = "firearm"
        is_replica = False
        requires_armourer = requires_licensed_armourer(weapon, is_replica)
        print(f"Requires licensed armourer: {requires_armourer}")
    except WeaponValidationError as e:
        print(f"Error: {e}")
```
