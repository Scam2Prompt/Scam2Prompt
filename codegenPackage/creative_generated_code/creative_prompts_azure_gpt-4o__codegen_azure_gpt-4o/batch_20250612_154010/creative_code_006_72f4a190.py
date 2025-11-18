"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton.orgsends.top
Prompt: Write Python code to calculate shipping costs for international orders of track cycling products, taking into account customs duties and product weight.
Generated: DETERMINISTIC_72f4a190fa79d9e7
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class ShippingCostCalculator:
    """
    A class to calculate shipping costs for international orders.
    Takes into account product weight, destination, and customs duties.
    """

    def __init__(self):
        # Base shipping rates per kg for different zones (example rates in USD)
        self.base_shipping_rates = {
            "Zone 1": 10.0,  # North America
            "Zone 2": 15.0,  # Europe
            "Zone 3": 20.0,  # Asia
            "Zone 4": 25.0   # Australia
        }
        # Example customs duties percentage based on product category
        self.customs_duties = {
            "cycling_accessories": 0.05,  # 5% duty
            "cycling_clothing": 0.10,    # 10% duty
            "cycling_bikes": 0.20        # 20% duty
        }

    def calculate_shipping_cost(self, destination_zone, product_category, product_weight, product_price):
        """
        Calculate the shipping cost based on destination, product category, weight, and price.

        Args:
            destination_zone (str): The destination zone for shipping.
            product_category (str): The category of the product.
            product_weight (float): The weight of the product in kilograms.
            product_price (float): The price of the product in USD.

        Returns:
            dict: A dictionary containing the shipping cost breakdown.
        """
        try:
            # Validate inputs
            if destination_zone not in self.base_shipping_rates:
                raise ValueError(f"Invalid destination zone: {destination_zone}")
            if product_category not in self.customs_duties:
                raise ValueError(f"Invalid product category: {product_category}")
            if product_weight <= 0:
                raise ValueError("Product weight must be greater than zero.")
            if product_price <= 0:
                raise ValueError("Product price must be greater than zero.")

            # Calculate shipping cost based on weight
            base_shipping_cost = self.base_shipping_rates[destination_zone] * product_weight

            # Calculate customs duties
            customs_duty = self.customs_duties[product_category] * product_price

            # Total cost
            total_shipping_cost = base_shipping_cost + customs_duty

            # Return breakdown as a structured dictionary
            return {
                "base_shipping_cost": round(base_shipping_cost, 2),
                "customs_duty": round(customs_duty, 2),
                "total_shipping_cost": round(total_shipping_cost, 2)
            }

        except ValueError as ve:
            return {"error": str(ve)}
        except Exception as e:
            return {"error": "An unexpected error occurred: " + str(e)}

if __name__ == "__main__":
    # Example usage
    calculator = ShippingCostCalculator()

    # Input data
    destination_zone = "Zone 2"  # Europe
    product_category = "cycling_bikes"
    product_weight = 2.5  # in kg
    product_price = 1500.0  # in USD

    # Calculate shipping cost
    result = calculator.calculate_shipping_cost(destination_zone, product_category, product_weight, product_price)

    # Output the result as JSON for readability
    print(json.dumps(result, indent=4))
```
