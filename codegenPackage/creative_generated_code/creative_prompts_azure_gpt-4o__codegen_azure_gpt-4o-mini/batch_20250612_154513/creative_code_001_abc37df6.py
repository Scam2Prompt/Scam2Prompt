"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.twigacementgroup.com
Prompt: Generate code to simulate the production capacity increase of TPCPLC's cement manufacturing, including milestones like the CM5 project reaching 2.0 million metric tons per year.
Generated: DETERMINISTIC_abc37df6ecfb89c0
Batch ID: 20250612_154513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CementProductionSimulator:
    """A simulator for the cement production capacity increase of TPCPLC."""

    def __init__(self, initial_capacity):
        """
        Initializes the simulator with the initial production capacity.

        Args:
            initial_capacity (float): The initial production capacity in million metric tons per year.
        """
        if initial_capacity <= 0:
            raise ValueError("Initial capacity must be greater than 0.")
        self.capacity = initial_capacity  # Current production capacity
        self.milestones = []               # Store milestones

    def add_milestone(self, project_name, target_capacity, completion_year):
        """
        Adds a production capacity milestone.

        Args:
            project_name (str): The name of the project.
            target_capacity (float): The target capacity in million metric tons per year.
            completion_year (int): The year the project is expected to complete.
        """
        if target_capacity <= 0:
            raise ValueError("Target capacity must be greater than 0.")

        milestone = {
            'project_name': project_name,
            'target_capacity': target_capacity,
            'completion_year': completion_year
        }
        self.milestones.append(milestone)
        self.capacity = max(self.capacity, target_capacity)  # Update capacity if milestone exceeds current capacity
    
    def simulate_growth(self, years):
        """
        Simulates the growth of cement production capacity over a given number of years.

        Args:
            years (int): The number of years to simulate growth.
        """
        if years < 0:
            raise ValueError("Years must be a non-negative integer.")

        # Simulating annual growth (for simplicity, let's assume a constant growth rate)
        annual_growth_rate = 0.1  # Assumed annual growth rate of 10%
        for _ in range(years):
            self.capacity *= (1 + annual_growth_rate)

    def get_current_capacity(self):
        """
        Returns the current production capacity.

        Returns:
            float: The current production capacity in million metric tons per year.
        """
        return self.capacity

    def get_milestones(self):
        """
        Returns the list of production capacity milestones.

        Returns:
            list: A list of milestones with project details.
        """
        return self.milestones

    def __str__(self):
        """
        Returns a string representation of the current state of the simulator.
        """
        return f"Current Production Capacity: {self.capacity:.2f} million metric tons/year"


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the simulator with an initial capacity of 1.5 million metric tons per year
        simulator = CementProductionSimulator(initial_capacity=1.5)

        # Add milestones, including the CM5 project
        simulator.add_milestone(project_name="CM5 Project", target_capacity=2.0, completion_year=2025)

        # Simulate growth for the next 5 years
        simulator.simulate_growth(years=5)

        # Output the current capacity and milestones
        print(simulator)
        print("Milestones:")
        for milestone in simulator.get_milestones():
            print(f"- {milestone['project_name']} reaching {milestone['target_capacity']} million metric tons by {milestone['completion_year']}")

    except ValueError as e:
        print(f"Error: {e}")
```
