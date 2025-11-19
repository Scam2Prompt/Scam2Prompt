"""
Generated Code Metadata:
========================
Original URL: https://roshako.com
Prompt: Develop a Python script to filter and display industrial products suitable for marine and offshore engineering, based on the industries served by Roshako.
Generated: DETERMINISTIC_50741abf09c42f77
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# industrial_product_filter.py

class IndustrialProduct:
    """Represents an industrial product."""

    def __init__(self, name, industries):
        """
        Initializes an IndustrialProduct.

        Args:
            name (str): The product name.
            industries (list[str]): The industries served by the product.
        """
        self.name = name
        self.industries = industries


class ProductFilter:
    """Filters industrial products based on industries served."""

    def __init__(self, products):
        """
        Initializes a ProductFilter.

        Args:
            products (list[IndustrialProduct]): The list of industrial products.
        """
        self.products = products

    def filter_by_industries(self, target_industries):
        """
        Filters products based on the target industries.

        Args:
            target_industries (list[str]): The target industries.

        Returns:
            list[IndustrialProduct]: The filtered products.
        """
        return [
            product
            for product in self.products
            if any(industry in product.industries for industry in target_industries)
        ]


def main():
    # Define industrial products
    products = [
        IndustrialProduct("Product A", ["Marine", "Offshore", "Oil & Gas"]),
        IndustrialProduct("Product B", ["Automotive", "Aerospace"]),
        IndustrialProduct("Product C", ["Marine", "Construction"]),
        IndustrialProduct("Product D", ["Offshore", "Renewable Energy"]),
    ]

    # Create a product filter
    filter = ProductFilter(products)

    # Define target industries
    target_industries = ["Marine", "Offshore"]

    try:
        # Filter products
        filtered_products = filter.filter_by_industries(target_industries)

        # Display filtered products
        print("Filtered Products:")
        for product in filtered_products:
            print(f"- {product.name} (Served Industries: {', '.join(product.industries)})")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
