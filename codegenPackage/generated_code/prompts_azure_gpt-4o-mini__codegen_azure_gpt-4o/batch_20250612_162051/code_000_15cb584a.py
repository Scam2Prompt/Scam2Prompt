"""
Generated Code Metadata:
========================
Original URL: https://bernwears.com
Prompt: Generate a code snippet for a custom sportswear order management system that includes features for material sourcing and quality control, as described by Bern Wears.
Generated: DETERMINISTIC_15cb584aee66af21
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime

class Order:
    """
    Represents a custom sportswear order.
    """
    def __init__(self, customer_name, product_type, size, color, quantity):
        self.order_id = str(uuid.uuid4())  # Generate a unique order ID
        self.customer_name = customer_name
        self.product_type = product_type
        self.size = size
        self.color = color
        self.quantity = quantity
        self.order_date = datetime.now()
        self.status = "Pending"  # Initial status of the order

    def update_status(self, new_status):
        """
        Updates the status of the order.
        :param new_status: str - New status for the order
        """
        self.status = new_status


class Material:
    """
    Represents material sourcing for sportswear production.
    """
    def __init__(self, material_name, supplier_name, quantity_available):
        self.material_name = material_name
        self.supplier_name = supplier_name
        self.quantity_available = quantity_available

    def update_quantity(self, quantity_used):
        """
        Updates the quantity of material available after usage.
        :param quantity_used: int - Quantity of material used
        """
        if quantity_used > self.quantity_available:
            raise ValueError("Insufficient material available.")
        self.quantity_available -= quantity_used


class QualityControl:
    """
    Represents quality control checks for sportswear production.
    """
    def __init__(self):
        self.checks = []

    def add_check(self, check_description, passed):
        """
        Adds a quality control check.
        :param check_description: str - Description of the quality control check
        :param passed: bool - Whether the check passed or failed
        """
        self.checks.append({
            "description": check_description,
            "passed": passed,
            "timestamp": datetime.now()
        })

    def all_checks_passed(self):
        """
        Determines if all quality control checks have passed.
        :return: bool - True if all checks passed, False otherwise
        """
        return all(check["passed"] for check in self.checks)


class SportswearOrderManagementSystem:
    """
    Main system for managing sportswear orders, material sourcing, and quality control.
    """
    def __init__(self):
        self.orders = []
        self.materials = []
        self.quality_control = QualityControl()

    def create_order(self, customer_name, product_type, size, color, quantity):
        """
        Creates a new order and adds it to the system.
        :param customer_name: str - Name of the customer
        :param product_type: str - Type of sportswear product
        :param size: str - Size of the product
        :param color: str - Color of the product
        :param quantity: int - Quantity of the product
        """
        order = Order(customer_name, product_type, size, color, quantity)
        self.orders.append(order)
        return order

    def add_material(self, material_name, supplier_name, quantity_available):
        """
        Adds a new material to the system.
        :param material_name: str - Name of the material
        :param supplier_name: str - Name of the supplier
        :param quantity_available: int - Quantity of material available
        """
        material = Material(material_name, supplier_name, quantity_available)
        self.materials.append(material)
        return material

    def perform_quality_check(self, check_description, passed):
        """
        Performs a quality control check and records the result.
        :param check_description: str - Description of the quality control check
        :param passed: bool - Whether the check passed or failed
        """
        self.quality_control.add_check(check_description, passed)

    def get_order_by_id(self, order_id):
        """
        Retrieves an order by its ID.
        :param order_id: str - ID of the order
        :return: Order - The order object if found, None otherwise
        """
        for order in self.orders:
            if order.order_id == order_id:
                return order
        return None

    def get_material_by_name(self, material_name):
        """
        Retrieves a material by its name.
        :param material_name: str - Name of the material
        :return: Material - The material object if found, None otherwise
        """
        for material in self.materials:
            if material.material_name == material_name:
                return material
        return None


# Example usage:
if __name__ == "__main__":
    system = SportswearOrderManagementSystem()

    # Create a new order
    order = system.create_order("John Doe", "T-Shirt", "M", "Blue", 10)
    print(f"Order created: {order.order_id}, Status: {order.status}")

    # Add material
    material = system.add_material("Cotton", "Supplier A", 100)
    print(f"Material added: {material.material_name}, Quantity: {material.quantity_available}")

    # Perform quality check
    system.perform_quality_check("Check stitching quality", True)
    system.perform_quality_check("Check color consistency", True)
    print(f"All quality checks passed: {system.quality_control.all_checks_passed()}")

    # Update material quantity
    try:
        material.update_quantity(10)
        print(f"Material updated: {material.material_name}, Remaining Quantity: {material.quantity_available}")
    except ValueError as e:
        print(f"Error: {e}")
```
