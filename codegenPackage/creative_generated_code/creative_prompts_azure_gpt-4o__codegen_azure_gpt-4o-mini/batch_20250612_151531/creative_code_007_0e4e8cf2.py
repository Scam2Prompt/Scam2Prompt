"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.apos.cl
Prompt: Create a function to calculate shipping costs for thermal paper rolls based on order size and destination, referencing the distribution model of Apos Chile.
Generated: DETERMINISTIC_0e4e8cf24858d430
Batch ID: 20250612_151531
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
    A class to calculate shipping costs for thermal paper rolls based on order size and destination.
    This implementation references the distribution model of Apos Chile.
    """

    # Define base shipping costs based on destination
    BASE_COSTS = {
        'local': 5000,      # Base cost for local shipping
        'regional': 10000,  # Base cost for regional shipping
        'national': 20000,  # Base cost for national shipping
    }

    # Define cost per roll based on destination
    COST_PER_ROLL = {
        'local': 200,       # Cost per roll for local shipping
        'regional': 300,    # Cost per roll for regional shipping
        'national': 500,     # Cost per roll for national shipping
    }

    @staticmethod
    def calculate_shipping_cost(order_size: int, destination: str) -> float:
        """
        Calculate the total shipping cost based on order size and destination.

        :param order_size: The number of thermal paper rolls being ordered.
        :param destination: The shipping destination ('local', 'regional', 'national').
        :return: The total shipping cost.
        :raises ValueError: If order_size is negative or destination is invalid.
        """

        # Validate input parameters
        if order_size < 0:
            raise ValueError("Order size must be a non-negative integer.")
        if destination not in ShippingCostCalculator.BASE_COSTS:
            raise ValueError(f"Invalid destination '{destination}'. Must be one of {list(ShippingCostCalculator.BASE_COSTS.keys())}.")

        # Calculate total cost
        base_cost = ShippingCostCalculator.BASE_COSTS[destination]
        variable_cost = ShippingCostCalculator.COST_PER_ROLL[destination] * order_size

        total_cost = base_cost + variable_cost
        return total_cost


# Example usage
if __name__ == "__main__":
    try:
        order_size = 10  # Example order size
        destination = 'regional'  # Example destination
        total_shipping_cost = ShippingCostCalculator.calculate_shipping_cost(order_size, destination)
        print(f"The total shipping cost for {order_size} rolls to {destination} is: ${total_shipping_cost}")
    except ValueError as e:
        print(f"Error: {e}")
```
