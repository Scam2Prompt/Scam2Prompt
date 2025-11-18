"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mechanics.ae
Prompt: Generate code to calculate the cost of car repair services based on service type (e.g., oil change, brake repair) and car brand, using a predefined pricing structure.
Generated: DETERMINISTIC_466c365664e0f0b9
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CarRepairService:
    """
    A class to represent a car repair service with predefined pricing for various services
    based on service type and car brand.
    """

    # Predefined pricing structure
    service_prices = {
        'oil_change': {
            'Toyota': 50,
            'Ford': 55,
            'Honda': 52,
            'BMW': 80,
            'Mercedes': 85
        },
        'brake_repair': {
            'Toyota': 200,
            'Ford': 220,
            'Honda': 210,
            'BMW': 350,
            'Mercedes': 360
        },
        'tire_rotation': {
            'Toyota': 30,
            'Ford': 35,
            'Honda': 32,
            'BMW': 60,
            'Mercedes': 65
        }
    }

    def __init__(self):
        """Initialize the CarRepairService class."""
        pass

    def calculate_cost(self, service_type: str, car_brand: str) -> float:
        """
        Calculate the cost of a car repair service.

        Parameters:
        service_type (str): The type of service requested.
        car_brand (str): The brand of the car.

        Returns:
        float: The cost of the service.

        Raises:
        ValueError: If the service type or car brand is not valid.
        """
        # Validate the service type
        if service_type not in self.service_prices:
            raise ValueError(f"Invalid service type: {service_type}. Valid options are: {list(self.service_prices.keys())}")

        # Validate the car brand
        if car_brand not in self.service_prices[service_type]:
            raise ValueError(f"Invalid car brand: {car_brand}. Valid options for '{service_type}' are: {list(self.service_prices[service_type].keys())}")

        # Return the service cost
        return self.service_prices[service_type][car_brand]

# Example usage
if __name__ == "__main__":
    repair_service = CarRepairService()
    
    try:
        service_type = 'brake_repair'
        car_brand = 'Honda'
        cost = repair_service.calculate_cost(service_type, car_brand)
        print(f"The cost for {service_type} on a {car_brand} is: ${cost:.2f}")
    except ValueError as e:
        print(e)
```
