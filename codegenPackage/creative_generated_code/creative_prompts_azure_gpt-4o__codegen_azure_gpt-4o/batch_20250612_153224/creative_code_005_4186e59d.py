"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nyikudesign.com
Prompt: Develop a Python program to design a cafe layout with an outdoor seating area, incorporating modern design elements as discussed in Nyiku Design's blog on outdoor cafe design.
Generated: DETERMINISTIC_4186e59d3f48387e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Cafe Layout Design Program
This Python program generates a cafe layout including an outdoor seating area,
incorporating modern design elements inspired by Nyiku Design's blog on outdoor cafe design.

Key Features:
- Indoor seating arrangement
- Outdoor seating arrangement
- Modern design elements such as greenery and lighting
- Error handling for invalid inputs
"""

# Required Imports
import json

# Constants
INDOOR_MAX_TABLES = 20
OUTDOOR_MAX_TABLES = 15
TABLE_CAPACITY = 4
DEFAULT_GREENERY = ['Potted Plants', 'Vertical Garden']
DEFAULT_LIGHTING = ['Ambient Lighting', 'LED String Lights']

class CafeLayout:
    """
    A class to represent the cafe layout, including indoor and outdoor seating areas.
    """
    def __init__(self, indoor_tables, outdoor_tables, greenery=None, lighting=None):
        """
        Initialize the cafe layout.

        :param indoor_tables: Number of indoor tables
        :param outdoor_tables: Number of outdoor tables
        :param greenery: List of greenery elements (default: DEFAULT_GREENERY)
        :param lighting: List of lighting elements (default: DEFAULT_LIGHTING)
        """
        # Validate table counts
        if not (0 <= indoor_tables <= INDOOR_MAX_TABLES):
            raise ValueError(f"Indoor tables must be between 0 and {INDOOR_MAX_TABLES}.")
        if not (0 <= outdoor_tables <= OUTDOOR_MAX_TABLES):
            raise ValueError(f"Outdoor tables must be between 0 and {OUTDOOR_MAX_TABLES}.")
        
        self.indoor_tables = indoor_tables
        self.outdoor_tables = outdoor_tables
        self.greenery = greenery or DEFAULT_GREENERY
        self.lighting = lighting or DEFAULT_LIGHTING

    def get_total_capacity(self):
        """
        Calculate total seating capacity.

        :return: Total seating capacity (indoor + outdoor)
        """
        return (self.indoor_tables + self.outdoor_tables) * TABLE_CAPACITY

    def to_dict(self):
        """
        Convert the cafe layout to a dictionary for display or storage.

        :return: Dictionary representation of the cafe layout
        """
        return {
            "Indoor Tables": self.indoor_tables,
            "Outdoor Tables": self.outdoor_tables,
            "Greenery": self.greenery,
            "Lighting": self.lighting,
            "Total Capacity": self.get_total_capacity()
        }


# Functions
def design_cafe_layout():
    """
    Facilitates the design of a cafe layout by taking user input.

    :return: CafeLayout object
    """
    try:
        print("Welcome to the Cafe Layout Designer!")
        
        # Get user input
        indoor_tables = int(input(f"Enter the number of indoor tables (0-{INDOOR_MAX_TABLES}): "))
        outdoor_tables = int(input(f"Enter the number of outdoor tables (0-{OUTDOOR_MAX_TABLES}): "))
        
        # Display options for greenery and lighting
        print("\nDefault Greenery Options:", DEFAULT_GREENERY)
        print("Default Lighting Options:", DEFAULT_LIGHTING)
        use_defaults = input("Use default design elements? (yes/no): ").strip().lower()

        if use_defaults == 'no':
            greenery = input("Enter greenery elements (comma-separated): ").split(',')
            lighting = input("Enter lighting elements (comma-separated): ").split(',')
        else:
            greenery = DEFAULT_GREENERY
            lighting = DEFAULT_LIGHTING

        # Create and return the cafe layout object
        layout = CafeLayout(indoor_tables, outdoor_tables, greenery, lighting)
        return layout

    except ValueError as e:
        print(f"Error: {e}. Please enter valid numbers for tables.")
        return None


# Main Execution
if __name__ == "__main__":
    layout = design_cafe_layout()
    if layout:
        print("\nCafe Layout Design:")
        print(json.dumps(layout.to_dict(), indent=4))
        print("Design complete!")
    else:
        print("Failed to design cafe layout. Please try again.")
```
