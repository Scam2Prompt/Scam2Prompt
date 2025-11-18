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
import logging

# Set up logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ShippingCalculator:
    """
    A class to calculate international shipping costs based on weight, destination, and shipping method.

    Attributes:
        air_rates (dict): Per kg rate for air freight to different destinations.
        ocean_rates (dict): Per kg rate for ocean freight to different destinations.
    """
    def __init__(self):
        # Example rates per kg for different destinations
        self.air_rates = {
            'USA': 10.0,
            'Canada': 8.5,
            'Australia': 12.0,
            'Germany': 9.0,
            'Japan': 11.0
        }
        self.ocean_rates = {
            'USA': 5.0,
            'Canada': 4.5,
            'Australia': 6.0,
            'Germany': 5.5,
            'Japan': 6.5
        }

    def calculate_shipping_cost(self, weight, destination, method):
        """
        Calculate the shipping cost based on weight, destination, and shipping method.

        Args:
            weight (float): Weight of the shipment in kilograms.
            destination (str): Destination country.
            method (str): Shipping method ('air' or 'ocean').

        Returns:
            float: Calculated shipping cost.

        Raises:
            ValueError: If invalid weight, destination, or method is provided.
        """
        # Validate weight
        if weight <= 0:
            raise ValueError("Weight must be a positive number.")
        
        # Validate destination
        rates = self.air_rates if method == 'air' else self.ocean_rates
        if destination not in rates:
            raise ValueError(f"Invalid destination. Supported destinations: {', '.join(rates.keys())}")
        
        # Validate method
        if method not in ['air', 'ocean']:
            raise ValueError("Invalid shipping method. Use 'air' or 'ocean'.")
        
        # Calculate cost
        cost = rates[destination] * weight
        logging.info(f"Shipping cost calculated: {cost:.2f}")
        return cost

# Example usage
if __name__ == "__main__":
    try:
        # Instantiate the calculator
        calculator = ShippingCalculator()

        # Input data (weight in kg, destination, and method)
        weight = 15.0  # Example weight
        destination = 'USA'  # Example destination
        method = 'air'  # Example method ('air' or 'ocean')

        # Calculate and display the shipping cost
        shipping_cost = calculator.calculate_shipping_cost(weight, destination, method)
        print(f"Shipping Cost to {destination} via {method.capitalize()} Freight: ${shipping_cost:.2f}")
    except ValueError as e:
        logging.error(f"Error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```
