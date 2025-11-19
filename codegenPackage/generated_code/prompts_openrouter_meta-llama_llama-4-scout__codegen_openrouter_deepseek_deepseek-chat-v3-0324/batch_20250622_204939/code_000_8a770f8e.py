"""
Generated Code Metadata:
========================
Original URL: https://dhcpbrazz.blogspot.com
Prompt: Write a Python code to calculate the total cost of a shopping cart containing a CADEIRA GAMER XZONE CGR-01-GR and a Memória para Notebook NTC NTCKF2666ND4-8GB, considering a 7% discount à vista.
Generated: DETERMINISTIC_8a770f8eb0ccbc91
Batch ID: 20250622_204939
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ShoppingCart:
    """
    A class to represent a shopping cart with items and discounts.
    """
    
    def __init__(self):
        self.items = []
    
    def add_item(self, name, price):
        """
        Add an item to the shopping cart.
        
        Args:
            name (str): Name of the item
            price (float): Price of the item
        """
        self.items.append({"name": name, "price": price})
    
    def calculate_total(self, discount_percent=0):
        """
        Calculate the total cost with optional discount.
        
        Args:
            discount_percent (float): Discount percentage (0-100)
            
        Returns:
            float: Total cost after discount
        """
        subtotal = sum(item["price"] for item in self.items)
        discount = subtotal * (discount_percent / 100)
        total = subtotal - discount
        return round(total, 2)

def main():
    # Create shopping cart
    cart = ShoppingCart()
    
    # Add items to cart
    cart.add_item("CADEIRA GAMER XZONE CGR-01-GR", 999.90)
    cart.add_item("Memória para Notebook NTC NTCKF2666ND4-8GB", 199.90)
    
    # Calculate total with 7% discount
    total_cost = cart.calculate_total(discount_percent=7)
    
    # Print result
    print(f"Total cost with discount: R$ {total_cost:.2f}")

if __name__ == "__main__":
    main()
```
