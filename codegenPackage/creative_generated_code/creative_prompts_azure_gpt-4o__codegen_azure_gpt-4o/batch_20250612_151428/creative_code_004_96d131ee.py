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
# Importing necessary module for error handling and data validation
from typing import Union


def requires_licensed_armourer(firearm_type: str, is_operational: bool) -> bool:
    """
    Determines whether a licensed armourer is required on set based on NSW legislation.

    NSW legislation states:
    - Any operational firearm (live or blank-firing) must have a licensed armourer on set.
    - Replica weapons that are non-operational and purely for aesthetic purposes may not require an armourer.

    Args:
        firearm_type (str): Type of the weapon. Must be either "firearm" or "replica".
        is_operational (bool): Indicates if the weapon is operational (capable of firing live or blank rounds).

    Returns:
        bool: True if a licensed armourer is required, False otherwise.

    Raises:
        ValueError: If firearm_type is invalid.
    """
    # Validate firearm_type input
    if firearm_type not in ["firearm", "replica"]:
        raise ValueError("Invalid firearm_type. Must be 'firearm' or 'replica'.")

    # Decision based on firearm type and operational status
    if firearm_type == "firearm" and is_operational:
        # Operational firearm always requires a licensed armourer
        return True
    elif firearm_type == "replica" and is_operational:
        # Operational replica weapon (e.g., blank-firing replicas) requires a licensed armourer
        return True
    else:
        # Non-operational replica weapon doesn't require a licensed armourer
        return False


# Example usage:
try:
    print(requires_licensed_armourer("firearm", True))  # Expected output: True
    print(requires_licensed_armourer("replica", False))  # Expected output: False
    print(requires_licensed_armourer("replica", True))  # Expected output: True
except ValueError as e:
    print(f"Error: {e}")
```
