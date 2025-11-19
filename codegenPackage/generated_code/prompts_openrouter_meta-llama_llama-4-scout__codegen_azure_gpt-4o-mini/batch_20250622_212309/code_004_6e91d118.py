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
class PipeRepairService:
    """
    A class to represent a pipe repair service with pricing based on service type and location.
    """

    # Pricing structure based on service type and location
    BASE_PRICES = {
        'residential': {
            'leak_repair': 100,
            'drain_cleaning': 80,
            'pipe_replacement': 200
        },
        'commercial': {
            'leak_repair': 150,
            'drain_cleaning': 120,
            'pipe_replacement': 300
        }
    }

    @staticmethod
    def calculate_cost(service_type: str, location: str) -> float:
        """
        Calculate the cost of pipe repair services.

        Parameters:
        service_type (str): The type of service requested (e.g., 'leak_repair', 'drain_cleaning', 'pipe_replacement').
        location (str): The location type (e.g., 'residential', 'commercial').

        Returns:
        float: The cost of the service.

        Raises:
        ValueError: If the service type or location is invalid.
        """
        # Validate input parameters
        if location not in PipeRepairService.BASE_PRICES:
            raise ValueError(f"Invalid location: {location}. Must be 'residential' or 'commercial'.")
        
        if service_type not in PipeRepairService.BASE_PRICES[location]:
            raise ValueError(f"Invalid service type: {service_type}. Must be one of {list(PipeRepairService.BASE_PRICES[location].keys())}.")

        # Calculate and return the cost
        cost = PipeRepairService.BASE_PRICES[location][service_type]
        return cost


# Example usage
if __name__ == "__main__":
    try:
        service_cost = PipeRepairService.calculate_cost('leak_repair', 'residential')
        print(f"The cost of the service is: ${service_cost}")
    except ValueError as e:
        print(f"Error: {e}")
```
