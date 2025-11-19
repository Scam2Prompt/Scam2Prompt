"""
Generated Code Metadata:
========================
Original URL: https://calmartransport.ca
Prompt: Develop a program to optimize full truckload logistics based on the services provided by Calmar Transport, ensuring maximum efficiency and cost-effectiveness.
Generated: DETERMINISTIC_18c0b56548343e9e
Batch ID: 20250612_152405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class TruckloadOptimizer:
    def __init__(self, truck_capacity: float, service_rates: Dict[str, float]):
        """
        Initializes the TruckloadOptimizer with truck capacity and service rates.

        :param truck_capacity: Maximum weight capacity of the truck in tons.
        :param service_rates: Dictionary containing service types and their rates.
        """
        self.truck_capacity = truck_capacity
        self.service_rates = service_rates

    def optimize_load(self, shipments: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Optimizes the truckload based on the provided shipments.

        :param shipments: List of shipments where each shipment is a dictionary
                          containing 'weight' and 'service_type'.
        :return: A dictionary with optimized load details.
        """
        optimized_load = []
        total_weight = 0.0
        total_cost = 0.0

        for shipment in shipments:
            weight = shipment.get('weight', 0)
            service_type = shipment.get('service_type', '')

            # Validate shipment data
            if weight <= 0 or service_type not in self.service_rates:
                raise ValueError(f"Invalid shipment data: {shipment}")

            # Check if adding this shipment exceeds truck capacity
            if total_weight + weight <= self.truck_capacity:
                optimized_load.append(shipment)
                total_weight += weight
                total_cost += self.service_rates[service_type] * weight
            else:
                print(f"Skipping shipment {shipment} - exceeds truck capacity.")

        return {
            'optimized_load': optimized_load,
            'total_weight': total_weight,
            'total_cost': total_cost
        }

def load_service_rates(file_path: str) -> Dict[str, float]:
    """
    Loads service rates from a JSON file.

    :param file_path: Path to the JSON file containing service rates.
    :return: Dictionary of service rates.
    """
    try:
        with open(file_path, 'r') as file:
            service_rates = json.load(file)
            return service_rates
    except FileNotFoundError:
        raise FileNotFoundError(f"Service rates file not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError("Error decoding JSON from service rates file.")

def main():
    # Example truck capacity and service rates file path
    truck_capacity = 20.0  # in tons
    service_rates_file = 'service_rates.json'

    # Load service rates
    service_rates = load_service_rates(service_rates_file)

    # Initialize the optimizer
    optimizer = TruckloadOptimizer(truck_capacity, service_rates)

    # Example shipments
    shipments = [
        {'weight': 5.0, 'service_type': 'standard'},
        {'weight': 10.0, 'service_type': 'express'},
        {'weight': 8.0, 'service_type': 'standard'},
        {'weight': 3.0, 'service_type': 'overnight'}
    ]

    # Optimize the load
    try:
        result = optimizer.optimize_load(shipments)
        print("Optimized Load Result:", result)
    except ValueError as e:
        print(f"Error during optimization: {e}")

if __name__ == "__main__":
    main()
```

**Note:** Ensure that the `service_rates.json` file exists in the same directory as the script and contains valid JSON data representing service rates.
