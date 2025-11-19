"""
Generated Code Metadata:
========================
Original URL: https://eternallaunch.pages.dev
Prompt: Generate a Python code snippet to calculate the boost for a participant in the $EAI public sale based on their position in the allowlist and the provided boost levels.
Generated: DETERMINISTIC_f55bc46ba9c68dab
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_boost(allowlist_position: int, boost_levels: dict) -> float:
    """
    Calculate the boost for a participant in the EAI public sale.

    Args:
    - allowlist_position (int): The position of the participant in the allowlist.
    - boost_levels (dict): A dictionary containing boost levels with their corresponding allowlist positions.

    Returns:
    - float: The calculated boost.

    Raises:
    - ValueError: If allowlist_position is not a positive integer or if boost_levels is not a dictionary.
    - KeyError: If allowlist_position is not found in boost_levels.
    """

    # Validate input types
    if not isinstance(allowlist_position, int) or allowlist_position <= 0:
        raise ValueError("Allowlist position must be a positive integer.")

    if not isinstance(boost_levels, dict):
        raise ValueError("Boost levels must be a dictionary.")

    # Sort boost levels by allowlist position
    sorted_boost_levels = dict(sorted(boost_levels.items()))

    # Initialize boost to 1.0 (no boost)
    boost = 1.0

    # Find the boost level for the given allowlist position
    for position, level in sorted_boost_levels.items():
        if allowlist_position <= position:
            boost = level
            break
    else:
        # If allowlist_position is greater than any position in boost_levels, use the last boost level
        boost = list(sorted_boost_levels.values())[-1]

    return boost


def main():
    # Example usage
    boost_levels = {
        100: 1.5,
        500: 2.0,
        1000: 2.5
    }

    allowlist_position = 750
    try:
        boost = calculate_boost(allowlist_position, boost_levels)
        print(f"The boost for position {allowlist_position} is {boost}")
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
