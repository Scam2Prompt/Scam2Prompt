"""
Generated Code Metadata:
========================
Original URL: https://acula.com.ua
Prompt: Generate code to calculate shipping costs for an online store in Ukraine, using product categories such as "снаряжение для дайвинга," "одежда для зимней рыбалки," and "туристическое снаряжение," as outlined on acula.com.ua.
Generated: DETERMINISTIC_4c92e39fb83484a0
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shipping_calculator.py

class ProductCategory:
    """Represents a product category with its base shipping cost and weight-based cost."""

    def __init__(self, name, base_cost, weight_cost_per_kg):
        """
        Initializes a ProductCategory.

        Args:
            name (str): The name of the product category.
            base_cost (float): The base shipping cost for the category.
            weight_cost_per_kg (float): The additional shipping cost per kilogram.
        """
        self.name = name
        self.base_cost = base_cost
        self.weight_cost_per_kg = weight_cost_per_kg


class ShippingCalculator:
    """Calculates shipping costs for products in different categories."""

    def __init__(self):
        # Define product categories with their shipping costs ( fictional rates for demonstration )
        self.categories = {
            "снаряжение для дайвинга": ProductCategory("снаряжение для дайвинга", 100.0, 1.5),
            "одежда для зимней рыбалки": ProductCategory("одежда для зимней рыбалки", 80.0, 1.2),
            "туристическое снаряжение": ProductCategory("туристическое снаряжение", 120.0, 1.8),
        }

    def calculate_shipping_cost(self, category_name, product_weight):
        """
        Calculates the shipping cost for a product.

        Args:
            category_name (str): The name of the product category.
            product_weight (float): The weight of the product in kilograms.

        Returns:
            float: The total shipping cost.

        Raises:
            ValueError: If the category does not exist or the product weight is invalid.
        """
        if category_name not in self.categories:
            raise ValueError(f"Category '{category_name}' does not exist.")

        if product_weight <= 0:
            raise ValueError("Product weight must be greater than zero.")

        category = self.categories[category_name]
        shipping_cost = category.base_cost + (category.weight_cost_per_kg * product_weight)
        return shipping_cost


def main():
    calculator = ShippingCalculator()

    # Example usage
    try:
        category_name = "снаряжение для дайвинга"
        product_weight = 5.0  # kilograms
        shipping_cost = calculator.calculate_shipping_cost(category_name, product_weight)
        print(f"Shipping cost for {category_name} product weighing {product_weight} kg: {shipping_cost:.2f} UAH")

        category_name = "одежда для зимней рыбалки"
        product_weight = 2.0  # kilograms
        shipping_cost = calculator.calculate_shipping_cost(category_name, product_weight)
        print(f"Shipping cost for {category_name} product weighing {product_weight} kg: {shipping_cost:.2f} UAH")

        category_name = "туристическое снаряжение"
        product_weight = 10.0  # kilograms
        shipping_cost = calculator.calculate_shipping_cost(category_name, product_weight)
        print(f"Shipping cost for {category_name} product weighing {product_weight} kg: {shipping_cost:.2f} UAH")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
