"""
Generated Code Metadata:
========================
Original URL: https://my-store-f9e36a.creator-spring.com
Prompt: What are the different types of EthXY apparel available, and how do I purchase a specific item like the EthXY Comfort Colors 1717 T-Shirt?
Generated: DETERMINISTIC_aad1acf4e8b26e6e
Batch ID: 20250622_204837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import json

# Define a class to represent EthXY apparel
class EthXYApparel:
    def __init__(self):
        # Initialize the available apparel items
        self.items = {
            "EthXY Comfort Colors 1717 T-Shirt": {
                "price": 25.99,
                "sizes": ["S", "M", "L", "XL"],
                "colors": ["Black", "White", "Blue", "Green"],
                "stock": 50
            },
            "EthXY Hoodie": {
                "price": 45.99,
                "sizes": ["M", "L", "XL"],
                "colors": ["Gray", "Black"],
                "stock": 30
            },
            "EthXY Cap": {
                "price": 19.99,
                "sizes": ["One Size"],
                "colors": ["Black", "White"],
                "stock": 100
            }
        }

    def list_items(self):
        """
        List all available EthXY apparel items.
        """
        return json.dumps(self.items, indent=4)

    def purchase_item(self, item_name, size, color, quantity):
        """
        Purchase a specific EthXY apparel item.
        
        Args:
            item_name (str): Name of the item to purchase.
            size (str): Desired size of the item.
            color (str): Desired color of the item.
            quantity (int): Quantity to purchase.
        
        Returns:
            str: Confirmation message or error message.
        """
        # Check if the item exists
        if item_name not in self.items:
            return f"Error: '{item_name}' is not available."

        item = self.items[item_name]

        # Validate size
        if size not in item["sizes"]:
            return f"Error: Size '{size}' is not available for '{item_name}'."

        # Validate color
        if color not in item["colors"]:
            return f"Error: Color '{color}' is not available for '{item_name}'."

        # Validate stock
        if quantity > item["stock"]:
            return f"Error: Only {item['stock']} units of '{item_name}' are available in stock."

        # Process the purchase
        item["stock"] -= quantity
        total_price = item["price"] * quantity
        return f"Success: You have purchased {quantity} '{item_name}' in size '{size}' and color '{color}' for ${total_price:.2f}. Remaining stock: {item['stock']}."

# Main function to demonstrate functionality
def main():
    # Create an instance of EthXYApparel
    store = EthXYApparel()

    # List all available items
    print("Available EthXY Apparel:")
    print(store.list_items())

    # Attempt to purchase an item
    print("\nPurchasing an item:")
    result = store.purchase_item("EthXY Comfort Colors 1717 T-Shirt", "M", "Blue", 2)
    print(result)

    # Attempt to purchase an item with invalid size
    print("\nPurchasing an item with invalid size:")
    result = store.purchase_item("EthXY Comfort Colors 1717 T-Shirt", "XXL", "Blue", 1)
    print(result)

    # Attempt to purchase an item with insufficient stock
    print("\nPurchasing an item with insufficient stock:")
    result = store.purchase_item("EthXY Comfort Colors 1717 T-Shirt", "M", "Blue", 100)
    print(result)

# Run the main function
if __name__ == "__main__":
    main()
```
