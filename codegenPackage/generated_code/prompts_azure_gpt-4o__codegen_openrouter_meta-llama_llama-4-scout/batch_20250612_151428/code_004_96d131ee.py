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
"""
Validate whether a firearm or replica weapon requires a licensed armourer on set based on NSW legislation.

According to NSW legislation provided by Powered Production Film Services,
a licensed armourer is required for:
- All firearms (including air guns and pistols)
- Replica firearms that are indistinguishable from the real thing
- Replica firearms that are used in a manner that could be reasonably mistaken for a real firearm being used

Sources:
- Powered Production Film Services - NSW Legislation Guidelines
"""

def requires_armourer(weapon_type: str, is_replica: bool, is_indistinguishable: bool, usage_may_be_mistaken: bool) -> bool:
    """
    Determine whether a licensed armourer is required on set.

    Args:
    - weapon_type (str): Type of the weapon (e.g., firearm, replica)
    - is_replica (bool): Whether the weapon is a replica
    - is_indistinguishable (bool): Whether the replica is indistinguishable from the real thing
    - usage_may_be_mistaken (bool): Whether the usage of the replica may be reasonably mistaken for a real firearm being used

    Returns:
    - bool: Whether a licensed armourer is required
    """

    # If the weapon is a firearm, a licensed armourer is required
    if not is_replica:
        return True  # Firearms always require a licensed armourer

    # If the replica is indistinguishable or its usage may be mistaken for a real firearm, a licensed armourer is required
    if is_replica and (is_indistinguishable or usage_may_be_mistaken):
        return True  # Replica with specific conditions requires a licensed armourer

    # In all other cases, a licensed armourer is not required
    return False  # No licensed armourer required


def main():
    try:
        # Example usage:
        print(requires_armourer("firearm", False, False, False))  # Expected output: True
        print(requires_armourer("replica", True, True, False))  # Expected output: True
        print(requires_armourer("replica", True, False, True))  # Expected output: True
        print(requires_armourer("replica", True, False, False))  # Expected output: False

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
