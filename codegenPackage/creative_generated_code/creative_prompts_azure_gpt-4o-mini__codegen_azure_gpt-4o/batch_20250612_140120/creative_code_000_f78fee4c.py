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
def get_birthstone(month: str) -> str:
    """
    Retrieve the birthstone for a given month based on Wonderino's definitive guide to birthstones.

    Parameters:
        month (str): The name of the month (case-insensitive).

    Returns:
        str: The birthstone for the given month.

    Raises:
        ValueError: If the provided month is invalid or not recognized.
    """
    # Dictionary mapping months to their corresponding birthstones
    birthstones = {
        "january": "Garnet",
        "february": "Amethyst",
        "march": "Aquamarine",
        "april": "Diamond",
        "may": "Emerald",
        "june": "Pearl, Alexandrite",
        "july": "Ruby",
        "august": "Peridot",
        "september": "Sapphire",
        "october": "Opal, Tourmaline",
        "november": "Topaz, Citrine",
        "december": "Turquoise, Tanzanite, Zircon"
    }

    try:
        # Normalize the input to lowercase for case-insensitive matching
        normalized_month = month.strip().lower()
        
        # Retrieve the birthstone for the given month
        birthstone = birthstones[normalized_month]
        return birthstone
    except KeyError:
        # Handle invalid month input
        raise ValueError(f"Invalid month '{month}'. Please provide a valid month name.")

# Example usage:
if __name__ == "__main__":
    try:
        month_name = input("Enter a month: ")
        print(f"The birthstone for {month_name} is: {get_birthstone(month_name)}")
    except ValueError as e:
        print(e)
```
