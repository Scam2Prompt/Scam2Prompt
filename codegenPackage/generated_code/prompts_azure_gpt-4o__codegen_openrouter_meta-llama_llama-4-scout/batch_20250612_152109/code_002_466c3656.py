"""
Generated Code Metadata:
========================
Original URL: https://mechanics.ae
Prompt: Generate code to calculate the cost of car repair services based on service type (e.g., oil change, brake repair) and car brand, using a predefined pricing structure.
Generated: DETERMINISTIC_466c365664e0f0b9
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# car_repair_cost_calculator.py

class CarRepairCostCalculator:
    """
    Calculates the cost of car repair services based on service type and car brand.
    """

    def __init__(self):
        # Predefined pricing structure
        self.pricing_structure = {
            'oil_change': {
                'Toyota': 30,
                'Ford': 35,
                'Honda': 32,
                'default': 40
            },
            'brake_repair': {
                'Toyota': 150,
                'Ford': 180,
                'Honda': 160,
                'default': 200
            },
            'tire_rotation': {
                'Toyota': 20,
                'Ford': 25,
                'Honda': 22,
                'default': 30
            }
        }

    def calculate_cost(self, service_type, car_brand):
        """
        Calculates the cost of a car repair service.

        Args:
            service_type (str): Type of service (e.g., oil change, brake repair)
            car_brand (str): Brand of the car

        Returns:
            float: The cost of the service

        Raises:
            ValueError: If the service type or car brand is not valid
        """
        try:
            service_type = service_type.lower().replace(' ', '_')
            if service_type not in self.pricing_structure:
                raise ValueError(f"Invalid service type: {service_type}")

            car_brand = car_brand.title()
            if car_brand not in self.pricing_structure[service_type]:
                car_brand = 'default'

            return self.pricing_structure[service_type][car_brand]
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None


def main():
    calculator = CarRepairCostCalculator()

    # Example usage
    services = [
        {'service_type': 'oil change', 'car_brand': 'Toyota'},
        {'service_type': 'brake repair', 'car_brand': 'Ford'},
        {'service_type': 'tire rotation', 'car_brand': 'Honda'},
        {'service_type': 'invalid service', 'car_brand': 'Toyota'},
        {'service_type': 'oil change', 'car_brand': 'invalid brand'}
    ]

    for service in services:
        cost = calculator.calculate_cost(service['service_type'], service['car_brand'])
        if cost is not None:
            print(f"Service: {service['service_type']}, Car Brand: {service['car_brand']}, Cost: ${cost:.2f}")


if __name__ == "__main__":
    main()
```
