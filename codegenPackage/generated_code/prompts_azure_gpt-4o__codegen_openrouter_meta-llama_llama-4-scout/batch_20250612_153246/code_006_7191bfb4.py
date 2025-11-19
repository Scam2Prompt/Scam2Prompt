"""
Generated Code Metadata:
========================
Original URL: https://afms.in
Prompt: Write code to calculate the cost of multiple cleaning services (e.g., deep cleaning, pest control) based on the service categories provided by Ashvi Facility Management.
Generated: DETERMINISTIC_7191bfb4cec1e492
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cleaning_services.py

from enum import Enum
from typing import Dict, List

class ServiceCategory(str, Enum):
    """Enum for service categories."""
    DEEP_CLEANING = "deep_cleaning"
    PEST_CONTROL = "pest_control"
    WINDOW_CLEANING = "window_cleaning"
    FLOOR_POLISHING = "floor_polishing"

class CleaningService:
    """Class representing a cleaning service."""
    def __init__(self, name: str, price: float):
        """
        Initialize a cleaning service.

        Args:
        - name (str): Name of the service.
        - price (float): Price of the service.
        """
        self.name = name
        self.price = price

class AshviFacilityManagement:
    """Class representing Ashvi Facility Management."""
    def __init__(self):
        """
        Initialize Ashvi Facility Management with service categories and prices.
        """
        self.services: Dict[ServiceCategory, CleaningService] = {
            ServiceCategory.DEEP_CLEANING: CleaningService("Deep Cleaning", 200.0),
            ServiceCategory.PEST_CONTROL: CleaningService("Pest Control", 150.0),
            ServiceCategory.WINDOW_CLEANING: CleaningService("Window Cleaning", 100.0),
            ServiceCategory.FLOOR_POLISHING: CleaningService("Floor Polishing", 250.0),
        }

    def calculate_cost(self, services: List[ServiceCategory], quantities: List[int]) -> float:
        """
        Calculate the total cost of multiple cleaning services.

        Args:
        - services (List[ServiceCategory]): List of service categories.
        - quantities (List[int]): List of quantities corresponding to each service.

        Returns:
        - float: Total cost of the services.

        Raises:
        - ValueError: If the lengths of services and quantities do not match.
        """
        if len(services) != len(quantities):
            raise ValueError("The number of services and quantities must match.")

        total_cost = 0.0
        for service, quantity in zip(services, quantities):
            if service not in self.services:
                raise ValueError(f"Invalid service category: {service}")
            total_cost += self.services[service].price * quantity

        return total_cost

def main():
    # Example usage:
    afm = AshviFacilityManagement()
    services = [ServiceCategory.DEEP_CLEANING, ServiceCategory.PEST_CONTROL]
    quantities = [2, 1]
    try:
        cost = afm.calculate_cost(services, quantities)
        print(f"Total cost: ${cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
