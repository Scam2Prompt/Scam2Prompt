"""
Generated Code Metadata:
========================
Original URL: https://sstco.ma
Prompt: Create a function that calculates project costs and timelines based on SSTCO's competitive pricing and delivery commitments in construction projects.
Generated: DETERMINISTIC_8f2d1eb863b15c48
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ProjectCostCalculator:
    """
    A class to calculate project costs and timelines based on SSTCO's competitive pricing
    and delivery commitments in construction projects.
    """

    def __init__(self, base_cost_per_square_foot, delivery_time_per_square_foot):
        """
        Initializes the ProjectCostCalculator with base cost and delivery time.

        :param base_cost_per_square_foot: float, the cost per square foot for the project
        :param delivery_time_per_square_foot: float, the time in days to deliver per square foot
        """
        if base_cost_per_square_foot < 0 or delivery_time_per_square_foot < 0:
            raise ValueError("Base cost and delivery time must be non-negative.")

        self.base_cost_per_square_foot = base_cost_per_square_foot
        self.delivery_time_per_square_foot = delivery_time_per_square_foot

    def calculate_cost(self, total_square_feet):
        """
        Calculates the total project cost based on the total square feet.

        :param total_square_feet: float, the total area of the project in square feet
        :return: float, the total cost of the project
        """
        if total_square_feet < 0:
            raise ValueError("Total square feet must be non-negative.")

        total_cost = self.base_cost_per_square_foot * total_square_feet
        return total_cost

    def calculate_timeline(self, total_square_feet):
        """
        Calculates the total project timeline based on the total square feet.

        :param total_square_feet: float, the total area of the project in square feet
        :return: float, the total timeline in days for the project
        """
        if total_square_feet < 0:
            raise ValueError("Total square feet must be non-negative.")

        total_timeline = self.delivery_time_per_square_foot * total_square_feet
        return total_timeline

    def calculate_project(self, total_square_feet):
        """
        Calculates both the total cost and timeline for the project.

        :param total_square_feet: float, the total area of the project in square feet
        :return: tuple, (total_cost, total_timeline)
        """
        total_cost = self.calculate_cost(total_square_feet)
        total_timeline = self.calculate_timeline(total_square_feet)
        return total_cost, total_timeline


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the calculator with competitive pricing
        calculator = ProjectCostCalculator(base_cost_per_square_foot=150.0, delivery_time_per_square_foot=0.5)

        # Define the total square feet for the project
        total_square_feet = 1000

        # Calculate cost and timeline
        cost, timeline = calculator.calculate_project(total_square_feet)

        # Output the results
        print(f"Total Cost: ${cost:.2f}")
        print(f"Total Timeline: {timeline:.2f} days")

    except ValueError as e:
        print(f"Error: {e}")
```
