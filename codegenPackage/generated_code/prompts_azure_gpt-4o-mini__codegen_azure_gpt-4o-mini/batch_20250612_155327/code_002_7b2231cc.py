"""
Generated Code Metadata:
========================
Original URL: https://shahkarco.com
Prompt: Create a script that allows users to filter coat racks by color and style, reflecting the diverse options available at Shahkar Industry.
Generated: DETERMINISTIC_7b2231cc5fcd7f30
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class CoatRack:
    """Class representing a coat rack with color and style attributes."""
    
    def __init__(self, color, style):
        """Initialize a coat rack with a specific color and style."""
        self.color = color
        self.style = style

    def __repr__(self):
        """Return a string representation of the coat rack."""
        return f"CoatRack(color='{self.color}', style='{self.style}')"


class CoatRackFilter:
    """Class to filter coat racks based on color and style."""
    
    def __init__(self, coat_racks):
        """Initialize the filter with a list of coat racks."""
        self.coat_racks = coat_racks

    def filter_by_color(self, color):
        """Filter coat racks by color."""
        return [rack for rack in self.coat_racks if rack.color.lower() == color.lower()]

    def filter_by_style(self, style):
        """Filter coat racks by style."""
        return [rack for rack in self.coat_racks if rack.style.lower() == style.lower()]

    def filter_by_color_and_style(self, color, style):
        """Filter coat racks by both color and style."""
        return [rack for rack in self.coat_racks if rack.color.lower() == color.lower() and rack.style.lower() == style.lower()]


def load_coat_racks_from_json(file_path):
    """Load coat racks from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [CoatRack(item['color'], item['style']) for item in data]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def main():
    """Main function to run the coat rack filtering application."""
    # Load coat racks from a JSON file
    coat_racks = load_coat_racks_from_json('coat_racks.json')

    # Create a filter instance
    filter_instance = CoatRackFilter(coat_racks)

    # Example usage of the filter
    color = input("Enter color to filter by: ")
    style = input("Enter style to filter by: ")

    filtered_racks = filter_instance.filter_by_color_and_style(color, style)

    # Display the filtered coat racks
    if filtered_racks:
        print("Filtered Coat Racks:")
        for rack in filtered_racks:
            print(rack)
    else:
        print("No coat racks found matching the criteria.")


if __name__ == "__main__":
    main()
```

**Note:** Ensure that the `coat_racks.json` file exists in the same directory as this script and contains a valid JSON array of coat rack objects, each with `color` and `style` attributes.
