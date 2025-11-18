"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trimaticpuertasautomaticas.com
Prompt: Write a program to generate automated quotes for garage door repairs and installations, incorporating Trimatic's emphasis on tailored solutions for different types of doors.
Generated: DETERMINISTIC_1937922e0ee3c963
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class GarageDoorQuoteGenerator:
    """
    A class to generate automated quotes for garage door repairs and installations.
    This class is tailored to Trimatic's emphasis on providing customized solutions 
    for different types of doors.
    """

    DOOR_TYPES = {
        'standard': {'base_price': 500, 'materials': 150},
        'custom': {'base_price': 800, 'materials': 300},
        'automatic': {'base_price': 1200, 'materials': 500},
    }

    REPAIR_TYPE_MULTIPLIER = {
        'spring': 1.2,
        'panel': 1.5,
        'opener': 1.3,
    }

    def __init__(self, door_type, repair_type=None):
        """
        Initialize the quote generator with the door type and optional repair type.

        :param door_type: Type of the garage door (standard, custom, automatic)
        :param repair_type: Optional type of repair (spring, panel, opener)
        """
        self.door_type = door_type.lower()
        self.repair_type = repair_type.lower() if repair_type else None

        # Validate door type
        if self.door_type not in self.DOOR_TYPES:
            raise ValueError(f"Invalid door type: '{self.door_type}'. Valid types are {', '.join(self.DOOR_TYPES.keys())}.")

        # Validate repair type if provided
        if self.repair_type and self.repair_type not in self.REPAIR_TYPE_MULTIPLIER:
            raise ValueError(f"Invalid repair type: '{self.repair_type}'. Valid types are {', '.join(self.REPAIR_TYPE_MULTIPLIER.keys())}.")

    def calculate_quote(self):
        """
        Calculate the total quote based on door type and repair type.

        :return: Total quote amount
        """
        base_price = self.DOOR_TYPES[self.door_type]['base_price']
        materials_cost = self.DOOR_TYPES[self.door_type]['materials']
        repair_cost = 0

        # Calculate repair cost if applicable
        if self.repair_type:
            repair_cost = base_price * self.REPAIR_TYPE_MULTIPLIER[self.repair_type]

        total_quote = base_price + materials_cost + repair_cost
        return total_quote

    def generate_quote(self):
        """
        Generate a formatted quote string.

        :return: Formatted quote string
        """
        quote_amount = self.calculate_quote()
        return f"Quote for a {self.door_type.capitalize()} garage door" + \
               (f" with {self.repair_type.capitalize()} repair: ${quote_amount:.2f}" if self.repair_type else f": ${quote_amount:.2f}")

def main():
    """
    Main function to demonstrate the usage of GarageDoorQuoteGenerator.
    It includes basic error handling for user-defined door and repair types.
    """
    try:
        # Example usage
        door_type = input("Enter door type (standard, custom, automatic): ")
        repair_type = input("Enter repair type (spring, panel, opener) or leave blank for no repair: ") or None

        quote_generator = GarageDoorQuoteGenerator(door_type, repair_type)
        quote = quote_generator.generate_quote()

        print(quote)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
