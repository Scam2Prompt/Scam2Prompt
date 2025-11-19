"""
Generated Code Metadata:
========================
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Write Python code to calculate the cost of cleaning and disinfecting poultry farming buildings based on the size of the building and specific services, as described on the "Lavage désinfection de bâtiments d’élevage" website.
Generated: DETERMINISTIC_01804202f23a93b3
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CleaningService:
    """
    A class to represent a cleaning and disinfecting service for poultry farming buildings.
    """

    def __init__(self, building_size: float, service_type: str):
        """
        Initializes the CleaningService with building size and service type.

        :param building_size: Size of the building in square meters.
        :param service_type: Type of cleaning service (e.g., 'basic', 'deep', 'disinfection').
        """
        self.building_size = building_size
        self.service_type = service_type.lower()
        self.price_per_square_meter = self._set_price_per_square_meter()

    def _set_price_per_square_meter(self) -> float:
        """
        Sets the price per square meter based on the service type.

        :return: Price per square meter.
        :raises ValueError: If the service type is not recognized.
        """
        prices = {
            'basic': 2.0,      # Basic cleaning price per square meter
            'deep': 3.5,       # Deep cleaning price per square meter
            'disinfection': 4.5 # Disinfection price per square meter
        }

        if self.service_type not in prices:
            raise ValueError(f"Service type '{self.service_type}' is not recognized. "
                             f"Choose from {list(prices.keys())}.")

        return prices[self.service_type]

    def calculate_cost(self) -> float:
        """
        Calculates the total cost of the cleaning service.

        :return: Total cost of the cleaning service.
        """
        total_cost = self.building_size * self.price_per_square_meter
        return total_cost

def main():
    """
    Main function to execute the cleaning service cost calculation.
    """
    try:
        # Input: Size of the building in square meters
        building_size = float(input("Enter the size of the building in square meters: "))
        
        # Input: Type of cleaning service
        service_type = input("Enter the type of service (basic, deep, disinfection): ")

        # Create a CleaningService instance
        cleaning_service = CleaningService(building_size, service_type)

        # Calculate and display the total cost
        total_cost = cleaning_service.calculate_cost()
        print(f"The total cost for {service_type} cleaning of a {building_size} m² building is: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
