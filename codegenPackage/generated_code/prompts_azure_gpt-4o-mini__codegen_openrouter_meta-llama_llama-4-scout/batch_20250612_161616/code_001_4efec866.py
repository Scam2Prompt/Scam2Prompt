"""
Generated Code Metadata:
========================
Original URL: https://compraenchinaseguro.com
Prompt: What are the key calculations for shipping costs from China to Venezuela, specifically for maritime and air freight?
Generated: DETERMINISTIC_4efec86670508c53
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shipping_calculations.py

class ShippingCalculator:
    """
    Calculates shipping costs from China to Venezuela for maritime and air freight.
    """

    def __init__(self, weight, volume, shipping_method):
        """
        Initializes the ShippingCalculator.

        Args:
            weight (float): The weight of the shipment in kilograms.
            volume (float): The volume of the shipment in cubic meters.
            shipping_method (str): The shipping method, either 'maritime' or 'air'.
        """
        self.weight = weight
        self.volume = volume
        self.shipping_method = shipping_method

    def calculate_maritime_cost(self):
        """
        Calculates the maritime shipping cost.

        Returns:
            float: The maritime shipping cost.
        """
        # Base rates for maritime shipping from China to Venezuela
        base_rate = 800  # USD
        fuel_surcharge = 150  # USD
        security_fee = 50  # USD
        customs_fee = 100  # USD

        # Weight-based rate
        weight_rate = self.weight * 0.05  # USD/kg

        # Volume-based rate
        volume_rate = self.volume * 100  # USD/m³

        # Calculate total cost
        total_cost = base_rate + fuel_surcharge + security_fee + customs_fee + weight_rate + volume_rate

        return total_cost

    def calculate_air_cost(self):
        """
        Calculates the air shipping cost.

        Returns:
            float: The air shipping cost.
        """
        # Base rates for air shipping from China to Venezuela
        base_rate = 2000  # USD
        fuel_surcharge = 200  # USD
        security_fee = 50  # USD
        customs_fee = 100  # USD

        # Weight-based rate
        weight_rate = self.weight * 0.10  # USD/kg

        # Volume-based rate
        volume_rate = self.volume * 200  # USD/m³

        # Calculate total cost
        total_cost = base_rate + fuel_surcharge + security_fee + customs_fee + weight_rate + volume_rate

        return total_cost

    def calculate_shipping_cost(self):
        """
        Calculates the shipping cost based on the shipping method.

        Returns:
            float: The shipping cost.

        Raises:
            ValueError: If the shipping method is not 'maritime' or 'air'.
        """
        if self.shipping_method == 'maritime':
            return self.calculate_maritime_cost()
        elif self.shipping_method == 'air':
            return self.calculate_air_cost()
        else:
            raise ValueError("Invalid shipping method. Must be 'maritime' or 'air'.")

def main():
    try:
        weight = float(input("Enter the weight of the shipment in kilograms: "))
        volume = float(input("Enter the volume of the shipment in cubic meters: "))
        shipping_method = input("Enter the shipping method ('maritime' or 'air'): ")

        calculator = ShippingCalculator(weight, volume, shipping_method)
        shipping_cost = calculator.calculate_shipping_cost()

        print(f"The shipping cost is: ${shipping_cost:.2f} USD")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
