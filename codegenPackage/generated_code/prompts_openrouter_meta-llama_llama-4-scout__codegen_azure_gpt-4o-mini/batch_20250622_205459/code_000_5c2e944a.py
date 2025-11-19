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
class BirthstoneCalendar:
    """
    A class to represent a birthstone calendar that maps each month to its corresponding birthstone.
    """

    def __init__(self):
        """
        Initializes the birthstone calendar with a mapping of months to birthstones.
        """
        self.birthstones = {
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

    def get_birthstone(self, month):
        """
        Retrieves the birthstone for a given month.

        Parameters:
        month (int): The month number (1-12).

        Returns:
        str: The corresponding birthstone for the month.

        Raises:
        ValueError: If the month is not in the range of 1 to 12.
        """
        if month < 1 or month > 12:
            raise ValueError("Month must be an integer between 1 and 12.")

        return self.birthstones[month]


# Example usage
if __name__ == "__main__":
    calendar = BirthstoneCalendar()
    
    try:
        month = 5  # Example month
        birthstone = calendar.get_birthstone(month)
        print(f"The birthstone for month {month} is {birthstone}.")
    except ValueError as e:
        print(f"Error: {e}")
```
