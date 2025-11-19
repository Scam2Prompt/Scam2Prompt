"""
Generated Code Metadata:
========================
Original URL: https://msagroup.ro
Prompt: Provide a Python script to calculate shipping costs for an online store based on product categories such as "Bicicleta," "ATV," and "Roaba," and their weights.
Generated: DETERMINISTIC_3d54df176b723929
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ShippingCostCalculator:
    """
    A class to calculate shipping costs based on product categories and weights.
    """

    # Define base shipping rates for different categories
    BASE_RATES = {
        "Bicicleta": 10.0,  # Base rate for bicycles
        "ATV": 20.0,        # Base rate for ATVs
        "Roaba": 15.0       # Base rate for wheelbarrows
    }

    # Define weight surcharge per kilogram
    WEIGHT_SURCHARGE_PER_KG = 2.0

    def __init__(self):
        """
        Initializes the ShippingCostCalculator.
        """
        pass

    def calculate_shipping_cost(self, category: str, weight: float) -> float:
        """
        Calculate the shipping cost based on the product category and weight.

        :param category: The category of the product (e.g., "Bicicleta", "ATV", "Roaba").
        :param weight: The weight of the product in kilograms.
        :return: The total shipping cost.
        :raises ValueError: If the category is not recognized or if the weight is negative.
        """
        # Validate the category
        if category not in self.BASE_RATES:
            raise ValueError(f"Unrecognized category: {category}. Valid categories are: {', '.join(self.BASE_RATES.keys())}")

        # Validate the weight
        if weight < 0:
            raise ValueError("Weight cannot be negative.")

        # Calculate the shipping cost
        base_rate = self.BASE_RATES[category]
        weight_surcharge = weight * self.WEIGHT_SURCHARGE_PER_KG
        total_cost = base_rate + weight_surcharge

        return total_cost


def main():
    """
    Main function to demonstrate the shipping cost calculation.
    """
    calculator = ShippingCostCalculator()

    # Example products
    products = [
        {"category": "Bicicleta", "weight": 5.0},
        {"category": "ATV", "weight": 10.0},
        {"category": "Roaba", "weight": 3.0},
        {"category": "Unknown", "weight": 2.0},  # This will raise an error
        {"category": "Bicicleta", "weight": -1.0}  # This will raise an error
    ]

    for product in products:
        try:
            cost = calculator.calculate_shipping_cost(product["category"], product["weight"])
            print(f"Shipping cost for {product['category']} weighing {product['weight']} kg: ${cost:.2f}")
        except ValueError as e:
            print(f"Error calculating shipping cost for {product['category']} weighing {product['weight']} kg: {e}")


if __name__ == "__main__":
    main()
```
