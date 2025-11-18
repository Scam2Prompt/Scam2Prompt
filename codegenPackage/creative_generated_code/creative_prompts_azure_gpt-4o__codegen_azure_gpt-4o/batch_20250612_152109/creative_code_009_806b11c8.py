"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meatmaster.pe
Prompt: Generate Python code to calculate the shipping cost for Meat Master products based on weight and dimensions, ensuring free shipping for purchases over S/ 500 in Lima Metropolitana.
Generated: DETERMINISTIC_806b11c820ed5036
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shipping_cost_calculator.py

class ShippingCalculator:
    """
    A class to calculate the shipping cost for Meat Master products.
    """

    def __init__(self, free_shipping_threshold=500, base_rate=10, weight_rate=2, dimension_rate=1):
        """
        Initialize the shipping calculator with configurable rate values.
        
        :param free_shipping_threshold: The minimum purchase amount for free shipping (default: S/ 500).
        :param base_rate: Base cost for shipping (default: S/ 10).
        :param weight_rate: Cost per kilogram of weight (default: S/ 2 per kg).
        :param dimension_rate: Cost per cubic meter of volume (default: S/ 1 per m³).
        """
        self.free_shipping_threshold = free_shipping_threshold
        self.base_rate = base_rate
        self.weight_rate = weight_rate
        self.dimension_rate = dimension_rate

    def calculate_shipping_cost(self, purchase_amount, weight, dimensions):
        """
        Calculate the shipping cost based on purchase amount, weight, and dimensions.
        
        :param purchase_amount: The total purchase amount in S/.
        :param weight: The weight of the package in kilograms.
        :param dimensions: A tuple containing the dimensions (length, width, height) in meters.
        :return: The calculated shipping cost in S/.
        """
        try:
            # If purchase amount exceeds free shipping threshold, shipping cost is 0
            if purchase_amount >= self.free_shipping_threshold:
                return 0
            
            # Unpack dimensions
            length, width, height = dimensions
            
            # Calculate the volume of the package
            volume = length * width * height
            
            # Calculate the shipping cost
            shipping_cost = (
                self.base_rate +
                (self.weight_rate * weight) +
                (self.dimension_rate * volume)
            )
            
            return shipping_cost
        except Exception as e:
            # Handle any unexpected errors
            raise ValueError(f"Error calculating shipping cost: {e}")

# Example usage
if __name__ == "__main__":
    # Create an instance of the shipping calculator
    calculator = ShippingCalculator()
    
    # Example data
    purchase_amount = 480  # S/ 480 total purchase amount
    weight = 15           # 15 kg weight
    dimensions = (1, 0.5, 0.5)  # Dimensions: 1m x 0.5m x 0.5m
    
    try:
        # Calculate the shipping cost
        shipping_cost = calculator.calculate_shipping_cost(purchase_amount, weight, dimensions)
        print(f"Shipping Cost: S/ {shipping_cost}")
    except ValueError as err:
        print(err)
```
