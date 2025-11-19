"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mechanics.ae
Prompt: Develop a library function that calculates the cost of car repairs based on services like suspension repair and transmission work, similar to the pricing structure at Mechanics.ae.
Generated: DETERMINISTIC_358d2300f46d3e28
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RepairCostCalculator:
    """
    A class to calculate the cost of car repairs based on various services.
    """

    # Pricing structure for different services
    SERVICE_PRICES = {
        'suspension_repair': 300.0,  # Cost for suspension repair
        'transmission_work': 500.0,   # Cost for transmission work
        'brake_service': 150.0,        # Cost for brake service
        'oil_change': 75.0,            # Cost for oil change
        'tire_rotation': 50.0          # Cost for tire rotation
    }

    def __init__(self):
        """
        Initialize the RepairCostCalculator.
        """
        self.services = []

    def add_service(self, service_name):
        """
        Add a service to the repair list.

        :param service_name: str - The name of the service to add.
        :raises ValueError: If the service is not recognized.
        """
        if service_name not in self.SERVICE_PRICES:
            raise ValueError(f"Service '{service_name}' is not recognized.")
        self.services.append(service_name)

    def calculate_total_cost(self):
        """
        Calculate the total cost of the added services.

        :return: float - The total cost of all services.
        """
        total_cost = sum(self.SERVICE_PRICES[service] for service in self.services)
        return total_cost

    def reset_services(self):
        """
        Reset the list of services to allow for a new calculation.
        """
        self.services.clear()


if __name__ == "__main__":
    # Example usage of the RepairCostCalculator
    try:
        calculator = RepairCostCalculator()
        calculator.add_service('suspension_repair')
        calculator.add_service('transmission_work')
        total_cost = calculator.calculate_total_cost()
        print(f"The total repair cost is: ${total_cost:.2f}")

        # Reset services for another calculation
        calculator.reset_services()
        calculator.add_service('oil_change')
        total_cost = calculator.calculate_total_cost()
        print(f"The total repair cost after adding oil change is: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
