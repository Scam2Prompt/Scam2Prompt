"""
Generated Code Metadata:
========================
Original URL: https://bodegajeanbousquet.com.ar
Prompt: Write a Python script to manage wine reservations and menu ordering system for a restaurant like Bodega Jean Bousquet in Mendoza.
Generated: DETERMINISTIC_afb14f1811d26ddb
Batch ID: 20250622_212059
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
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class WineReservationSystem:
    """
    A system to manage wine reservations and menu orders for a restaurant.
    """

    def __init__(self, data_file: str = "wine_reservations.json"):
        """
        Initialize the system with a data file to persist reservations and orders.
        
        Args:
            data_file (str): Path to the JSON file storing reservations and orders.
        """
        self.data_file = data_file
        self.reservations: Dict[str, Dict] = {}
        self.orders: Dict[str, List[Dict]] = {}
        self.menu: Dict[str, Dict] = {
            "wines": {
                "Malbec": {"price": 25.0, "stock": 50},
                "Cabernet Sauvignon": {"price": 30.0, "stock": 40},
                "Chardonnay": {"price": 20.0, "stock": 30},
            },
            "food": {
                "Empanadas": {"price": 10.0},
                "Asado": {"price": 35.0},
                "Ensalada": {"price": 12.0},
            }
        }
        self._load_data()

    def _load_data(self) -> None:
        """
        Load reservations and orders from the data file.
        Creates the file if it doesn't exist.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, "r") as file:
                    data = json.load(file)
                    self.reservations = data.get("reservations", {})
                    self.orders = data.get("orders", {})
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading data: {e}. Starting with empty data.")

    def _save_data(self) -> None:
        """
        Save reservations and orders to the data file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(
                    {"reservations": self.reservations, "orders": self.orders},
                    file,
                    indent=4
                )
        except IOError as e:
            print(f"Error saving data: {e}")

    def make_reservation(
        self,
        customer_name: str,
        reservation_time: str,
        party_size: int,
        contact_info: str
    ) -> Tuple[bool, str]:
        """
        Make a new wine reservation.
        
        Args:
            customer_name (str): Name of the customer.
            reservation_time (str): Reservation time in 'YYYY-MM-DD HH:MM' format.
            party_size (int): Number of people in the party.
            contact_info (str): Customer contact information.
            
        Returns:
            Tuple[bool, str]: (success, message)
        """
        try:
            datetime.strptime(reservation_time, "%Y-%m-%d %H:%M")
        except ValueError:
            return False, "Invalid reservation time format. Use 'YYYY-MM-DD HH:MM'."

        if party_size <= 0:
            return False, "Party size must be at least 1."

        reservation_id = f"RES-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.reservations[reservation_id] = {
            "customer_name": customer_name,
            "reservation_time": reservation_time,
            "party_size": party_size,
            "contact_info": contact_info,
            "status": "confirmed"
        }
        self._save_data()
        return True, f"Reservation {reservation_id} confirmed."

    def cancel_reservation(self, reservation_id: str) -> Tuple[bool, str]:
        """
        Cancel an existing reservation.
        
        Args:
            reservation_id (str): ID of the reservation to cancel.
            
        Returns:
            Tuple[bool, str]: (success, message)
        """
        if reservation_id not in self.reservations:
            return False, "Reservation not found."

        if self.reservations[reservation_id]["status"] == "cancelled":
            return False, "Reservation already cancelled."

        self.reservations[reservation_id]["status"] = "cancelled"
        self._save_data()
        return True, f"Reservation {reservation_id} cancelled."

    def place_order(
        self,
        reservation_id: str,
        items: List[Dict[str, int]]
    ) -> Tuple[bool, str]:
        """
        Place an order for a reservation.
        
        Args:
            reservation_id (str): ID of the reservation.
            items (List[Dict[str, int]]): List of items with 'name' and 'quantity'.
            
        Returns:
            Tuple[bool, str]: (success, message)
        """
        if reservation_id not in self.reservations:
            return False, "Reservation not found."

        if self.reservations[reservation_id]["status"] == "cancelled":
            return False, "Cannot place order for cancelled reservation."

        order_id = f"ORD-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        order_items = []
        total_price = 0.0

        for item in items:
            name = item.get("name")
            quantity = item.get("quantity", 1)

            if name in self.menu["wines"]:
                wine = self.menu["wines"][name]
                if wine["stock"] < quantity:
                    return False, f"Insufficient stock for {name}."
                wine["stock"] -= quantity
                price = wine["price"] * quantity
            elif name in self.menu["food"]:
                price = self.menu["food"][name]["price"] * quantity
            else:
                return False, f"Item {name} not found in menu."

            order_items.append({"name": name, "quantity": quantity, "price": price})
            total_price += price

        self.orders[order_id] = {
            "reservation_id": reservation_id,
            "items": order_items,
            "total_price": total_price,
            "status": "pending"
        }
        self._save_data()
        return True, f"Order {order_id} placed. Total: ${total_price:.2f}"

    def get_reservation(self, reservation_id: str) -> Optional[Dict]:
        """
        Get reservation details by ID.
        
        Args:
            reservation_id (str): ID of the reservation.
            
        Returns:
            Optional[Dict]: Reservation details or None if not found.
        """
        return self.reservations.get(reservation_id)

    def get_order(self, order_id: str) -> Optional[Dict]:
        """
        Get order details by ID.
        
        Args:
            order_id (str): ID of the order.
            
        Returns:
            Optional[Dict]: Order details or None if not found.
        """
        return self.orders.get(order_id)

    def update_order_status(self, order_id: str, status: str) -> Tuple[bool, str]:
        """
        Update the status of an order.
        
        Args:
            order_id (str): ID of the order.
            status (str): New status (e.g., 'completed', 'cancelled').
            
        Returns:
            Tuple[bool, str]: (success, message)
        """
        if order_id not in self.orders:
            return False, "Order not found."

        self.orders[order_id]["status"] = status
        self._save_data()
        return True, f"Order {order_id} status updated to {status}."

    def get_menu(self) -> Dict[str, Dict]:
        """
        Get the current menu with prices and stock (for wines).
        
        Returns:
            Dict[str, Dict]: Menu items categorized by 'wines' and 'food'.
        """
        return self.menu


# Example usage
if __name__ == "__main__":
    system = WineReservationSystem()

    # Make a reservation
    success, message = system.make_reservation(
        "John Doe",
        "2023-12-25 20:00",
        4,
        "john@example.com"
    )
    print(message)

    if success:
        reservation_id = message.split()[1]  # Extract reservation ID from message

        # Place an order
        success, message = system.place_order(
            reservation_id,
            [
                {"name": "Malbec", "quantity": 2},
                {"name": "Asado", "quantity": 1}
            ]
        )
        print(message)

        # Get reservation details
        reservation = system.get_reservation(reservation_id)
        print(f"Reservation details: {reservation}")

        # Get menu
        menu = system.get_menu()
        print("Menu:")
        print(json.dumps(menu, indent=2))
```
