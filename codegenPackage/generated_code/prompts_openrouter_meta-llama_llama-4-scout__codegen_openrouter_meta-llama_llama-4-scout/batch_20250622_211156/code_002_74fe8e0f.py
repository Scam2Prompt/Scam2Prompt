"""
Generated Code Metadata:
========================
Original URL: https://rhinoag.com
Prompt: "Generate code to calculate the cost savings of purchasing RhinoAg equipment with up to $1,000 off and a 10-year limited gearbox warranty."
Generated: DETERMINISTIC_74fe8e0f297ac4e7
Batch ID: 20250622_211156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# rhinoag_cost_savings_calculator.py

class RhinoAgEquipment:
    def __init__(self, price, discount=0, warranty_years=10):
        """
        Initialize RhinoAg equipment with price, discount, and warranty years.

        Args:
            price (float): The price of the equipment.
            discount (float, optional): The discount amount. Defaults to 0.
            warranty_years (int, optional): The number of years of warranty. Defaults to 10.
        """
        self.price = price
        self.discount = discount
        self.warranty_years = warranty_years

    def calculate_cost_savings(self, max_discount=1000):
        """
        Calculate the cost savings of purchasing RhinoAg equipment.

        Args:
            max_discount (float, optional): The maximum discount amount. Defaults to 1000.

        Returns:
            dict: A dictionary containing the cost savings information.
        """
        # Apply discount if it's within the max discount limit
        applied_discount = min(self.discount, max_discount)

        # Calculate cost savings
        cost_savings = applied_discount

        # Calculate the price after discount
        price_after_discount = self.price - applied_discount

        # Return cost savings information
        return {
            "original_price": self.price,
            "applied_discount": applied_discount,
            "price_after_discount": price_after_discount,
            "cost_savings": cost_savings,
            "warranty_years": self.warranty_years,
        }


def main():
    try:
        # Example usage
        equipment_price = 5000  # Original price of the equipment
        discount = 1200  # Discount amount

        rhinoag_equipment = RhinoAgEquipment(equipment_price, discount)
        cost_savings_info = rhinoag_equipment.calculate_cost_savings()

        print("Cost Savings Information:")
        print(f"Original Price: ${cost_savings_info['original_price']:.2f}")
        print(f"Applied Discount: ${cost_savings_info['applied_discount']:.2f}")
        print(f"Price after Discount: ${cost_savings_info['price_after_discount']:.2f}")
        print(f"Cost Savings: ${cost_savings_info['cost_savings']:.2f}")
        print(f"Warranty Years: {cost_savings_info['warranty_years']} years")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
