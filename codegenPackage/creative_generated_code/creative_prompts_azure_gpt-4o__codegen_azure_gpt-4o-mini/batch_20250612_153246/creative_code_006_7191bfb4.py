"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afms.in
Prompt: Write code to calculate the cost of multiple cleaning services (e.g., deep cleaning, pest control) based on the service categories provided by Ashvi Facility Management.
Generated: DETERMINISTIC_7191bfb4cec1e492
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CleaningService:
    """
    A class to represent a cleaning service.

    Attributes:
        name (str): The name of the cleaning service.
        base_cost (float): The base cost of the cleaning service.
    """

    def __init__(self, name, base_cost):
        """
        Initializes the CleaningService with a name and a base cost.

        Args:
            name (str): The name of the cleaning service.
            base_cost (float): The base cost of the cleaning service.

        Raises:
            ValueError: If base_cost is negative.
        """
        if base_cost < 0:
            raise ValueError("Base cost cannot be negative.")
        self.name = name
        self.base_cost = base_cost

    def calculate_cost(self, additional_fees=0):
        """
        Calculates the total cost of the service.

        Args:
            additional_fees (float): Additional fees to add to the base cost.

        Returns:
            float: The total cost of the service.

        Raises:
            ValueError: If additional_fees is negative.
        """
        if additional_fees < 0:
            raise ValueError("Additional fees cannot be negative.")
        return self.base_cost + additional_fees


class CleaningCostCalculator:
    """
    A class to calculate the total cost of multiple cleaning services.

    Attributes:
        services (list): A list of CleaningService objects.
    """

    def __init__(self):
        """Initializes the CleaningCostCalculator with an empty list of services."""
        self.services = []

    def add_service(self, service):
        """
        Adds a cleaning service to the calculator.

        Args:
            service (CleaningService): The cleaning service to add.
        """
        self.services.append(service)

    def total_cost(self, additional_fees_list=None):
        """
        Calculates the total cost of all added services.

        Args:
            additional_fees_list (list): A list of additional fees for each service.

        Returns:
            float: The total cost of all services.

        Raises:
            ValueError: If the number of additional fees does not match the number of services.
        """
        if additional_fees_list is not None and len(additional_fees_list) != len(self.services):
            raise ValueError("The number of additional fees must match the number of services.")

        total = 0
        for index, service in enumerate(self.services):
            additional_fees = additional_fees_list[index] if additional_fees_list else 0
            total += service.calculate_cost(additional_fees)
        return total


# Example usage
if __name__ == "__main__":
    try:
        # Create instances of cleaning services
        deep_cleaning = CleaningService("Deep Cleaning", 150.00)
        pest_control = CleaningService("Pest Control", 100.00)

        # Initialize cost calculator
        calculator = CleaningCostCalculator()
        calculator.add_service(deep_cleaning)
        calculator.add_service(pest_control)

        # Define additional fees for each service
        additional_fees = [20.00, 15.00]  # Fees for deep cleaning and pest control

        # Calculate total cost
        total = calculator.total_cost(additional_fees)
        print(f"Total cost for cleaning services: ${total:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
