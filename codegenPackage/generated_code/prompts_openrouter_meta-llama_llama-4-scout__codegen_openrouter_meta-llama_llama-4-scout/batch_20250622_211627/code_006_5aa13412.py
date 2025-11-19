"""
Generated Code Metadata:
========================
Original URL: https://mahadevent.com
Prompt: What are the key features of Mahadev Enterprise's product sourcing and packaging process, and how can they be integrated into a business application?
Generated: DETERMINISTIC_5aa13412dfb3f6dd
Batch ID: 20250622_211627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_sourcing_packaging.py

class ProductSourcing:
    """
    Represents Mahadev Enterprise's product sourcing process.
    """

    def __init__(self, product_name, supplier, cost):
        """
        Initializes a ProductSourcing instance.

        Args:
            product_name (str): Name of the product.
            supplier (str): Supplier of the product.
            cost (float): Cost of the product.
        """
        self.product_name = product_name
        self.supplier = supplier
        self.cost = cost

    def get_product_info(self):
        """
        Returns a dictionary containing product information.

        Returns:
            dict: Product information.
        """
        return {
            "product_name": self.product_name,
            "supplier": self.supplier,
            "cost": self.cost
        }


class Packaging:
    """
    Represents Mahadev Enterprise's packaging process.
    """

    def __init__(self, packaging_material, packaging_cost):
        """
        Initializes a Packaging instance.

        Args:
            packaging_material (str): Material used for packaging.
            packaging_cost (float): Cost of packaging.
        """
        self.packaging_material = packaging_material
        self.packaging_cost = packaging_cost

    def get_packaging_info(self):
        """
        Returns a dictionary containing packaging information.

        Returns:
            dict: Packaging information.
        """
        return {
            "packaging_material": self.packaging_material,
            "packaging_cost": self.packaging_cost
        }


class BusinessApplication:
    """
    Integrates product sourcing and packaging processes into a business application.
    """

    def __init__(self):
        """
        Initializes a BusinessApplication instance.
        """
        self.product_sourcing = None
        self.packaging = None

    def set_product_sourcing(self, product_sourcing):
        """
        Sets the product sourcing process.

        Args:
            product_sourcing (ProductSourcing): Product sourcing process.
        """
        self.product_sourcing = product_sourcing

    def set_packaging(self, packaging):
        """
        Sets the packaging process.

        Args:
            packaging (Packaging): Packaging process.
        """
        self.packaging = packaging

    def get_total_cost(self):
        """
        Calculates the total cost of the product, including sourcing and packaging costs.

        Returns:
            float: Total cost.

        Raises:
            ValueError: If product sourcing or packaging is not set.
        """
        if not self.product_sourcing or not self.packaging:
            raise ValueError("Product sourcing and packaging must be set")

        product_cost = self.product_sourcing.cost
        packaging_cost = self.packaging.packaging_cost
        return product_cost + packaging_cost

    def print_product_info(self):
        """
        Prints product information, including sourcing and packaging details.
        """
        if not self.product_sourcing or not self.packaging:
            raise ValueError("Product sourcing and packaging must be set")

        product_info = self.product_sourcing.get_product_info()
        packaging_info = self.packaging.get_packaging_info()

        print("Product Information:")
        print(f"Name: {product_info['product_name']}")
        print(f"Supplier: {product_info['supplier']}")
        print(f"Cost: ${product_info['cost']:.2f}")

        print("\nPackaging Information:")
        print(f"Material: {packaging_info['packaging_material']}")
        print(f"Cost: ${packaging_info['packaging_cost']:.2f}")

        print(f"\nTotal Cost: ${self.get_total_cost():.2f}")


def main():
    try:
        # Create product sourcing instance
        product_sourcing = ProductSourcing(
            product_name="Example Product",
            supplier="Example Supplier",
            cost=100.0
        )

        # Create packaging instance
        packaging = Packaging(
            packaging_material="Cardboard",
            packaging_cost=5.0
        )

        # Create business application instance
        business_app = BusinessApplication()
        business_app.set_product_sourcing(product_sourcing)
        business_app.set_packaging(packaging)

        # Print product information
        business_app.print_product_info()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
