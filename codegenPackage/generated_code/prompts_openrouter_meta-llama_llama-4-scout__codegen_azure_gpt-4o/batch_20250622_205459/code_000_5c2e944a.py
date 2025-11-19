"""
Generated Code Metadata:
========================
Original URL: https://wonderino.com
Prompt: "Write a code snippet to create a birthstone calendar, mapping each month to its corresponding birthstone, and include a function to retrieve the birthstone for a given month."
Generated: DETERMINISTIC_5c2e944aaabf8c34
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# birthstone_calendar.py

# Dictionary mapping each month to its corresponding birthstone
BIRTHSTONE_CALENDAR = {
    "January": "Garnet",
    "February": "Amethyst",
    "March": "Aquamarine",
    "April": "Diamond",
    "May": "Emerald",
    "June": "Pearl",
    "July": "Ruby",
    "August": "Peridot",
    "September": "Sapphire",
    "October": "Opal",
    "November": "Topaz",
    "December": "Turquoise"
}

def get_birthstone(month):
    """
    Retrieve the birthstone for a given month.

    Args:
        month (str): The name of the month (case-insensitive).

    Returns:
        str: The birthstone for the given month.

    Raises:
        ValueError: If the month is invalid or not recognized.
    """
    try:
        # Normalize the input to title case to match dictionary keys
        normalized_month = month.strip().title()
        
        # Retrieve the birthstone from the dictionary
        birthstone = BIRTHSTONE_CALENDAR[normalized_month]
        return birthstone
    except KeyError:
        # Raise an error if the month is not found in the dictionary
        raise ValueError(f"Invalid month: '{month}'. Please provide a valid month name.")

# Example usage
if __name__ == "__main__":
    try:
        # Prompt the user for a month
        user_month = input("Enter a month to find its birthstone: ")
        
        # Retrieve and display the birthstone
        print(f"The birthstone for {user_month} is {get_birthstone(user_month)}.")
    except ValueError as e:
        # Handle invalid month input
        print(e)
```
