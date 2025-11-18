"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alexashipping.com
Prompt: Write Python code to calculate shipping costs for international freight based on weight and destination, referencing Alexa Shipping's services like air and ocean freight.
Generated: DETERMINISTIC_83592f3ea3c12446
Batch ID: 20250612_153224
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
    A class to calculate shipping costs for international freight based on weight and destination.
    """

    # Define shipping rates (in USD) for different weight categories and methods
    AIR_FREIGHT_RATE_PER_KG = {
        'USA': 5.0,
        'EU': 7.0,
        'Asia': 6.5,
        'Africa': 8.0,
    }

    OCEAN_FREIGHT_RATE_PER_KG = {
        'USA': 2.0,
        'EU': 3.0,
        'Asia': 2.5,
        'Africa': 4.0,
    }

    def __init__(self):
        """
        Initialize the ShippingCostCalculator.
        """
        pass

    def calculate_air_freight_cost(self, weight, destination):
        """
        Calculate the air freight cost based on weight and destination.

        Args:
            weight (float): Weight of the package in kilograms.
            destination (str): Destination country.

        Returns:
            float: Cost of shipping via air freight.

        Raises:
            ValueError: If weight is negative or destination is unknown.
        """
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        
        if destination not in self.AIR_FREIGHT_RATE_PER_KG:
            raise ValueError(f"Unknown destination: {destination}. Please provide a valid destination.")

        cost = weight * self.AIR_FREIGHT_RATE_PER_KG[destination]
        return cost

    def calculate_ocean_freight_cost(self, weight, destination):
        """
        Calculate the ocean freight cost based on weight and destination.

        Args:
            weight (float): Weight of the package in kilograms.
            destination (str): Destination country.

        Returns:
            float: Cost of shipping via ocean freight.

        Raises:
            ValueError: If weight is negative or destination is unknown.
        """
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        
        if destination not in self.OCEAN_FREIGHT_RATE_PER_KG:
            raise ValueError(f"Unknown destination: {destination}. Please provide a valid destination.")

        cost = weight * self.OCEAN_FREIGHT_RATE_PER_KG[destination]
        return cost

    def calculate_shipping_cost(self, weight, destination, method):
        """
        Calculate the shipping cost based on weight, destination, and method.

        Args:
            weight (float): Weight of the package in kilograms.
            destination (str): Destination country.
            method (str): Shipping method ('air' or 'ocean').

        Returns:
            float: Total shipping cost.

        Raises:
            ValueError: If method is not recognized.
        """
        if method == 'air':
            return self.calculate_air_freight_cost(weight, destination)
        elif method == 'ocean':
            return self.calculate_ocean_freight_cost(weight, destination)
        else:
            raise ValueError("Invalid shipping method. Choose 'air' or 'ocean'.")

# Example usage
if __name__ == "__main__":
    calculator = ShippingCostCalculator()
    
    try:
        weight = 10.0  # Weight in kg
        destination = 'EU'
        method = 'air'
        
        cost = calculator.calculate_shipping_cost(weight, destination, method)
        print(f"The shipping cost by {method} to {destination} for {weight} kg is: ${cost:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
```
