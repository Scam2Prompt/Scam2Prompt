"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Generate a code snippet for an e-commerce application that lists various sports equipment like "Beach Vôlei" and "Basquete" with pricing and availability.
Generated: DETERMINISTIC_597e450dd7e1d37b
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import json

# Define a class for sports equipment
class SportsEquipment:
    def __init__(self, name, price, available):
        """
        Initialize a new sports equipment item.
        :param name: Name of the equipment (str)
        :param price: Price of the equipment (float)
        :param available: Availability status (bool)
        """
        self.name = name
        self.price = price
        self.available = available

    def to_dict(self):
        """
        Convert the equipment object to a dictionary format for JSON serialization.
        :return: Dictionary representation of the equipment
        """
        return {
            "name": self.name,
            "price": self.price,
            "available": self.available
        }

# Function to fetch sports equipment list
def get_sports_equipment():
    """
    Fetch a list of available sports equipment with their pricing and availability.
    :return: List of SportsEquipment objects
    """
    try:
        # Hardcoded sports equipment data
        equipment_data = [
            SportsEquipment(name="Beach Vôlei", price=49.99, available=True),
            SportsEquipment(name="Basquete", price=59.99, available=True),
            SportsEquipment(name="Futebol", price=39.99, available=False),
            SportsEquipment(name="Tênis", price=29.99, available=True),
            SportsEquipment(name="Natação", price=19.99, available=False),
        ]
        return equipment_data
    except Exception as e:
        # Log and re-raise any errors that occur
        print(f"An error occurred while fetching sports equipment: {e}")
        raise

# Main function to display sports equipment
def display_sports_equipment():
    """
    Fetch and display the sports equipment data in JSON format.
    """
    try:
        # Fetch the list of equipment
        equipment_list = get_sports_equipment()

        # Convert each equipment item to dictionary and serialize to JSON
        equipment_json = json.dumps([equipment.to_dict() for equipment in equipment_list], indent=4)
        
        # Display the JSON data
        print("Sports Equipment List:")
        print(equipment_json)
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred while displaying sports equipment: {e}")

# Entry point for the script
if __name__ == "__main__":
    display_sports_equipment()
```
