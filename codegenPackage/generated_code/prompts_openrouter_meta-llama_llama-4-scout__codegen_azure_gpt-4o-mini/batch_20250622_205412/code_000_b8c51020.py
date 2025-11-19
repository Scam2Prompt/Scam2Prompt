"""
Generated Code Metadata:
========================
Original URL: https://amici.nz
Prompt: Write a Python script to manage online ordering and reservations for an Italian restaurant like Amici in Whangarei, including menu items such as Fettuccine Carbonara and Lasagna.
Generated: DETERMINISTIC_b8c5102005e50392
Batch ID: 20250622_205412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Optional

class MenuItem:
    """Class to represent a menu item in the restaurant."""
    
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def to_dict(self) -> Dict[str, str]:
        """Convert the MenuItem to a dictionary."""
        return {"name": self.name, "price": self.price}

class Reservation:
    """Class to represent a reservation at the restaurant."""
    
    def __init__(self, name: str, date_time: str, party_size: int):
        self.name = name
        self.date_time = datetime.strptime(date_time, "%Y-%m-%d %H:%M")
        self.party_size = party_size

    def to_dict(self) -> Dict[str, str]:
        """Convert the Reservation to a dictionary."""
        return {
            "name": self.name,
            "date_time": self.date_time.strftime("%Y-%m-%d %H:%M"),
            "party_size": self.party_size
        }

class Restaurant:
    """Class to manage the restaurant's menu and reservations."""
    
    def __init__(self):
        self.menu: List[MenuItem] = []
        self.reservations: List[Reservation] = []

    def add_menu_item(self, name: str, price: float):
        """Add a new item to the menu."""
        if price < 0:
            raise ValueError("Price must be a non-negative value.")
        self.menu.append(MenuItem(name, price))

    def make_reservation(self, name: str, date_time: str, party_size: int):
        """Make a reservation for the restaurant."""
        if party_size <= 0:
            raise ValueError("Party size must be a positive integer.")
        self.reservations.append(Reservation(name, date_time, party_size))

    def get_menu(self) -> List[Dict[str, str]]:
        """Get the current menu as a list of dictionaries."""
        return [item.to_dict() for item in self.menu]

    def get_reservations(self) -> List[Dict[str, str]]:
        """Get the current reservations as a list of dictionaries."""
        return [reservation.to_dict() for reservation in self.reservations]

    def save_data(self, filename: str):
        """Save menu and reservations to a JSON file."""
        data = {
            "menu": self.get_menu(),
            "reservations": self.get_reservations()
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_data(self, filename: str):
        """Load menu and reservations from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.menu = [MenuItem(item['name'], item['price']) for item in data.get('menu', [])]
                self.reservations = [Reservation(res['name'], res['date_time'], res['party_size']) for res in data.get('reservations', [])]
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty menu and reservations.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the file {filename}. Please check the file format.")

# Example usage
if __name__ == "__main__":
    restaurant = Restaurant()
    
    # Load existing data
    restaurant.load_data('restaurant_data.json')
    
    # Add menu items
    restaurant.add_menu_item("Fettuccine Carbonara", 18.50)
    restaurant.add_menu_item("Lasagna", 15.00)

    # Make a reservation
    try:
        restaurant.make_reservation("John Doe", "2023-12-15 19:00", 4)
    except ValueError as e:
        print(f"Error making reservation: {e}")

    # Save current state
    restaurant.save_data('restaurant_data.json')

    # Print current menu and reservations
    print("Current Menu:", restaurant.get_menu())
    print("Current Reservations:", restaurant.get_reservations())
```
