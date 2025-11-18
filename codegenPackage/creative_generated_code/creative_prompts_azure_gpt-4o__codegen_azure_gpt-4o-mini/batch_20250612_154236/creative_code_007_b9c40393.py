"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://penguinbookspublishers.com
Prompt: Generate a Python script to calculate printing and shipping costs for print-on-demand services, ensuring transparency as described by Penguin Books Publishers.
Generated: DETERMINISTIC_b9c40393b3bd6263
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class PrintOnDemandService:
    def __init__(self, base_print_cost, shipping_rate_per_kg):
        """
        Initializes the PrintOnDemandService with base printing cost and shipping rate.

        :param base_print_cost: The base cost for printing a single unit.
        :param shipping_rate_per_kg: The cost of shipping per kilogram.
        """
        self.base_print_cost = base_print_cost
        self.shipping_rate_per_kg = shipping_rate_per_kg

    def calculate_print_cost(self, pages: int, color: bool) -> float:
        """
        Calculates the printing cost based on the number of pages and whether it's color.

        :param pages: Number of pages to print.
        :param color: Boolean flag indicating if the print is in color.
        :return: Total printing cost.
        """
        if pages <= 0:
            raise ValueError("Number of pages must be greater than zero.")

        color_multiplier = 1.5 if color else 1.0
        print_cost = self.base_print_cost * pages * color_multiplier
        return print_cost

    def calculate_shipping_cost(self, weight: float) -> float:
        """
        Calculates the shipping cost based on the weight of the package.

        :param weight: Weight of the package in kilograms.
        :return: Total shipping cost.
        """
        if weight <= 0:
            raise ValueError("Weight must be greater than zero.")
        
        shipping_cost = self.shipping_rate_per_kg * weight
        return shipping_cost

    def calculate_total_cost(self, pages: int, color: bool, weight: float) -> float:
        """
        Calculates the total cost including printing and shipping.

        :param pages: Number of pages to print.
        :param color: Boolean flag indicating if print is in color.
        :param weight: Weight of the package in kilograms for shipping.
        :return: Total cost for printing and shipping.
        """
        print_cost = self.calculate_print_cost(pages, color)
        shipping_cost = self.calculate_shipping_cost(weight)
        total_cost = print_cost + shipping_cost
        return total_cost


def main():
    """
    Main function to demonstrate the PrintOnDemandService capabilities.
    """
    # Example configuration
    BASE_PRINT_COST = 0.10  # Base cost per page
    SHIPPING_RATE_PER_KG = 5.0  # Shipping cost per kg

    # Instantiate the service
    service = PrintOnDemandService(BASE_PRINT_COST, SHIPPING_RATE_PER_KG)

    # Example inputs (these could be gathered from user input or other sources)
    pages = 100  # Number of pages
    color = True  # Whether the print is in color
    weight = 0.5  # Weight of the printed material in kg

    try:
        total_cost = service.calculate_total_cost(pages, color, weight)
        print(f"Total cost for printing and shipping: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
