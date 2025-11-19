"""
Generated Code Metadata:
========================
Original URL: https://chedanthe.dk
Prompt: "Write a Python script to calculate the total cost of a furniture shopping cart, considering discounts and taxes, for an online store like Chedanthe."
Generated: DETERMINISTIC_9d05cf906a16f18b
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Union

class FurnitureCart:
    """
    A class to represent a shopping cart for furniture items with discount and tax calculations.
    """
    
    def __init__(self):
        self.items = []
        self.discount_rules = {
            "BULK_10": {"min_quantity": 10, "discount": 0.10},
            "BULK_20": {"min_quantity": 20, "discount": 0.20},
            "LOYALTY": {"discount": 0.05}
        }
        self.tax_rate = 0.08  # Default 8% tax rate
    
    def add_item(self, item_id: str, name: str, price: float, quantity: int = 1) -> None:
        """
        Add an item to the shopping cart.
        
        Args:
            item_id: Unique identifier for the item
            name: Name of the item
            price: Price per unit
            quantity: Quantity to add (default 1)
        """
        if price <= 0:
            raise ValueError("Price must be positive")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
            
        # Check if item already exists in cart
        for item in self.items:
            if item["item_id"] == item_id:
                item["quantity"] += quantity
                return
        
        # Add new item
        self.items.append({
            "item_id": item_id,
            "name": name,
            "price": price,
            "quantity": quantity
        })
    
    def remove_item(self, item_id: str, quantity: int = 1) -> None:
        """
        Remove an item or reduce its quantity from the cart.
        
        Args:
            item_id: ID of the item to remove
            quantity: Quantity to remove (default 1)
        """
        for index, item in enumerate(self.items):
            if item["item_id"] == item_id:
                if item["quantity"] <= quantity:
                    del self.items[index]
                else:
                    item["quantity"] -= quantity
                return
        raise ValueError("Item not found in cart")
    
    def apply_discount(self, discount_code: str) -> None:
        """
        Apply a discount to the entire cart if conditions are met.
        
        Args:
            discount_code: Discount code to apply
        """
        if discount_code not in self.discount_rules:
            raise ValueError("Invalid discount code")
        
        rule = self.discount_rules[discount_code]
        
        if discount_code in ["BULK_10", "BULK_20"]:
            total_quantity = sum(item["quantity"] for item in self.items)
            if total_quantity >= rule["min_quantity"]:
                for item in self.items:
                    item["discount"] = rule["discount"]
        elif discount_code == "LOYALTY":
            for item in self.items:
                item["discount"] = rule["discount"]
    
    def calculate_subtotal(self) -> float:
        """Calculate the subtotal before discounts and taxes."""
        return sum(item["price"] * item["quantity"] for item in self.items)
    
    def calculate_discounts(self) -> float:
        """Calculate total discounts applied to all items."""
        total_discount = 0.0
        for item in self.items:
            discount = item.get("discount", 0)
            total_discount += item["price"] * item["quantity"] * discount
        return total_discount
    
    def calculate_tax(self, subtotal: float, discount_total: float) -> float:
        """Calculate tax amount based on taxable amount."""
        taxable_amount = subtotal - discount_total
        return taxable_amount * self.tax_rate
    
    def calculate_total(self) -> Dict[str, Union[float, List[Dict]]]:
        """
        Calculate the total cost including discounts and taxes.
        
        Returns:
            A dictionary containing:
            - subtotal: Before discounts and taxes
            - discount_total: Total discounts applied
            - tax_amount: Calculated tax
            - total: Final amount to pay
            - items: List of items in cart
        """
        subtotal = self.calculate_subtotal()
        discount_total = self.calculate_discounts()
        tax_amount = self.calculate_tax(subtotal, discount_total)
        total = subtotal - discount_total + tax_amount
        
        return {
            "subtotal": subtotal,
            "discount_total": discount_total,
            "tax_amount": tax_amount,
            "total": total,
            "items": self.items.copy()
        }
    
    def clear_cart(self) -> None:
        """Clear all items from the cart."""
        self.items = []
    
    def to_json(self) -> str:
        """Serialize the cart to JSON."""
        return json.dumps({
            "items": self.items,
            "tax_rate": self.tax_rate,
            "discount_rules": self.discount_rules
        }, indent=2)
    
    @classmethod
    def from_json(cls, json_str: str) -> 'FurnitureCart':
        """Deserialize JSON to a FurnitureCart instance."""
        data = json.loads(json_str)
        cart = cls()
        cart.items = data["items"]
        cart.tax_rate = data["tax_rate"]
        cart.discount_rules = data["discount_rules"]
        return cart


# Example usage
if __name__ == "__main__":
    cart = FurnitureCart()
    
    # Add items to cart
    cart.add_item("CHAIR001", "Ergonomic Chair", 199.99, 2)
    cart.add_item("DESK002", "Executive Desk", 599.99)
    cart.add_item("LAMP003", "Desk Lamp", 49.99, 3)
    
    # Apply discount
    try:
        cart.apply_discount("BULK_10")
    except ValueError as e:
        print(f"Discount not applied: {e}")
    
    # Calculate total
    total_info = cart.calculate_total()
    print("Cart Summary:")
    print(f"Subtotal: ${total_info['subtotal']:.2f}")
    print(f"Discounts: -${total_info['discount_total']:.2f}")
    print(f"Tax ({cart.tax_rate*100:.0f}%): ${total_info['tax_amount']:.2f}")
    print(f"Total: ${total_info['total']:.2f}")
```
