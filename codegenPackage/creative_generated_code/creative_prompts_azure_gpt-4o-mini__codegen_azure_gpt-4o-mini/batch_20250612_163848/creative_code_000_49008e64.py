"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meta-mask-co-wallet.blogspot.com
Prompt: Generate a code snippet for a restaurant management system that includes features for tracking local ingredient suppliers, similar to the practices of A Pizza da Mooca.
Generated: DETERMINISTIC_49008e643a4c9fea
Batch ID: 20250612_163848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# restaurant_management.py

class Supplier:
    """
    Represents a local ingredient supplier.
    
    Attributes:
        name (str): Name of the supplier.
        contact_info (str): Contact information for the supplier.
        ingredients (list): List of ingredients supplied by the supplier.
    """
    
    def __init__(self, name, contact_info, ingredients):
        self.name = name
        self.contact_info = contact_info
        self.ingredients = ingredients
    
    def __str__(self):
        return f"Supplier: {self.name}, Contact: {self.contact_info}, Ingredients: {', '.join(self.ingredients)}"


class Ingredient:
    """
    Represents an ingredient used in the restaurant.
    
    Attributes:
        name (str): Name of the ingredient.
        quantity (int): Quantity available in stock.
        supplier (Supplier): Supplier of the ingredient.
    """
    
    def __init__(self, name, quantity, supplier):
        self.name = name
        self.quantity = quantity
        self.supplier = supplier
    
    def update_quantity(self, amount):
        """Update the ingredient quantity by the specified amount."""
        if self.quantity + amount < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity += amount


class Restaurant:
    """
    Represents the restaurant management system.
    
    Attributes:
        suppliers (list): List of ingredient suppliers.
        ingredients (list): List of ingredients used in the kitchen.
    """
    
    def __init__(self):
        self.suppliers = []
        self.ingredients = []
    
    def add_supplier(self, supplier):
        """Add a new supplier to the suppliers list."""
        if not isinstance(supplier, Supplier):
            raise TypeError("Expected a Supplier instance")
        self.suppliers.append(supplier)
    
    def add_ingredient(self, ingredient):
        """Add a new ingredient to the ingredients list."""
        if not isinstance(ingredient, Ingredient):
            raise TypeError("Expected an Ingredient instance")
        self.ingredients.append(ingredient)

    def find_supplier_by_name(self, name):
        """Find a supplier by name."""
        for supplier in self.suppliers:
            if supplier.name.lower() == name.lower():
                return supplier
        raise ValueError(f"Supplier with name '{name}' not found.")

    def report_inventory(self):
        """Generate a report of current inventory."""
        report = "Current Inventory:\n"
        for ingredient in self.ingredients:
            report += f"{ingredient.name}: {ingredient.quantity} (Supplier: {ingredient.supplier.name})\n"
        return report


# Example usage
if __name__ == "__main__":
    try:
        # Create suppliers
        supplier1 = Supplier("Local Farm Co.", "contact@localfarmco.com", ["Tomato", "Basil"])
        supplier2 = Supplier("Fresh Greens Ltd.", "info@freshgreens.com", ["Lettuce", "Spinach"])

        # Create ingredients 
        ingredient1 = Ingredient("Tomato", 100, supplier1)
        ingredient2 = Ingredient("Basil", 50, supplier1)
        ingredient3 = Ingredient("Lettuce", 200, supplier2)

        # Create restaurant management system
        restaurant = Restaurant()
        
        # Add suppliers and ingredients
        restaurant.add_supplier(supplier1)
        restaurant.add_supplier(supplier2)
        restaurant.add_ingredient(ingredient1)
        restaurant.add_ingredient(ingredient2)
        restaurant.add_ingredient(ingredient3)
        
        # Report inventory
        print(restaurant.report_inventory())
        
    except Exception as e:
        print(f"Error: {e}")
```
