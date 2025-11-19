"""
Generated Code Metadata:
========================
Original URL: https://dotcomachinery.co.tz
Prompt: Generate a script to filter and display "Deals of the Day" for products like concrete mixers and lawnmowers, inspired by Dotcom Machinery's promotional features.
Generated: DETERMINISTIC_c3465978fd1810f4
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# deals_of_the_day.py

class Product:
    """Represents a product with its name, price, and discount."""

    def __init__(self, name, price, discount=0):
        """
        Initializes a Product instance.

        Args:
            name (str): The product name.
            price (float): The product price.
            discount (float, optional): The product discount. Defaults to 0.
        """
        self.name = name
        self.price = price
        self.discount = discount

    def get_discounted_price(self):
        """Calculates the discounted price."""
        return self.price * (1 - self.discount / 100)


class DealsOfTheDay:
    """Manages and displays 'Deals of the Day' for various products."""

    def __init__(self):
        """Initializes an empty list of deals."""
        self.deals = []

    def add_deal(self, product):
        """
        Adds a product deal.

        Args:
            product (Product): The product to add.
        """
        self.deals.append(product)

    def filter_deals(self, product_types):
        """
        Filters deals by product type.

        Args:
            product_types (list[str]): The product types to filter by.

        Returns:
            list[Product]: The filtered deals.
        """
        return [deal for deal in self.deals if deal.name.lower() in [pt.lower() for pt in product_types]]

    def display_deals(self, deals):
        """
        Displays the deals.

        Args:
            deals (list[Product]): The deals to display.
        """
        if not deals:
            print("No deals available.")
            return

        print("Deals of the Day:")
        for i, deal in enumerate(deals, start=1):
            discounted_price = deal.get_discounted_price()
            print(f"{i}. {deal.name} - Original Price: ${deal.price:.2f}, Discounted Price: ${discounted_price:.2f} ({deal.discount}% off)")


def main():
    try:
        # Create deals of the day instance
        deals_of_the_day = DealsOfTheDay()

        # Create products
        concrete_mixer = Product("Concrete Mixer", 500, 10)
        lawnmower = Product("Lawnmower", 200, 15)
        generator = Product("Generator", 800, 5)

        # Add deals
        deals_of_the_day.add_deal(concrete_mixer)
        deals_of_the_day.add_deal(lawnmower)
        deals_of_the_day.add_deal(generator)

        # Filter and display deals
        product_types = ["Concrete Mixer", "Lawnmower"]
        filtered_deals = deals_of_the_day.filter_deals(product_types)
        deals_of_the_day.display_deals(filtered_deals)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
