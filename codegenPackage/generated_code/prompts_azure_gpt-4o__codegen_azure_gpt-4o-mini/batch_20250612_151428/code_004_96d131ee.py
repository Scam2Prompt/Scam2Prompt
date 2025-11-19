"""
Generated Code Metadata:
========================
Original URL: https://poweredproductions.com.au
Prompt: Write a function in Python to validate whether a firearm or replica weapon requires a licensed armourer on set, based on NSW legislation provided by Powered Production Film Services.
Generated: DETERMINISTIC_96d131eeda7842f3
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FirearmValidationError(Exception):
    """Custom exception for firearm validation errors."""
    pass

def requires_licensed_armourer(weapon_type: str, is_replica: bool) -> bool:
    """
    Determine if a firearm or replica weapon requires a licensed armourer on set
    based on NSW legislation.

    Parameters:
    weapon_type (str): The type of weapon (e.g., 'firearm', 'replica', 'non-firearm').
    is_replica (bool): Indicates if the weapon is a replica.

    Returns:
    bool: True if a licensed armourer is required, False otherwise.

    Raises:
    FirearmValidationError: If the weapon_type is invalid.
    """
    
    # Normalize the weapon type to lower case for consistent comparison
    weapon_type = weapon_type.lower()

    # Define valid weapon types
    valid_weapon_types = ['firearm', 'replica', 'non-firearm']

    # Check if the provided weapon type is valid
    if weapon_type not in valid_weapon_types:
        raise FirearmValidationError(f"Invalid weapon type: {weapon_type}. Must be one of {valid_weapon_types}.")

    # Logic to determine if a licensed armourer is required
    if weapon_type == 'firearm':
        return True  # Firearms always require a licensed armourer
    elif weapon_type == 'replica':
        return is_replica  # Replicas require a licensed armourer if they are indeed replicas
    else:  # 'non-firearm'
        return False  # Non-firearm weapons do not require a licensed armourer

# Example usage
if __name__ == "__main__":
    try:
        weapon = 'replica'
        is_replica = True
        if requires_licensed_armourer(weapon, is_replica):
            print("A licensed armourer is required on set.")
        else:
            print("A licensed armourer is not required on set.")
    except FirearmValidationError as e:
        print(f"Error: {e}")
```
