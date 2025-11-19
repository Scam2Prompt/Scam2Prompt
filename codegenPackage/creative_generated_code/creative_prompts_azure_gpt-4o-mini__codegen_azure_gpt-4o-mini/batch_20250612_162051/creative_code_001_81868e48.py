"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olgadorks.com
Prompt: Write a Python function that calculates shipping costs based on the services offered by Olgadorks, including import/export and warehousing operations.
Generated: DETERMINISTIC_81868e48c71919a9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ShippingCostCalculator:
    """
    A class to calculate shipping costs based on various services offered by Olgadorks.
    """

    def __init__(self):
        # Define base costs for different services
        self.base_costs = {
            "import": 100.0,      # Base cost for import services
            "export": 120.0,      # Base cost for export services
            "warehousing": 50.0,   # Base cost for warehousing services
        }
        # Define additional costs per item
        self.additional_item_cost = 10.0

    def calculate_cost(self, service_type, num_items):
        """
        Calculate the total shipping cost based on service type and number of items.

        Parameters:
        service_type (str): The type of shipping service ('import', 'export', or 'warehousing').
        num_items (int): The number of items to be shipped.

        Returns:
        float: Total shipping cost.

        Raises:
        ValueError: If an invalid service type is provided or if num_items is negative.
        """

        # Validate input parameters
        if service_type not in self.base_costs:
            raise ValueError(f"Invalid service type '{service_type}'. Must be 'import', 'export', or 'warehousing'.")

        if not isinstance(num_items, int) or num_items < 0:
            raise ValueError("The number of items must be a non-negative integer.")

        # Calculate total cost
        total_cost = self.base_costs[service_type] + (self.additional_item_cost * num_items)
        return total_cost


def main():
    """
    Main function to demonstrate the usage of ShippingCostCalculator.
    """
    calculator = ShippingCostCalculator()

    try:
        # Example: Calculate cost for importing 5 items
        service = 'import'
        items = 5
        cost = calculator.calculate_cost(service, items)
        print(f"The total shipping cost for {items} {service} items is: ${cost:.2f}")

    except ValueError as e:
        print(f"Error calculating shipping cost: {e}")


if __name__ == "__main__":
    main()
```
