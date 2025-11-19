"""
Generated Code Metadata:
========================
Original URL: https://pahubel.com
Prompt: "Write a Python script to calculate the costs of a clinic renovation based on Pahubel's experience with dental clinic reforms."
Generated: DETERMINISTIC_55b54ef793eb7c66
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Clinic Renovation Cost Calculator

This script calculates the estimated costs for renovating a dental clinic based on Pahubel's experience.
It takes into account various factors like area size, material quality, and additional services.

Author: Your Name
Date: YYYY-MM-DD
"""

import math
from typing import Dict, Union


class ClinicRenovationCalculator:
    """
    A class to calculate renovation costs for dental clinics based on Pahubel's experience.
    """

    # Base cost per square meter for different quality tiers (in USD)
    BASE_COSTS = {
        'basic': 150,
        'standard': 250,
        'premium': 400
    }

    # Additional services and their costs
    ADDITIONAL_SERVICES = {
        'xray_room': 5000,
        'sterilization_room': 3000,
        'waiting_area_upgrade': 2000,
        'digital_equipment': 10000,
        'custom_cabinetry': 8000
    }

    def __init__(self):
        """Initialize the calculator with default values."""
        self.area = 0.0
        self.quality = 'standard'
        self.additional_services = []

    def calculate_total_cost(self) -> Dict[str, Union[float, str]]:
        """
        Calculate the total renovation cost based on inputs.

        Returns:
            A dictionary containing:
            - base_cost: The base renovation cost
            - additional_services_cost: Cost of additional services
            - total_cost: Sum of base and additional costs
            - cost_per_sqm: Cost per square meter
            - message: Any relevant messages about the calculation
        """
        if not self._validate_inputs():
            return {
                'base_cost': 0,
                'additional_services_cost': 0,
                'total_cost': 0,
                'cost_per_sqm': 0,
                'message': 'Invalid inputs. Please check area and quality.'
            }

        try:
            # Calculate base cost
            base_cost = self.area * self.BASE_COSTS[self.quality]

            # Calculate additional services cost
            additional_cost = sum(
                self.ADDITIONAL_SERVICES[service]
                for service in self.additional_services
            )

            total_cost = base_cost + additional_cost
            cost_per_sqm = total_cost / self.area if self.area > 0 else 0

            return {
                'base_cost': round(base_cost, 2),
                'additional_services_cost': round(additional_cost, 2),
                'total_cost': round(total_cost, 2),
                'cost_per_sqm': round(cost_per_sqm, 2),
                'message': 'Calculation successful'
            }

        except Exception as e:
            return {
                'base_cost': 0,
                'additional_services_cost': 0,
                'total_cost': 0,
                'cost_per_sqm': 0,
                'message': f'Error in calculation: {str(e)}'
            }

    def _validate_inputs(self) -> bool:
        """Validate that inputs are within acceptable ranges."""
        if self.area <= 0:
            return False
        if self.quality not in self.BASE_COSTS:
            return False
        return True

    def set_area(self, area: float) -> None:
        """Set the area of the clinic in square meters."""
        self.area = area

    def set_quality(self, quality: str) -> None:
        """Set the quality tier for the renovation."""
        self.quality = quality.lower()

    def add_service(self, service: str) -> None:
        """Add an additional service to the renovation."""
        if service in self.ADDITIONAL_SERVICES:
            self.additional_services.append(service)


def main():
    """Main function to demonstrate the calculator."""
    calculator = ClinicRenovationCalculator()

    try:
        # Get user inputs
        area = float(input("Enter clinic area in square meters: "))
        quality = input("Enter quality tier (basic/standard/premium): ")
        
        calculator.set_area(area)
        calculator.set_quality(quality)

        # Add additional services
        print("\nAvailable additional services:")
        for service in calculator.ADDITIONAL_SERVICES:
            print(f"- {service}")
        
        while True:
            service = input("\nEnter service to add (or 'done' to finish): ")
            if service.lower() == 'done':
                break
            calculator.add_service(service)

        # Calculate and display results
        result = calculator.calculate_total_cost()
        print("\nRenovation Cost Breakdown:")
        print(f"Base Cost: ${result['base_cost']:,.2f}")
        print(f"Additional Services: ${result['additional_services_cost']:,.2f}")
        print(f"Total Cost: ${result['total_cost']:,.2f}")
        print(f"Cost per sqm: ${result['cost_per_sqm']:,.2f}")
        print(f"Status: {result['message']}")

    except ValueError:
        print("Error: Please enter valid numerical values for area.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
