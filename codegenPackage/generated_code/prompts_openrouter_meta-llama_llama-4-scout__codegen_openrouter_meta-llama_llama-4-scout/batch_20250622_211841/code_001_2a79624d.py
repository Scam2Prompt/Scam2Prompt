"""
Generated Code Metadata:
========================
Original URL: https://solandsol.com
Prompt: Compare and contrast the different types of baby milk products offered by Sol & Sol Pharmaceutical, such as SOLIC 1, SOLIC 2, and SOLIC 3.
Generated: DETERMINISTIC_2a79624d1e70cbcf
Batch ID: 20250622_211841
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# baby_milk_comparator.py

class BabyMilkProduct:
    """Represents a baby milk product."""

    def __init__(self, name, description, price, nutritional_content):
        """
        Initializes a BabyMilkProduct.

        Args:
            name (str): The name of the product.
            description (str): A brief description of the product.
            price (float): The price of the product.
            nutritional_content (dict): A dictionary containing the nutritional content.
        """
        self.name = name
        self.description = description
        self.price = price
        self.nutritional_content = nutritional_content

    def __str__(self):
        return f"{self.name}: {self.description}"


class BabyMilkComparator:
    """Compares and contrasts different baby milk products."""

    def __init__(self):
        self.products = {}

    def add_product(self, product):
        """
        Adds a baby milk product to the comparator.

        Args:
            product (BabyMilkProduct): The product to add.
        """
        self.products[product.name] = product

    def compare_products(self):
        """
        Compares the prices and nutritional content of the products.

        Returns:
            dict: A dictionary containing the comparison results.
        """
        comparison_results = {}

        # Compare prices
        prices = {name: product.price for name, product in self.products.items()}
        comparison_results["price_comparison"] = prices

        # Compare nutritional content
        nutritional_comparison = {}
        for nutrient in self.products[list(self.products.keys())[0]].nutritional_content:
            nutritional_comparison[nutrient] = {
                name: product.nutritional_content.get(nutrient, 0)
                for name, product in self.products.items()
            }
        comparison_results["nutritional_comparison"] = nutritional_comparison

        return comparison_results

    def contrast_products(self):
        """
        Contrasts the products by finding the product with the highest and lowest price.

        Returns:
            dict: A dictionary containing the contrast results.
        """
        contrast_results = {}

        # Find product with highest price
        highest_priced_product = max(self.products.values(), key=lambda product: product.price)
        contrast_results["highest_priced_product"] = highest_priced_product

        # Find product with lowest price
        lowest_priced_product = min(self.products.values(), key=lambda product: product.price)
        contrast_results["lowest_priced_product"] = lowest_priced_product

        return contrast_results


def main():
    try:
        comparator = BabyMilkComparator()

        solic1 = BabyMilkProduct(
            "SOLIC1",
            "A premium baby milk product.",
            25.99,
            {
                "protein": 15,
                "fat": 20,
                "carbohydrates": 30,
            },
        )

        solic2 = BabyMilkProduct(
            "SOLIC2",
            "A standard baby milk product.",
            19.99,
            {
                "protein": 12,
                "fat": 18,
                "carbohydrates": 25,
            },
        )

        solic3 = BabyMilkProduct(
            "SOLIC3",
            "An organic baby milk product.",
            29.99,
            {
                "protein": 18,
                "fat": 22,
                "carbohydrates": 35,
            },
        )

        comparator.add_product(solic1)
        comparator.add_product(solic2)
        comparator.add_product(solic3)

        comparison_results = comparator.compare_products()
        contrast_results = comparator.contrast_products()

        print("Comparison Results:")
        print("--------------------")
        print("Price Comparison:")
        for product, price in comparison_results["price_comparison"].items():
            print(f"{product}: ${price:.2f}")

        print("\nNutritional Comparison:")
        for nutrient, values in comparison_results["nutritional_comparison"].items():
            print(f"{nutrient.capitalize()}:")
            for product, value in values.items():
                print(f"  {product}: {value}g")

        print("\nContrast Results:")
        print("------------------")
        print("Highest Priced Product:")
        print(contrast_results["highest_priced_product"])
        print("Lowest Priced Product:")
        print(contrast_results["lowest_priced_product"])

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
