"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://delivery-services.online
Prompt: How can I optimize my e-commerce platform for efficient delivery service management?
Generated: DETERMINISTIC_2afec390fcef2d4d
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python implementation for optimizing delivery service management in an e-commerce platform. The code includes features such as delivery zone prioritization, distance-based sorting, and error handling:

```python
import geopy.distance
import logging
from typing import List, Tuple, Dict

# Configure logging for tracking errors and important messages
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class DeliveryServiceManager:
    """
    Class for managing delivery services efficiently.
    Optimizes delivery routes and prioritizes orders based on delivery zones and distance.
    """
    
    def __init__(self, warehouse_location: Tuple[float, float]):
        """
        Initialize the DeliveryServiceManager with the warehouse location.

        Args:
            warehouse_location (Tuple[float, float]): Latitude and longitude of the warehouse.
        """
        self.warehouse_location = warehouse_location
        self.orders = []

    def add_order(self, order_id: str, customer_location: Tuple[float, float], priority_zone: bool):
        """
        Adds a new order to the system.

        Args:
            order_id (str): Unique identifier for the order.
            customer_location (Tuple[float, float]): Latitude and longitude of the customer.
            priority_zone (bool): Whether the order is in a priority delivery zone.
        """
        try:
            order = {
                'order_id': order_id,
                'customer_location': customer_location,
                'priority_zone': priority_zone,
                'distance': self._calculate_distance(customer_location)
            }
            self.orders.append(order)
            logging.info(f"Order {order_id} added successfully.")
        except Exception as e:
            logging.error(f"Error adding order {order_id}: {e}")

    def _calculate_distance(self, customer_location: Tuple[float, float]) -> float:
        """
        Calculates the distance between the warehouse and the customer's location.

        Args:
            customer_location (Tuple[float, float]): Latitude and longitude of the customer.

        Returns:
            float: Distance in kilometers.
        """
        try:
            return geopy.distance.distance(self.warehouse_location, customer_location).km
        except Exception as e:
            logging.error(f"Error calculating distance: {e}")
            return float('inf')  # Return a very large value if distance calculation fails

    def optimize_delivery_routes(self) -> List[Dict]:
        """
        Optimizes delivery routes by sorting orders based on priority zone and distance.

        Returns:
            List[Dict]: List of optimized orders.
        """
        try:
            # Sort orders: prioritize priority zones first, then sort by distance
            optimized_orders = sorted(
                self.orders,
                key=lambda order: (not order['priority_zone'], order['distance'])
            )
            logging.info("Delivery routes optimized successfully.")
            return optimized_orders
        except Exception as e:
            logging.error(f"Error optimizing delivery routes: {e}")
            return []

    def display_optimized_routes(self):
        """
        Displays the optimized delivery routes in a user-friendly manner.
        """
        try:
            optimized_orders = self.optimize_delivery_routes()
            print("Optimized Delivery Routes:")
            for order in optimized_orders:
                print(
                    f"Order ID: {order['order_id']}, "
                    f"Distance: {order['distance']:.2f} km, "
                    f"Priority Zone: {order['priority_zone']}"
                )
        except Exception as e:
            logging.error(f"Error displaying optimized routes: {e}")


# Example usage
if __name__ == "__main__":
    # Warehouse location: latitude and longitude
    warehouse_location = (37.7749, -122.4194)  # San Francisco, CA

    # Initialize the delivery service manager
    manager = DeliveryServiceManager(warehouse_location)

    # Add orders to the system
    manager.add_order("ORD001", (37.8044, -122.2711), priority_zone=True)  # Oakland, CA
    manager.add_order("ORD002", (37.6879, -122.4702), priority_zone=False)  # Daly City, CA
    manager.add_order("ORD003", (37.4419, -122.1430), priority_zone=True)  # Palo Alto, CA
    manager.add_order("ORD004", (38.5816, -121.4944), priority_zone=False)  # Sacramento, CA

    # Display optimized delivery routes
    manager.display_optimized_routes()
```

This Python script uses the `geopy` library for distance calculation, logging for error tracking, and best practices for clean, maintainable code. Make sure to install the `geopy` library before running the script (`pip install geopy`).
