"""
Generated Code Metadata:
========================
Original URL: https://olgadorks.com
Prompt: Write a Python function that calculates shipping costs based on the services offered by Olgadorks, including import/export and warehousing operations.
Generated: DETERMINISTIC_81868e48c71919a9
Batch ID: 20250612_162051
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
    A class to calculate shipping costs based on various services offered by Olgadorks.
    """

    def __init__(self, base_rate: float):
        """
        Initializes the ShippingCostCalculator with a base rate.

        :param base_rate: The base rate for shipping costs.
        """
        if base_rate < 0:
            raise ValueError("Base rate must be a non-negative value.")
        self.base_rate = base_rate

    def calculate_import_cost(self, weight: float, distance: float) -> float:
        """
        Calculates the import shipping cost based on weight and distance.

        :param weight: The weight of the shipment in kilograms.
        :param distance: The distance to the destination in kilometers.
        :return: The calculated import shipping cost.
        """
        if weight <= 0 or distance <= 0:
            raise ValueError("Weight and distance must be positive values.")
        
        import_cost = self.base_rate + (weight * 0.5) + (distance * 0.2)
        return round(import_cost, 2)

    def calculate_export_cost(self, weight: float, distance: float) -> float:
        """
        Calculates the export shipping cost based on weight and distance.

        :param weight: The weight of the shipment in kilograms.
        :param distance: The distance to the destination in kilometers.
        :return: The calculated export shipping cost.
        """
        if weight <= 0 or distance <= 0:
            raise ValueError("Weight and distance must be positive values.")
        
        export_cost = self.base_rate + (weight * 0.6) + (distance * 0.25)
        return round(export_cost, 2)

    def calculate_warehousing_cost(self, days: int, weight: float) -> float:
        """
        Calculates the warehousing cost based on the number of days and weight.

        :param days: The number of days the goods are stored.
        :param weight: The weight of the goods in kilograms.
        :return: The calculated warehousing cost.
        """
        if days < 0 or weight <= 0:
            raise ValueError("Days must be non-negative and weight must be positive.")
        
        warehousing_cost = days * (weight * 0.1)
        return round(warehousing_cost, 2)

# Example usage:
if __name__ == "__main__":
    try:
        calculator = ShippingCostCalculator(base_rate=50.0)
        import_cost = calculator.calculate_import_cost(weight=100, distance=200)
        export_cost = calculator.calculate_export_cost(weight=100, distance=200)
        warehousing_cost = calculator.calculate_warehousing_cost(days=10, weight=100)

        print(f"Import Cost: ${import_cost}")
        print(f"Export Cost: ${export_cost}")
        print(f"Warehousing Cost: ${warehousing_cost}")
    except ValueError as e:
        print(f"Error: {e}")
```
