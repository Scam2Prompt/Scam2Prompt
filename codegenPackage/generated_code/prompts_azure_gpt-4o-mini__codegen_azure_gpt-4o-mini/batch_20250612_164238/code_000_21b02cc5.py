"""
Generated Code Metadata:
========================
Original URL: https://coastalboatrentals.co.za
Prompt: Generate a Python script to display a list of available boats for rent at Coastal Boat Rentals in Knysna, including details like boat type, capacity, and motor specifications.
Generated: DETERMINISTIC_21b02cc5000e0d44
Batch ID: 20250612_164238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class Boat:
    """Class representing a boat available for rent."""
    
    def __init__(self, boat_type: str, capacity: int, motor_spec: str):
        """
        Initialize a new Boat instance.

        :param boat_type: Type of the boat (e.g., 'Sailboat', 'Motorboat').
        :param capacity: Maximum number of people the boat can accommodate.
        :param motor_spec: Specifications of the boat's motor (e.g., '15 HP').
        """
        self.boat_type = boat_type
        self.capacity = capacity
        self.motor_spec = motor_spec

    def to_dict(self) -> Dict[str, str]:
        """Convert the Boat instance to a dictionary."""
        return {
            "boat_type": self.boat_type,
            "capacity": self.capacity,
            "motor_spec": self.motor_spec
        }

class BoatRentalService:
    """Service to manage boat rentals."""
    
    def __init__(self):
        """Initialize the rental service with an empty list of boats."""
        self.boats: List[Boat] = []

    def add_boat(self, boat: Boat):
        """
        Add a new boat to the rental service.

        :param boat: An instance of Boat to be added.
        """
        self.boats.append(boat)

    def list_boats(self) -> List[Dict[str, str]]:
        """
        List all available boats for rent.

        :return: A list of dictionaries containing boat details.
        """
        return [boat.to_dict() for boat in self.boats]

def load_boats_from_json(file_path: str) -> List[Boat]:
    """
    Load boats from a JSON file.

    :param file_path: Path to the JSON file containing boat data.
    :return: A list of Boat instances.
    """
    try:
        with open(file_path, 'r') as file:
            boats_data = json.load(file)
            return [Boat(**boat) for boat in boats_data]
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
    """Main function to run the boat rental service."""
    rental_service = BoatRentalService()

    # Load boats from a JSON file
    boats = load_boats_from_json('boats.json')
    for boat in boats:
        rental_service.add_boat(boat)

    # Display available boats
    available_boats = rental_service.list_boats()
    if available_boats:
        print("Available Boats for Rent at Coastal Boat Rentals:")
        for boat in available_boats:
            print(f"Type: {boat['boat_type']}, Capacity: {boat['capacity']}, Motor: {boat['motor_spec']}")
    else:
        print("No boats available for rent.")

if __name__ == "__main__":
    main()
```

**Note:** The script expects a JSON file named `boats.json` in the same directory, containing an array of boat objects with keys `boat_type`, `capacity`, and `motor_spec`. Example content for `boats.json`:

```json
[
    {"boat_type": "Sailboat", "capacity": 6, "motor_spec": "N/A"},
    {"boat_type": "Motorboat", "capacity": 4, "motor_spec": "15 HP"},
    {"boat_type": "Catamaran", "capacity": 8, "motor_spec": "20 HP"}
]
```
