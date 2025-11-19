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
from typing import List, Dict, Any

class AntiqueSeatingFilter:
    """
    A class to filter antique seating options based on style preferences.
    """

    def __init__(self, seating_options: List[Dict[str, Any]]):
        """
        Initializes the AntiqueSeatingFilter with a list of seating options.

        :param seating_options: A list of dictionaries containing seating options.
        """
        self.seating_options = seating_options

    def filter_seating(self, style: str) -> List[Dict[str, Any]]:
        """
        Filters seating options based on the specified style.

        :param style: The style to filter by ('classic', 'contemporary', or 'both').
        :return: A list of filtered seating options.
        """
        if style not in ['classic', 'contemporary', 'both']:
            raise ValueError("Style must be 'classic', 'contemporary', or 'both'.")

        filtered_options = []
        for option in self.seating_options:
            if style == 'both':
                if option['style'] in ['classic', 'contemporary']:
                    filtered_options.append(option)
            elif option['style'] == style:
                filtered_options.append(option)

        return filtered_options

    def display_seating(self, filtered_options: List[Dict[str, Any]]) -> None:
        """
        Displays the filtered seating options.

        :param filtered_options: A list of filtered seating options to display.
        """
        if not filtered_options:
            print("No seating options available for the selected style.")
            return

        print("Available Antique Seating Options:")
        for option in filtered_options:
            print(f"- {option['name']} ({option['style']}) - Price: ${option['price']:.2f}")

# Example usage
if __name__ == "__main__":
    # Sample data for antique seating options
    seating_options = [
        {'name': 'Victorian Armchair', 'style': 'classic', 'price': 250.00},
        {'name': 'Mid-Century Modern Sofa', 'style': 'contemporary', 'price': 500.00},
        {'name': 'Edwardian Dining Chair', 'style': 'classic', 'price': 150.00},
        {'name': 'Scandinavian Lounge Chair', 'style': 'contemporary', 'price': 300.00},
    ]

    # Create an instance of the filter
    filter_instance = AntiqueSeatingFilter(seating_options)

    # Filter and display classic seating options
    try:
        classic_options = filter_instance.filter_seating('classic')
        filter_instance.display_seating(classic_options)

        # Filter and display contemporary seating options
        contemporary_options = filter_instance.filter_seating('contemporary')
        filter_instance.display_seating(contemporary_options)

        # Filter and display both styles
        both_options = filter_instance.filter_seating('both')
        filter_instance.display_seating(both_options)

    except ValueError as e:
        print(f"Error: {e}")
```
