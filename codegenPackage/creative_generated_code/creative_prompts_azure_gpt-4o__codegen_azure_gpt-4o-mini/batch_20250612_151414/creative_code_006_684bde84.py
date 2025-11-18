"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Generate code to implement a shopping cart system for an online sports store, allowing users to add items like "Bolas de Futebol Americano" and "Roda de Exercício."
Generated: DETERMINISTIC_684bde8415a3d90f
Batch ID: 20250612_151414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Product:
    """
    Represents a product in the store.

    Attributes:
        id (int): Unique identifier for the product.
        name (str): The name of the product.
        price (float): Price of the product.
    """

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class ShoppingCart:
    """
    Represents a shopping cart for an online store.

    Attributes:
        items (dict): A dictionary that holds products and their quantities.
    """

    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity=1):
        """
        Adds a product to the cart.

        Args:
            product (Product): The product to add.
            quantity (int): The number of items to add (default is 1).

        Raises:
            ValueError: If the quantity is less than 1.
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        
        if product.id in self.items:
            self.items[product.id]['quantity'] += quantity
        else:
            self.items[product.id] = {'product': product, 'quantity': quantity}

    def remove_item(self, product_id):
        """
        Removes a product from the cart.

        Args:
            product_id (int): The ID of the product to remove.

        Raises:
            KeyError: If the product is not in the cart.
        """
        if product_id not in self.items:
            raise KeyError("Product not found in the cart.")
        
        del self.items[product_id]

    def view_cart(self):
        """
        Returns a list of items in the cart along with their quantities and total price.

        Returns:
            List[dict]: A list of dictionaries containing product details and total price.
        """
        total_price = 0
        cart_contents = []
        
        for item in self.items.values():
            product = item['product']
            quantity = item['quantity']
            total_price += product.price * quantity
            cart_contents.append({
                'name': product.name,
                'quantity': quantity,
                'price': product.price,
                'total': product.price * quantity
            })

        return cart_contents, total_price


# Example of usage
if __name__ == "__main__":
    # Create products
    bola_futebol = Product(1, "Bolas de Futebol Americano", 29.99)
    roda_exercicio = Product(2, "Roda de Exercício", 19.99)

    # Create a shopping cart
    cart = ShoppingCart()

    try:
        # Add products to the cart
        cart.add_item(bola_futebol, 2)
        cart.add_item(roda_exercicio)

        # View the cart
        items, total = cart.view_cart()
        print("Items in Cart:")
        for item in items:
            print(f"- {item['name']} (x{item['quantity']}): ${item['total']:.2f}")
        print(f"Total Price: ${total:.2f}")

    except (ValueError, KeyError) as e:
        print(f"An error occurred: {e}")
```
