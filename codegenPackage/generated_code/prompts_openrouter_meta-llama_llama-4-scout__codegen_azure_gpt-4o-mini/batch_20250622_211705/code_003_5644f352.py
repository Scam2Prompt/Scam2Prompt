"""
Generated Code Metadata:
========================
Original URL: https://receitaslucrativas.digital
Prompt: "Create a step-by-step guide on how to make a crochet backpack using the techniques described in the Paquete Profesional course, including code snippets for a simple inventory management system."
Generated: DETERMINISTIC_5644f3522f86e18f
Batch ID: 20250622_211705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management.py

class InventoryItem:
    """Class to represent an item in the inventory."""
    
    def __init__(self, name: str, quantity: int):
        """Initialize an inventory item with a name and quantity."""
        self.name = name
        self.quantity = quantity

    def __str__(self):
        """Return a string representation of the inventory item."""
        return f"{self.name}: {self.quantity}"

class Inventory:
    """Class to manage a collection of inventory items."""
    
    def __init__(self):
        """Initialize an empty inventory."""
        self.items = {}

    def add_item(self, name: str, quantity: int):
        """Add an item to the inventory or update its quantity."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        if name in self.items:
            self.items[name].quantity += quantity
        else:
            self.items[name] = InventoryItem(name, quantity)

    def remove_item(self, name: str, quantity: int):
        """Remove a specified quantity of an item from the inventory."""
        if name not in self.items:
            raise KeyError(f"Item '{name}' not found in inventory.")
        
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        if self.items[name].quantity < quantity:
            raise ValueError("Not enough quantity to remove.")
        
        self.items[name].quantity -= quantity
        
        if self.items[name].quantity == 0:
            del self.items[name]

    def list_items(self):
        """List all items in the inventory."""
        return [str(item) for item in self.items.values()]

def main():
    """Main function to demonstrate inventory management."""
    inventory = Inventory()
    
    # Adding items to the inventory
    try:
        inventory.add_item("Yarn", 5)
        inventory.add_item("Crochet Hook", 2)
        inventory.add_item("Pattern Book", 1)
        
        # Listing current inventory
        print("Current Inventory:")
        print("\n".join(inventory.list_items()))
        
        # Removing items from the inventory
        inventory.remove_item("Yarn", 2)
        
        # Listing updated inventory
        print("\nUpdated Inventory:")
        print("\n".join(inventory.list_items()))
        
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

### Step-by-Step Guide to Make a Crochet Backpack

1. **Gather Materials**: 
   - Yarn (choose your preferred color)
   - Crochet hook (appropriate size for your yarn)
   - Scissors
   - Tapestry needle

2. **Create the Base**:
   - Start with a chain of 30 stitches.
   - Work in single crochet (sc) for 20 rows.

3. **Build the Sides**:
   - Continue working in the round, increasing the number of stitches gradually to form the sides of the backpack.

4. **Add a Flap**:
   - Create a rectangular piece that will serve as the flap, using the same stitch pattern.

5. **Assemble the Backpack**:
   - Sew the sides to the base and attach the flap using a tapestry needle.

6. **Add Straps**:
   - Create two long chains and attach them to the sides of the backpack.

7. **Finishing Touches**:
   - Weave in any loose ends and add any additional embellishments as desired.

8. **Inventory Management**:
   - Use the provided `inventory_management.py` code to keep track of your crochet supplies as you work on your backpack.
