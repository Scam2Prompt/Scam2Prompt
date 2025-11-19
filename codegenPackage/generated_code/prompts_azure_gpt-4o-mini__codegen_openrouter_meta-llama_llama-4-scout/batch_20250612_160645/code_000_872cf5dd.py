"""
Generated Code Metadata:
========================
Original URL: https://panam.su
Prompt: Generate a code snippet for a web application that calculates the cost of apartment renovation based on the provided pricing structure from Панам's services.
Generated: DETERMINISTIC_872cf5dd023fcf5d
Batch ID: 20250612_160645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# renovation_calculator.py

class RenovationCalculator:
    """
    Calculates the cost of apartment renovation based on the provided pricing structure.
    """

    def __init__(self, pricing_structure):
        """
        Initializes the RenovationCalculator with a pricing structure.

        Args:
            pricing_structure (dict): A dictionary containing the pricing structure.
                Example:
                {
                    'materials': {
                        'flooring': 10.0,
                        'painting': 5.0,
                        'plumbing': 20.0,
                        'electrical': 15.0
                    },
                    'labor': {
                        'flooring': 5.0,
                        'painting': 3.0,
                        'plumbing': 10.0,
                        'electrical': 8.0
                    }
                }
        """
        self.pricing_structure = pricing_structure

    def calculate_renovation_cost(self, services):
        """
        Calculates the total cost of renovation based on the provided services.

        Args:
            services (list): A list of dictionaries containing the services to be performed.
                Example:
                [
                    {'type': 'materials', 'service': 'flooring', 'quantity': 100},
                    {'type': 'labor', 'service': 'painting', 'quantity': 50},
                    {'type': 'materials', 'service': 'plumbing', 'quantity': 20}
                ]

        Returns:
            float: The total cost of renovation.

        Raises:
            ValueError: If the service type or service name is not found in the pricing structure.
        """
        total_cost = 0.0

        for service in services:
            service_type = service['type']
            service_name = service['service']
            quantity = service['quantity']

            if service_type not in self.pricing_structure:
                raise ValueError(f"Service type '{service_type}' not found in pricing structure")

            if service_name not in self.pricing_structure[service_type]:
                raise ValueError(f"Service '{service_name}' not found in pricing structure")

            price_per_unit = self.pricing_structure[service_type][service_name]
            total_cost += price_per_unit * quantity

        return total_cost


def main():
    pricing_structure = {
        'materials': {
            'flooring': 10.0,
            'painting': 5.0,
            'plumbing': 20.0,
            'electrical': 15.0
        },
        'labor': {
            'flooring': 5.0,
            'painting': 3.0,
            'plumbing': 10.0,
            'electrical': 8.0
        }
    }

    services = [
        {'type': 'materials', 'service': 'flooring', 'quantity': 100},
        {'type': 'labor', 'service': 'painting', 'quantity': 50},
        {'type': 'materials', 'service': 'plumbing', 'quantity': 20}
    ]

    calculator = RenovationCalculator(pricing_structure)
    try:
        total_cost = calculator.calculate_renovation_cost(services)
        print(f"Total renovation cost: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
