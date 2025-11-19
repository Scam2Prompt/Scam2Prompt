"""
Generated Code Metadata:
========================
Original URL: https://spedition-steinhuebl.de
Prompt: Generate a code snippet for an API that calculates shipping costs for packages sent from Germany to Austria, considering the services offered by Spedition Steinhübl.
Generated: DETERMINISTIC_34dfbad0c7ce662f
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shipping_api.py

from enum import Enum
from typing import Dict

class PackageType(str, Enum):
    """Package type enum"""
    STANDARD = "standard"
    EXPRESS = "express"

class SpeditionSteinhublService(str, Enum):
    """Spedition Steinhübl service enum"""
    STANDARD_DELIVERY = "standard_delivery"
    EXPRESS_DELIVERY = "express_delivery"
    PRIORITY_DELIVERY = "priority_delivery"

class ShippingCalculator:
    """Shipping calculator class"""

    def __init__(self):
        # Base rates for Spedition Steinhübl services in EUR
        self.base_rates: Dict[SpeditionSteinhublService, float] = {
            SpeditionSteinhublService.STANDARD_DELIVERY: 10.0,
            SpeditionSteinhublService.EXPRESS_DELIVERY: 20.0,
            SpeditionSteinhublService.PRIORITY_DELIVERY: 30.0
        }

        # Weight-based rates for Spedition Steinhübl services in EUR/kg
        self.weight_rates: Dict[SpeditionSteinhublService, float] = {
            SpeditionSteinhublService.STANDARD_DELIVERY: 0.5,
            SpeditionSteinhublService.EXPRESS_DELIVERY: 1.0,
            SpeditionSteinhublService.PRIORITY_DELIVERY: 1.5
        }

    def calculate_shipping_cost(self, package_type: PackageType, weight: float, length: float, width: float, height: float) -> float:
        """
        Calculate shipping cost for a package.

        Args:
        - package_type (PackageType): Type of package (standard or express)
        - weight (float): Weight of package in kg
        - length (float): Length of package in cm
        - width (float): Width of package in cm
        - height (float): Height of package in cm

        Returns:
        - float: Shipping cost in EUR
        """

        # Determine Spedition Steinhübl service based on package type
        if package_type == PackageType.STANDARD:
            service = SpeditionSteinhublService.STANDARD_DELIVERY
        elif package_type == PackageType.EXPRESS:
            service = SpeditionSteinhublService.EXPRESS_DELIVERY
        else:
            raise ValueError("Invalid package type")

        # Calculate volume of package in cubic meters
        volume = (length * width * height) / 1e6

        # Calculate shipping cost based on base rate, weight, and volume
        base_rate = self.base_rates[service]
        weight_rate = self.weight_rates[service]
        shipping_cost = base_rate + (weight * weight_rate)

        # Add volumetric weight surcharge if applicable
        volumetric_weight = volume * 1000 * 1.5  # assuming 1.5 EUR/kg for volumetric weight
        if volumetric_weight > weight:
            shipping_cost += (volumetric_weight - weight) * weight_rate

        return shipping_cost

def main():
    calculator = ShippingCalculator()

    # Example usage:
    package_type = PackageType.EXPRESS
    weight = 5.0  # kg
    length = 30.0  # cm
    width = 20.0  # cm
    height = 10.0  # cm

    try:
        shipping_cost = calculator.calculate_shipping_cost(package_type, weight, length, width, height)
        print(f"Shipping cost: {shipping_cost:.2f} EUR")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
