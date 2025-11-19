"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gigantic-afternoon-sparse.on-fleek.app
Prompt: Generate a code snippet for an online store that allows users to purchase comic volumes, specifically for the "Top G #3.1 Parallel Protocols" comic.
Generated: DETERMINISTIC_79639ac7dfcca5b0
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class ComicStore:
    """
    A class to simulate an online store where users can purchase comic volumes.
    """
    def __init__(self):
        # Initialize inventory with comic details and stock
        self.inventory = {
            "Top G #3.1 Parallel Protocols": {
                "price": 14.99,
                "stock": 10
            }
        }

    def display_comic_details(self, comic_name):
        """
        Display comic details including price and stock.
        """
        if comic_name in self.inventory:
            comic = self.inventory[comic_name]
            print(f"Comic Name: {comic_name}")
            print(f"Price: ${comic['price']}")
            print(f"Stock: {comic['stock']} units")
        else:
            print(f"Error: Comic '{comic_name}' not found in inventory.")

    def purchase_comic(self, comic_name, quantity):
        """
        Allow users to purchase a comic volume.
        """
        if comic_name not in self.inventory:
            print(f"Error: Comic '{comic_name}' not found in inventory.")
            return
        
        comic = self.inventory[comic_name]
        
        # Check if requested quantity is available
        if comic['stock'] < quantity:
            print(f"Error: Only {comic['stock']} units of '{comic_name}' are available.")
            return

        # Calculate total cost
        total_cost = comic['price'] * quantity

        # Reduce stock
        comic['stock'] -= quantity

        print(f"Successfully purchased {quantity} unit(s) of '{comic_name}'.")
        print(f"Total Cost: ${total_cost:.2f}")
        print(f"Remaining Stock: {comic['stock']} unit(s)")

    def add_stock(self, comic_name, quantity):
        """
        Add stock for a comic volume.
        """
        if comic_name not in self.inventory:
            print(f"Error: Comic '{comic_name}' not found in inventory.")
            return

        if quantity <= 0:
            print("Error: Quantity to add must be greater than zero.")
            return
        
        self.inventory[comic_name]['stock'] += quantity
        print(f"Successfully added {quantity} unit(s) of '{comic_name}'.")
        print(f"New Stock: {self.inventory[comic_name]['stock']} unit(s)")

# Entry point
def main():
    store = ComicStore()
    comic_name = "Top G #3.1 Parallel Protocols"

    print("Welcome to the Comic Store!")
    
    # Display comic details
    store.display_comic_details(comic_name)
    
    # Simulate a purchase
    try:
        quantity_to_purchase = int(input("Enter the quantity to purchase: "))
        store.purchase_comic(comic_name, quantity_to_purchase)
    except ValueError:
        print("Error: Invalid quantity entered. Please enter a valid number.")
        sys.exit(1)
    
    # Optionally add stock
    try:
        add_stock_quantity = int(input("Enter quantity to add to stock (or 0 to skip): "))
        if add_stock_quantity > 0:
            store.add_stock(comic_name, add_stock_quantity)
    except ValueError:
        print("Error: Invalid quantity entered. Please enter a valid number.")
        sys.exit(1)

    print("Thank you for visiting the Comic Store!")

if __name__ == "__main__":
    main()
```
