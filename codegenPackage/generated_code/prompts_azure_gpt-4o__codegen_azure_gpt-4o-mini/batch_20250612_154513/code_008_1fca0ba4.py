"""
Generated Code Metadata:
========================
Original URL: https://www.twigacementgroup.com
Prompt: Create a program to simulate the logistics of cement distribution in Tanzania, referencing TPCPLC's partnerships and infrastructure improvement projects.
Generated: DETERMINISTIC_1fca0ba43f88ce89
Batch ID: 20250612_154513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Tuple

class CementDistribution:
    def __init__(self, suppliers: List[str], distribution_centers: List[str]):
        """
        Initializes the CementDistribution system with suppliers and distribution centers.

        :param suppliers: List of cement suppliers.
        :param distribution_centers: List of distribution centers.
        """
        self.suppliers = suppliers
        self.distribution_centers = distribution_centers
        self.orders = []

    def create_order(self, quantity: int, destination: str) -> Dict[str, str]:
        """
        Creates a new cement order.

        :param quantity: The quantity of cement to be ordered.
        :param destination: The destination distribution center.
        :return: A dictionary containing order details.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if destination not in self.distribution_centers:
            raise ValueError("Invalid distribution center.")

        order_id = len(self.orders) + 1
        order = {
            'order_id': order_id,
            'quantity': quantity,
            'destination': destination,
            'supplier': random.choice(self.suppliers)
        }
        self.orders.append(order)
        return order

    def simulate_distribution(self) -> List[Tuple[int, str]]:
        """
        Simulates the distribution of cement orders.

        :return: A list of tuples containing order IDs and their distribution status.
        """
        distribution_status = []
        for order in self.orders:
            # Simulate a random success or failure in distribution
            success = random.choice([True, False])
            status = "Delivered" if success else "Failed"
            distribution_status.append((order['order_id'], status))
        return distribution_status

    def generate_report(self) -> None:
        """
        Generates a report of all orders and their distribution status.
        """
        print("Cement Distribution Report")
        print("---------------------------")
        for order in self.orders:
            print(f"Order ID: {order['order_id']}, Quantity: {order['quantity']}, "
                  f"Destination: {order['destination']}, Supplier: {order['supplier']}")

        distribution_status = self.simulate_distribution()
        print("\nDistribution Status:")
        for order_id, status in distribution_status:
            print(f"Order ID: {order_id}, Status: {status}")

if __name__ == "__main__":
    # Example suppliers and distribution centers
    suppliers = ["Supplier A", "Supplier B", "Supplier C"]
    distribution_centers = ["Center 1", "Center 2", "Center 3"]

    # Initialize the CementDistribution system
    cement_distribution = CementDistribution(suppliers, distribution_centers)

    # Create some orders
    try:
        cement_distribution.create_order(100, "Center 1")
        cement_distribution.create_order(200, "Center 2")
        cement_distribution.create_order(150, "Center 3")
    except ValueError as e:
        print(f"Error creating order: {e}")

    # Generate the report
    cement_distribution.generate_report()
```
