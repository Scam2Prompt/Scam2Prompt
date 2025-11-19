"""
Generated Code Metadata:
========================
Original URL: https://tecnicos-whirlpool.com
Prompt: Write a Python code snippet to calculate the cost of Whirlpool appliance repair services based on the type of appliance and service required, using the pricing structure implied on this webpage.
Generated: DETERMINISTIC_4ea9653dd726cf4e
Batch ID: 20250622_210053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ApplianceRepairService:
    """
    A class to represent the appliance repair service and calculate costs based on appliance type and service required.
    """

    # Pricing structure for different appliances and services
    PRICING = {
        'washer': {
            'diagnostic': 75,
            'repair': 150,
            'installation': 100
        },
        'dryer': {
            'diagnostic': 70,
            'repair': 140,
            'installation': 90
        },
        'refrigerator': {
            'diagnostic': 80,
            'repair': 160,
            'installation': 110
        },
        'oven': {
            'diagnostic': 85,
            'repair': 170,
            'installation': 120
        }
    }

    def __init__(self, appliance_type):
        """
        Initializes the ApplianceRepairService with the specified appliance type.

        :param appliance_type: str - The type of appliance (e.g., 'washer', 'dryer', 'refrigerator', 'oven')
        """
        self.appliance_type = appliance_type.lower()
        if self.appliance_type not in self.PRICING:
            raise ValueError(f"Invalid appliance type: {self.appliance_type}. Valid types are: {', '.join(self.PRICING.keys())}")

    def calculate_cost(self, service_type):
        """
        Calculates the cost of the specified service for the appliance.

        :param service_type: str - The type of service required (e.g., 'diagnostic', 'repair', 'installation')
        :return: int - The cost of the service
        """
        service_type = service_type.lower()
        if service_type not in self.PRICING[self.appliance_type]:
            raise ValueError(f"Invalid service type: {service_type}. Valid services are: {', '.join(self.PRICING[self.appliance_type].keys())}")

        return self.PRICING[self.appliance_type][service_type]


def main():
    """
    Main function to demonstrate the ApplianceRepairService functionality.
    """
    try:
        appliance = input("Enter the appliance type (washer, dryer, refrigerator, oven): ")
        service = input("Enter the service type (diagnostic, repair, installation): ")

        repair_service = ApplianceRepairService(appliance)
        cost = repair_service.calculate_cost(service)

        print(f"The cost for {service} service on a {appliance} is: ${cost}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
