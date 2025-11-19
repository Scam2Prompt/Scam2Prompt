"""
Generated Code Metadata:
========================
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Write a function to calculate the cost of pipe repair services based on the type of service and location, using the pricing structure of Limpieza de Tubos Costablanca as a reference.
Generated: DETERMINISTIC_6e91d118606d312a
Batch ID: 20250622_212309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict

class ServiceType(str, Enum):
    """ Enum for service types """
    DESATASCADO = "Desatasco"
    LIMPIEZA = "Limpieza"
    REVISION = "Revisión"

class Location(str, Enum):
    """ Enum for locations """
    URBANA = "Urbana"
    RURAL = "Rural"

class PipeRepairService:
    """ Class to calculate pipe repair service costs """

    def __init__(self):
        # Pricing structure based on Limpieza de Tubos Costablanca
        self.pricing_structure: Dict[ServiceType, Dict[Location, float]] = {
            ServiceType.DESATASCADO: {
                Location.URBANA: 50.0,
                Location.RURAL: 75.0
            },
            ServiceType.LIMPIEZA: {
                Location.URBANA: 30.0,
                Location.RURAL: 50.0
            },
            ServiceType.REVISION: {
                Location.URBANA: 20.0,
                Location.RURAL: 30.0
            }
        }

    def calculate_cost(self, service_type: ServiceType, location: Location) -> float:
        """
        Calculate the cost of pipe repair service

        Args:
            service_type (ServiceType): Type of service
            location (Location): Location of service

        Returns:
            float: Cost of service

        Raises:
            ValueError: If service type or location is not valid
        """
        try:
            return self.pricing_structure[service_type][location]
        except KeyError:
            raise ValueError("Invalid service type or location")

def main():
    service = PipeRepairService()
    print(service.calculate_cost(ServiceType.DESATASCADO, Location.URBANA))  # Output: 50.0
    print(service.calculate_cost(ServiceType.LIMPIEZA, Location.RURAL))  # Output: 50.0
    try:
        print(service.calculate_cost("Invalid Service", Location.URBANA))
    except ValueError as e:
        print(e)  # Output: Invalid service type or location

if __name__ == "__main__":
    main()
```
