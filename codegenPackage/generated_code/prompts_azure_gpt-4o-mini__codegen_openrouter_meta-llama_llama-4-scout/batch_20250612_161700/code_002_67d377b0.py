"""
Generated Code Metadata:
========================
Original URL: https://geddesign.it
Prompt: Write a function to filter and display antique seating options on a website, ensuring a balance between classic elegance and contemporary style.
Generated: DETERMINISTIC_67d377b0839b37d2
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# antique_seating_filter.py

class SeatingOption:
    """Represents an antique seating option."""

    def __init__(self, name, style, era, material, price):
        """
        Initializes a SeatingOption object.

        Args:
            name (str): Name of the seating option.
            style (str): Style of the seating option (e.g., classic, contemporary).
            era (str): Era of the seating option (e.g., Victorian, Art Deco).
            material (str): Material of the seating option (e.g., wood, metal).
            price (float): Price of the seating option.
        """
        self.name = name
        self.style = style
        self.era = era
        self.material = material
        self.price = price

def filter_seating_options(seating_options, min_price, max_price, style=None, era=None):
    """
    Filters antique seating options based on price, style, and era.

    Args:
        seating_options (list[SeatingOption]): List of SeatingOption objects.
        min_price (float): Minimum price filter.
        max_price (float): Maximum price filter.
        style (str, optional): Style filter. Defaults to None.
        era (str, optional): Era filter. Defaults to None.

    Returns:
        list[SeatingOption]: Filtered list of SeatingOption objects.
    """
    filtered_options = [
        option for option in seating_options
        if min_price <= option.price <= max_price
    ]

    if style:
        filtered_options = [option for option in filtered_options if option.style == style]

    if era:
        filtered_options = [option for option in filtered_options if option.era == era]

    return filtered_options

def display_seating_options(seating_options):
    """
    Displays antique seating options in a formatted manner.

    Args:
        seating_options (list[SeatingOption]): List of SeatingOption objects.
    """
    for option in seating_options:
        print(f"**{option.name}**")
        print(f"Style: {option.style}")
        print(f"Era: {option.era}")
        print(f"Material: {option.material}")
        print(f"Price: ${option.price:.2f}")
        print("------------------------")

def main():
    # Example seating options
    seating_options = [
        SeatingOption("Victorian Chair", "Classic", "Victorian", "Wood", 500.0),
        SeatingOption("Art Deco Sofa", "Contemporary", "Art Deco", "Metal", 800.0),
        SeatingOption("Mid-Century Modern Chair", "Contemporary", "Mid-Century Modern", "Wood", 300.0),
        SeatingOption("Antique Armchair", "Classic", "Antique", "Wood", 700.0),
    ]

    try:
        min_price = 400.0
        max_price = 900.0
        filtered_options = filter_seating_options(seating_options, min_price, max_price)

        print("Filtered Seating Options:")
        display_seating_options(filtered_options)

        # Filter by style
        style = "Classic"
        filtered_options = filter_seating_options(seating_options, min_price, max_price, style=style)

        print(f"\nFiltered Seating Options ({style} style):")
        display_seating_options(filtered_options)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
