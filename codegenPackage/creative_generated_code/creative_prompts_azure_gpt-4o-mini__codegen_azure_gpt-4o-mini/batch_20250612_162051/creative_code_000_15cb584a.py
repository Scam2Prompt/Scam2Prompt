"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bernwears.com
Prompt: Generate a code snippet for a custom sportswear order management system that includes features for material sourcing and quality control, as described by Bern Wears.
Generated: DETERMINISTIC_15cb584aee66af21
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Material:
    """
    Represents a material used in sportswear manufacturing.
    """
    def __init__(self, name: str, quality_grade: str, supplier: str):
        self.name = name
        self.quality_grade = quality_grade
        self.supplier = supplier

    def __str__(self):
        return f"{self.name} (Grade: {self.quality_grade}, Supplier: {self.supplier})"


class Order:
    """
    Represents an order for sportswear, including material sourcing and quality control.
    """
    def __init__(self, order_id: int):
        self.order_id = order_id
        self.materials = []
        self.status = 'Pending'

    def add_material(self, material: Material):
        """
        Adds a material to the order.
        :param material: Material instance to be added.
        """
        self.materials.append(material)

    def quality_control_passed(self) -> bool:
        """
        Checks if all materials in the order pass quality control.
        :return: True if all materials are of 'A' grade, False otherwise.
        """
        return all(material.quality_grade == 'A' for material in self.materials)

    def finalize_order(self):
        """
        Finalizes the order if all materials pass quality control.
        """
        if self.quality_control_passed():
            self.status = 'Completed'
            return True
        else:
            self.status = 'Quality Control Failed'
            return False


class OrderManager:
    """
    Manages the lifecycle of sportswear orders.
    """
    def __init__(self):
        self.orders = {}

    def create_order(self, order_id: int) -> Order:
        """
        Creates a new order with the given order ID.
        :param order_id: Unique identifier for the order.
        :return: Newly created Order instance.
        """
        if order_id in self.orders:
            raise ValueError(f"Order ID {order_id} already exists.")
        order = Order(order_id)
        self.orders[order_id] = order
        return order

    def get_order(self, order_id: int) -> Order:
        """
        Retrieves an existing order by its ID.
        :param order_id: Unique identifier for the order.
        :return: Order instance or raises an error if not found.
        """
        try:
            return self.orders[order_id]
        except KeyError:
            raise LookupError(f"Order ID {order_id} not found.")


# Example usage
if __name__ == "__main__":
    order_manager = OrderManager()

    # Create an order
    order = order_manager.create_order(1)

    # Add materials to the order
    order.add_material(Material("Polyester", "A", "Supplier A"))
    order.add_material(Material("Nylon", "B", "Supplier B"))  # This should fail quality control

    # Finalize the order
    if order.finalize_order():
        print(f"Order {order.order_id} completed successfully.")
    else:
        print(f"Order {order.order_id} status: {order.status}")
```
