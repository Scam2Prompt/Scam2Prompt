"""
Generated Code Metadata:
========================
Original URL: https://www.vircomem.ro
Prompt: "Write a Python code to manage inventory of industrial brushes with different dimensions and characteristics, similar to those offered by Vircomem."
Generated: DETERMINISTIC_f028883801104bb0
Batch ID: 20250622_205654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

class Brush:
    """Represents an industrial brush with dimensions and characteristics."""

    def __init__(self, 
                 brush_id: int, 
                 name: str, 
                 length: float, 
                 width: float, 
                 height: float, 
                 bristle_type: str, 
                 quantity: int):
        """
        Initializes a Brush object.

        Args:
            brush_id (int): Unique identifier for the brush.
            name (str): Name of the brush.
            length (float): Length of the brush in inches.
            width (float): Width of the brush in inches.
            height (float): Height of the brush in inches.
            bristle_type (str): Type of bristles used in the brush.
            quantity (int): Quantity of brushes in stock.
        """
        self.brush_id = brush_id
        self.name = name
        self.dimensions = {
            "length": length,
            "width": width,
            "height": height
        }
        self.bristle_type = bristle_type
        self.quantity = quantity

    def __str__(self):
        return f"Brush {self.brush_id}: {self.name}"


class Inventory:
    """Manages a collection of industrial brushes."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.brushes = {}

    def add_brush(self, brush: Brush):
        """
        Adds a brush to the inventory.

        Args:
            brush (Brush): Brush object to add.

        Raises:
            ValueError: If a brush with the same ID already exists.
        """
        if brush.brush_id in self.brushes:
            raise ValueError("Brush with this ID already exists")
        self.brushes[brush.brush_id] = brush

    def remove_brush(self, brush_id: int):
        """
        Removes a brush from the inventory.

        Args:
            brush_id (int): ID of the brush to remove.

        Raises:
            KeyError: If the brush ID is not found.
        """
        if brush_id not in self.brushes:
            raise KeyError("Brush ID not found")
        del self.brushes[brush_id]

    def update_quantity(self, brush_id: int, new_quantity: int):
        """
        Updates the quantity of a brush in the inventory.

        Args:
            brush_id (int): ID of the brush to update.
            new_quantity (int): New quantity of the brush.

        Raises:
            KeyError: If the brush ID is not found.
            ValueError: If the new quantity is negative.
        """
        if brush_id not in self.brushes:
            raise KeyError("Brush ID not found")
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.brushes[brush_id].quantity = new_quantity

    def get_brush(self, brush_id: int) -> Brush:
        """
        Retrieves a brush from the inventory.

        Args:
            brush_id (int): ID of the brush to retrieve.

        Returns:
            Brush: Brush object if found.

        Raises:
            KeyError: If the brush ID is not found.
        """
        if brush_id not in self.brushes:
            raise KeyError("Brush ID not found")
        return self.brushes[brush_id]

    def list_brushes(self):
        """Prints a list of all brushes in the inventory."""
        for brush in self.brushes.values():
            print(f"ID: {brush.brush_id}, Name: {brush.name}, Quantity: {brush.quantity}")


def main():
    # Create an inventory
    inventory = Inventory()

    try:
        # Create brushes
        brush1 = Brush(1, "Vircomem Industrial Brush", 10.0, 5.0, 2.0, "Nylon", 100)
        brush2 = Brush(2, "Vircomem Cleaning Brush", 8.0, 3.0, 1.5, "Polyester", 50)

        # Add brushes to inventory
        inventory.add_brush(brush1)
        inventory.add_brush(brush2)

        # List brushes
        print("Brushes in Inventory:")
        inventory.list_brushes()

        # Update quantity
        inventory.update_quantity(1, 80)

        # Get brush
        retrieved_brush = inventory.get_brush(1)
        print(f"\nRetrieved Brush: {retrieved_brush}")
        print(f"Dimensions: {retrieved_brush.dimensions}")
        print(f"Bristle Type: {retrieved_brush.bristle_type}")
        print(f"Quantity: {retrieved_brush.quantity}")

        # Remove brush
        inventory.remove_brush(2)

        # List brushes after removal
        print("\nBrushes in Inventory after removal:")
        inventory.list_brushes()

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
