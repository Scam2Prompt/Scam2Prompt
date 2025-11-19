"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://windscreensreplacementmelbourne.com.au
Prompt: Generate a function that calculates the cost of windscreen repairs based on vehicle type and service type, similar to the pricing model of Cheap Windscreens Melbourne.
Generated: DETERMINISTIC_092e054244eba3d5
Batch ID: 20250612_164058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WindscreenRepairService:
    """
    A class to represent a windscreens repair service with pricing based on vehicle type and service type.
    """

    # Define pricing models
    BASE_PRICES = {
        'sedan': {
            'standard': 150.00,
            'premium': 200.00,
        },
        'SUV': {
            'standard': 180.00,
            'premium': 230.00,
        },
        'truck': {
            'standard': 250.00,
            'premium': 300.00,
        }
    }

    @staticmethod
    def calculate_cost(vehicle_type: str, service_type: str) -> float:
        """
        Calculate the cost of windscreen repairs based on vehicle and service type.
        
        :param vehicle_type: The type of vehicle (e.g., 'sedan', 'SUV', 'truck').
        :param service_type: The type of service (e.g., 'standard', 'premium').
        :return: The cost of the repair.
        :raises ValueError: If the vehicle or service type is not recognized.
        """

        try:
            # Normalize input to lowercase to avoid case sensitivity issues
            vehicle_type = vehicle_type.lower()
            service_type = service_type.lower()

            # Check if the vehicle type is valid
            if vehicle_type not in WindscreenRepairService.BASE_PRICES:
                raise ValueError(f"Invalid vehicle type: '{vehicle_type}'. Valid types are: {', '.join(WindscreenRepairService.BASE_PRICES.keys())}")

            # Check if the service type is valid
            if service_type not in WindscreenRepairService.BASE_PRICES[vehicle_type]:
                raise ValueError(f"Invalid service type: '{service_type}'. Valid types for '{vehicle_type}' are: {', '.join(WindscreenRepairService.BASE_PRICES[vehicle_type].keys())}")

            # Return the calculated cost
            return WindscreenRepairService.BASE_PRICES[vehicle_type][service_type]

        except ValueError as e:
            # Handle invalid input gracefully
            print(f"Error: {e}")
            return 0.0

# Example usage:
if __name__ == "__main__":
    vehicle = 'SUV'
    service = 'premium'
    cost = WindscreenRepairService.calculate_cost(vehicle, service)
    if cost > 0:
        print(f"The cost of {service} service for a {vehicle} is: ${cost:.2f}")
```
