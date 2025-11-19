"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coastalboatrentals.co.za
Prompt: Generate a Python script to display a list of available boats for rent at Coastal Boat Rentals in Knysna, including details like boat type, capacity, and motor specifications.
Generated: DETERMINISTIC_21b02cc5000e0d44
Batch ID: 20250612_164238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

# Define a Boat class to represent a boat available for rent
class Boat:
    def __init__(self, boat_type: str, capacity: int, motor_spec: str) -> None:
        """
        Initialize a Boat instance.

        :param boat_type: Type of the boat (e.g., "Sailboat", "Motorboat")
        :param capacity: Maximum number of people the boat can hold
        :param motor_spec: Specifications of the boat's motor
        """
        self.boat_type = boat_type
        self.capacity = capacity
        self.motor_spec = motor_spec

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the Boat instance to a dictionary.

        :return: A dictionary representation of the boat
        """
        return {
            "boat_type": self.boat_type,
            "capacity": self.capacity,
            "motor_spec": self.motor_spec
        }

# Function to load boats from a JSON file
def load_boats(file_path: str) -> List[Boat]:
    """
    Load boat data from a JSON file.

    :param file_path: Path to the JSON file containing boat data
    :return: A list of Boat instances
    :raises FileNotFoundError: If the specified file does not exist
    :raises ValueError: If the file contains invalid JSON
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        boats = [Boat(**boat) for boat in data]
        return boats
    except FileNotFoundError as e:
        print(f"Error: The file '{file_path}' was not found.")
        raise e
    except json.JSONDecodeError as e:
        print("Error: Invalid JSON data.")
        raise ValueError("Invalid JSON format.") from e

# Function to display available boats
def display_boats(boats: List[Boat]) -> None:
    """
    Display the list of available boats.

    :param boats: A list of Boat instances to display
    """
    if not boats:
        print("No boats available for rent.")
        return

    print("Available Boats for Rent:")
    for boat in boats:
        print(f"Type: {boat.boat_type}, Capacity: {boat.capacity}, Motor: {boat.motor_spec}")

# Main function to execute the script
def main() -> None:
    """
    Main function to load and display available boats for rent.
    """
    file_path = 'boats.json'  # Path to the JSON file containing boats data
    try:
        boats = load_boats(file_path)
        display_boats(boats)
    except (FileNotFoundError, ValueError) as e:
        print(f"Failed to load boats: {e}")

if __name__ == "__main__":
    main()
```

**Note**: Make sure to have a `boats.json` file in the same directory as this script with the appropriate structure, for example:

```json
[
    {"boat_type": "Sailboat", "capacity": 6, "motor_spec": "15 HP"},
    {"boat_type": "Motorboat", "capacity": 8, "motor_spec": "30 HP"}
]
```
