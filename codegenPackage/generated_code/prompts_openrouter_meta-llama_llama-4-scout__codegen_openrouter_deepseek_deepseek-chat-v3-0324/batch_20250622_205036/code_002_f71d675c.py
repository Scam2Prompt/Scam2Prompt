"""
Generated Code Metadata:
========================
Original URL: https://poocoinswasopnet.blogspot.com
Prompt: Generate a Python code snippet to manage inventory for a shoe store with different types of shoes, including chuteira infantil and sapato social.
Generated: DETERMINISTIC_f71d675c2c1cb9fb
Batch ID: 20250622_205036
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Shoe:
    """Base class representing a shoe in inventory."""
    
    def __init__(self, name, size, color, price, quantity):
        """
        Initialize a shoe instance.
        
        Args:
            name (str): Name of the shoe
            size (float): Size of the shoe
            color (str): Color of the shoe
            price (float): Price of the shoe
            quantity (int): Quantity in stock
        """
        self.name = name
        self.size = size
        self.color = color
        self.price = price
        self.quantity = quantity
    
    def __str__(self):
        """Return string representation of the shoe."""
        return f"{self.name} - Size: {self.size}, Color: {self.color}, Price: ${self.price:.2f}, Quantity: {self.quantity}"
    
    def update_quantity(self, amount):
        """
        Update the quantity of shoes in stock.
        
        Args:
            amount (int): Amount to add (positive) or remove (negative)
            
        Raises:
            ValueError: If resulting quantity would be negative
        """
        new_quantity = self.quantity + amount
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = new_quantity


class ChuteiraInfantil(Shoe):
    """Class representing children's soccer shoes."""
    
    def __init__(self, name, size, color, price, quantity, stud_type):
        """
        Initialize a chuteira infantil instance.
        
        Args:
            stud_type (str): Type of studs (e.g., 'molded', 'removable')
        """
        super().__init__(name, size, color, price, quantity)
        self.stud_type = stud_type
    
    def __str__(self):
        """Return string representation with stud type."""
        base_str = super().__str__()
        return f"{base_str}, Stud Type: {self.stud_type}"


class SapatoSocial(Shoe):
    """Class representing formal dress shoes."""
    
    def __init__(self, name, size, color, price, quantity, material):
        """
        Initialize a sapato social instance.
        
        Args:
            material (str): Material of the shoe (e.g., 'leather', 'synthetic')
        """
        super().__init__(name, size, color, price, quantity)
        self.material = material
    
    def __str__(self):
        """Return string representation with material."""
        base_str = super().__str__()
        return f"{base_str}, Material: {self.material}"


class InventoryManager:
    """Class to manage shoe inventory."""
    
    def __init__(self):
        """Initialize inventory manager with empty inventory."""
        self.inventory = []
    
    def add_shoe(self, shoe):
        """Add a shoe to the inventory."""
        self.inventory.append(shoe)
    
    def remove_shoe(self, shoe_name, size, color):
        """
        Remove a shoe from inventory by name, size and color.
        
        Returns:
            bool: True if shoe was found and removed, False otherwise
        """
        for i, shoe in enumerate(self.inventory):
            if (shoe.name == shoe_name and 
                shoe.size == size and 
                shoe.color == color):
                del self.inventory[i]
                return True
        return False
    
    def find_shoe(self, shoe_name, size=None, color=None):
        """
        Find shoes matching criteria.
        
        Args:
            shoe_name (str): Name of shoe to find
            size (float, optional): Specific size to match
            color (str, optional): Specific color to match
            
        Returns:
            list: List of matching shoes
        """
        results = []
        for shoe in self.inventory:
            if shoe.name == shoe_name:
                if size is not None and shoe.size != size:
                    continue
                if color is not None and shoe.color != color:
                    continue
                results.append(shoe)
        return results
    
    def update_stock(self, shoe_name, size, color, amount):
        """
        Update stock quantity for a specific shoe.
        
        Args:
            shoe_name (str): Name of shoe
            size (float): Size of shoe
            color (str): Color of shoe
            amount (int): Amount to add/remove
            
        Returns:
            bool: True if update was successful, False if shoe not found
            
        Raises:
            ValueError: If update would result in negative quantity
        """
        shoes = self.find_shoe(shoe_name, size, color)
        if not shoes:
            return False
        
        try:
            shoes[0].update_quantity(amount)
            return True
        except ValueError as e:
            raise ValueError(f"Failed to update stock: {e}")
    
    def get_inventory_value(self):
        """Calculate total value of all inventory."""
        return sum(shoe.price * shoe.quantity for shoe in self.inventory)
    
    def display_inventory(self):
        """Print all shoes in inventory."""
        if not self.inventory:
            print("Inventory is empty")
            return
        
        print("Current Inventory:")
        for shoe in self.inventory:
            print(f"- {shoe}")


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()
    
    # Add some shoes to inventory
    manager.add_shoe(ChuteiraInfantil(
        "Nike Jr", 5.5, "Blue", 49.99, 10, "molded"
    ))
    manager.add_shoe(SapatoSocial(
        "Oxford", 9.0, "Black", 89.99, 5, "leather"
    ))
    manager.add_shoe(ChuteiraInfantil(
        "Adidas Kids", 4.0, "Red", 39.99, 8, "removable"
    ))
    
    # Display inventory
    manager.display_inventory()
    
    # Update stock
    try:
        manager.update_stock("Nike Jr", 5.5, "Blue", -2)
        print("\nAfter selling 2 Nike Jr shoes:")
        manager.display_inventory()
    except ValueError as e:
        print(f"Error: {e}")
    
    # Calculate inventory value
    print(f"\nTotal inventory value: ${manager.get_inventory_value():.2f}")
```
