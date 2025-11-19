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
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

# Constants
MENU_FILE = "menu.json"
ORDERS_FILE = "orders.json"
RESERVATIONS_FILE = "reservations.json"
TIME_FORMAT = "%Y-%m-%d %H:%M"

class RestaurantManager:
    """
    A class to manage online orders and reservations for an Italian restaurant.
    """
    
    def __init__(self):
        """
        Initialize the restaurant manager by loading existing data from files.
        """
        self.menu = self._load_data(MENU_FILE, default=[])
        self.orders = self._load_data(ORDERS_FILE, default=[])
        self.reservations = self._load_data(RESERVATIONS_FILE, default=[])
    
    def _load_data(self, filename: str, default=None) -> Dict:
        """
        Load data from a JSON file or return default if file doesn't exist.
        
        Args:
            filename: Name of the file to load
            default: Default value if file doesn't exist
            
        Returns:
            Loaded data or default value
        """
        try:
            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    return json.load(file)
        except Exception as e:
            print(f"Error loading {filename}: {e}")
        return default if default is not None else {}
    
    def _save_data(self, data: Dict, filename: str) -> bool:
        """
        Save data to a JSON file.
        
        Args:
            data: Data to save
            filename: Name of the file to save to
            
        Returns:
            True if successful, False otherwise
        """
        try:
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
            return True
        except Exception as e:
            print(f"Error saving to {filename}: {e}")
            return False
    
    def get_menu(self) -> List[Dict]:
        """
        Get the current menu items.
        
        Returns:
            List of menu items with details
        """
        return self.menu
    
    def add_menu_item(self, name: str, description: str, price: float, category: str) -> bool:
        """
        Add a new item to the menu.
        
        Args:
            name: Name of the item (e.g., "Fettuccine Carbonara")
            description: Description of the item
            price: Price of the item
            category: Category (e.g., "Pasta", "Main")
            
        Returns:
            True if successful, False otherwise
        """
        new_item = {
            "id": len(self.menu) + 1,
            "name": name,
            "description": description,
            "price": price,
            "category": category
        }
        self.menu.append(new_item)
        return self._save_data(self.menu, MENU_FILE)
    
    def place_order(self, customer_name: str, items: List[int], delivery_address: str) -> Optional[Dict]:
        """
        Place a new food order.
        
        Args:
            customer_name: Name of the customer
            items: List of menu item IDs to order
            delivery_address: Delivery address
            
        Returns:
            Order details if successful, None otherwise
        """
        # Validate items exist in menu
        valid_items = []
        total_price = 0.0
        menu_ids = {item["id"] for item in self.menu}
        
        for item_id in items:
            if item_id not in menu_ids:
                print(f"Menu item ID {item_id} not found")
                return None
            valid_items.append(item_id)
            total_price += next(item["price"] for item in self.menu if item["id"] == item_id)
        
        new_order = {
            "id": len(self.orders) + 1,
            "customer_name": customer_name,
            "items": valid_items,
            "total_price": total_price,
            "delivery_address": delivery_address,
            "status": "Received",
            "timestamp": datetime.now().strftime(TIME_FORMAT)
        }
        
        self.orders.append(new_order)
        if self._save_data(self.orders, ORDERS_FILE):
            return new_order
        return None
    
    def make_reservation(self, customer_name: str, party_size: int, reservation_time: str) -> Optional[Dict]:
        """
        Make a new table reservation.
        
        Args:
            customer_name: Name of the customer
            party_size: Number of people in the party
            reservation_time: Desired reservation time (YYYY-MM-DD HH:MM)
            
        Returns:
            Reservation details if successful, None otherwise
        """
        try:
            res_time = datetime.strptime(reservation_time, TIME_FORMAT)
        except ValueError:
            print("Invalid time format. Please use YYYY-MM-DD HH:MM")
            return None
        
        # Check if reservation is in the future
        if res_time < datetime.now():
            print("Reservation time must be in the future")
            return None
        
        # Check for available tables (simplified - in reality would check capacity)
        conflicting_reservations = [
            r for r in self.reservations
            if datetime.strptime(r["reservation_time"], TIME_FORMAT) == res_time
        ]
        
        if len(conflicting_reservations) >= 10:  # Assuming 10 tables max
            print("No available tables at that time")
            return None
        
        new_reservation = {
            "id": len(self.reservations) + 1,
            "customer_name": customer_name,
            "party_size": party_size,
            "reservation_time": reservation_time,
            "status": "Confirmed",
            "created_at": datetime.now().strftime(TIME_FORMAT)
        }
        
        self.reservations.append(new_reservation)
        if self._save_data(self.reservations, RESERVATIONS_FILE):
            return new_reservation
        return None
    
    def get_order_status(self, order_id: int) -> Optional[str]:
        """
        Get the status of an order.
        
        Args:
            order_id: ID of the order to check
            
        Returns:
            Order status if found, None otherwise
        """
        for order in self.orders:
            if order["id"] == order_id:
                return order["status"]
        return None
    
    def update_order_status(self, order_id: int, new_status: str) -> bool:
        """
        Update the status of an order.
        
        Args:
            order_id: ID of the order to update
            new_status: New status (e.g., "Preparing", "Delivered")
            
        Returns:
            True if successful, False otherwise
        """
        for order in self.orders:
            if order["id"] == order_id:
                order["status"] = new_status
                return self._save_data(self.orders, ORDERS_FILE)
        return False
    
    def cancel_reservation(self, reservation_id: int) -> bool:
        """
        Cancel a reservation.
        
        Args:
            reservation_id: ID of the reservation to cancel
            
        Returns:
            True if successful, False otherwise
        """
        for i, reservation in enumerate(self.reservations):
            if reservation["id"] == reservation_id:
                self.reservations[i]["status"] = "Cancelled"
                return self._save_data(self.reservations, RESERVATIONS_FILE)
        return False

# Example usage
if __name__ == "__main__":
    manager = RestaurantManager()
    
    # Initialize sample menu if empty
    if not manager.menu:
        manager.add_menu_item("Fettuccine Carbonara", "Creamy pasta with bacon and egg", 18.50, "Pasta")
        manager.add_menu_item("Lasagna", "Layered pasta with meat and cheese", 20.00, "Main")
        manager.add_menu_item("Tiramisu", "Coffee-flavored dessert", 9.50, "Dessert")
    
    # Example order
    order = manager.place_order(
        customer_name="John Doe",
        items=[1, 3],  # Fettuccine Carbonara and Tiramisu
        delivery_address="123 Main St, Whangarei"
    )
    
    if order:
        print(f"Order placed successfully. Total: ${order['total_price']:.2f}")
    
    # Example reservation
    future_time = (datetime.now() + timedelta(days=1)).strftime(TIME_FORMAT)
    reservation = manager.make_reservation(
        customer_name="Jane Smith",
        party_size=4,
        reservation_time=future_time
    )
    
    if reservation:
        print(f"Reservation confirmed for {reservation['reservation_time']}")
```
