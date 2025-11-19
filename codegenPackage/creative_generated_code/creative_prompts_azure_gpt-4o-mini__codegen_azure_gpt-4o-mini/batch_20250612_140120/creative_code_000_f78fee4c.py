"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wonderino.com
Prompt: Generate a Python function that retrieves the birthstone for a given month using the data from Wonderino's definitive guide to birthstones.
Generated: DETERMINISTIC_f78fee4c3f58674f
Batch ID: 20250612_140120
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def get_birthstone(month: int) -> str:
    """
    Retrieve the birthstone for a given month.

    Args:
        month (int): The month as an integer (1 for January, 2 for February, ..., 12 for December).

    Returns:
        str: The birthstone associated with the given month.

    Raises:
        ValueError: If the month is not in the range of 1 to 12.
    """

    # Dictionary mapping month numbers to birthstones
    birthstones = {
        1: "Garnet",
        2: "Amethyst",
        3: "Aquamarine",
        4: "Diamond",
        5: "Emerald",
        6: "Alexandrite",
        7: "Ruby",
        8: "Peridot",
        9: "Sapphire",
        10: "Opal",
        11: "Topaz",
        12: "Turquoise"
    }

    # Validate the month input
    if month < 1 or month > 12:
        raise ValueError("Month must be an integer between 1 and 12.")

    # Retrieve and return the birthstone for the specified month
    return birthstones[month]

# Example usage
if __name__ == "__main__":
    try:
        month = 5  # Example month (May)
        print(f"The birthstone for month {month} is: {get_birthstone(month)}")
    except ValueError as e:
        print(f"Error: {e}")
```
