"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ohclift.com
Prompt: Develop a function that estimates the cost of installing a hydraulic freight elevator based on load capacity and installation location.
Generated: DETERMINISTIC_4ec421267e55fff4
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ElevatorInstallationCostEstimator:
    """
    A class to estimate the cost of installing a hydraulic freight elevator
    based on load capacity and installation location.
    """

    def __init__(self):
        """
        Initializes the cost estimator with base pricing factors.
        """
        self.base_cost_per_kg = 50  # Base cost per kg load capacity
        self.location_multiplier = {
            'urban': 1.2,
            'suburban': 1.0,
            'rural': 0.8
        }

    def estimate_cost(self, load_capacity_kg, location):
        """
        Estimates the installation cost of a hydraulic freight elevator.

        Parameters:
        load_capacity_kg (int): The load capacity of the elevator in kilograms.
        location (str): The installation location type ('urban', 'suburban', 'rural').

        Returns:
        float: Estimated cost for installing the elevator.

        Raises:
        ValueError: If load_capacity_kg is negative or location is invalid.
        """
        if load_capacity_kg < 0:
            raise ValueError("Load capacity must be a non-negative integer.")
        
        if location not in self.location_multiplier:
            raise ValueError("Invalid location type. Choose from 'urban', 'suburban', or 'rural'.")

        # Calculate the base cost based on load capacity
        base_cost = load_capacity_kg * self.base_cost_per_kg
        
        # Apply the location multiplier
        estimated_cost = base_cost * self.location_multiplier[location]

        return estimated_cost


# Example usage:
if __name__ == "__main__":
    estimator = ElevatorInstallationCostEstimator()

    try:
        load_capacity = 1000  # Example load capacity in kg
        installation_location = 'urban'  # Example installation location

        cost = estimator.estimate_cost(load_capacity, installation_location)
        print(f"The estimated cost for installing the elevator is: ${cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
