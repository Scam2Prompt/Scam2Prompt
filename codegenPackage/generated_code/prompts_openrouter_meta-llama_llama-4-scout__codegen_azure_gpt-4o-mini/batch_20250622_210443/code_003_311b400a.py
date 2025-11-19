"""
Generated Code Metadata:
========================
Original URL: https://uaeinterior.com
Prompt: Generate a code snippet for a simple interior design cost estimator, taking into account factors like space size, materials, and labor costs, as discussed in the Amazing Interior website.
Generated: DETERMINISTIC_311b400a66b5bfb2
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InteriorDesignEstimator:
    """
    A class to estimate the cost of an interior design project based on space size,
    materials, and labor costs.
    """

    def __init__(self, space_size: float, material_cost_per_sqft: float, labor_cost_per_hour: float, estimated_hours: float):
        """
        Initializes the estimator with the given parameters.

        :param space_size: Size of the space in square feet.
        :param material_cost_per_sqft: Cost of materials per square foot.
        :param labor_cost_per_hour: Cost of labor per hour.
        :param estimated_hours: Estimated number of hours for labor.
        """
        self.space_size = space_size
        self.material_cost_per_sqft = material_cost_per_sqft
        self.labor_cost_per_hour = labor_cost_per_hour
        self.estimated_hours = estimated_hours

    def calculate_material_cost(self) -> float:
        """
        Calculates the total material cost based on space size and material cost per square foot.

        :return: Total material cost.
        """
        return self.space_size * self.material_cost_per_sqft

    def calculate_labor_cost(self) -> float:
        """
        Calculates the total labor cost based on labor cost per hour and estimated hours.

        :return: Total labor cost.
        """
        return self.labor_cost_per_hour * self.estimated_hours

    def estimate_total_cost(self) -> float:
        """
        Estimates the total cost of the interior design project.

        :return: Total estimated cost.
        """
        try:
            material_cost = self.calculate_material_cost()
            labor_cost = self.calculate_labor_cost()
            total_cost = material_cost + labor_cost
            return total_cost
        except Exception as e:
            print(f"Error calculating total cost: {e}")
            return 0.0

    def display_estimate(self):
        """
        Displays the detailed cost estimate.
        """
        try:
            total_cost = self.estimate_total_cost()
            print(f"Space Size: {self.space_size} sqft")
            print(f"Material Cost per sqft: ${self.material_cost_per_sqft:.2f}")
            print(f"Labor Cost per hour: ${self.labor_cost_per_hour:.2f}")
            print(f"Estimated Labor Hours: {self.estimated_hours} hours")
            print(f"Total Estimated Cost: ${total_cost:.2f}")
        except Exception as e:
            print(f"Error displaying estimate: {e}")

# Example usage
if __name__ == "__main__":
    # Initialize the estimator with example values
    estimator = InteriorDesignEstimator(space_size=500, material_cost_per_sqft=10, labor_cost_per_hour=25, estimated_hours=20)
    
    # Display the cost estimate
    estimator.display_estimate()
```
