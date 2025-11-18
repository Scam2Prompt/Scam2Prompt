"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecoswap.us
Prompt: Develop a function to calculate shipping costs and taxes for selling or purchasing Apple devices, tailored to EcoSwap's checkout process.
Generated: DETERMINISTIC_cc685e25b52cd13d
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class EcoSwapShippingCalculator:
    """
    A class to calculate shipping costs and taxes for Apple devices in EcoSwap's checkout process.
    """

    BASE_SHIPPING_COST = 5.00  # Base shipping cost in USD
    TAX_RATE = 0.07            # Sales tax rate (7%)

    def __init__(self, device_value: float):
        """
        Initialize the shipping calculator with the value of the Apple device.

        :param device_value: The value of the Apple device (must be a positive float).
        """
        if device_value < 0:
            raise ValueError("Device value must be a non-negative float.")
        
        self.device_value = device_value

    def calculate_shipping_cost(self, distance: float) -> float:
        """
        Calculate the shipping cost based on distance.

        :param distance: The distance for shipping in miles (must be a non-negative float).
        :return: The calculated shipping cost in USD.
        """
        if distance < 0:
            raise ValueError("Distance must be a non-negative float.")
        
        # Calculate shipping cost based on distance (e.g., $0.10 per mile)
        shipping_cost = self.BASE_SHIPPING_COST + (0.10 * distance)
        return round(shipping_cost, 2)

    def calculate_tax(self) -> float:
        """
        Calculate sales tax based on the value of the Apple device.

        :return: The calculated tax in USD.
        """
        tax = self.device_value * self.TAX_RATE
        return round(tax, 2)

    def calculate_total_cost(self, distance: float) -> float:
        """
        Calculate the total cost including device value, shipping, and tax.

        :param distance: The distance for shipping in miles (must be a non-negative float).
        :return: The total cost in USD.
        """
        shipping_cost = self.calculate_shipping_cost(distance)
        tax = self.calculate_tax()
        total_cost = self.device_value + shipping_cost + tax
        return round(total_cost, 2)


# Example usage
if __name__ == "__main__":
    try:
        device_value = 999.99  # Example value for an Apple device
        distance = 50          # Example distance for shipping
        
        calculator = EcoSwapShippingCalculator(device_value)
        shipping_cost = calculator.calculate_shipping_cost(distance)
        tax = calculator.calculate_tax()
        total_cost = calculator.calculate_total_cost(distance)
        
        print(f"Shipping Cost: ${shipping_cost}")
        print(f"Tax: ${tax}")
        print(f"Total Cost: ${total_cost}")

    except ValueError as e:
        print(f"Error: {e}")
```
