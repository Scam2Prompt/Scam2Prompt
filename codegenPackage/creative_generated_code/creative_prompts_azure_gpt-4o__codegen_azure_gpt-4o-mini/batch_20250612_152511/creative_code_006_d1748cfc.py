"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://irgift.info
Prompt: Write code to implement a comparison feature for an e-commerce site, allowing users to compare digital products like "2500 جم زپتو" and "2800 جم براول استارز," as seen on "ای ار گیفت."
Generated: DETERMINISTIC_d1748cfc9d554158
Batch ID: 20250612_152511
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
    Represents a digital product in the e-commerce platform.
    """

    def __init__(self, name: str, price: float, description: str):
        """
        Initializes a new instance of the Product class.

        :param name: The name of the product.
        :param price: The price of the product.
        :param description: A brief description of the product.
        """
        self.name = name
        self.price = price
        self.description = description

    def __repr__(self):
        """Returns a string representation of the product."""
        return f"Product(name={self.name}, price={self.price}, description={self.description})"


class ProductComparison:
    """
    Manages the comparison of multiple products.
    """

    def __init__(self):
        """Initializes a new instance of the ProductComparison class."""
        self.products = []

    def add_product(self, product: Product):
        """
        Adds a product to the comparison list.

        :param product: An instance of Product to be added.
        """
        if not isinstance(product, Product):
            raise TypeError("Expected a Product instance.")
        self.products.append(product)

    def compare(self):
        """
        Compares the products in the comparison list.

        :return: A dictionary containing comparison details.
        """
        if not self.products:
            raise ValueError("No products to compare.")

        comparison_data = {
            'products': [],
            'cheapest': None,
            'most_expensive': None,
        }

        for product in self.products:
            comparison_data['products'].append({
                'name': product.name,
                'price': product.price,
                'description': product.description,
            })

            # Determine the cheapest and most expensive products
            if comparison_data['cheapest'] is None or product.price < comparison_data['cheapest'].price:
                comparison_data['cheapest'] = product
            if comparison_data['most_expensive'] is None or product.price > comparison_data['most_expensive'].price:
                comparison_data['most_expensive'] = product

        return comparison_data


def main():
    """Main function to demonstrate product comparison."""
    try:
        # Create products
        product1 = Product("2500 جم زپتو", 2500, "زپتو digital product")
        product2 = Product("2800 جم براول استارز", 2800, "براول استارز digital product")

        # Initialize comparison
        comparison = ProductComparison()
        
        # Add products to comparison
        comparison.add_product(product1)
        comparison.add_product(product2)

        # Perform comparison
        comparison_result = comparison.compare()

        # Print comparison results
        print("Comparison Results:")
        for product in comparison_result['products']:
            print(f"Name: {product['name']}, Price: {product['price']}, Description: {product['description']}")
        
        print(f"\nCheapest Product: {comparison_result['cheapest']}")
        print(f"Most Expensive Product: {comparison_result['most_expensive']}")

    except (TypeError, ValueError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
