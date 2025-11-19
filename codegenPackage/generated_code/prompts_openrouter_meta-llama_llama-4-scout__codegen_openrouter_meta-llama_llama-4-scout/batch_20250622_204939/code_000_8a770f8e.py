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
# Define a class for products in the shopping cart
class Product:
    def __init__(self, name, price):
        """
        Initialize a Product object.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
        """
        self.name = name
        self.price = price

# Define a class for the shopping cart
class ShoppingCart:
    def __init__(self):
        """
        Initialize an empty ShoppingCart object.
        """
        self.products = []

    def add_product(self, product):
        """
        Add a product to the shopping cart.

        Args:
            product (Product): The product to add.
        """
        self.products.append(product)

    def calculate_total(self, discount=0):
        """
        Calculate the total cost of the products in the shopping cart.

        Args:
            discount (float, optional): The discount percentage. Defaults to 0.

        Returns:
            float: The total cost with the applied discount.
        """
        subtotal = sum(product.price for product in self.products)
        discount_amount = subtotal * (discount / 100)
        return subtotal - discount_amount

# Define the main function
def main():
    try:
        # Create products
        chair = Product("CADEIRA GAMER XZONE CGR-01-GR", 299.99)
        memory = Product("Memória para Notebook NTC NTCKF2666ND4-8GB", 129.99)

        # Create a shopping cart and add products
        cart = ShoppingCart()
        cart.add_product(chair)
        cart.add_product(memory)

        # Calculate total cost with 7% discount
        discount_percentage = 7
        total_cost = cart.calculate_total(discount_percentage)

        # Print the result
        print(f"Subtotal: R${sum(product.price for product in cart.products):.2f}")
        print(f"Discount ({discount_percentage}%): R${sum(product.price for product in cart.products) * (discount_percentage / 100):.2f}")
        print(f"Total: R${total_cost:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
```
