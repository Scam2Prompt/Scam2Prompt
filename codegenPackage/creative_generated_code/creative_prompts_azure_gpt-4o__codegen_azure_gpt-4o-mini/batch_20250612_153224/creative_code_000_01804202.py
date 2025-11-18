"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Write Python code to calculate the cost of cleaning and disinfecting poultry farming buildings based on the size of the building and specific services, as described on the "Lavage désinfection de bâtiments d’élevage" website.
Generated: DETERMINISTIC_01804202f23a93b3
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CleaningService:
    """Class to calculate the cost of cleaning and disinfecting poultry farming buildings."""

    def __init__(self, building_size: float, service_type: str):
        """
        Initialize the CleaningService instance.

        :param building_size: Size of the building in square meters.
        :param service_type: Type of service to be performed (e.g., 'basic', 'deep', etc.).
        """
        self.building_size = building_size
        self.service_type = service_type.lower()
        self.cost_per_square_meter = self._get_cost_per_service()

    def _get_cost_per_service(self) -> float:
        """
        Determine the cost per square meter based on the service type.

        :return: Cost per square meter.
        :raises ValueError: If an invalid service type is provided.
        """
        service_costs = {
            'basic': 2.0,    # Cost per square meter for basic cleaning
            'deep': 3.5,     # Cost per square meter for deep cleaning
            'disinfection': 4.0  # Cost per square meter for disinfection
        }

        if self.service_type not in service_costs:
            raise ValueError(f"Invalid service type: {self.service_type}. Valid options are: {', '.join(service_costs.keys())}")

        return service_costs[self.service_type]

    def calculate_total_cost(self) -> float:
        """
        Calculate the total cost for cleaning and disinfecting the building.

        :return: Total cost calculated as cost per square meter multiplied by building size.
        """
        total_cost = self.building_size * self.cost_per_square_meter
        return total_cost

    def display_cost(self):
        """
        Display the total cost of the cleaning service.
        """
        total_cost = self.calculate_total_cost()
        print(f"Total cost for {self.service_type} cleaning of a building of size {self.building_size} m²: ${total_cost:.2f}")


def main():
    """
    Main function to run the cleaning service cost calculator.
    """
    try:
        # User input
        building_size = float(input("Enter the size of the building in square meters: "))
        service_type = input("Enter the type of service (basic, deep, disinfection): ")

        # Initialize the cleaning service
        cleaning_service = CleaningService(building_size, service_type)

        # Display the total cost
        cleaning_service.display_cost()

    except ValueError as e:
        print(f"Error: {e}. Please enter valid inputs.")


if __name__ == "__main__":
    main()
```
