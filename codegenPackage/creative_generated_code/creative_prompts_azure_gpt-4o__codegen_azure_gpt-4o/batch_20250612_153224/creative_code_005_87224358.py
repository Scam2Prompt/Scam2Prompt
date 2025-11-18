"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://laotaigroup.com
Prompt: Write code to calculate the cost estimation for construction projects, including bridges and residential buildings, based on the expertise of Lao Tai Trading - Investment Group.
Generated: DETERMINISTIC_87224358cb4f0e24
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class ConstructionCostEstimator:
    """
    A class to calculate cost estimation for construction projects
    (bridges and residential buildings) based on the expertise of Lao Tai Trading - Investment Group.
    """

    def __init__(self):
        # Default cost per square meter for different types of projects
        self.cost_per_square_meter = {
            "bridge": 1500,  # Estimated cost per square meter for bridges
            "residential_building": 1200  # Estimated cost per square meter for residential buildings
        }

    def estimate_cost(self, project_type, area_in_square_meters):
        """
        Estimate the total cost of the construction project.

        :param project_type: Type of the construction project ('bridge' or 'residential_building')
        :param area_in_square_meters: Total area of the project in square meters
        :return: Estimated cost of the project (float)
        :raises ValueError: If the project_type is invalid or area is negative
        """
        if project_type not in self.cost_per_square_meter:
            raise ValueError("Invalid project type. Valid types are 'bridge' and 'residential_building'.")
        
        if area_in_square_meters <= 0:
            raise ValueError("Area must be greater than zero.")

        # Calculate the cost
        cost = self.cost_per_square_meter[project_type] * area_in_square_meters
        return cost

def main():
    """
    Main function to accept user input and calculate the cost estimation.
    """
    print("Welcome to Lao Tai Trading - Investment Group Construction Cost Estimator!")
    
    try:
        # Get project type and validate input
        project_type = input("Enter the project type ('bridge' or 'residential_building'): ").strip().lower()
        
        # Get project area and validate input
        area_in_square_meters = float(input("Enter the total area in square meters: "))

        # Create the cost estimator object
        estimator = ConstructionCostEstimator()

        # Calculate the cost
        estimated_cost = estimator.estimate_cost(project_type, area_in_square_meters)

        # Output the result
        print(f"The estimated cost for your {project_type} project is: ${estimated_cost:,.2f}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
