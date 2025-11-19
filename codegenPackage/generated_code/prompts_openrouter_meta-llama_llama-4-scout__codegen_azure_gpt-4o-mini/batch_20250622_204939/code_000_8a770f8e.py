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
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []
        self.total_cost = 0.0

    def add_item(self, name, price, quantity=1):
        """
        Add an item to the shopping cart.

        :param name: str - The name of the item.
        :param price: float - The price of a single item.
        :param quantity: int - The quantity of the item to add (default is 1).
        """
        if price < 0 or quantity < 1:
            raise ValueError("Price must be non-negative and quantity must be at least 1.")
        
        self.items.append({'name': name, 'price': price, 'quantity': quantity})
        self.total_cost += price * quantity

    def apply_discount(self, discount_percentage):
        """
        Apply a discount to the total cost.

        :param discount_percentage: float - The discount percentage to apply.
        :return: float - The total cost after discount.
        """
        if discount_percentage < 0 or discount_percentage > 100:
            raise ValueError("Discount percentage must be between 0 and 100.")
        
        discount_amount = (self.total_cost * discount_percentage) / 100
        self.total_cost -= discount_amount
        return self.total_cost

    def get_total_cost(self):
        """Return the total cost of the shopping cart."""
        return self.total_cost

    def __str__(self):
        """Return a string representation of the shopping cart items."""
        return '\n'.join([f"{item['quantity']} x {item['name']} at ${item['price']:.2f}" for item in self.items])


def main():
    """Main function to calculate the total cost of the shopping cart."""
    cart = ShoppingCart()

    # Define item details
    items = [
        {"name": "CADEIRA GAMER XZONE CGR-01-GR", "price": 499.99, "quantity": 1},
        {"name": "Memória para Notebook NTC NTCKF2666ND4-8GB", "price": 129.99, "quantity": 1}
    ]

    # Add items to the cart
    for item in items:
        cart.add_item(item['name'], item['price'], item['quantity'])

    # Apply a 7% discount
    discount_percentage = 7
    total_cost_after_discount = cart.apply_discount(discount_percentage)

    # Output the results
    print("Shopping Cart Items:")
    print(cart)
    print(f"\nTotal cost after {discount_percentage}% discount: ${total_cost_after_discount:.2f}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
